# Mongodb_assignment

### Create a Python application to connect to MongoDB.
1. By using MongoClient from pymongo library connection is established between python application and local MongoDB server.

### Bulk load the JSON files in the individual MongoDB collections using Python. MongoDB collections
1. For bulk loading the data I used subprocess. By using subprocess we can run mongoimport terminal command. 

### Create Python methods and MongoDB queries to insert new comments, movies, theatres, and users into respective MongoDB collections.
1. Here, I created seperate methods for each collection to insert document. Document is given in dictionary format.
2. By using insert_one command I inserted documents into collections.


### Find top 10 users who made the maximum number of comments
1.In grouping, I grouped the comments collection using name and count is counted by using sum aggregate funtion.
2. In sorting, I sort the data based on count and given limit 10 in limiting.
3. These are passed to appregate pipelin.
