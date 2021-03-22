# w4111-proj1

Sunday, March 21, 2021

This is the README file for Project 1 Intro to Databases

PostgreSQL account where the database resides:
Nikhilesh Belulkar	nb2953

URL of web application:

" "

The following is a description of the parts of the original proposal in Part 1 that were implemented:


Our original proposal stated the following 

Our application will be taking into account what we feel to be the highlights of planning the World Cup. 
These include the teams playing in every match as well as their respective players, the referees, the broadcasters 
for each match, and the sponsors for the event. Some of the attributes for each one of these entities are Conference, 
name and position, country (from where the referee is from), and the region broadcasting from, respectively.


The implementation of our proposal took the following form. There are five main webpages

"budget.html"

This is responsible of displaying the costs of organizing the Fifa World Cup in respects to the
costs of hiring referees as well as broadcasting contracts. The code makes
calls to the Referee and Broadcasters tables in the PostgreSQL database. Its output is two tables. One
table has the names of the referees and their pay. The other table includes the names of the broadcasters 
and the value of their contracts.

"playerInformation.html"

This is responsible of displaying the information of a player. The user will first have the option to
make a query on the table in the database containing the nations playing in the elimination rounds. They 
will pick a team and the output will be a table of the player names for that particular nation.

From here the user will be prompted to select a player from a list of players (all played for the same
nation) to view important information about them. The code makes calls to the Team, Player, and Equipment
tables in our database.


"schedule.html"

This is responsible of displaying the times of matches in the World Cup. The user is prompted once again to
select select a nation from a list of nations in the final rounds of the tournament. The code calls on the Match
table in our database and outputs the columns containing the following values: Time and date, Name of the Stadium,
Opponent.

"sponsors.html"

This is responsible of displaying the sponsors and their associated information (Name, Industry, Deal Value)

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

"playerInformation.html" gives the user the ability to gain a strong sense of the statistics for each player and the equipment
needed to maintain a team. "stadiums.html" provides the user to understand the World Cup from a big picture sense. They can
narrow down on the names of the teams played and important characteristics pertaining to those teams.
