# Sqs and sns

import boto3
import mysql.connector

# AWS SQS configuration
sqs = boto3.client('sqs', region_name='eu-west-1')
queue_url = 'https://sqs.eu-west-1.amazonaws.com/106129732153/ruchitha'
 
# AWS SNS configuration
sns = boto3.client('sns', region_name='eu-west-1')
topic_arn = 'arn:aws:sns:eu-west-1:106129732153:ruchitha'
 
# MySQL configuration
db_host = 'ruchitha-bills.cj8000i6gxgi.eu-west-1.rds.amazonaws.com'
db_user = 'admin'
db_password = 'Ruchi123'
db_name = 'your_database_name'
 
try:
    # Establish database connection
    connection = mysql.connector.connect(host=db_host, user=db_user, password=db_password, database=db_name)
    cursor = connection.cursor()
 
    # Receive messages from SQS
    receive_message_request = {
        'QueueUrl': queue_url,
        'MaxNumberOfMessages': 5
    }
    rece_message_result = sqs.receive_message(**receive_message_request)
    print("Message received from SQS Queue")
 
    for message in rece_message_result.get('Messages', []):
        print("Message", message['Body'])
        print("Attributes", message['MessageAttributes'])
 
        # Publish message to SNS
        publish_request = {
            'TopicArn': topic_arn,
            'Message': message['Body']
        }
        sns.publish(**publish_request)
        print("Message Published")
 
except mysql.connector.Error as e:
    print(f"MySQL Error: {e}")
 
finally:
    # Close database connection
    if connection:
        connection.close()