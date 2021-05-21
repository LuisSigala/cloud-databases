""" FLask configuration to the database """
from flask_pymongo import pymongo
import os

DB_USER = os.getenev("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")


client = pymongo.MongoClient(f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@db-example.du4lj.mongodb.net/{DB_NAME}?retryWrites=true&w=majority")

db = client.test
