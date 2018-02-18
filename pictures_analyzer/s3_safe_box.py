import uuid

import boto3

from pictures_analyzer.safe_box import SafeBox


class S3SafeBox(SafeBox):

    def __init__(self, environment):
        self.environment = environment

    def upload(self, picture_path: str) -> str:
        bucket_name = self.environment.get('S3_SAFE_BOX_BUCKET_NAME')
        bucket = boto3.resource('s3').Bucket(bucket_name)
        key = self._generate_key()
        bucket.upload_file(picture_path, key)
        return self._get_resource_url(bucket_name, key)

    def _get_resource_url(self, bucket_name, key):
        region = self.environment.get('AWS_DEFAULT_REGION')
        created_resource_url = 'https://s3.' + region + '.amazonaws.com/' + bucket_name + '/' + key
        return created_resource_url

    def _generate_key(self):
        key_prefix = self.environment.get('S3_SAFE_BOX_PREFIX')
        key = key_prefix + '/' + str(uuid.uuid1())
        return key
