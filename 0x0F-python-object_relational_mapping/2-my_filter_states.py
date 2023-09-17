#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa starting with N"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd="", db=sys.argv[3], port=3306)
    cur = db.cursor()
    qry = "SELECT * FROM states WHERE name \
    LIKE BINARY {} ORDER BY states.id".format(sys.argv[4])
    cur.execute(qry)
    rows = cur.fetchall()
    for row in rows:
        print("%s" % str(row))

    cur.close()
    db.close()
