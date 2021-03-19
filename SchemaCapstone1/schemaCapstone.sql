CREATE TABLE user ( 
	email                varchar(80) NOT NULL  PRIMARY KEY  ,
	user                 varchar(80) NOT NULL    ,
	password             varchar(80) NOT NULL    ,
	frm                  varchar(80) NOT NULL    ,
	to                   varchar(80) NOT NULL    
 );

INSERT INTO user( email, user, password, frm, to ) VALUES ( 'bob@gmail.com', 'bob', 'NewYEAR', ' Phoenix ', ' Orlando ');