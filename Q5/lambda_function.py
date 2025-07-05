import boto3
from datetime import datetime

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    # Debug log
    print(f"Received event: {event}")
    
    try:
        instance_id = event['detail']['instance-id']
        current_date = datetime.utcnow().strftime('%Y-%m-%d')

        # Create tags
        tags = [
            {'Key': 'LaunchDate', 'Value': current_date},
            {'Key': 'Environment', 'Value': 'Dev'}  # You can change this tag
        ]

        # Apply tags
        ec2.create_tags(Resources=[instance_id], Tags=tags)
        print(f"✅ Successfully tagged instance {instance_id} with {tags}")

    except Exception as e:
        print(f"❌ Failed to tag instance: {e}")
