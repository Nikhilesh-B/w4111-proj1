w4111-proj1
Monday, April 5, 2021

This is the README file for Project 1 Part 4 Intro to Databases

1. Name and Uni of teammates:
nb2953 Nikhilesh Belulkar
jio2108 Jordan I. Ordonez-Chaguay

2. PostgreSQL account where the database resides: **Nikhilesh Belulkar** 
nb2953 psql -U nb2953 -h 34.73.36.248 -d project1 <------command for accesing our DB

Password sql: 277727 <----password for DB


**3. A thorough explanation of the three items above with which you expanded your project. Explain carefully your rationale behind your modifications to the schema and how these modifications fit within your overall project:**

-The following 3 items are the additions to our database: Array attribute, Composite Type, Text attribute which we are to do full-text search. Here is the explanantion for the rationale behind each one of these modifications to the schema and how they fit within the overall project. Our project is based on the 2018 FIFA World Cup with the aim to help the planning of this large event. 

One of the main concerns for the day of the match is the weather, especially the wind speed. This is a crucial piece of information when considering how to prepare the field for optimal playing conditions. Hence, we added a column in the already existing "match" entity that was of an integer array type holding integers representing the wind speed (mph) for different times in the match. 

Every instance of the FIFA World Cup is filled with all kinds of entertainment that is broadcasted on live television all over the world. We decided to add another column to the "match" entity that had a user-defined attribute called "entertainment_type" which consisted of the following attributes an id, the category of entertainment, the artist name, and the duration for the event. Each row in the entertainment column will related to a particular match.

Finally, sport commentators are crucial to the experience of watching a FIFA World Cup game on live television. Hence, we made another addition to the schema being another entity called "commentator." The entity has the following attributes match_id, commentator_id, name, age, nationality, years of experience, a document (filled with a paragraph length of text), and a tsvector which takes in the text from the document column and turns it into a tsvector which we can use alongside a tsquery for full text search.


**4. If you added a trigger, explain carefully what it is meant to achieve and why. Also include in your README file a real example of an "event" (i.e., an insertion, deletion, or update of a relation in your database, as specified in your trigger definition) that causes the trigger to be executed, together with a clear explanation of what the trigger does as a result of the event, including listing clearly any modifications to the database that happen as part of the trigger. Your description should be detailed enough so that we can recreate on your PostgreSQL database the execution of the trigger exactly as you describe it, and part of your grade will be based on the quality and accuracy of this description.**


We made an addition to the schema by creating a trigger that updates the tsvector column in the "commentator" entity every time a new value (match_id, commentator_id, name, age, nationality, years of experience, a document (filled with a paragraph length of text)) is inserted. This saves the time of having to manually make a tsvector every time we want to query for a phrase. 

CREATE TRIGGER tsvupdate BEFORE INSERT OR 
UPDATE ON commentator FOR EACH ROW
EXECUTE PROCEDURE tsvector_update_trigger
(tsv,’pg_catalog.english’, doc);

CREATE INDEX fts_idx ON commentator
USING gin(tsv);



**5. Substantial, meaningful queries involving the new attributes and tables in your schema, with a sentence or two per query explaining what the query is supposed to compute. If one of your three added items is a trigger, then you need to submit two queries (in addition to the trigger information in the previous bullet); otherwise, you need to submit three queries. All your new attributes and tables should appear at least once in one of the queries that you submit. For a text attribute, make sure at least one of your queries uses full-text search, as described here. For an array attribute, make sure at least one of your queries accesses elements in the array. Overall, your queries should work over your PostgreSQL database as submitted. We will run them against your database and part of your grade will be based on them, so please choose your queries carefully. We strongly suggest that you submit well formed queries that run without problems, so please make sure that you have tested your queries by running them on your database exactly as submitted (use copy and paste):**


QUERY 1:
Description: Provide the text in which the lexeme 'goal' appears in a comment made by a commentator at a particular match as well as information about that match and the commentator.



Results:

SELECT name, years_of_exp, stadium, score, doc FROM commentator, match WHERE tsv @@ to_tsquery('goal') and commentator.match_id = match.match_id;

name      | years_of_exp |         stadium                 | score |            doc                                                                                                            
 roger gonzalez |            8 | Saint Petersburg Stadium | 2-0   | Sweden eked out a win over Switzerland in an all-European battle at the 2018 FIFA World Cup on Tuesday, advancing 
to the quarterfinals with a 1-0 scoreline. The Swiss team dominated possession, had more shots (18 to 12), but just could not break through a stingy Swedish defense, as the yellow an
d blue move on to face either England or Colombia on Saturday.It was a goal by Emil Forsberg in the 66th minute which deflected off a Swiss defender and went in that proved to be the
 difference in this one..A tough blow for Switzerland, which played well, but could not find a breakthrough against a strong, tall Swedish defense that was compact and shielded its g
oalkeeper from danger. Sweden once again did not dominate the ball, did not create many chances, but got the job done. There is no doubt the Swedes will be a tough out for either Eng
land or Colombia in the quarterfinals.
 
 andrew das     |           12 | Fisht Stadium            | 3-3   | But it was the next two goals, the low, hard shots that delivered the World Cup back into French hands, the goals 
that crowned its latest generation of stars, that confirmed what everyone knew even before its 4-2 victory over Croatia was complete: France was the best team in the field this summe
r in Russia, a potent mix of greatness, grit and good fortune. And now it can call itself the world champion again.The title is France second, and its first since it won on home soil
 in 1998, and it ended a thrilling run by Croatia over the past five weeks. The Croats survived three consecutive extra-time games — and two penalty shootouts — in the knockout round
s to reach their first final, and they even had the better of the game on Sunday. But bad bounces and a better opponent made all the difference.

QUERY 2:
Description: Provide information about a particular performing artist for a match that took place in either Samara Arena or Saint Petersburg Stadium.

Results:

SELECT (entertainment).artist_name, (entertainment).category,round,score, stadium
FROM match m 
WHERE m.stadium = 'Samara Arena' or m.stadium = 'Saint Petersburg Stadium';

artist_name    | category |      round      | score |         stadium
------------------+----------+-----------------+-------+--------------------------
 shakira          | dancing  | Round of 16     | 2-0   | Samara Arena
 gianni infantino | speech   | Semi-finals     | 1-0   | Saint Petersburg Stadium
 wolf             | mascot   | 3rd Place Match | 2-0   | Saint Petersburg Stadium
(3 rows)

Query 3:
Description:

Results: Provide the average wind speed for the knockout round matches that occured in Kazan Arena or Saint Petersburg Stadium.

SELECT AVG((select AVG(a) FROM unnest(wind_speed_mph) AS a)),stadium, time,round,bracket 
from match 
WHERE match.stadium = 'Kazan Arena' OR match.stadium = 'Saint Petersburg Stadium' 
GROUP BY stadium,match.time,match.round,match.bracket;

avg         |         stadium          |        time         |      round      | bracket
---------------------+--------------------------+---------------------+-----------------+---------
  7.2000000000000000 | Kazan Arena              | 2018-05-16 13:00:00 |                 | C
  8.1250000000000000 | Kazan Arena              | 2018-06-20 17:00:00 | Round of 16     |
  5.8000000000000000 | Kazan Arena              | 2018-07-06 21:00:00 | Quarter finals  |
 13.5000000000000000 | Saint Petersburg Stadium | 2018-07-10 21:00:00 | Semi-finals     |
  8.1428571428571429 | Saint Petersburg Stadium | 2018-07-14 21:00:00 | 3rd Place Match |
(5 rows)






