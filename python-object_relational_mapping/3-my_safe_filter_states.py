#!/usr/bin/python3

""" displays all values in the states table but safe from injections  """

import MySQLdb
import sys


if __name__ == '__main__':

    user = sys.argv[1]
    pwd = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]
    db = MySQLdb.connect(host='localhost', user=user, passwd=pwd, db=database)
    cur = db.cursor()

    query = """SELECT *
        FROM states
        WHERE name = BINARY %s
        ORDER BY states.id;"""

    staterows = cur.execute(query, (state,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
