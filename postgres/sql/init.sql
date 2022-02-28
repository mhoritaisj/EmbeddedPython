create database testdb ENCODING = 'UTF8';

\c testdb;

CREATE TABLE Anime (
  Rank INTEGER,
  Name VARCHAR(1024),
  Japanese_name VARCHAR(1024),
  Type VARCHAR(10),
  Episodes INTEGER,
  Studio VARCHAR(50),
  Release_season VARCHAR(50),
  Tags VARCHAR(8192),
  Rating NUMERIC(4, 2),
  Release_year INTEGER,
  End_year INTEGER,
  Description VARCHAR(8192),
  Content_Warning VARCHAR(8192),
  Related_Mange VARCHAR(8192),
  Related_anime VARCHAR(8192),
  Voice_actors VARCHAR(8192),
  staff VARCHAR(8192)
);
