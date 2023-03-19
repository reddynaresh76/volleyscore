import mysql.connector
from mysql.connector import Error


def create_connection(host, user, password, database):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        print("MySQL Database connection successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def close_connection(connection):
    if connection:
        connection.close()
        print("MySQL connection closed")

