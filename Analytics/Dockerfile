FROM python:latest


COPY . . 

#install connexion
RUN pip install connexion

#install sqlalchemy
RUN pip install SQLAlchemy


#install pymysql and mysql.connector
RUN pip install pymysql
RUN pip install mysql.connector
RUN pip install mongoengine
RUN pip install pymongo
RUN pip install pandas


EXPOSE 8100

#install yaml
RUN pip install pyyaml


CMD ["python", "./app.py"]