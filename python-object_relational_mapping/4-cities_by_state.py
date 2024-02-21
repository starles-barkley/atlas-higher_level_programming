#!/usr/bin/python3

""" This finds all cities and the state they're in in the database """

import MySQLdb
import sys


if __name__ == '__main__':

    user = sys.argv[1]
    pwd = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(host='localhost', user=user, passwd=pwd, db=database)
    cur = db.cursor()

    query = """SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states
        ON states.id = cities.state_id
        ORDER BY cities.id;"""

    staterows = cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
