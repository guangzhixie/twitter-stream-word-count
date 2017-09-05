# Twitter Stream Word Count

Use Apache Storm to ingest live tweets from Twitter Stream API, and stores word count in Postgres database for further analysis

*****************************
Steps to run the application
*****************************

1. Create AWS EC2 instance using UCB W205 AMI
2. Make sure all the dependencies are there:
	* Python 2.7
	* virtualenv
	* lein
	* streamparse
	* psycopg2
	* tweepy
	* redis
3. Start Postgres DB
4. Download the project folder to your preferred location
5. Go into the project folder
6. Run dbsetup python script to create databse and table:
	$ python dbsetup.py
7. Go into tweetwordcount folder:
	$ cd tweetwordcount
8. Run storm application:
	$ sparse run
9. You may see the following warning:
	* WARNING: You're currently running as root; probably by accident.
	* Press control-C to abort or Enter to continue as root.
	* Set LEIN_ROOT to disable this warning.
10. Just press enter to continue
11. Application should be running now. You can exit with Ctrl-C


*********************************
Steps to run the serving scripts
*********************************

1. Go into the project folder
2. Go into serves folder
	$ cd serves
3. Get all the words with their total count of occurrences, sorted alphabetically in an ascending order:
	$ python finalresults.py
4. Get counts for a particular word:
	$ python finalresults.py <your word>
5. Get counts for a range ordered by their total number of occurrences:
	$ python histogram.py <lower>,<upper>