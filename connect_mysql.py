import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",         # your MySQL username
    password="Utpr@1212",  # your MySQL password
    database="testdb"    # a database you have created
)

cursor = conn.cursor()

# Run a query
cursor.execute("SELECT * FROM students")

# Fetch and display results
for row in cursor.fetchall():
    print(row)

# Close connection
cursor.close()
conn.close()
