import psycopg2
from optparse import OptionParser

def fetchRecords(lower, upper):
	conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
	cur = conn.cursor()
	cur.execute("SELECT * FROM tweetwordcount WHERE count>=%s AND count<=%s ORDER BY count DESC", (lower, upper))
	records = cur.fetchall()
	conn.commit()
	conn.close()
	return records


def main():
	parser = OptionParser()
	parser.add_option("-v", "--verbose", action = "store_true")

	(options, args) = parser.parse_args()

	if len(args) > 0:
		lower = int(args[0].split(',')[0])
		upper = int(args[0].split(',')[1])

		recs = fetchRecords(lower, upper)
		for r in recs:
			if (r[1]>=lower) and (r[1]<=upper):
				print ('%s: %d' % (r[0], r[1]))
	else:
		print "Wrong argument. Please follows the form: python histogram.py 3,8"

if __name__ == '__main__':
	main()
