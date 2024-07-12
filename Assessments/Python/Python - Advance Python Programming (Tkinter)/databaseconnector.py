
import mysql.connector

try:
    conn = mysql.connector.connect(
        user='root',
        password='Priyank2289@',
        host='127.0.0.1',
        database='Product_Management_System'
    )

    if conn.is_connected():
        print("Connected to MySQL database.")
    else:
        print("Failed to connect to MySQL database.")

    mycursor = conn.cursor()

    # Now you can execute your SQL queries or perform other operations

except mysql.connector.Error as err:
    print("Error:", err)
