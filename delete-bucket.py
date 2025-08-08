import boto3
from credentials import session
import sys

s3 = session.resource('s3')

if len(sys.argv)>1:
    bucket_name = sys.argv[1]
    try:
       bucket = s3.Bucket(bucket_name)
       bucket.objects.all().delete()
       print(f"Emptied the bucket: {bucket}")
       bucket.delete()
       print(f"Deleted the bucket: {bucket}")
    except Exception as error:
        print(f"Error deleting Bucket: {bucket} as {error}")   
else:
    print("Not enough arguments!")