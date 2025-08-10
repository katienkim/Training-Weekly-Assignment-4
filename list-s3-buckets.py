import boto3

bucketList = []
s3 = boto3.resource('s3')
clients3 = boto3.client('s3')

for bucket in s3.buckets.all():
    currbucket = {}
    name = bucket.name
    region = clients3.get_bucket_location(Bucket=name)['LocationConstraint']
    if region is None:
        region = 'us-east-1'
    if region == 'EU':
        region = 'eu-west-1'

    currbucket["Name"] = name
    currbucket["URL"] = f'http://{name}.s3-website.{region}.amazonaws.com'
    currbucket["Encrypted"] = clients3.get_bucket_encryption(Bucket=name)['ServerSideEncryptionConfiguration']['Rules'][0]['BucketKeyEnabled']
    bucketList.append(currbucket)

print(bucketList)