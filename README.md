# ACIT 3495 Docker Project

Use docker to build a data collection and analytics system with six containerized microservices.

This project creates a simple application that allows user to enter their grades, then calucate and present user's max, min, and avg grades.

## Table of Contents

- [Getting Started](#Getting-Started)
  - [Prerequisites](#Prerequisites)
  - [Installation](#Installation)
  - [Teardown](#Teardown)
- [Application Architecture](#Application-Architecture)
  - [Data Entry](#Data-Entry)
  - [Authentication](#Authentication)
  - [MySQL](#MySQL)
  - [Analytics Service](#Analytics-Service)
  - [Mongo](#Mongo)
  - [Show Results](#Show-Results)
- [File Tree](#File-Tree)
- [Contributor](#Contributor)

## Getting Started

### Prerequisites

You need to have docker installed

### Installation

1. Clone the repository
2. Navigate to the repository directory in your terminal
3. Run `docker compose up`
4. Once docker containers are running, navigate to browser and enter `localhost:8080`

### Teardown

1. `Ctrl + C` to stop the running containers
2. Run `docker compose down`

## Application Architecture

The Data collection and Analytics System Architecture for this project:
![Application Architecture](architecture.PNG)

The features and functions for each containers are:

### Data Entry

The frontend web application that askes user to login with their username and password. This application was built using python.

Then POST the credentials to the Authentication container to verfiy their identites.

Once identity is authenticated, user will be redirected to the web page to enter grades for math, english, physics, chemistry, and biology.

Those data will be POST to MySQL container.

### Authentication

The Authentication service will use the credentials from Data Entry to verify user's identity. This service was built using python.

The Username and password are sent to the authentication service and Once credentials match it will return a status code which will be used in Data Entry to decide on the next action of either allowing user to input grades or prompt to login again.

### MySQL

MySQL container receives grades from Data Entry and insert into database _data_db_ table _gpa_table_.

### Analytics Service

The Analytics container retrieve grades from MySQL container and calculate the min, max and avg grades. Then write the data into Mongo database. Service built using python.

### Mongo

Store data from Analytics service into a databas grades_db table summary.

### Show Results

The Show Results container prompts the user to authenticate which the request is sent to the authentication service. Once authenticated the application will pull the min, max, and avg grade from Mongo database and display on a simple web app using node js.

### Docker-compose.yml

All the services are building using docker-compose.yml file. where their specific images, build, ports, volumes and networking information is configured.

Note: For networking specific IP addresses are required without it the container won't be able to talk to each other. So we specify a default subnet and gateway for the network and lease out an IP to each container within that subnet.

## File Tree

![File Tree](filetree.png)

## Contributor

- **Kamaljit Singh Bhullar**

- **Zhe Zhang**

- **Zhaotong Jia**
