from math import pi
import random

games = 82 # number of games
year_end = 2019
sport = "CNF" #coinflipping
currentgame = 0
wins = {}
losses = {}
year_start = 1970

teams = [
'Team 1', 
'Team 2', 
'Team 3', 
'Team 4', 
'Team 5', 
'Team 6', 
'Team 7', 
'Team 8', 
'Team 9', 
'Team 10', 
'Team 11', 
'Team 12', 
'Team 13', 
'Team 14', 
'Team 15', 
'Team 16', 
'Team 17', 
'Team 18', 
'Team 19', 
'Team 20', 
'Team 21', 
'Team 22', 
'Team 23', 
'Team 24', 
'Team 25', 
'Team 26', 
'Team 27', 
'Team 28', 
'Team 29', 
'Team 30'
    ]

while year_start <= year_end:
    for team in teams:
        while currentgame < games:
            if team not in wins:
                wins[team] = 0
            if team not in losses:
                losses[team] = 0
            if random.uniform(0, 1) >= 0.5:
                wins[team] += 1
            else:
                losses[team] += 1
            currentgame += 1
        currentgame = 0
    for team in teams:
        zscore = (wins[team] - (0.5 * (wins[team] + losses[team]))) / ((wins[team] + losses[team]) * 0.5 * 0.5)**(0.5)
        zscoreabs = abs(zscore)
        print(f'{sport},{team},{wins[team]},{losses[team]},{year_start},{zscore},{zscoreabs}')
    wins = {}
    losses = {}
    year_start += 1

