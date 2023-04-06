# MongoDB Assignment Peer Review

### Rithish Assignment Review

1. He created a Python application to connect to the MongoDB server by using the Pymongo library.
2. He loaded the bulk data to the MongoDB database from the command line using the Mongoimport command.

##### Find top 10 users who made the maximum number of comments
1. He used aggregation pipeline to group the comments by the name field, count the number of comments made by each user, sort the results in descending order of the comment count, limit the output to 10 documents, and project only the User and count fields while excluding the _id field. The resulting documents are printed using the pprint() function.

##### Find top 10 movies with most comments
1. By using aggregation pipeline to group the comments by the movie_id field, count the number of comments for each movie, sort the results in descending order of the comment count, and limit the output to 10 documents.


##### Given a year find the total number of comments created each month in that year
1. Aggregation pipeline is used to project the year and month fields from the date field, match only the documents that correspond to the given year, group the documents by month and count the number of comments made each month, project only the month and count fields while excluding the _id field, and finally sort the results by month in ascending order.

##### Find top `N` movies with the highest IMDB rating
1. The pipeline consists of four stages The first stage filters out movies that do not have an IMDB rating.The second stage sorts the remaining movies by IMDB rating in descending order.The third stage limits the output to N movies.
2. The fourth stage projects only the movie title and IMDB rating, and excludes the "_id" field.


##### Find top `N` movies with the highest IMDB rating in given year
1. Similar to above question add year validation parameter to above query.

#### Find top `N` movies with highest IMDB rating with number of votes > 1000
1. Similar to above question in match add condition to check imbd.votes is greater than 1000 or not using "$gte" operator.

#### Find top 'N' movies with title matching a given pattern sorted by highest tomatoes ratings
1. In this question pattern is matched using regex "$regex" operator rest of the pipeline is same.

#### Find top `N` directors who created the maximum number of movies
1. The method executes an aggregation pipeline the first stage unwinds the "directors" array field in each movie document to create a separate document for each director.The second stage groups the movie documents by director and calculates the count of movies per director using the "$sum" accumulator.
2. The third stage sorts the directors by the number of movies they have directed in descending order.The fourth stage projects only the director's name and the number of movies they have directed, and excludes the "_id" field.The fifth stage limits the output to N documents.


#### Find top `N` directors who created the maximum number of movies in a given year
1. Similar to above query add match {"$match":{"year":year}} stage to the pipeline for validating year.


#### Find top `N` directors who created the maximum number of movies for a given genre
1. Similar to above query add match {"$match":{"genres":genre}} stage to the pipeline for validating genres.

#### Find top `N` actors who starred in the maximum number of movies
1. The method executes an aggregation pipeline the first stage "unwinds" the "cast" array field in each movie document to create a separate document for each actor. The second stage groups the movie documents by actor and calculates the count of movies per actor using the "$sum" accumulator.
2. The third stage sorts the actors by the number of movies they have appeared in, in descending order. The fourth stage projects only the actor's name and the number of movies they have appeared in, and excludes the "_id" field. The fifth stage limits the output to N documents.

#### Find top `N` actors who starred in the maximum number of movies in a given year
1. Similar to above query add match {"$match":{"year":year}} stage to the pipeline for validating year.

#### Find top `N` actors who starred in the maximum number of movies in a given genre
1. Similar to above query add match {"$match":{"genres":genre}} stage to the pipeline for validating genres.

#### Top 10 cities with the maximum number of theatres
1. The method executes an aggregation pipeline consists of four stages the first stage groups the theaters documents by city and calculates the count of theaters per city using the "$sum" accumulator.
2.The second stage sorts the cities by the number of theaters in descending order. The third stage projects only the city name and the count of theaters, and excludes the "_id" field. The fourth stage limits the output to 10 documents.


#### top 10 theatres nearby given coordinates
1. The method first creates a 2dsphere index on the "location.geo" field of the collection using the create_index method. 
2. The method then constructs a query using the find method on the theaters collection with a $near operator, which returns documents that are closest to the given coordinates. 
3. The "$near" operator requires a 2dsphere index to be created on the field being queried. The query specifies the $geometry parameter with the type and coordinates fields to define the point location to search for. 
4. The projection parameter specifies which fields to include in the result set.
