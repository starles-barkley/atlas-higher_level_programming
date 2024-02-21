#!/usr/bin/python3

""" displays all values in the states table of hbtn_0e_0_usa where name matches the argument """

import MySQLdb
import sys


if __name__ == '__main__':

    user = sys.argv[1]
    pwd = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]
    db = MySQLdb.connect(host='localhost', user=user, passwd=pwd, db=database)
    cur = db.cursor()

    staterows = cur.execute(
        """SELECT *
        FROM states
        WHERE name=BINARY '{}'
        ORDER BY states.id;""".format(state)
        )
    for row in cur._rows:
        print(row)