import pymongo
from pymongo import MongoClient
import json
import subprocess
from bson.objectid import ObjectId
import numpy as np
import datetime
from insert_theaters import insert_theaters
from insert_users import insert_users
from insert_movies import insert_movies
from insert_comments import insert_comments
client = MongoClient('localhost',27017)
mydb = client["assignment"]

comments = mydb["comments"]
mongoimport_cmd = ['mongoimport', '--db', 'assignment', '--collection', 'comments', '--type', 'json','--file', '/Users/kothapallygnanapraneeth/Documents/Sigmoid/mongodb/Mongo_Assignment/Source/comments.json']
process = subprocess.Popen(mongoimport_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


movies = mydb["movies"]
mongoimport_cmd = ['mongoimport', '--db', 'assignment', '--collection', 'movies', '--type', 'json','--file', '/Users/kothapallygnanapraneeth/Documents/Sigmoid/mongodb/Mongo_Assignment/Source/movies.json']
process = subprocess.Popen(mongoimport_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


theaters = mydb["theaters"]
mongoimport_cmd = ['mongoimport', '--db', 'assignment', '--collection', 'theaters', '--type', 'json','--file', '/Users/kothapallygnanapraneeth/Documents/Sigmoid/mongodb/Mongo_Assignment/Source/theaters.json']
process = subprocess.Popen(mongoimport_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


users = mydb["users"]
mongoimport_cmd = ['mongoimport', '--db', 'assignment', '--collection', 'users', '--type', 'json','--file', '/Users/kothapallygnanapraneeth/Documents/Sigmoid/mongodb/Mongo_Assignment/Source/users.json']
process = subprocess.Popen(mongoimport_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# insert_movies(movies)
# insert_comments(comments,movies)
# insert_theaters(theaters)
# insert_users(users)

# Find top 10 users who made the maximum number of comments
def question4_a_1(comments):
    grouping={"$group": { "_id": "$name","count":{"$sum" : 1}}}
    sorting={"$sort":{"count": pymongo.DESCENDING}}
    limiting = { "$limit": 10 }
    result = comments.aggregate([grouping,sorting,limiting])
    for i in result:
        print(i)
    
# Find top 10 movies with most comments
def question4_a_2(comments,movies):
    grouping={"$group": { "_id": "$movie_id","count":{"$sum" : 1}}}
    sorting={"$sort":{"count": pymongo.DESCENDING}}
    limiting = { "$limit": 10 }
    result = comments.aggregate([grouping,sorting,limiting])
    for i in result:
        print("title:- " + movies.find_one({"_id":i.get("_id")},{"title":1,"_id":0}).get("title") + " count:- " + str(i.get("count")))


# Given a year find the total number of comments created each month in that year
def question4_a_3(comments):
    year_ = int(input("Enter year:- "))
    matching = {"$match":{'date': {'$gte': datetime.datetime(year_, 1, 1), '$lt': datetime.datetime(year_ + 1, 1, 1)} }}
    grouping = {"$group":{"_id": {"month":{"$month":"$date"}},"count":{"$sum":1}}}
    sorting = {"$sort":{"_id.month":1}}
    result = comments.aggregate([matching,grouping,sorting])
    for i in result:
        print(i)

# Find top `N` movies with the highest IMDB rating
def question4_b_1(movies):
    n=int(input("Enter n value: "))
    result = movies.find({"imdb.rating":{"$ne":''}},{"_id":0,"title":1,"imdb.rating":1}).sort("imdb.rating",-1).limit(n)
    for i in result:
        print(i)

# Find top `N` movies with the highest IMDB rating in a given year
def question4_b_2(movies):
    n= int(input("Enter n value: "))
    year_ = int(input(("Enter year value: ")))
    result = movies.find({"imdb.rating":{"$ne":''},"year":{"$eq": year_}},{"_id":0,"title":1,"imdb.rating":1,"year":1}).sort("imdb.rating",-1).limit(n)
    for i in result:
        print(i)

# Find top `N` movies with highest IMDB rating with number of votes > 1000
def question4_b_3(movies):
    n=int(input("Enter n value: "))
    result = movies.find({"imdb.rating":{"$ne":''},"imdb.votes":{"$gt": 1000} },{"_id":0,"title":1,"imdb.rating":1,"imdb.votes":1}).sort("imdb.rating",-1).limit(n)
    for i in result:
        print(i)

# Find top `N` movies with title matching a given pattern sorted by highest tomatoes ratings
def question4_b_4(movies):
    n=int(input("enter n value: "))
    regex_ = input("enter regex:- ")
    result = movies.find({"tomatoes.viewer.rating":{"$ne":''},"title":{"$regex": regex_} },{"_id":0,"title":1,"tomatoes.viewer.rating":1}).sort("tomatoes.viewer.rating",-1).limit(n)
    for i in result:
        print(i)


# Find top `N` directors who created the maximum number of movies
def question4_b_5(movies):
    n=int(input("Enter value of n: "))
    unwinding = {"$unwind": "$directors"}
    grouping={"$group":{"_id": "$directors", "count":{"$sum":1}}}
    sorting={"$sort":{"count":pymongo.DESCENDING}}
    limiting={"$limit": n}
    result=movies.aggregate([unwinding,grouping,sorting,limiting])
    for i in result:
        print(i)

# Find top `N` directors who created the maximum number of movies in a given year
def question4_b_6(movies):
    n=int(input("Enter value of n: "))
    year_ = int(input("Enter year: "))
    matching = {"$match":{"year":{"$eq": year_}}}
    unwinding = {"$unwind": "$directors"}
    grouping={"$group":{"_id": {"director" : "$directors", "year" : "$year"}, "count":{"$sum":1}}}
    sorting={"$sort":{"count":pymongo.DESCENDING}}
    limiting={"$limit": n}
    result=movies.aggregate([unwinding,matching,grouping,sorting,limiting])
    for i in result:
        print(i)

# Find top `N` directors who created the maximum number of movies in a given genre
def question4_b_7(movies):
    n=int(input("Enter value of n: "))
    val = int(input("Enter number of genres: "))
    genres_ = []
    for i in range(0,val):
        genre = input("Enter next genere: ")
        genres_.append(genre)
    matching = {"$match":{"genres": {"$all" : genres_}}}
    unwinding = {"$unwind": "$directors"}
    grouping={"$group":{"_id": "$directors", "count":{"$sum":1}}}
    sorting={"$sort":{"count":pymongo.DESCENDING}}
    limiting={"$limit": n}
    result=movies.aggregate([matching,unwinding,grouping,sorting,limiting])
    for i in result:
        print(i)

# Find top `N` actors who starred in the maximum number of movies
def question4_b_8(movies):
    n = int(input("Enter n value: "))
    unwinding = {"$unwind": "$cast"}
    grouping = {"$group":{"_id": "$cast", "count":{"$sum":1}}}
    sorting = {"$sort":{"count":pymongo.DESCENDING}}
    limiting = {"$limit": n}
    result = movies.aggregate([unwinding,grouping,sorting,limiting])
    for i in result:
        print(i)

# Find top `N` actors who starred in the maximum number of movies in a given year
def question4_b_9(movies):
    n = int(input("Enter n value: "))
    year_ = int(input("Enter year: "))
    matching = {"$match":{"year":{"$eq": year_}}}
    unwinding = {"$unwind": "$cast"}
    grouping = {"$group":{"_id": "$cast", "count":{"$sum":1}}}
    sorting = {"$sort":{"count":pymongo.DESCENDING}}
    limiting = {"$limit": n}
    result = movies.aggregate([matching,unwinding,grouping,sorting,limiting])
    for i in result:
        print(i)

# Find top `N` actors who starred in the maximum number of movies in a given genre
def question4_b_10(movies):
    n = int(input("Enter n value: "))
    val = int(input("Enter number of genres: "))
    genres_ = []
    for i in range(0,val):
        genre = input("Enter next genere: ")
        genres_.append(genre)
    matching = {"$match":{"genres": {"$all" : genres_}}}
    unwinding = {"$unwind": "$cast"}
    grouping = {"$group":{"_id": "$cast", "count":{"$sum":1}}}
    sorting = {"$sort":{"count":pymongo.DESCENDING}}
    limiting = {"$limit": n}
    result = movies.aggregate([matching,unwinding,grouping,sorting,limiting])
    for i in result:
        print(i)

#Find top `N` movies for each genre with the highest IMDB rating
def question4_b_11(movies):
    n=int(input("Enter value of n: "))
    matching = {"$match":{"imdb.rating":{"$ne":''}}}
    unwinding = {"$unwind": "$genres"}
    sorting1 = {"$sort": { "imdb.rating":-1}}
    grouping = {"$group":{"_id":"$genres", "film":{"$push": "$title"}}}
    project = {"$project": {"_id": 1, "film": {"$slice": ["$film", n]}}}
    sorting2 = {"$sort":{"_id":1}}
    result = movies.aggregate([matching,unwinding,sorting1,grouping,project,sorting2])
    for i in result:
        print(i)

# Top 10 cities with the maximum number of theatres
def question5_a(theaters):
    grouping={"$group": {"_id": "$location.address.city", "count":{"$sum":1}}}
    sorting = {"$sort":{"count":-1}}
    limiting = {"$limit":10}
    result = theaters.aggregate([grouping,sorting,limiting])
    for i in result:
        print(i)


# top 10 theatres nearby given coordinates
def question5_b(theaters):
    # longitude = -118.113953
    # latitude = 33.760466
    theaters.create_index([("location.geo", "2dsphere" )])
    longitude = float(input("Enter longitude: "))
    latitude = float(input("Enter latitude: "))
    result= theaters.find({ "location.geo":{ "$near":{"$geometry":{"type":"point","coordinates":[longitude,latitude]}}}},{"theaterId" : 1,"_id":0,"location.geo":1}).limit(10)
    for i in result:
        print(i)



while True:
    print("""
     enter 1 to insert movie \n 
     enter 2 to insert comments \n
     enter 3 to insert theaters \n
     enter 4 to insert users \n
     enter 5 to Find top 10 users who made the maximum number of comments \n
     enter 6 to Find top 10 movies with most comments \n
     enter 7 to find the total number of comments created each month in that year \n
     enter 8 to Find top `N` movies with the highest IMDB rating \n
     enter 9 to Find top `N` movies with the highest IMDB rating in a given year \n
     enter 10 to Find top `N` movies with highest IMDB rating with number of votes > 1000 \n
     enter 11 to Find top `N` movies with title matching a given pattern sorted by highest tomatoes ratings \n
     enter 12 to Find top `N` directors who created the maximum number of movies \n
     enter 13 to Find top `N` directors who created the maximum number of movies in a given year \n
     enter 14 to Find top `N` directors who created the maximum number of movies in a given genre
     enter 15 to Find top `N` actors who starred in the maximum number of movies \n
     enter 16 to Find top `N` actors who starred in the maximum number of movies in a given year \n
     enter 17 to Find top `N` actors who starred in the maximum number of movies in a given genre \n
     enter 18 to Find top `N` movies for each genre with the highest IMDB rating \n
     enter 19 to get Top 10 cities with the maximum number of theatres \n
     enter 20 to get  top 10 theatres nearby given coordinates \n
     enter 21 to stop the loop \n
    """)

    choice  = int(input("Enter your choice:- "))

    if(choice == 1):
        insert_movies(movies)
    elif(choice == 2):
        insert_comments(comments, movies)
    elif(choice == 3):
        insert_theaters(theaters)
    elif(choice == 4):
        insert_users(users)
    elif(choice == 5):
        question4_a_1(comments)
    elif(choice == 6):
        question4_a_2(comments, movies)
    elif(choice == 7):
        question4_a_3(comments)
    elif(choice == 8):
        question4_b_1(movies)
    elif(choice == 9):
        question4_b_2(movies)
    elif(choice == 10):
        question4_b_3(movies)
    elif(choice == 11):
        question4_b_4(movies)
    elif(choice == 12):
        question4_b_5(movies)
    elif(choice == 13):
        question4_b_6(movies)
    elif(choice == 14):
        question4_b_7(movies)
    elif(choice == 15):
        question4_b_8(movies)
    elif(choice == 16):
        question4_b_9(movies)
    elif(choice == 17):
        question4_b_10(movies)
    elif(choice == 18):
        question4_b_11(movies)
    elif(choice == 19):
        question5_a(theaters)
    elif(choice == 20):
        question5_b(theaters)
    elif(choice == 21):
        break






