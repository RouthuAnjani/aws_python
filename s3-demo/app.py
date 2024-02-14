# import boto3

# s3 = boto3.resource('s3',region_name='ap-southeast-2')

# for bucket in s3.buckets.all():
#     print(bucket.name)
#     # client.delete_bucket (Bucket=bucket.name)
    
# response = s3.create_bucket(
#     Bucket='zabcd36468', 
#     CreateBucketConfiguration={
#         'LocationConstraint':'ap-southeast-2'
#         })
# print (response)

# ## Get the S3 client to perform CRUD on bucket objects
# client = boto3.client('s3')
# client.put_object(Bucket='zabcd36468', Key='file101.txt', Body=b'Hello World')

# client.delete_bucket (Bucket="cm08-vvh-bk")

#Deleting the entire bucket which is not empty
# import boto3

# s3 = boto3.resource('s3')
# client = boto3.client('s3')

# s3_bucket = s3.Bucket("cm08-vvh-bk")
# bucket_versioning = s3.BucketVersioning("cm08-vvh-bk")
# if bucket_versioning.status == 'Enabled':
#     s3_bucket.object_versions.delete()

# else:
#     s3_bucket.objects.all().delete()
#     client.delete_bucket (Bucket="cm08-vvh-bk")

# or

# response = client.delete_object(
#     Bucket='examplebucket',
#     Key='objectkey.jpg',
# )
# print(response)


# list buckets
# response = client.list_buckets()



# copy bucket
# import boto3
# s3 = boto3.resource('s3')
# copy_source = {
#     'Bucket': 'zabcd36468',
#     'Key': 'file101.txt'
# }
# s3.meta.client.copy(copy_source, 'f1-reports', 'file10.txt')



# download only one file
# import boto3
# s3 = boto3.resource('s3', region_name= "ap-northeast-2")
# client = boto3.client('s3')
# client.download_file(Bucket = "trying12333", Key = "jan.txt", Filename="D:/awsfile/AWS_notes.txt")