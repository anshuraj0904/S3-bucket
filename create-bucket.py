from credentials import session
import sys
import os
from dotenv import load_dotenv


def create_bucket():
    if len(sys.argv)>1:   
       s3 = session.resource('s3')
       bucket_name=sys.argv[1]

       try:
        response = s3.create_bucket(Bucket=bucket_name,CreateBucketConfiguration={'LocationConstraint': os.getenv('AWS_REGION')})
        # LocationConstarint is necessary while creating the bucket to ensure that the bucket is created at this very location.
        print("Bucket Created Successfully!")
       except Exception as error:
        print("Error while creating bucket: ", error)
    else:
        print("Not enough arguments to move ahead!")
        sys.exit(1)