import os
import boto3
from dotenv import load_dotenv

load_dotenv()

access_key = os.getenv("AWS_ACCESS_KEY")
secret_key = os.getenv("AWS_SECRET_KEY")
region_name = os.getenv("AWS_REGION")
session_token = None

session = boto3.session.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        aws_session_token=session_token,
        region_name=region_name
)
        
