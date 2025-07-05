import boto3
import os

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    # Read environment variables
    instance_id = os.environ['INSTANCE_ID']
    ami_id = os.environ['AMI_ID']
    instance_type = os.environ['INSTANCE_TYPE']
    key_name = os.environ['KEY_NAME']
    security_group_id = os.environ['SECURITY_GROUP_ID']
    subnet_id = os.environ['SUBNET_ID']
    availability_zone = os.environ['AVAILABILITY_ZONE']

    try:
        # Step 1: Get the volume attached to the original EC2 instance
        response = ec2.describe_instances(InstanceIds=[instance_id])
        volume_id = response['Reservations'][0]['Instances'][0]['BlockDeviceMappings'][0]['Ebs']['VolumeId']
        print(f"✅ Original Volume ID: {volume_id}")

        # Step 2: Get the latest snapshot for that volume
        snapshots_response = ec2.describe_snapshots(
            Filters=[{'Name': 'volume-id', 'Values': [volume_id]}],
            OwnerIds=['self']
        )

        snapshots = snapshots_response.get('Snapshots', [])
        print(f"🔍 Number of snapshots found: {len(snapshots)}")

        if not snapshots:
            print("❌ No snapshots found for volume.")
            return {
                'statusCode': 500,
                'body': 'Error: No snapshots found for the volume.'
            }

        snapshots = sorted(snapshots, key=lambda x: x['StartTime'], reverse=True)
        latest_snapshot_id = snapshots[0]['SnapshotId']
        print(f"✅ Latest Snapshot ID: {latest_snapshot_id}")

        # Wait for snapshot to be in 'completed' state
        print(f"⏳ Waiting for snapshot {latest_snapshot_id} to become available...")
        snapshot_waiter = ec2.get_waiter('snapshot_completed')
        snapshot_waiter.wait(SnapshotIds=[latest_snapshot_id])
        print(f"✅ Snapshot {latest_snapshot_id} is now completed.")

        # Step 3: Create a new volume from the snapshot
        volume_response = ec2.create_volume(
            SnapshotId=latest_snapshot_id,
            AvailabilityZone=availability_zone,
            VolumeType='gp2',
            TagSpecifications=[
                {
                    'ResourceType': 'volume',
                    'Tags': [{'Key': 'Name', 'Value': 'RestoredVolume'}]
                }
            ]
        )
        new_volume_id = volume_response['VolumeId']
        print(f"🆕 New Volume ID: {new_volume_id}")

        # Wait until the new volume is available
        waiter = ec2.get_waiter('volume_available')
        waiter.wait(VolumeIds=[new_volume_id])
        print(f"✅ New volume {new_volume_id} is now available.")

        # Step 4: Launch a new EC2 instance using the snapshot-based volume
        instance_response = ec2.run_instances(
            ImageId=ami_id,
            InstanceType=instance_type,
            KeyName=key_name,
            MinCount=1,
            MaxCount=1,
            NetworkInterfaces=[{
                'DeviceIndex': 0,
                'SubnetId': subnet_id,
                'AssociatePublicIpAddress': True,
                'Groups': [security_group_id]
            }],
            BlockDeviceMappings=[
                {
                    'DeviceName': '/dev/xvda',
                    'Ebs': {
                        'SnapshotId': latest_snapshot_id,
                        'VolumeSize': 8,
                        'VolumeType': 'gp2',
                        'DeleteOnTermination': True
                    }
                }
            ],
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [{'Key': 'Name', 'Value': 'RestoredEC2'}]
                }
            ]
        )

        new_instance_id = instance_response['Instances'][0]['InstanceId']
        print(f"✅ New EC2 Instance launched: {new_instance_id}")

        return {
            'statusCode': 200,
            'body': f'Successfully launched new EC2 instance from snapshot: {new_instance_id}'
        }

    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
        }
