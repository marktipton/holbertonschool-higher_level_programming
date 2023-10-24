#!/usr/bin/python3
"""
takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument.
"""


import MySQLdb
import sys

def list_states_Match(username, password, database_name, state_searched):
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database_name
    )

    cursor = db.cursor()
    # Execute SQL Query
    cursor.execute("""
        SELECT *
        FROM states
        WHERE name = state_searched
        ORDER BY states.id
    """)

    results = cursor.fetchall()

    for state in results:
        print(state)

    cursor.close()
    db.close()

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_searched = sys.argv[4]
    list_states_Match(username, password, database_name, state_searched)