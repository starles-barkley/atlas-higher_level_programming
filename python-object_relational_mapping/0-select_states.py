#!/usr/bin/python3
""" This script lists all states in a database """ 
import sys
import MySQLdb

def list_states(username, password, database_name):
    try:
        # Connect to the MySQL server
        connection = MySQLdb.connect(host="localhost",
                                     port=3306,
                                     user=username,
                                     passwd=password,
                                     db=database_name)

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Execute the SQL query to retrieve states
        query = "SELECT * FROM states ORDER BY states.id ASC"
        cursor.execute(query)

        # Fetch all the rows
        rows = cursor.fetchall()

        # Display the results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == "__main__":
    # Check if all 3 arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <mysql_username> <mysql_password> <database_name>")
    else:
        # Extract arguments
        mysql_username, mysql_password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]

        # Call the function to list states
        list_states(mysql_username, mysql_password, database_name)
