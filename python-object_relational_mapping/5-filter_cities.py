#!/usr/bin/python3
"""
Lists all cities from database hbtn_0e_4_usa
"""


import MySQLdb
import sys


def list_cities(username, password, database_name, state_name):
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
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name LIKE BINARY '{}'
        ORDER BY cities.id
    """.format(state_name))

    results = cursor.fetchall()

    cities = [city[0] for city in results]
    cities_string = ', '.join(cities)
    print(cities_string)

    cursor.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]
    list_cities(username, password, database_name, state_name)
