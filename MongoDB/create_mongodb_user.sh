#!/bin/bash

until mongo --eval "print(\"waiting for connection\")" &> /dev/null; do sleep 1; done

mongo --eval "db.createUser({user: '$MONGO_INITDB_ROOT_USERNAME', pwd: '$MONGO_INITDB_ROOT_PASSWORD', roles: [{role: 'root', db: 'admin'}]})"

