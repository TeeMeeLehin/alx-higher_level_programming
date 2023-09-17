#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd="", db=sys.argv[3], port=3306)
    cur = db.cursor()
    qry = """SELECT * FROM states WHERE name=%s ORDER BY states.id""", (sys.argv[4],)
    cur.execute(qry)
    rows = cur.fetchall()
    for row in rows:
        print("%s" % str(row))

    cur.close()
    db.close()
