import mysql.connector

def import_data(con):
    cursor=con.cursor()

    DriverName=input("Enter name of the driver: ")
    CustomerName=input("Enter name of the customer: ")
    PassengerCount=int(input("Enter number of passengers: "))

    rides=[(DriverName,CustomerName,PassengerCount)]
    for ride in rides:
            cursor.execute("INSERT INTO ride_details (DriverName,CustomerName,PassengerCount) VALUES (%s,%s,%s)",ride)
    con.commit()
    print("Inserted Successfully.")

def main():
    con=None
    try:
        con=mysql.connector.connect(
        host="anjanir.ctmaa6g0kdvh.ap-southeast-2.rds.amazonaws.com",
        user="admin",
        password="Admin123",
        database="ride_details"
    )
        print("Connected to the database")
    except Exception as err:
             print(f"Error: {err}")
    if con is not None:
          import_data(con)
          con.close()
    return con
   

if __name__=="__main__":
        main()
            


