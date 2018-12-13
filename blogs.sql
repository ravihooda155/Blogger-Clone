PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE users (
    username text not null,
    password text not null,
    age text,
    gender text ,
    interest text 
);
INSERT INTO users VALUES('test','$5$rounds=535000$0QDxzfT6nsarfDV5$i6idiIe0birm4l1srn6m2G0vumrteInjVvx7X6onmD/','21','Male','Computers');
INSERT INTO users VALUES('rekha','$5$rounds=535000$QCgKRbQC0OzsRs28$IzlLA1G5RSbA66U8ztASRsp2KH02bQthMhTZydCit4.','67','Female','Fiction');
INSERT INTO users VALUES('test1','$5$rounds=535000$I56KjFX9yt3dHJyL$Lg06pl3xW93.JD4xhyiKw3fdUPuI6PBSnFT4Yh3MAF8','34','Female','Fiction');
INSERT INTO users VALUES('test3','$5$rounds=535000$G3xkE4d0VS5gDqyS$1bkWCVHtps/IMCsW8hertmbc3wEVwOCMSW1zzDRiPHB','23','Male','swimming');
INSERT INTO users VALUES('test4','$5$rounds=535000$dIjgPtJWn6LRU8wm$kGC16N9aAA08CSCcWjDkvXCisVTl4aX4ODwQX0OXo26','23','Male','swimming');
INSERT INTO users VALUES('rajneesh','$5$rounds=535000$R8qGMD4e2Jansad4$G35ZuXgvkzxPO859rARmLtTxTfqtqaTzvg/1xu2RPQ9','21','Male','Computers');
INSERT INTO users VALUES('rajat','$5$rounds=535000$fHQA2wpFys6ahVqm$kP84nVE9oetwZt6NrSynpqMDfXDbIBXK.a39Vlf0Me/','12','Male','Computers');
CREATE TABLE user_details (
username text PRIMARY KEY,
password text NOT NULL,
name text NOT NULL,
DOB text NOT NULL,
email text NOT NULL,
gender text NOT NULL,
isAdmin boolean NOT NULL);
CREATE TABLE blog_detail (
    blog_id integer PRIMARY KEY AUTOINCREMENT,
    user_name text NOT NULL,
    title text NOT NULL,
    content text NOT NULL,
    date text NOT NULL,
    published BOOLEAN NOT NULL,
    FOREIGN KEY (user_name) 
    REFERENCES user_details (username));
CREATE TABLE comment (
    comment_id integer PRIMARY KEY AUTOINCREMENT,
    comment text NOT NULL,
    blog_id integer NOT NULL,
    FOREIGN KEY (blog_id)
    REFERENCES blog_detail (blog_id));
DELETE FROM sqlite_sequence;
COMMIT;
blog_detail   comment       user_details  users       
CREATE TABLE users (
    username text not null,
    password text not null,
    age text,
    gender text ,
    interest text 
);
CREATE TABLE user_details (
username text PRIMARY KEY,
password text NOT NULL,
name text NOT NULL,
DOB text NOT NULL,
email text NOT NULL,
gender text NOT NULL,
isAdmin boolean NOT NULL);
CREATE TABLE blog_detail (
    blog_id integer PRIMARY KEY AUTOINCREMENT,
    user_name text NOT NULL,
    title text NOT NULL,
    content text NOT NULL,
    date text NOT NULL,
    published BOOLEAN NOT NULL,
    FOREIGN KEY (user_name) 
    REFERENCES user_details (username));
CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE comment (
    comment_id integer PRIMARY KEY AUTOINCREMENT,
    comment text NOT NULL,
    blog_id integer NOT NULL,
    FOREIGN KEY (blog_id)
    REFERENCES blog_detail (blog_id));
