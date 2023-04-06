# Mongodb_assignment

##### Create a Python application to connect to MongoDB.
1. By using MongoClient from pymongo library connection is established between python application and local MongoDB server.

##### Bulk load the JSON files in the individual MongoDB collections using Python. MongoDB collections
1. For bulk loading the data I used subprocess. By using subprocess we can run mongoimport terminal command. 

##### Create Python methods and MongoDB queries to insert new comments, movies, theatres, and users into respective MongoDB collections.
1. Here, I created seperate methods for each collection to insert document. Document is given in dictionary format.
2. By using insert_one command I inserted documents into collections.


##### Find top 10 users who made the maximum number of comments
1. The function creates three pipeline stages using MongoDB aggregation pipeline operators.The first pipeline stage uses the $group operator to group comments by their "name" field, and calculates the count of comments for each group using the $sum operator.
2. The second pipeline stage uses the $sort operator to sort the resulting groups in descending order based on their count of comments.The third pipeline stage uses the $limit operator to limit the number of results to the top 10.

##### Find top 10 movies with most comments
1. The function creates three pipeline stages using MongoDB aggregation pipeline operators.The first pipeline stage uses the $group operator to group comments by their "movie_id" field, and calculates the count of comments for each group using the $sum operator.
2. The second pipeline stage uses the $sort operator to sort the resulting groups in descending order based on their count of comments.The third pipeline stage uses the $limit operator to limit the number of results to the top 10.

##### Given a year find the total number of comments created each month in that year
1. This function takes user input for a year, and then queries the comments collection to count the number of comments made each month in that year. First, it creates a matching variable which uses the $match operator to filter the comments by date, including only those that are within the specified year.
2. Then it creates a grouping variable which groups the comments by month and counts the number of comments made in each month. Next, it sorts the results by month using the sorting variable.

##### Find top `N` movies with the highest IMDB rating
1. This function takes input from the user for the value of n. It then queries the movies collection to find the top n movies based on their IMDB ratings, where the IMDB rating is not empty. 
2. The query uses find() method with a filter object to find documents that match the specified criteria. The sort() method is used to sort the results in descending order based on the IMDB rating, and limit() method is used to limit the results to n. 
3. Finally, the function prints the title and IMDB rating of each movie in the result.

##### Find top `N` movies with the highest IMDB rating in a given year
1. Similar to above query add condition ""year":{"$eq": year_}}" to validate year.

##### Find top `N` movies with highest IMDB rating with number of votes > 1000
1. Similar to above query add condition " "imdb.votes":{"$gt": 1000} } "to validate number of votes.

##### Find top `N` movies with title matching a given pattern sorted by highest tomatoes ratings
1.  Similar to above query add condition " "title":{"$regex": regex_} } "to validate pattern.

##### Find top `N` directors who created the maximum number of movies
1. This query takes an input value n, and then it performs an aggregation on the movies collection using the aggregate() method.
2. The pipeline stages of the aggregation are $unwind the directors field to create a separate document for each director.
3. $group the documents by directors and create a count field that contains the number of movies each director has directed.
4. $sort the documents by the count field in descending order.
5. $limit the number of documents to n.

##### Find top `N` directors who created the maximum number of movies in a given year
1. Similar to above query add match stage " {"$match":{"year":{"$eq": year_}}} " to validate year.

##### Find top `N` directors who created the maximum number of movies in a given genre
1. Similar to above query add match stage " {"$match":{"genres": {"$all" : genres_}}} " to validate genres.

##### Find top `N` actors who starred in the maximum number of movies
1. The function prompts the user to enter a value n. Then aggregation pipeline that performs the following operations on the movies collection:
2. $unwind the cast array to create a new document for each cast member in a movie.
3. $group the documents by cast to count the number of movies each cast member has acted in.
4. $sort the documents in descending order by the count field, which represents the number of movies.
5. $limit the output to n documents.

##### Find top `N` actors who starred in the maximum number of movies in a given year
1. Similar to above query add match stage " {"$match":{"year":{"$eq": year_}}} " to validate year.

##### Find top `N` actors who starred in the maximum number of movies in a given genre
1. Similar to above query add match stage " {"$match":{"genres": {"$all" : genres_}}} " to validate genres.

##### Find top `N` movies for each genre with the highest IMDB rating
1. The function prompts the user to enter a value of n and then performs an aggregation on the movies collection using the aggregate() method.
2. The aggregation pipeline consists of the following stages $match: This stage filters out any documents that do not have a value for the imdb.rating field.
3. $unwind: This stage splits the genres field into separate documents.
4. $sort: This stage sorts the documents by imdb.rating in descending order.
5. $group: This stage groups the documents by genres and creates an array of movie titles for each genre using the $push accumulator.
6. $project: This stage creates a new field called film that contains only the top n movies for each genre, using the $slice operator.
7. $sort: This stage sorts the documents by _id in ascending order.

##### Top 10 cities with the maximum number of theatres
1. It performs an aggregation pipeline using the $group, $sort, and $limit operators to find the top 10 cities with the highest number of theaters. The pipeline groups the theaters by city, counts the number of theaters in each city, sorts the result in descending order based on the count, and finally limits the result to the top 10 cities.

##### top 10 theatres nearby given coordinates
1. The function creates a 2dsphere index on the location.geo field of the theaters collection. Then, the function prompts the user to enter a longitude and a latitude. Using the $near operator, the function finds the 10 theaters closest to the given location, and returns the theaterId and location.geo fields for each theater.

