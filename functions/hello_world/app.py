import json
import boto3

# boto3 S3 initialization
s3_client = boto3.client("s3")


def run(event, context):
   destination_bucket_name = 'rsr-bucket-test2'

   # event contains all information about uploaded object
 #  print("Event :", event)
   print("Hello world")
   # S3 copy object operation
#   s3_client.copy_object(source_bucket.objects, Bucket=destination_bucket_name, Key=object)

   return {
       'statusCode': 200,
       'body': json.dumps('Copy data from lmabda!')
   }