#!/usr/bin/python3
""" Your Comments Here """
import MySQLdb
import sys


If __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
            passwd+sys.argv[2], dbdb=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute("SELECT * FROM states")
    rows = c.fetchall()
    for row in rows:
        print(row)
        c.close()
        db.close()
