FROM mongo:4.4-bionic

# ENV MONGO_INITDB_ROOT_USERNAME=root
# ENV MONGO_INITDB_ROOT_PASSWORD=root

# COPY create_mongodb_user.sh /docker-entrypoint-initdb.d/
# RUN chmod +x /docker-entrypoint-initdb.d/create_mongodb_user.sh


COPY create_mongodb_user.sh /docker-entrypoint-initdb.d/

# Set execute permissions on createuser.sh script
RUN chmod +x /docker-entrypoint-initdb.d/create_mongodb_user.sh

# Set environment variables for MongoDB
ENV MONGO_INITDB_ROOT_USERNAME=root \
    MONGO_INITDB_ROOT_PASSWORD=root \
    MONGO_INITDB_DATABASE=grades_db

# Expose port 27017
EXPOSE 27017

# Start MongoDB
CMD ["mongod"]

