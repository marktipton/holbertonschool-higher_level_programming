#!/usr/bin/python3
"""
Lists all cities from database hbtn_0e_4_usa
"""


import MySQLdb
import sys

def list_cities(username, password, database_name):
    """Lists all cities from the database hbtn0e_4_usa"""
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
        FROM cities
        ORDER BY cities.id
    """)

    results = cursor.fetchall()

    for city in results:
        print(city)

    cursor.close()
    db.close()

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    list_cities(username, password, database_name)
