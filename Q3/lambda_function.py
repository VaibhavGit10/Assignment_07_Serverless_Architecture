import boto3
import botocore
import time

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    encrypted_buckets = []
    unencrypted_buckets = []

    try:
        buckets = s3.list_buckets().get('Buckets', [])
    except Exception as e:
        print(f"❌ Failed to list buckets: {e}")
        return {
            "encrypted_buckets": [],
            "unencrypted_buckets": [],
            "error": str(e)
        }

    start_time = time.time()

    for bucket in buckets:
        bucket_name = bucket['Name']

        # Stop early if timeout is approaching
        if time.time() - start_time > context.get_remaining_time_in_millis() / 1000.0 - 5:
            print("⚠️ Approaching Lambda timeout, exiting early.")
            break

        try:
            response = s3.get_bucket_encryption(Bucket=bucket_name)
            rules = response['ServerSideEncryptionConfiguration']['Rules']
            encryption_type = rules[0]['ApplyServerSideEncryptionByDefault']['SSEAlgorithm']
            print(f"✅ Encrypted bucket: {bucket_name} (Encryption: {encryption_type})")
            encrypted_buckets.append(bucket_name)

        except botocore.exceptions.ClientError as e:
            error_code = e.response['Error'].get('Code')
            if error_code == 'ServerSideEncryptionConfigurationNotFoundError':
                print(f"⚠️ Unencrypted bucket: {bucket_name}")
                unencrypted_buckets.append(bucket_name)
            elif error_code == 'AccessDenied':
                print(f"⛔ Access denied to bucket: {bucket_name}")
            else:
                print(f"❌ Error checking bucket {bucket_name}: {e}")
        except Exception as e:
            print(f"❌ Unexpected error with bucket {bucket_name}: {e}")

    print("✅ Done.")
    print(f"🔐 Encrypted Buckets: {encrypted_buckets}")
    print(f"🚫 Unencrypted Buckets: {unencrypted_buckets}")

    return {
        "encrypted_buckets": encrypted_buckets,
        "unencrypted_buckets": unencrypted_buckets
    }
