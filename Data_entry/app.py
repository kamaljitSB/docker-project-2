from flask import Flask, request, render_template
import mysql.connector
import requests 

import os

app = Flask(__name__, template_folder="./sites")

@app.route("/")
def index():
    with open("./sites/login.html", "r") as file:
        return file.read()

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    print(username, password)

    response = requests.post(
        f"http://10.30.0.2:8090/login?username={username}&password={password}"
    )
    print("this is response: ",response.status_code)
    if response.status_code == 204:
        return render_template("enter.html")
    else:
        return render_template("login.html")

@app.route('/enter', methods=['POST'])
def enter():
    if request.method == 'POST':
        math = request.form['math']
        english = request.form['english']
        physics = request.form['physics']
        chemistry = request.form['chemistry']
        biology = request.form['biology']

        connection = mysql.connector.connect(
            host='10.30.0.3',
            user='dbuser',
            password='dbpassword',
            database='data_db',
            port=3306
        )
        cursor = connection.cursor()

        cursor.execute("INSERT INTO gpa_table (math, english, physics, chemistry, biology) VALUES (%s, %s, %s, %s, %s)", (math, english, physics, chemistry, biology,))

        connection.commit()
        cursor.close()
        connection.close

        return render_template("show_result.html")

if __name__ == '__main__':
    app.run(host="localhost", port=8080)