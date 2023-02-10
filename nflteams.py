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
    print(htmltable)
    #display(HTML(htmltable))
    #return render_template('nfteams.html', team=teams)
    return htmltable

getNFLTeams()