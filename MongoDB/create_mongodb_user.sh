#!/bin/bash

until mongo --eval "print(\"waiting for connection\")" &> /dev/null; do sleep 1; done

mongo --eval "db.createUser({user: '$MONGO_INITDB_ROOT_USERNAME', pwd: '$MONGO_INITDB_ROOT_PASSWORD', roles: [{role: 'root', db: 'admin'}]})"


# until mongo --eval "print(\"waiting for connection\")" &> /dev/null; do sleep 1; done

# mongo --eval "use grades_db; db.createUser({user: 'root', pwd: 'root', roles: [{role: 'readWrite', db: 'grades_db'}]})"

