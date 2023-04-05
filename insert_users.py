import datetime
from bson.objectid import ObjectId
import numpy as np

def insert_users(users):
    document={
	"_id" : ObjectId(),
	"name" : input("Enter Name: "),
	"email" : input("Enter email: "),
	"password" : input("Enter password: ")
    }
    result=users.insert_one(document)
    print(result.inserted_id)


