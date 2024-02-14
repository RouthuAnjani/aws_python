import boto3
client = boto3.client('sns')
response = client.list_topics()
for topic in response['Topics']:
    arn = topic['TopicArn']
    name = arn.split(':')
    print ("Topic Name: ",name[5])
    response=client.list_subscriptions_by_topic(TopicArn=arn)
    for sub in response['Subscriptions']:
        print("[{}] {}".format(sub['Protocol'],sub['Endpoint']))

client.publish(
             TopicArn = "arn:aws:sns:ap-southeast-2:106129732153:my_news",
             Message = "Hi This is Anjani",
             Subject ="Welcome"
  )
print("Response Sent..!!")


