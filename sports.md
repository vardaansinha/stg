# Sports


## Shaurya Goel

### NFL2

```
{python} 
import sqlite3
#import markdown
from flask import Flask, render_template, request, flash, redirect, url_for
from IPython.display import display, HTML

def get_db_connection():
    conn = sqlite3.connect('volumes/sqlite.db')
    conn.row_factory = sqlite3.Row
    return conn



def getNFLTeams():
    conn = get_db_connection()
    db_teams = conn.execute('SELECT id, _division, _team FROM NFLTeam;').fetchall()
    conn.close()
    htmltable = ""
    htmltable +="<table>"
    teams = []
    for team in db_teams:
       htmltable +="<tr>"
       team = dict(team)
       htmltable +="<td>%s</td>" % team["id"]
       htmltable +="<td>%s</td>" % team["_division"]
       htmltable +="<td>%s</td>" % team["_team"]
       #print(team)
       #team['content'] = markdown.markdown(team['content'])
       teams.append(team)
       htmltable +="</tr>"

    htmltable +="</table>"
    #print(htmltable)
    display(HTML(htmltable))
    #return render_template('nfteams.html', team=teams)
    return htmltable

getNFLTeams()
```

<table style="border-collapse: separate;" border="1"><tbody><tr><th>Team</th><th>Division</th><th>Games Played</th><th>Games Won</th><th>Games Lost</th><th>Games Drawn</th><th>Games Played At Home</th><th>Games Played Away</th><th>Games Won At Home</th><th>Games Won Away</th><th>Games Lost At Home</th><th>Games Lost Away</th><th>Points For</th><th>Points Against</th><th>Playoffs</th></tr><tr><td>Washington Commanders</td><td>NFC East</td><td>17</td><td>8</td><td>1</td><td>8</td><td>9</td><td>4</td><td>4</td><td>5</td><td>3</td><td>321</td><td>343</td><td>343</td></tr><tr><td>New York Giants</td><td>NFC East</td><td>17</td><td>9</td><td>1</td><td>9</td><td>8</td><td>5</td><td>4</td><td>3</td><td>4</td><td>365</td><td>371</td><td>371</td></tr><tr><td>Dallas Cowboys</td><td>NFC East</td><td>17</td><td>12</td><td>0</td><td>9</td><td>8</td><td>8</td><td>4</td><td>1</td><td>4</td><td>467</td><td>342</td><td>342</td></tr><tr><td>Philadelphia Eagles</td><td>NFC East</td><td>17</td><td>14</td><td>0</td><td>9</td><td>8</td><td>7</td><td>7</td><td>2</td><td>1</td><td>477</td><td>344</td><td>344</td></tr><tr><td>Arizona Cardinals</td><td>NFC West</td><td>17</td><td>4</td><td>0</td><td>9</td><td>8</td><td>1</td><td>3</td><td>8</td><td>5</td><td>340</td><td>449</td><td>449</td></tr><tr><td>Los Angeles Rams</td><td>NFC West</td><td>17</td><td>5</td><td>0</td><td>9</td><td>8</td><td>4</td><td>1</td><td>5</td><td>7</td><td>307</td><td>384</td><td>384</td></tr><tr><td>Seattle Seahawks</td><td>NFC West</td><td>17</td><td>9</td><td>0</td><td>9</td><td>8</td><td>5</td><td>4</td><td>4</td><td>4</td><td>407</td><td>401</td><td>401</td></tr><tr><td>San Francisco 49ers</td><td>NFC West</td><td>17</td><td>13</td><td>0</td><td>9</td><td>8</td><td>8</td><td>5</td><td>1</td><td>3</td><td>450</td><td>277</td><td>277</td></tr><tr><td>Green Bay Packers</td><td>NFC North</td><td>17</td><td>8</td><td>0</td><td>9</td><td>8</td><td>5</td><td>3</td><td>4</td><td>5</td><td>370</td><td>371</td><td>371</td></tr><tr><td>Chicago Bears</td><td>NFC North</td><td>17</td><td>3</td><td>0</td><td>9</td><td>8</td><td>2</td><td>1</td><td>7</td><td>7</td><td>326</td><td>463</td><td>463</td></tr><tr><td>Detroit Lions</td><td>NFC North</td><td>17</td><td>9</td><td>0</td><td>9</td><td>8</td><td>5</td><td>4</td><td>4</td><td>4</td><td>453</td><td>427</td><td>427</td></tr><tr><td>Minnesota Vikings</td><td>NFC North</td><td>17</td><td>13</td><td>0</td><td>9</td><td>8</td><td>8</td><td>5</td><td>1</td><td>3</td><td>424</td><td>427</td><td>427</td></tr><tr><td>New Orleans Saints</td><td>NFC South</td><td>17</td><td>7</td><td>0</td><td>9</td><td>8</td><td>4</td><td>3</td><td>5</td><td>5</td><td>330</td><td>345</td><td>345</td></tr><tr><td>Atlanta Falcons</td><td>NFC South</td><td>17</td><td>7</td><td>0</td><td>9</td><td>8</td><td>6</td><td>1</td><td>3</td><td>7</td><td>365</td><td>386</td><td>386</td></tr><tr><td>Tampa Bay Buccaneers</td><td>NFC South</td><td>17</td><td>8</td><td>0</td><td>9</td><td>8</td><td>5</td><td>3</td><td>4</td><td>5</td><td>313</td><td>358</td><td>358</td></tr><tr><td>Carolina Panthers</td><td>NFC South</td><td>17</td><td>7</td><td>0</td><td>9</td><td>8</td><td>5</td><td>2</td><td>4</td><td>6</td><td>347</td><td>374</td><td>374</td></tr></tbody></table>