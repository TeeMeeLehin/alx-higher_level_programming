#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd="", db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print("%s" % str(row))
