import datetime
from bson.objectid import ObjectId
import numpy as np

def insert_theaters(theaters):
    document={
	"_id" : ObjectId(),
	"theaterId" : 1234,
	"location" : {
		"address" : {
			"street1" : "Gandi",
			"city" : "Pembarthy",
			"state" : "telanagana",
			"zipcode" : "506201"
		},
		"geo" : {
			"type" : "Point",
			"coordinates" : [
				-118.113953,
                33.760466
			]}}}
    result=theaters.insert_one(document)
    print(result.inserted_id)


