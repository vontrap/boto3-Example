import boto3

s3 = boto3.client('s3')
s3.upload_file('/home/abas/Desktop/Boto3.Example/cloud.jpg1', 'abas-bucket', 'cloud.jpg1',)
