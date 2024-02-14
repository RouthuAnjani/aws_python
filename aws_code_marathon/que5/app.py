import boto3
 
sqs = boto3.client('sqs', region_name='ap-southeast-2')
queue_url = 'https://sqs.ap-southeast-2.amazonaws.com/106129732153/anjani_ride_requests'

Source=input("Enter your Source Address: ")
Destination=input("Enter your Destination Address: ")
rides=[(Source,Destination)]
for ride in rides:
    response = sqs.send_message(QueueUrl=queue_url, MessageBody=f"Book a ride from {Source} and {Destination}")
    print("Message Sent")
