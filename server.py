
"""
Columbia's COMS W4111.001 Introduction to Databases
Example Webserver
To run locally:
    python server.py Go to http://localhost:8111 in your browser.
A debugger such as "pdb" may be helpful for debugging.
Read about it online.
"""
import os
  # accessible as a variable in index.html:
from sqlalchemy import *
from sqlalchemy.pool import NullPool
from flask import Flask, request, render_template, g, redirect, Response

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)


#
# The following is a dummy URI that does not connect to a valid database. You will need to modify it to connect to your Part 2 database in order to use the data.
#
# XXX: The URI should be in the format of: 
#
#     postgresql://USER:PASSWORD@34.73.36.248/project1
#
# For example, if you had username zy2431 and password 123123, then the following line would be:
#
#     DATABASEURI = "postgresql://zy2431:123123@34.73.36.248/project1"
#
DATABASEURI = "postgresql://nb2953:277727@34.73.36.248/project1" # Modify this with your own credentials you received from Joseph!


#
# This line creates a database engine that knows how to connect to the URI above.
#
engine = create_engine(DATABASEURI)

#
# Example of running queries in your database
# Note that this will probably not work if you already have a table named 'test' in your database, containing meaningful data. This is only an example showing you how to run queries in your database using SQLAlchemy.
#
engine.execute("""CREATE TABLE IF NOT EXISTS test (
  id serial,
  name text
);""")
engine.execute("""INSERT INTO test(name) VALUES ('grace hopper'), ('alan turing'), ('ada lovelace');""")


@app.before_request
def before_request():
  """
  This function is run at the beginning of every web request 
  (every time you enter an address in the web browser).
  We use it to setup a database connection that can be used throughout the request.

  The variable g is globally accessible.
  """
  try:
    g.conn = engine.connect()
    print("the before rquest response has worked.")
  except:
    print("uh oh, problem connecting to database")
    import traceback; traceback.print_exc()
    g.conn = None

@app.teardown_request
def teardown_request(exception):
  """
  At the end of the web request, this makes sure to close the database connection.
  If you don't, the database could run out of memory!
  """
  try:
    g.conn.close()
  except Exception as e:
    pass


#
# @app.route is a decorator around index() that means:
#   run index() whenever the user tries to access the "/" path using a GET request
#
# If you wanted the user to go to, for example, localhost:8111/foobar/ with POST or GET then you could use:
#
#       @app.route("/foobar/", methods=["POST", "GET"])
#
# PROTIP: (the trailing / in the path is important)
# 
# see for routing: https://flask.palletsprojects.com/en/1.1.x/quickstart/#routing
# see for decorators: http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
#




def extractStadInfo(stadium):
    cursor = g.conn.execute("""SELECT T1.country,T1.manager_name,T1.captain, T2.country, T2.manager_name, T2.captain, M.score 
                            FROM match M, teams T1, teams T2, playsin P 
                            WHERE P.team_id=T1.team_id AND P.team2_id = T2.team_id AND P.match_id = M.match_id AND M.stadium = '{}' """.format(stadium))
    stadium_info = []
    for result in cursor:
        stadium_info.append(result)
    cursor.close()
    return stadium_info


def getTeamId(country):
     cursor = g.conn.execute("""SELECT team_id
                                FROM teams
                                WHERE country = '{}'
                            """.format(country))
     print("Japan:"+country)
     tid = []
     for result in cursor:
         tid.append(result[0])
    
     print(tid)
     cursor.close()
     return tid[0]
    
def getRefInfo():
    cursor = g.conn.execute("""SELECT name , SUM(ref_pay) as total
                               FROM  referee NATURAL JOIN officiates
                               GROUP BY name """)
    ref = []
    for result in cursor:
        ref.append(result)
    cursor.close()
    return ref

def getBroInfo():
    cursor = g.conn.execute("""SELECT broadcaster_name as name, region_broadcast as region, SUM(broadcasting_fee) as total
                               FROM   tvbroadcasters NATURAL JOIN broadcasts
                               GROUP BY broadcaster_name, region_broadcast""")
    bro = []
    for result in cursor:
        bro.append(result)
    cursor.close()
    return bro


def extractSponsorInfo(tid):
    cursor = g.conn.execute("""SELECT s.name, s.industry, a.deal_value
                                FROM sponsor s, sponsorship_deal a
                                WHERE a.team_id='{}' AND a.sponsor_id=s.sponsor_id""".format(tid))
    sponsor_info = []
    for result in cursor:
        sponsor_info.append(result)
    cursor.close()
    return sponsor_info


def getCountries():
    cursor = g.conn.execute("""SELECT country from teams""")
    countries = []
    for result in cursor:
        countries.append(result[0])
    cursor.close()
    return countries


def getAllEquipment(pid):
    cursor = g.conn.execute("""SELECT itemtype, brand_name
                               FROM equipment NATURAL JOIN has 
                               WHERE player_id='{}'
                            """.format(pid))

    equipment = []
    for result in cursor:
        equipment.append(result)
    cursor.close()
    return equipment



