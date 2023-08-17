import ibm_boto3

class COSManager:
    def __init__(self, access_key, secret_key, endpoint_url):
        self.cos = ibm_boto3.client('s3',
                                    aws_access_key_id=access_key,
                                    aws_secret_access_key=secret_key,
                                    endpoint_url=endpoint_url)

    def update_bucket_permissions(self, bucket_name, new_permissions):
        try:
            self.cos.put_bucket_acl(Bucket=bucket_name, ACL=new_permissions)
        except ibm_boto3.exceptions.S3UploadFailedError as e:
            print("Error updating bucket permissions: {}".format(e))

