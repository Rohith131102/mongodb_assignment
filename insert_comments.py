import datetime
from bson.objectid import ObjectId
import numpy as np

def insert_comments(comments,movies):
    name=input("Enter name: ")
    title=input("Enter title of movie: ")
    email=input("Enter email: ")
    text=input("enter comments: ")
    

    document = {
    "name": name,
    "email": email,
    "movie_id": movies.find_one({"title": title},{"_id":1}).get("_id"),
    "text": text,
    "date": datetime.datetime.now()
     }
    result=comments.insert_one(document)
    print(result.inserted_id)