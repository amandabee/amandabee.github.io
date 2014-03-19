# `SELECT member_id FROM member WHERE last_name = "Santiago”;`

Results: 
# 30


# `SELECT member_id FROM member WHERE  organizer="Adele" AND election_district="31";`

Results: 
# 10,11,25,33


## `SELECT last_name FROM member LEFT JOIN action_member_map USING (member_id) LEFT JOIN action_team USING (actionteam_id) WHERE action_team.name="Mobile Home Parks";`

Results:
# Goris, Jordan, Chowdhury


## `SELECT last_name FROM member LEFT JOIN action_member_map USING(member_id) LEFT JOIN action_team USING(actionteam_id) WHERE action_team.name="At Home Infant Care";`

Results:
#Jackson, Gupta, Lindsey, Hewitt,  Gonzales, Basco


# `SELECT member_id FROM member WHERE last_name = "Jackson" AND first_name NOT LIKE "Shawn";`

Results:
# 2


## `SELECT member_id FROM member LEFT JOIN action_member_map USING (member_id) LEFT JOIN action_team USING (actionteam_id) WHERE action_team.name = "Workplace Justice Project";`

Results:
# 4,  6, 15, 21, 27, 34
