import pymysql
import pymongo
import connexion


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["grades_db"]
collection = db["summary"]

conn = pymysql.connect(
    host='localhost',
    user='dbuser',
    password='dbpassword',
    database='data_db'
)

cursor = conn.cursor()




print("db",db)
print("collection:", collection)



cursor.execute('SELECT * FROM gpa_table')

results = cursor.fetchall()

total = 0
min_grade = 0
max_grade = 0

for row in results:
    column = [int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5])]
    total = sum(column)
    avg = total / len(column)
    min_grade = min(*column)
    max_grade = max(*column)

print("Grades summary saved")

conn.close()

toInsert = {"avg": int(avg), "min": int(min_grade), "max":int(max_grade)}
print(toInsert)
collection.insert_one(toInsert)

client.close()

app = connexion.FlaskApp(__name__, specification_dir="")
# app.add_api("analytics.yaml")

if __name__ == "__main__":
    app.run(port=8100, threaded=True)





