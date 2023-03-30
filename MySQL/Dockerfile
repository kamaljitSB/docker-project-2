FROM mysql

ENV MYSQL_ROOT_PASSWORD root_password 
ENV MYSQL_USER dbuser
ENV MYSQL_PASSWORD dbpassword
ENV MYSQL_DATABASE data_db

ADD ./create_db.sql /docker-entrypoint-initdb.d
# COPY ./create_db.sql /tmp