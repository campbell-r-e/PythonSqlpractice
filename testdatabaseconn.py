import mysql.connector
from mysql.connector import Error

try:
    testConnection = mysql.connector.connect(
        user="",
        password="",
        host="localhost",
        database="Company")
    
    if testConnection.is_connected():
        print("Connected to MySQL database")

except mysql.connector.Error as err:
    print("Cannot connect to database:", err)

else:
    # Execute database operations...
    testConnection.close()