import boto3
sns = boto3.resource("sns")
topic = sns.create_topic(Name='Discount-offers-anjani')
protocol='Email'
endpoint='anjanirouthu@gmail.com'
topic.subscribe(Protocol=protocol,Endpoint=endpoint,ReturnSubscriptionArn=True)
topic.publish(Message = "Hi This is Anjani",Subject ="Welcome")


# topic.confirm_subscription(
#     Token='string',
#     AuthenticateOnUnsubscribe='string'
# )

# delete_topic
# response = client.delete_topic(
#     TopicArn='string'
# )

# unsubscribe
# response = client.unsubscribe(
#     SubscriptionArn='string'
# )