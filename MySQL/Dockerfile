FROM mysql

ENV MYSQL_ROOT_PASSWORD password 
ENV MYSQL_USER dbuser
ENV MYSQL_PASSWORD dbpassword
ENV MYSQL_DATABASE data_db

COPY init.sql /docker-entrypoint-initdb.d/1-init.sql
# Expose the MySQL port
EXPOSE 3306

# Start MySQL service
CMD ["mysqld"]