CREATE DATABASE IF NOT EXISTS data_db;

USE data_db;


CREATE TABLE IF NOT EXISTS gpa_table
    (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, 
    math VARCHAR(50) NOT NULL,
    english VARCHAR(50) NOT NULL,
    physics VARCHAR(50) NOT NULL,
    chemistry VARCHAR(50) NOT NULL,
    biology VARCHAR(50) NOT NULL)

      