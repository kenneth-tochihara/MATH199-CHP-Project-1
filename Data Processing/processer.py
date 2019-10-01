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


mlbYears = processData("../Data Fetching/Data/mlb.csv")
mlbAverageZ = average(mlbYears)
mlbMaxZ = max(mlbYears)

nflYears = processData("../Data Fetching/Data/nfl.csv")
nflAverageZ = average(nflYears)
nflMaxZ = max(nflYears)

nhlYears = processData("../Data Fetching/Data/nhl.csv")
nhlAverageZ = average(nhlYears)
nhlMaxZ = max(nhlYears)


labels = []
mlb = []
nfl = []
nhl = []

for year in mlbYears:
    labels.append(year[0][1])
for z in mlbAverageZ:
    mlb.append(z)
for z in nflAverageZ:
    nfl.append(z)
for z in nhlAverageZ:
    nhl.append(z)

plt.rcParams.update({'font.size': 8})
x = np.arange(len(labels))  # the label locations
width = 0.2  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, mlb, width, color='orange', label='MLB')
rects2 = ax.bar(x + width/2, nfl, width, color='blue', label='NFL')
rects3 = ax.bar(x + 3*width/2, nhl, width, color='green', label='NHL')
ax.set_ylabel('Average Z Score')
ax.set_title('Average Z Score by Season')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
fig.tight_layout()
plt.savefig('averageZgraph.png', dpi=100)

mlb = []
nfl = []
nhl = []
for z in mlbMaxZ:
    mlb.append(z)
for z in nflMaxZ:
    nfl.append(z)
for z in nhlMaxZ:
    nhl.append(z)

fig2, ax2 = plt.subplots()
rects4 = ax2.bar(x - width/2, mlb, width, color='orange', label='MLB')
rects5 = ax2.bar(x + width/2, nfl, width, color='blue', label='NFL')
rects6 = ax2.bar(x + 3*width/2, nhl, width, color='green', label='NHL')

ax2.set_ylabel('Max Z Score')
ax2.set_title('Max Z Score by Season')
ax2.set_xticks(x)
ax2.set_xticklabels(labels)
ax2.legend()
fig2.tight_layout()

plt.savefig('maxZgraph.png', dpi=100)