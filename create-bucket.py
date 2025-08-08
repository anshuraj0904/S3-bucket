from credentials import session
import sys
import os
from dotenv import load_dotenv

if len(sys.argv)>1:   
    s3 = session.resource('s3')
    bucket_name=sys.argv[1]

    try:
        response = s3.create_bucket(Bucket=bucket_name,CreateBucketConfiguration={'LocationConstraint': os.getenv('AWS_REGION')})
        print("Bucket Created Successfully!")
    except Exception as error:
        print("Error while creating bucket: ", error)
else:
    print("Not enough arguments to move ahead!")
    sys.exit(1)