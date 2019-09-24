from sportsreference.nfl.teams import Teams

year_start = 1999 # starting year
year_end = 2018 # ending year
sport = 'NFL'

while year_start <= year_end:
    teams = Teams(year_start)
    for team in teams:
        zscore = (team.wins - (0.5 * (team.wins + team.losses))) / ((team.wins + team.losses) * 0.5 * 0.5)**(0.5)
        zscoreabs = abs(zscore)
        print(f'{sport},{team.name},{team.wins},{team.losses},{year_start},{zscore},{zscoreabs}')
    year_start += 1
