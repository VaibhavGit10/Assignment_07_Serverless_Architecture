import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    # Auto-Stop Instances
    stop_instances = ec2.describe_instances(
        Filters=[
            {'Name': 'tag:Action', 'Values': ['Vaibhav_Auto_Stop']},
            {'Name': 'instance-state-name', 'Values': ['running']}
        ]
    )
    stop_ids = [i['InstanceId'] for r in stop_instances['Reservations'] for i in r['Instances']]
    if stop_ids:
        ec2.stop_instances(InstanceIds=stop_ids)
        print(f'Stopped Instances: {stop_ids}')
    else:
        print("No Auto-Stop instances found in running state.")

    # Auto-Start Instances
    start_instances = ec2.describe_instances(
        Filters=[
            {'Name': 'tag:Action', 'Values': ['Vaibhav_Auto_Start']},
            {'Name': 'instance-state-name', 'Values': ['stopped']}
        ]
    )
    start_ids = [i['InstanceId'] for r in start_instances['Reservations'] for i in r['Instances']]
    if start_ids:
        ec2.start_instances(InstanceIds=start_ids)
        print(f'Started Instances: {start_ids}')
    else:
        print("No Auto-Start instances found in stopped state.")
