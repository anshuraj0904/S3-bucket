from credentials import session


s3_client = session.client('s3')
# Listing all the buckets:
buckets = s3_client.list_buckets()

if len(buckets["Buckets"])==0:
    print("No active S3 buckets at the moment!")
else:
    print("Your buckets list!")
    for bucket in buckets["Buckets"]:
       print(f" - {bucket['Name']}")

