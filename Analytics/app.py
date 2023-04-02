import pymysql
import connexion


conn = pymysql.connect(
    host='mysql-db',
    user='dbuser',
    password='dbpassword',
    database='data_db',
    port=3306
)

cursor = conn.cursor()

cursor.execute('SELECT * FROM gpa_table')

results = cursor.fetchall()

total = 0
min_grade = 0
max_grade = 0
avg = 0

for row in results:
    column = [int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5])]
    total = sum(column)
    avg = total / len(column)
    min_grade = min(*column)
    max_grade = max(*column)

print("Grades summary saved")

cursor.execute('TRUNCATE TABLE summary')
cursor.execute('INSERT INTO summary (avg, min, max) VALUES (%s, %s, %s)', (int(avg), int(min_grade), int(max_grade)))
conn.commit()

conn.close()

app = connexion.FlaskApp(__name__, specification_dir="")
# app.add_api("analytics.yaml")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8100, threaded=True)
