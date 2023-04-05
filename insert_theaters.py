import datetime
from bson.objectid import ObjectId
import numpy as np

def insert_theaters(theaters):
    document={
	"_id" : ObjectId(),
	"theaterId" : input("Enter TheaterId: "),
	"location" : {
		"address" : {
			"street1" : input("enter street1: "),
			"city" : input("Enter city: "),
			"state" : input("Enter sate: "),
			"zipcode" : input("Enter zipcode: ")
		},
		"geo" : {
			"type" : input("Enter Type: "),
			"coordinates" : [
				input("enter cordinate1: "),input("enter coordinate2 : ")
			]}}}
    result=theaters.insert_one(document)
    print(result.inserted_id)


