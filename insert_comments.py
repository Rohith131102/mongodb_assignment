import datetime
from bson.objectid import ObjectId
import numpy as np

def insert_comments(comments,movies):
    document = {
    "name": "Kannamma",
    "email": "Kannamma@gmail.com",
    "movie_id": ObjectId("573a1390f29313caabcd413b"),
    "text": "Super movie",
    "date": datetime.datetime.now()
     }
    result=comments.insert_one(document)
    print(result.inserted_id)