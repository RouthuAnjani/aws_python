import boto3

sqs=boto3.client('sqs')
queueUrl="https://sqs.ap-southeast-2.amazonaws.com/106129732153/web_queue234"
sqs.send_message(
    QueueUrl=queueUrl,
    MessageBody=("Hi, You bill for month <MONTH-FROM_DB> is due. Please pay Rs <AMT-FROM-DB> in 15 days.")
)
response=sqs.receive_message(QueueUrl=queueUrl)
for message in response['Messages']:
    print(message['Body'])