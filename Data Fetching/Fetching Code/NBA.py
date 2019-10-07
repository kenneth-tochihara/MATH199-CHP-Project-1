import requests

i = 0

alldata = ''
temp = ''

bad = '''
         <th aria-label="Rank" data-stat="ranker" class="ranker sort_default_asc show_partial_when_sorting right" data-tip="Rank" >Rk</th>
         <th aria-label="If listed as single number, the year the season ended.&#x2605; - Indicates All-Star for league.Only on regular season tables." data-stat="season" class=" sort_default_asc center" data-tip="If listed as single number, the year the season ended.<br>&#x2605; - Indicates All-Star for league.<br>Only on regular season tables." >Season</th>
         <th aria-label="Team" data-stat="team_id" class=" sort_default_asc left" data-tip="Team" >Tm</th>
         <th aria-label="League" data-stat="lg_id" class=" sort_default_asc left" data-tip="League" >Lg</th>
         <th aria-label="Games" data-stat="g" class=" right" data-tip="Games" >G</th>
         <th aria-label="Wins" data-stat="wins" class=" right" data-tip="Wins" >W</th>
         <th aria-label="Losses" data-stat="losses" class=" right" data-tip="Losses" >L</th>
         <th aria-label="Win-Loss Percentage" data-stat="win_loss_pct" class=" right" data-tip="Win-Loss Percentage" >W/L%</th>
         <th aria-label="Minutes Played" data-stat="mp" class=" right" data-tip="Minutes Played" >MP</th>
         <th aria-label="Field Goals" data-stat="fg" class=" right" data-tip="Field Goals" >FG</th>
         <th aria-label="Field Goal Attempts" data-stat="fga" class=" right" data-tip="Field Goal Attempts" >FGA</th>
         <th aria-label="2-Point Field Goals" data-stat="fg2" class=" right" data-tip="2-Point Field Goals" >2P</th>
         <th aria-label="2-point Field Goal Attempts" data-stat="fg2a" class=" right" data-tip="2-point Field Goal Attempts" >2PA</th>
         <th aria-label="3-Point Field Goals" data-stat="fg3" class=" right" data-tip="3-Point Field Goals" >3P</th>
         <th aria-label="3-Point Field Goal Attempts" data-stat="fg3a" class=" right" data-tip="3-Point Field Goal Attempts" >3PA</th>
         <th aria-label="Free Throws" data-stat="ft" class=" right" data-tip="Free Throws" >FT</th>
         <th aria-label="Free Throw Attempts" data-stat="fta" class=" right" data-tip="Free Throw Attempts" >FTA</th>
         <th aria-label="Offensive Rebounds" data-stat="orb" class=" right" data-tip="Offensive Rebounds" >ORB</th>
         <th aria-label="Defensive Rebounds" data-stat="drb" class=" right" data-tip="Defensive Rebounds" >DRB</th>
         <th aria-label="Total Rebounds" data-stat="trb" class=" right" data-tip="Total Rebounds" >TRB</th>
         <th aria-label="Assists" data-stat="ast" class=" right" data-tip="Assists" >AST</th>
         <th aria-label="Steals" data-stat="stl" class=" right" data-tip="Steals" >STL</th>
         <th aria-label="Blocks" data-stat="blk" class=" right" data-tip="Blocks" >BLK</th>
         <th aria-label="Turnovers" data-stat="tov" class=" right" data-tip="Turnovers" >TOV</th>
         <th aria-label="Personal Fouls" data-stat="pf" class=" right" data-tip="Personal Fouls" >PF</th>
         <th aria-label="Points" data-stat="pts" class=" right" data-tip="Points" >PTS</th>
'''

bad2 = '<tr class="thead">      </tr>'

bad3 = '''
      
      
      

'''

bad4 = '''

</tbody></table>
'''
bad5 = '''</tr><tr >'''
bad6 = '''</tr>\n<tr >'''
bad7 = '''<tr ><th scope="row" class="right " data-stat="ranker" csk="4" >4</th><td class="left " data-stat="season" >'''
bad8 = '''      </div>'''

while i < 13:
    url = 'https://www.basketball-reference.com/play-index/tsl_finder.cgi?request=1&match=single&type=team_totals&year_min=1970&year_max=2019&lg_id=NBA&franch_id=&c1stat=&c1comp=&c1val=&c2stat=&c2comp=&c2val=&c3stat=&c3comp=&c3val=&c4stat=&c4comp=&c4val=&order_by=year_id&order_by_asc=&offset='+str(i*100)
    website = requests.get( url )
    temp = website.text[:]
    temp = "\n".join(temp.split("\n")[2216:])
    temp = "\n".join(temp.split("\n")[:-500])
    temp = temp.replace(bad,'')
    temp = temp.replace(bad2,'')
    temp = temp.replace(bad3,'')
    temp = temp.replace(bad4,'')
    temp = temp.replace(bad5,bad6)
    alldata += temp
    i += 1

alldata = alldata.replace(bad5,bad6)
alldata = alldata.replace(bad8,'')

print(alldata)







