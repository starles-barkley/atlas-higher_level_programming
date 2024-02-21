#!/usr/bin/python3
"""This module defines a function that establishes a connection to a SQL server"""

import MySQLdb
import sys

def sql_connect(usr, pw, db_name):
    """This function imports a database to use"""
