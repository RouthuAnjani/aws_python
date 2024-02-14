import mysql.connector

try:
    connection=mysql.connector.connect(
        host="anjani-database-1.ctmaa6g0kdvh.ap-southeast-2.rds.amazonaws.com",
        user="admin",
        password="Admin123",
        database="anjani"
    )
    if connection.is_connected():
        print("Connected to the database")

        cursor=connection.cursor()
        cursor.execute("SELECT * FROM employees")
        rows = cursor.fetchall()

        # Process the result
        for row in rows:
            print(row[1:])

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the cursor and connection
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Connection closed")