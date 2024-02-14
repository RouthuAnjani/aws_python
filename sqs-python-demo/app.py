import boto3

sqs=boto3.client('sqs')
queueUrl="https://sqs.ap-southeast-2.amazonaws.com/106129732153/web_queue234"
sqs.send_message(
    QueueUrl=queueUrl,
    MessageBody=('Welcome Anjani')
)
response=sqs.receive_message(QueueUrl=queueUrl)
for message in response['Messages']:
    print(message['Body'])


# create_queue
# response = sqs.create_queue(
#     QueueName='shruthicreate',
#     Attributes={},
#     tags={
#         'user': 'string'
#     }
# )
    


# delete_message
# response = client.delete_message(
#     QueueUrl='string',
#     ReceiptHandle='string'
# )
    
 
    
# delete_queue
# response = client.delete_queue(
#     QueueUrl='string'
# )
    

