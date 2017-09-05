import psycopg2
from optparse import OptionParser

#fetch all records in asc order by count
def fetchAndPrintRecords():
	conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
	cur = conn.cursor()
	cur.execute("SELECT * FROM tweetwordcount ORDER BY word ASC")
	records = cur.fetchall()
	conn.commit()
	conn.close()

	print [(r[0],r[1]) for r in records]

#fetch one record by key name
def fetchAndPrintOneRecord(searchword):
	conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
	cur = conn.cursor()
	cur.execute("SELECT word, count from Tweetwordcount WHERE word=%s", (searchword,))
	record = cur.fetchone()
	conn.commit()
	conn.close()

	if record:
		print ('Total number of occurances of "%s": %d' % (searchword, record[1]))
	else:
		print ('Total number of occurances of "%s": %d' % (searchword, 0))

def main():
	parser = OptionParser()
	parser.add_option("-v", "--verbose", action = "store_true")

	(options, args) = parser.parse_args()

	if len(args) > 0:
		fetchAndPrintOneRecord(args[0])
	else:
		fetchAndPrintRecords()


if __name__ == '__main__':
	main()
