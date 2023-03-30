import mysql.connector

db_conn = mysql.connector.connect(host="localhost", user="dbuser", 
password="dbpassword", database="data_db")

db_cursor = db_conn.cursor()

db_cursor.execute('''
    CREATE TABLE IF NOT EXISTS gpa_table
    (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, 
    math VARCHAR(50) NOT NULL,
    english VARCHAR(50) NOT NULL,
    physics VARCHAR(50) NOT NULL,
    chemistry VARCHAR(50) NOT NULL,
    biology VARCHAR(50) NOT NULL)
    ''')
db_conn.commit()
db_conn.close()
