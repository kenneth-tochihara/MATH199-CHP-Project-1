from sportsreference.nhl.teams import Teams

year_start = 1999 #starting year, don't include 2005
year_end = 2019
sport = 'NHL'

while year_start <= year_end: #ending year, doesn't include 2005
    if year_start == 2005:
        year_start += 1
    teams = Teams(year_start)
    for team in teams:
        losses = team.losses
        otl = team.overtime_losses
        if type(otl) == type(losses):
            combined_losses = losses + otl
        else:
            combined_losses = losses

        zscore = (team.wins - (0.5 * (team.wins + combined_losses))) / ((team.wins + combined_losses) * 0.5 * 0.5)**(0.5)
        zscoreabs = abs(zscore)
        print(f'{sport},{team.name},{team.wins},{combined_losses},{year_start},{zscore},{zscoreabs}')
    year_start += 1
