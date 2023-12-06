from testcontainers.mongodb import MongoDbContainer
from pymongo.database import Database
from pymongo import MongoClient
import pytest


@pytest.fixture(scope="session")
def mongo_client() -> MongoClient:
    with MongoDbContainer() as mongo:
        yield mongo.get_connection_client()


@pytest.fixture
def mongo_db(request: pytest.FixtureRequest, mongo_client) -> Database:
    return getattr(mongo_client, request.node.name)


def test_mongo_insert_and_find(mongo_db: Database):
    doc = {
        "address": {
            "street": "2 Avenue",
            "zipcode": "10075",
            "building": "1480",
            "coord": [-73.9557413, 40.7720266],
        },
        "borough": "Manhattan",
        "cuisine": "Italian",
        "name": "Vella",
        "restaurant_id": "41704620",
    }
    mongo_db.restaurants.insert_one(doc)
    cursor = mongo_db.restaurants.find({"borough": "Manhattan"})
    assert cursor.next()["restaurant_id"] == doc["restaurant_id"]


# This test uses other db instance so no data will be found
def test_mongo_no_data(mongo_db: Database):
    cursor = mongo_db.restaurants.find({"borough": "Manhattan"})
    with pytest.raises(StopIteration):
        cursor.next()["restaurant_id"]
