# lucas_marchel_test

# Ormuco challenge

## TECHNICAL TEST

## Question A

Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis and returns whether they overlap. As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).

## Question B

The goal of this question is to write a software library that accepts 2 version string as input and returns whether one is greater than, equal, or less than the other. As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of.

## Question C

At Ormuco, we want to optimize every bits of software we write. Your goal is to write a new library that can be integrated to the Ormuco stack. Dealing with network issues everyday, latency is our biggest problem. Thus, your challenge is to write a new Geo Distributed LRU (Least Recently Used) cache with time expiration. This library will be used extensively by many of our services so it needs to meet the following criteria:

1 - Simplicity. Integration needs to be dead simple.

2 - Resilient to network failures or crashes.

3 - Near real time replication of data across Geolocation. Writes need to be in real time.

4 - Data consistency across regions

5 - Locality of reference, data should almost always be available from the closest region

6 - Flexible Schema

7 - Cache can expire

As a hint, we are not looking for quantity, but rather quality, maintainability, scalability, testability and a code that you can be proud of. 
When submitting your code add the necessary documentation to explain your overall design and missing functionalities.  Do it to the best of your knowledge.

Clone this repository and start an server passing PORT, EXPIRATION_TIME and MAX_SIZE as environment variables as arguments.
Run main.py passing the same PORT as environment variable to connected to the recently created server.

I have created a small example that send 10 different data to the server and save it. These data will expire if it reach the expiration time supplied or if overcome the maximium size (memory capacity). Every time the data is inserted, it will show the entire database to check if everything is ok.
