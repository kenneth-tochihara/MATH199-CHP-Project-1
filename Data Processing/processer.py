import csv
import matplotlib.pyplot as plt
import numpy as np


def processData(filename):
    with open(filename) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        data = []
        for row in readCSV:
            data.append((row[1], int(row[4]), float(row[6])))

        years = []
        prev = data[0][1]
        currentYear = []
        for season in data:
            if season[1] != prev:
                prev = season[1]
                years.append(currentYear)
                currentYear = []
            currentYear.append(season)

        return years


def average(data):
    avs = []
    for year in data:
        zSum = 0.0
        for team in year:
            zSum += team[2]
        avs.append(zSum / len(year))
    return avs


def max(data):
    maxs = []
    for year in data:
        max = 0.0
        for team in year:
            if team[2] > max:
                max = team[2]
        maxs.append(max)
    return maxs


mlbYears = processData("../Data Fetching/Data/mlb_50_years.csv")
mlbAverageZ = average(mlbYears)
mlbMaxZ = max(mlbYears)

nflYears = processData("../Data Fetching/Data/nfl_50_years.csv")
nflAverageZ = average(nflYears)
nflMaxZ = max(nflYears)

nhlYears = processData("../Data Fetching/Data/nhl_50_years.csv")
nhlAverageZ = average(nhlYears)
nhlMaxZ = max(nhlYears)

nbaYears = processData("../Data Fetching/Data/nba_50_years.csv")
nbaAverageZ = average(nbaYears)
nbaMaxZ = max(nbaYears)

labels = []
mlb = []
nfl = []
nhl = []
nba = []

for year in mlbYears:
    labels.append(year[0][1])
for z in mlbAverageZ:
    mlb.append(z)
for z in nflAverageZ:
    nfl.append(z)
for z in nhlAverageZ:
    nhl.append(z)
for z in nbaAverageZ:
    nba.append(z)

plt.rcParams.update({'font.size': 6})
x = np.arange(len(labels))  # the label locations
width = 0.2  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - 3*width/2, mlb, width, color='orange', label='MLB')
rects2 = ax.bar(x - width/2, nfl, width, color='blue', label='NFL')
rects3 = ax.bar(x + width/2, nhl, width, color='green', label='NHL')
rects7 = ax.bar(x + 3*width/2, nba, width, color='black', label='NBA')
ax.set_ylabel('Average Z Score')
ax.set_title('Average Z Score by Season')
ax.set_xticks(x)
plt.xticks(rotation='vertical')
ax.set_xticklabels(labels)
ax.legend()
fig.tight_layout()
plt.autoscale(tight=True)
plt.savefig('averageZgraph.png', dpi=100)

mlb = []
nfl = []
nhl = []
nba = []
for z in mlbMaxZ:
    mlb.append(z)
for z in nflMaxZ:
    nfl.append(z)
for z in nhlMaxZ:
    nhl.append(z)
for z in nbaMaxZ:
    nba.append(z)

fig2, ax2 = plt.subplots()
rects4 = ax2.bar(x - 3*width/2, mlb, width, color='orange', label='MLB')
rects5 = ax2.bar(x - width/2, nfl, width, color='blue', label='NFL')
rects6 = ax2.bar(x + width/2, nhl, width, color='green', label='NHL')
rects8 = ax2.bar(x + 3*width/2, nba, width, color='black', label='NBA')

ax2.set_ylabel('Max Z Score')
ax2.set_title('Max Z Score by Season')
ax2.set_xticks(x)
ax2.set_xticklabels(labels)
plt.xticks(rotation='vertical')
ax2.legend()
fig2.tight_layout()
plt.autoscale(tight=True)
plt.savefig('maxZgraph.png', dpi=100)