#!/bin/bash

DB_NAME="myDatabase"
COLLECTION_NAME="myCollection"
MONGO_HOST="localhost"
MONGO_PORT="27017"

# Find whether the documents were populated to secondary Replica set instance
mongosh --host $MONGO_HOST:$MONGO_PORT <<EOF
use $DB_NAME
db.$COLLECTION_NAME.find({}).toArray()
EOF
