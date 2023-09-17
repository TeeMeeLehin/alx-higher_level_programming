#!/usr/bin/python3
"""  lists all cities from the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd="", db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities
                    JOIN states ON state_id=states.id ORDER BY cities.id""")
    rows = cur.fetchall()
    for row in rows:
        print("%s" % str(row))

    cur.close()
    db.close()
