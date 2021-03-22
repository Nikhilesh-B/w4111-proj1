# w4111-proj1

Sunday, March 21, 2021

This is the README file for Project 1 Intro to Databases

PostgreSQL account where the database resides:
Nikhilesh Belulkar	nb2953
psql -U nb2953 -h 34.73.36.248 -d project1
^command for accesing our DB

Password sql: 
277727
^ passowrd for DB


URL of web application:

"http://34.75.147.176:8111"

The following is a description of the parts of the original proposal in Part 1 that were implemented:


Our original proposal stated the following 

Our application will be taking into account what we feel to be the highlights of planning the World Cup. 
These include the teams playing in every match as well as their respective players, the referees, the broadcasters 
for each match, and the sponsors for the event. Some of the attributes for each one of these entities are Conference, 
name and position, country (from where the referee is from), and the region broadcasting from, respectively.


The implementation of our proposal took the following form. There are five main webpages

route: "http://34.75.147.176:8111/budget"
"budget.html"

This is responsible of displaying the costs of organizing the Fifa World Cup in respects to the
costs of hiring referees as well as broadcasting contracts. The code makes
calls to the Referee and Broadcasters tables in the PostgreSQL database. Its output is two tables. One
table has the names of the referees and their pay. The other table includes the names of the broadcasters 
and the value of their contracts.

route:"http://34.75.147.176:8111/player"
"playerInformation.html"

This is responsible of displaying the information of a player. The user will first have the option to
make a query on the table in the database containing the nations playing in the elimination rounds. They 
will pick a team and the output will be a table of the player names for that particular nation.

From here the user will be prompted to select a player from a list of players (all played for the same
nation) to view important information about them. The code makes calls to the Team, Player, and Equipment
tables in our database.

"http://34.75.147.176:8111/schedule"
"schedule.html"

This is responsible of displaying the times of matches in the World Cup. The user is prompted once again to
select select a nation from a list of nations in the final rounds of the tournament. The code calls on the Match
table in our database and outputs the columns containing the following values: Time and date, Name of the Stadium,
Opponent.

"http://34.75.147.176:8111/sponsor"
"sponsors.html"

This is responsible of displaying the sponsors and their associated information (Name, Industry, Deal Value)


"http://34.75.147.176:8111/stadiums"
"stadiums.html"

Here the user will have the chance to interact with 7 different options including all of the stadiums that
held matches in the final rounds of the Fifa World Cup. Once a particular stadium is selected all of the relevant
information regarding to that location will be displayed in a table. This table will include
the names of the two teams involved in the match, their respective captain's name, and the respective manager's name.


 
The following is a description of the parts of the original proposal in Part 1 that were not implemented:

In part 1 we stated that the results displayed in our front-end implementation would revolve around an aggregate
of the entity "teams" and the relationship "match." After the feedback from our project mentor we decided
to instead make "match" an entity. This greatly improved the implementation of our database by allowing us
to handle exceptions for the requirements of a match. Besides this everything from the original proposal was implemented.
Our webpages are mainly lookup functionalities that make queries in the database containing the relevant information.


Two of the webpages that require what we consider the most interesting database operations in terms of what the pages
are used for are "playerInformation.html" and "stadiums.html." 

route:"http://34.75.147.176:8111/player": gives the user the ability to gain a strong sense of the statistics for each player and the equipment
needed to maintain a team. "stadiums.html" provides the user to understand the World Cup from a big picture sense. They can
narrow down on the names of the teams played and important characteristics pertaining to those teams.i

On this route users input a country they want to select players from using a radio button this makes a backend request for the players statistics ; then after this users input a player they want to see the statistics for them as well as all the inofrmation pertaining to the equipment that particular player has. 

These queries are interstng because they use mutltiple differnet relationships such as has to render information for each player. 

"http://34.75.147.176:8111/schedule"
"schedule.html"

On this route a user inputs a country they want to see the schedule of using radio buttons. It is interesting because it provides an ordered schdule for each team. I think the query is interesting because it has a very unique construction in terms of the where clauses to render the teams that are not the team and to include all matches that a team played in. It involves OR + AND statements which i haven't seen in too many queries in class. It involves some more complex boolean logic which is why I think it's quite intersting, we also order the output in ascending order.








