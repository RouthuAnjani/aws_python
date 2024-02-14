# RDS with sqs
 
import boto3
import mysql.connector
 
# AWS SQS configuration
sqs = boto3.client('sqs', region_name='eu-west-1')
queue_url = 'https://sqs.eu-west-1.amazonaws.com/106129732153/ruchitha'
 
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
 
    # Send messages to SQS
    for row in rows:
        var1 = row[0]
        var3 = row[2]
        message_body = f"Your {var1} bill is {var3}"
        response = sqs.send_message(QueueUrl=queue_url, MessageBody=message_body)
        print("Message Sent:", response['MessageId'])
 
except mysql.connector.Error as e:
    print(f"MySQL Error: {e}")
 
finally:
    # Close database connection
    if connection:
        connection.close()