#!/usr/bin/python3

""" Script that lists all states in a database """
import MySQLdb
import sys

if __name__ == '__main__':

    user = sys.argv[1]
    pwd = sys.argv[2]
    database = sys.argv[3]
	@@ -15,4 +16,3 @@
    for row in cur._rows:
        print(row)
