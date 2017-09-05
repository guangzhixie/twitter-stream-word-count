from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt
from redis import StrictRedis

import psycopg2

class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()
        self.redis = StrictRedis()

        #clear database
        conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
        cur = conn.cursor()
        cur.execute('''DELETE FROM tweetwordcount''')
       	conn.commit()
        conn.close()

    def process(self, tup):
        #clean the word a bit
        word = tup.values[0].lower().replace("'","").replace("`","")
        # Increment the local count
        self.counts[word] += 1
        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))

        # Codes to increment the word count in Postgres
        # Use psycopg to interact with Postgres
        # Database name: tcount
        # Table name: tweetwordcount
        # Need to create both the database and the table in advance.
        conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
        cur = conn.cursor()
        if self.counts[word] == 1:
            #Insert
            cur.execute("INSERT INTO tweetwordcount (word,count) \
                  VALUES (%s, %s)", (word, self.counts[word]));
        else:
            #Update
            cur.execute("UPDATE tweetwordcount SET count=%s WHERE word=%s", (self.counts[word], word))
        conn.commit()
        conn.close()

        self.emit([word, self.counts[word]])
