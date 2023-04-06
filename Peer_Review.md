# MongoDB Assignment Peer Review

### Rithish Assignment Review

1. He created a Python application to connect to the MongoDB server by using the Pymongo library.
2. He loaded the bulk data to the MongoDB database from the command line using the Mongoimport command.

### Find top 10 users who made the maximum number of comments
1. He used aggregation pipeline to group the comments by the name field, count the number of comments made by each user, sort the results in descending order of the comment count, limit the output to 10 documents, and project only the User and count fields while excluding the _id field. The resulting documents are printed using the pprint() function.

### Find top 10 movies with most comments
1. By using aggregation pipeline to group the comments by the movie_id field, count the number of comments for each movie, sort the results in descending order of the comment count, and limit the output to 10 documents.


### Given a year find the total number of comments created each month in that year
1. Aggregation pipeline is used to project the year and month fields from the date field, match only the documents that correspond to the given year, group the documents by month and count the number of comments made each month, project only the month and count fields while excluding the _id field, and finally sort the results by month in ascending order.

### Find top `N` movies with the highest IMDB rating
The pipeline consists of four stages The first stage filters out movies that do not have an IMDB rating.The second stage sorts the remaining movies by IMDB rating in descending order.The third stage limits the output to N movies.
The fourth stage projects only the movie title and IMDB rating, and excludes the "_id" field.
