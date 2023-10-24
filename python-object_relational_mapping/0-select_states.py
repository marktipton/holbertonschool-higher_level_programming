#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""


import MySQLdb
import sys

def list_states(username, password, database_name):
    db = MySQLdb.connect(host="localhost", user=username, passwd=password,
    db=database_name)

    cursor = db.cursor()
    # Execute SQL Query
    cursor.execute("SELECT * FROM states ORDER BY states.id")

    results = cursor.fetchall()

    for state in results:
        print(state)

    cursor.close()
    db.close()

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    list_states(username, password, database_name)