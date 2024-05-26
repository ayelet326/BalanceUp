from pymongo import MongoClient
from app.db_manegement.config import MONGODB_URI, DATABASE_NAME

client = MongoClient(MONGODB_URI)
db = client[DATABASE_NAME]


def get_database():
    return db