def getAllStat(pid):
    cursor = g.conn.execute("""SELECT position, height_cm, weight_lbs, preferred_foot
                                FROM player
                                WHERE player_id ='{}'
                            """.format(pid))
    stats= []
    for result in cursor:
        stats.append(result)
    cursor.close()
    return stats


def getTeamInfo():
     cursor = g.conn.execute("""SELECT team_id, country
                                FROM teams""")
     country= []
     for result in cursor:
         country.append(result)

     cursor.close()
     return country


def getAllPlayers(nation): 
    cursor = g.conn.execute("""SELECT player_id, name  
                            FROM player
                            WHERE team_id = '{}'
                            """.format(nation))
    players = []
    for result in cursor: 
        players.append(result)
    cursor.close()
    return players


def getSchedule(nid):
    cursor = g.conn.execute("""SELECT M.time, M.stadium, T.country
                            FROM match M, teams T, playsin P
                            WHERE (P.team_id='{}' OR P.team2_id = '{}') AND (P.team_id = T.team_id OR P.team2_id = T.team_id) AND T.team_id !='{}' AND P.match_id = M.match_id
                            ORDER BY M.time ASC"""
                            .format(nid,nid,nid))

    schedule = []
    for result in cursor:
        schedule.append(result)
    cursor.close()
    return schedule

def getCountryName(nid):
    cursor = g.conn.execute("""SELECT country
                            FROM teams
                            WHERE team_id = '{}'
                            """.format(nid))
    countries = []
    for result in cursor: 
        countries.append(result)

    cursor.close()
    return countries


def getPlayerName(pid):
    cursor = g.conn.execute("""SELECT name
                               FROM player
                               WHERE player_id = '{}'
                            """.format(pid))
    player = []
    for result in cursor:
        player.append(result)

    cursor.close()
    return player


@app.route('/player', methods=['GET','POST'])
def player():
     if request.method == 'GET':
         team = getTeamInfo()
         return render_template("playerInformation.html", team=team)
    
     if request.method == 'POST' and 'nation' in request.form:
         nationID =  request.form['nation']
         country = getCountryName(nationID)[0]
         players = getAllPlayers(nationID)
         p1 = True
         return render_template("playerInformation.html",p1=p1,players=players,country=country)


     if request.method == 'POST' and 'player' in request.form:
         playerID =  request.form['player']
         playerName = getPlayerName(playerID)[0][0]
         equip = getAllEquipment(playerID)
         stat = getAllStat(playerID)
         p2 = True
         return render_template("playerInformation.html",equip=equip,stat=stat,playerName=playerName,p2=p2)
       
     else: 
         return redirect('/player')
         
         
         
@app.route('/schedule',methods=['GET','POST'])
def schedule():
    if request.method == 'GET':
        team = getTeamInfo()
        return render_template("schedule.html", team=team)
         
    if request.method == 'POST':
        if('nation' in request.form):
            nationID =  request.form['nation']
            schedule = getSchedule(nationID)
            country = getCountryName(nationID)[0]
            post = True
            return render_template("schedule.html",post=post,schedule=schedule,country=country)
        
        else:
            return redirect('/schedule')            



@app.route('/sponsors', methods=['GET','POST'])
def sponsors():
    if request.method == 'GET':
        countries =  getCountries()
        return  render_template("sponsors.html",countries=countries)
    else:
        if ('options' in request.form):
            get = True
            country = request.form['options']
            tid = getTeamId(country)
            sponsor_info = extractSponsorInfo(tid)
            context = sponsor_info
            return render_template("sponsors.html",context=context,country=country,get=get)
        else:
            return redirect('/sponsors')



@app.route('/budget', methods = ['GET'])
def budget():
    if request.method == 'GET':
        bro = getBroInfo()
        ref = getRefInfo()
        return render_template("budget.html",ref=ref,bro=bro)


@app.route('/stadiums', methods=['GET','POST'])
def stadiums():
    if request.method == 'GET':
       return render_template("stadiums.html")
    else:
        if('options' in request.form):
            stadium = request.form['options']
            stadium_info = extractStadInfo(stadium)
            context = stadium_info
            post = True
            return render_template("stadiums.html",context=context,post=post)
        else:
           return redirect('/stadiums')

if __name__ == "__main__":
  import click
  @click.command()
  @click.option('--debug', is_flag=True)
  @click.option('--threaded', is_flag=True)
  @click.argument('HOST', default='0.0.0.0')
  @click.argument('PORT', default=8111, type=int)
  def run(debug, threaded, host, port):
    """
    This function handles command line parameters.
    Run the server using:
        python server.py
    Show the help text using:
        python server.py --help
    """
    HOST, PORT = host, port
    print("running on %s:%d" % (HOST, PORT))
    app.run(host=HOST, port=PORT, debug=debug, threaded=threaded)
  run()
      






