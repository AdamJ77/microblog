#!/bin/bash

# Define variables
DB_NAME="myDatabase"
COLLECTION_NAME="myCollection"
MONGO_HOST="localhost"
MONGO_PORT="27017"

# Define the JSON documents to insert
DOCUMENT1='{"username":"johndoe","email":"johndoe@example.com","age":28}'
DOCUMENT2='{"username":"janedoe","email":"janedoe@example.com","age":25}'

# Command to connect to MongoDB and insert documents into collection
mongosh --host $MONGO_HOST:$MONGO_PORT <<EOF
use $DB_NAME
db.createCollection("$COLLECTION_NAME")
db.$COLLECTION_NAME.insertMany([$DOCUMENT1, $DOCUMENT2])
EOF
