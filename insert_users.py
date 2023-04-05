import datetime
from bson.objectid import ObjectId
import numpy as np

def insert_users(users):
    document={
	"_id" : ObjectId(),
	"name" : "Kannamma",
	"email" : "kannamma@gmail.com",
	"password" : "12345"
    }
    result=users.insert_one(document)
    print(result.inserted_id)


