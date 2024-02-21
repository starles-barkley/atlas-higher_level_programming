#!/usr/bin/python3
"""This module defines a function that establishes a connection to a SQL server"""

import MySQLdb
import sys

def sql_connect(username, password, db_name):
    """This function imports a database to use"""
    try:
        """ Connect to the MySQL server"""
        connection = MySQLdb.connect(host="localhost",
                                     port=3306,
                                     user=username,
                                     passwd=password,
                                     db=database_name)
