#COaTI SQL Bingo

**Objectives:** Help participants understand that SQL is not complicated, just precise, and that any search they perform in a database is really an SQL Query. Hopefully understanding how SQL works will help players create better database searches.

**Materials:**

+ Markers for the Bingo Cards (chocolate kiss sized candies work well but prepare for some snacking)
+ Prizes for the winners
+ A projector or some alternate means of presenting the queries
+ The SQL Bingo Kit (includes README.txt, which describes each file by name):
 + + Query Slides (Power Point and PDF)  
 + + Bingo Cards (Excel and PDF) there are six unique cards, only one of which will win. Print enough for each participant to have one or two cards.
 + + Base Data (Excel and PDF) there are three tables. Each participant should have their own set with one of each table.
 + + SQL Cheat Sheets: two sample SQL guides. 

**Overview:** Start by explaining what SQL is and how it works; distribute data sheets (one of each to each participant) and one or two bingo cards to each participant. Read each queries and  make sure everyone has enough time to understand the right answers. Ask someone to provide all the acceptable answers to each query before you go onto the next one. Hand out some SQL Cheat Sheets for future reference. 

**Explaining SQL** … a sample script …
When I was in fifth grade or so we had to do an exercise where we instructed a classmate to make a peanut butter sandwich, as part of a lesson on Robots. I thought everyone did that, but maybe I was wrong. The whole thing was very funny because we were telling the robot to put the knife in the jar before the jar was open. We also learned about apple logo, which I know some people here also had to learn–the programming game where you tell the turtles to draw? 

The point is that SQL, or Structured Query Language (some people pronounce it *sequel*) is a pretty simple language, but your database can only do what it is told. When it seems to think for itself, that is because some human got in there and gave it ideas. When you are searching in any database, what you are really doing is filling out a form that the database application translates into some form of SQL and uses to query the underlying data of the database. 

If you have a command line interface to your database, you could just type in a query yourself. Here are the queries:
 
Query One: `SELECT member_id FROM member WHERE last_name="Santiago"`

Results:
30

The “member_id” is the unique number that the database uses to tell Gilberto Mejia, the seventeen year old youth activist, from Councilman Gilberto Mejia (no relation) when you’ve got  both in your database. 

Query Two: `SELECT member_id FROM member WHERE organizer="Adele" AND election_district="31";`

Results: 10,11,25,33

Query Three: `SELECT last_name FROM member LEFT JOIN action_member_map USING (member_id) LEFT JOIN action_team USING (actionteam_id) WHERE action_team.name="Mobile Home Parks";`

Results:
Goris, Jordan, Chowdhury

The “map” lets the database map one member to multiple committees, and vice versa. Sometimes it is called a "lookup table" Let people puzzle this one out and answer each other. It only gets worse:

Query Four: `SELECT last_name FROM member LEFT JOIN action_member_map USING(member_id) LEFT JOIN action_team USING(actionteam_id) WHERE action_team.name="At Home Infant Care";`

Results:
Jackson, Gupta, Lindsey, Hewitt,  Gonzales, Basco

Sometimes you aren’t sure who you are looking for and you need to eliminate some listings that you know aren’t the right one:

Query Five: `SELECT member_id FROM member WHERE last_name = "Jackson" AND first_name NOT LIKE "Shawn";`

Results:
2

And the last query:
`SELECT member_id FROM member LEFT JOIN action_member_map USING (member_id) LEFT JOIN action_team USING (actionteam_id) WHERE action_team.name = "Workplace Justice Project";`

Results:
4,  6, 15, 21, 27, 34

By now someone should have called BINGO. If they didn’t, you maybe goofed somewhere because one of the six card templates will always win. The game is rigged like that. 

---
&copy; 2014 Amanda Hickman

SQL Bingo was originally created by Amanda Hickman & the LINC Project for the Progressive Technology Project’s Community Organizing and Technology Institute (COaTI), circa 2004. It is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 2.5 License. Contact me to discuss commericial use. 