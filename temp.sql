PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE blogs_details (
blogID integer PRIMARY KEY,
username text NOT NULL,
title text NOT NULL,
content text NOT NULL,
date_created text NOT NULL,
date_published text NOT_NULL,
FOREIGN KEY (username) REFERENCES user_details (username));
COMMIT;
