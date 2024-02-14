import boto3

# # Replace these values with your own
# aws_access_key_id = 'YOUR_ACCESS_KEY'
# aws_secret_access_key = 'YOUR_SECRET_KEY'
# region_name = 'YOUR_REGION'
# table_name = 'YourTableName'

# Initialize DynamoDB client
dynamodb = boto3.client(
    'dynamodb',
    # aws_access_key_id=aws_access_key_id,
    # aws_secret_access_key=aws_secret_access_key,
    # region_name=region_name
)

# Define the table schema
table_schema = [
    {
        'AttributeName': 'studentId',
        'KeyType': 'HASH'  # Hash key
    },
    {
        'AttributeName': 'studentLName',
        'KeyType': 'RANGE'  # Sort key
    }
]

# Define the provisioned throughput for the table
provisioned_throughput = {
    'ReadCapacityUnits': 5,
    'WriteCapacityUnits': 5
}

# Create the table
dynamodb.create_table(
    TableName="mystudents",
    AttributeDefinitions=[
        {'AttributeName': 'studentId', 'AttributeType': 'N'},
        {'AttributeName': 'studentLName', 'AttributeType': 'S'}
    ],
    KeySchema=table_schema,
    ProvisionedThroughput=provisioned_throughput
)

print(f'Table {"mystudents"} created. Please wait for it to become active.')

# Wait for the table to become active
dynamodb.get_waiter('table_exists').wait(
    TableName="mystudents"
)

# Put some sample records into the table
items_to_put = [
    {'studentId': {'N': '101'}, 'studentLName': {'S': 'Routhu'}, 'studentFName': {'S': 'Anjani'}},
    {'studentId': {'N': '102'}, 'studentLName': {'S': 'Routhu'}, 'studentFName': {'S': 'Balaji'}},
    # Add more items as needed
]

for item in items_to_put:
    dynamodb.put_item(
        TableName="mystudents",
        Item=item
    )

print('Records added to the table.')