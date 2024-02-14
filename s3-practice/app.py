import os
import boto3

s3 = boto3.resource('s3',region_name='ap-southeast-2')

for bucket in s3.buckets.all():
    print(bucket.name)
    
response = s3.create_bucket(
    Bucket='anjanibuck', 
    CreateBucketConfiguration={
        'LocationConstraint':'ap-southeast-2'
        })
print (response)


client = boto3.client('s3')
# client.put_object(Bucket='anjanibuck', Key='jan.txt', Body=b'January')
# client.put_object(Bucket='anjanibuck', Key='feb.txt', Body=b'February')
# client.put_object(Bucket='anjanibuck', Key='march.txt', Body=b'March')



my_bucket = s3.Bucket('anjanibuck')
local_folder="C:\\files"
lists = client.list_objects(Bucket='anjanibuck')['Contents']
 
for obj in lists:
    file_key = obj['Key']
    local_path = os.path.join(local_folder, file_key)
 
    client.download_file('anjanibuck', file_key, local_path)
 
    print(f"Downloaded {file_key} to {local_path}")



