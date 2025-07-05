import boto3
from datetime import datetime, timezone, timedelta

# Set your bucket name here
BUCKET_NAME = 'vaibhav-s3-cleanup'

# Set how many days old the files should be to delete (for testing, we use 1 day)
DAYS_OLD = 30

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    deleted_files = []
    
    # Get current time in UTC
    now = datetime.now(timezone.utc)
    
    try:
        response = s3.list_objects_v2(Bucket=BUCKET_NAME)
        objects = response.get('Contents', [])
        
        for obj in objects:
            key = obj['Key']
            last_modified = obj['LastModified']
            
            age = now - last_modified
            
            if age > timedelta(days=DAYS_OLD):
                print(f"🗑 Deleting: {key} (Age: {age})")
                s3.delete_object(Bucket=BUCKET_NAME, Key=key)
                deleted_files.append(key)
        
        print(f"✅ Deleted {len(deleted_files)} files: {deleted_files}")
        return {
            'statusCode': 200,
            'body': f"Deleted {len(deleted_files)} files: {deleted_files}"
        }

    except Exception as e:
        print(f"❌ Error: {e}")
        return {
            'statusCode': 500,
            'body': f"Error: {e}"
        }
