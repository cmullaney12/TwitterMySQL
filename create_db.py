import MySQLdb as mysql
import configparser

## SQL Query for creating the twitter_rdb database
CREATE_DB = 'CREATE DATABASE IF NOT EXISTS twitter_rdb;'

## SQL Query to switch to the recently created database
USE_DB = 'USE twitter_rdb;'

## SQL Query to create the 'User' table.
## Columns:
## 		- uid: The User ID, a Unique, non-null, BIGINT number

CREATE_USER_TABLE = 'CREATE TABLE IF NOT EXISTS Users (' \
					'uid BIGINT UNIQUE NOT NULL, ' \
					'PRIMARY KEY (uid));'

## SQL Query to create the 'Tweets' table.
## Columns:
## 		- tweet_id: The Tweet ID, a non-null, BIGINT number that is auto incremented after each insert
## 		- user_id: The ID for the User who created this tweet
##		- tweet_ts: A datetime timestamp for when the tweet is inserted into the database
## 		- tweet_text: The actual content of the Tweet

CREATE_TWEET_TABLE = 'CREATE TABLE IF NOT EXISTS Tweets (' \
					   'tweet_id BIGINT NOT NULL AUTO_INCREMENT, ' \
					   'user_id BIGINT NOT NULL, ' \
					   'tweet_ts datetime DEFAULT CURRENT_TIMESTAMP, ' \
					   'tweet_text varchar(140) NOT NULL, ' \
					   'PRIMARY KEY (tweet_id), ' \
					   'FOREIGN KEY (user_id) REFERENCES Users (uid));'

## SQL Query to create the 'Followers' table.
## Columns:
## 		- user_id: The ID for the User who is doing the following
## 		- follows_id: The ID for the User who is being followed

CREATE_FOLLOWER_TABLE = 'CREATE TABLE IF NOT EXISTS Followers (' \
					    'user_id BIGINT NOT NULL, ' \
					    'follows_id BIGINT NOT NULL, ' \
					    'PRIMARY KEY (user_id, follows_id), ' \
					    'FOREIGN KEY (user_id) REFERENCES Users (uid), ' \
					    'FOREIGN KEY (follows_id) REFERENCES Users (uid));'

## Load the config file, containing the credentials for the database

config = configparser.ConfigParser()
config.read('config.txt')

## Get the proper host, username, and password credentials

host = config.get("db_credentials", "host")
user = config.get("db_credentials", "user")
passwd = config.get("db_credentials", "passwd")

## Connect to the MySQL database
db = mysql.connect(host=host, user=user, passwd=passwd)

## Create a cursor and execute our SQL queries
cursor = db.cursor()

## Create the twitter_rdb database
cursor.execute(CREATE_DB)

## Select the twitter_rdb database
cursor.execute(USE_DB)

## Create the Users table
cursor.execute(CREATE_USER_TABLE)

## Create the Tweets table
cursor.execute(CREATE_TWEET_TABLE)

## Create the Followers table
cursor.execute(CREATE_FOLLOWER_TABLE)

## Close the database connection
db.close()

