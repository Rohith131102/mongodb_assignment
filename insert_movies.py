import datetime
from bson.objectid import ObjectId
import numpy as np

def insert_movies(movies):
    document= {
        "_id" : ObjectId(),
        "plot" : "Cartoon figures announce, via comic strip balloons, that they will move - and move they do, in a wildly exaggerated style.",
        "genres" : [
            "Animation",
            "Short",
            "Comedy"
        ],
        "runtime" : 7,
        "cast" : [
            "Winsor McCay"
        ],
        "num_mflix_comments" : 1,
        "poster" : "https://m.media-amazon.com/images/M/MV5BYzg2NjNhNTctMjUxMi00ZWU4LWI3ZjYtNTI0NTQxNThjZTk2XkEyXkFqcGdeQXVyNzg5OTk2OA@@._V1_SY1000_SX677_AL_.jpg",
        "title" : "Winsor McCay, the Famous Cartoonist of the N.Y. Herald and His Moving Comics",
        "fullplot" : "Cartoonist Winsor McCay agrees to create a large set of drawings that will be photographed and made into a motion picture. The job requires plenty of drawing supplies, and the cartoonist must also overcome some mishaps caused by an assistant. Finally, the work is done, and everyone can see the resulting animated picture.",
        "languages" : [
            "English"
        ],
        "released" : datetime.datetime(2022, 4, 1, 12, 30, 0),
        "directors" : [
            "Winsor McCay",
            "J. Stuart Blackton"
        ],
        "writers" : [
            "Winsor McCay (comic strip \"Little Nemo in Slumberland\")",
            "Winsor McCay (screenplay)"
        ],
        "awards" : {
            "wins" : 1,
            "nominations" : 0,
            "text" : "1 win."
        },
        "lastupdated" : datetime.datetime.now(),
        "year" : 1911,
        "imdb" : {
            "rating" : 7.3,
            "votes" : 1034,
            "id" : 1737
        },
        "countries" : [
            "USA"
        ],
        "type" : "movie",
        "tomatoes" : {
            "viewer" : {
                "rating" : 3.4,
                "numReviews" : 89,
                "meter" : 47
            },
            "lastUpdated" : datetime.datetime.now() }}
    result=movies.insert_one(document)
    print(result.inserted_id)