# RDS with sns
 
import boto3
import mysql.connector
 
# AWS SNS configuration
client = boto3.client('sns', region_name='eu-west-1')
topic_arn = 'arn:aws:sns:eu-west-1:106129732153:ruchitha-topic'
 
# Database configuration
db_host = 'ruchitha-bills.cj8000i6gxgi.eu-west-1.rds.amazonaws.com'
db_user = 'admin'
db_password = 'Ruchi123'
db_name = 'bills'
 
try:
    # Establish database connection
    connection = mysql.connector.connect(host=db_host, user=db_user, password=db_password, database=db_name)
    cursor = connection.cursor()
 
    # Query database
    cursor.execute("SELECT * FROM utilitytable")
    rows = cursor.fetchall()
 
    # Publish messages to SNS
    for row in rows:
        month = row[0]
        amount = row[2]
        message = f"Your bill for the month {month} is: {amount} monthly bills"
        client.publish(TopicArn=topic_arn, Message=message)
        print("Published")
 
except mysql.connector.Error as e:
    print(f"MySQL Error: {e}")
 
finally:
    # Close database connection
    if connection:
        connection.close()