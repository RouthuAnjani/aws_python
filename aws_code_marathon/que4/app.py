import os
import boto3

s3 = boto3.resource('s3',region_name='ap-southeast-2')
client = boto3.client('s3')

my_bucket = s3.Bucket('anjanibuck')
# local_folder="C:\\files"
local_folder=input("Enter Path where files should be downloaded: ")
lists = client.list_objects(Bucket='anjanibuck')['Contents']
 
for obj in lists:
    file_key = obj['Key']
    local_path = os.path.join(local_folder, file_key)
 
    client.download_file('anjanibuck', file_key, local_path)
 
    print(f"Downloaded {file_key} to {local_path}")



