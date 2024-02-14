import boto3
import mysql.connector
 
# AWS configuration
client = boto3.client('sns')
topic_arn = "arn:aws:sns:ap-southeast-2:106129732153:bill-alerts-anjani"

try:
    connection = mysql.connector.connect(
        host = "adb.ctmaa6g0kdvh.ap-southeast-2.rds.amazonaws.com",
        user = "admin",
        password = "Admin123",
        database = "bills"
    )
 
    if connection.is_connected():
        cursor = connection.cursor()
 
        # cursor.execute('select count(month) from utility_bills')
        # total_bills = cursor.fetchall()
        # print(total_bills)
 
        cursor.execute('select * from utilitybills')
 
        rows = cursor.fetchall()
 
        for row in rows:
            # print(row)
            client.publish(TopicArn =topic_arn, Message="Hi,\n You bill for month {} is due. Please pay Rs {} in 15 days.".format(row[1],row[3]))
            print("Mail sent successfully")
 
except mysql.connector.Error as err:
    print("Error found as {}".format(err))
 
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Connection closed")