import boto3
from credentials import session
import sys



def delete_bucket():

    if len(sys.argv)>1:
      s3 = session.resource('s3')
      bucket_name = sys.argv[1]
      try:
        bucket = s3.Bucket(bucket_name)
        bucket.objects.all().delete()
        print(f"Emptied the bucket: {bucket}")
        bucket.delete()
        print(f"Deleted the bucket: {bucket}")
      except Exception as error:
        print(f"Error deleting Bucket: {error}")   
    else:
      print("Please pass the bucket name which you want to be deleted!")

delete_bucket()      