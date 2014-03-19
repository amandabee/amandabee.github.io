CREATE TABLE member (
  member_id int(11) NOT NULL auto_increment,
  first_name varchar(50) NOT NULL default '',
  middle_name varchar(50) default NULL,
  last_name varchar(50) NOT NULL default '',
  streetaddress varchar(50) default NULL,
  apt_number varchar(6) default NULL,
  address_extra_line varchar(50) default NULL,
  city varchar(50) default NULL,
  state char(2) default NULL,
  zip varchar(9) default NULL,
  is_registered char(2) default NULL,
  election_district int(6) default NULL,
  home_phone varchar(15) default NULL,
  work_phone varchar(15) default NULL,
  mobile_phone varchar(15) default NULL,  
  PRIMARY KEY  (member_id)
) ;
CREATE TABLE action_member_map (
	map_id int(11) UNIQUE NOT NULL auto_increment,
	member_id int(11) NOT NULL,
	actionteam_id int(11) NOT NULL,
	PRIMARY KEY  (map_id)
);

CREATE TABLE action_team (
	actionteam_id int(11) NOT NULL auto_increment,
	name varchar(50) default NULL,
	description blob default NULL,
	PRIMARY KEY (actionteam_id)
);