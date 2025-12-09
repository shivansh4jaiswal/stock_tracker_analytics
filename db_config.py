import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Change if different
        password="Utpr@1212",
        database="stocks_db"
    )
