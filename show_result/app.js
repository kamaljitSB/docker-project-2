const express = require("express");
const session = require("express-session");
const fetch = require("node-fetch");
const app = express();

const http = require("http").createServer(app);
app.use(
  session({
    secret: "secret",
    resave: true,
    saveUninitialized: true,
  })
);
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static("public"));
app.set("view engine", "ejs");

const mysql = require("mysql2/promise");

const connection = mysql.createPool({
  host: "mysql-db",
  user: "dbuser",
  password: "dbpassword",
  database: "data_db",
  waitForConnections: true,
  connectionLimit: 10,
  queueLimit: 0,
});

http.listen(3000);

app.get("/", (req, res) => {
  res.render("./login.ejs");
});

app.get("/login", (req, res) => {
  res.render("./login.ejs");
});

app.post("/login", (req, res) => {
  let username = req.body.username;
  let password = req.body.password;
  const settings = {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
  };
  fetch(
    `http://auth:8090/login?username=${username}&password=${password}`,
    settings
  )
    .then((response) => response.status)
    .then(() => {
      //retrieve the data from the MySQL database
      connection
        .execute("SELECT * FROM summary ORDER BY id DESC LIMIT 1")
        .then(([result]) => {
          if (result.length == 0) {
            var items = {
              body: "No grades in the database yet.",
            };
            res.render("empty", items);
          } else {
            console.log(result);
            var items = {
              avg: result[0].avg,
              min_grade: result[0].min,
              max_grade: result[0].max,
            };
            res.render("grades_info.ejs", items);
          }
        })
        .catch((err) => {
          console.log(err);
          response.render("login.ejs");
        });
    })
    .catch((err) => {
      console.log(err);
      response.render("login.ejs");
    });
});

console.log("App running at http://localhost:3000/show");
