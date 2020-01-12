CREATE TABLE IF NOT EXISTS users{
id SERIAL,
username VARCHAR NOT NULL,
pass VARCHAR NOT NULL,
UNIQUE(username),
};

-- CREATE TABLE foods{
-- id INTEGER PRIMARY KEY,
-- name VARCHAR NOT NULL,
-- calories INTEGER,
-- quantity INTEGER,
-- fdate VARCHAR,
-- consumer VARCHAR NOT NULL,
-- FOREIGN KEY(consumer) REFERENCES users(username)
-- };
--
-- CREATE TABLE purchases{
-- id INTEGER,
-- title VARCHAR,
-- cost FLOAT,
-- quantity INTEGER,
-- fdate VARCHAR,
-- consumer VARCHAR NOT NULL,
-- FOREIGN KEY(consumer) REFERENCES users(username)
-- };
--
-- CREATE TABLE exercises{
-- id INTEGER PRIMARY KEY,
-- workout VARCHAR,
-- duration INTEGER,
-- fdate VARCHAR,
-- consumer VARCHAR NOT NULL,
-- FOREIGN KEY(consumer) REFERENCES users(username)
-- };
