from unittest import TestCase
from unittest.mock import patch, Mock, ANY

from pictures_analyzer.s3_safe_box import S3SafeBox

PICTURE_PATH = './picture.jpg'

ENVIRONMENT = {'S3_SAFE_BOX_BUCKET_NAME': 'secure_bucket',
               'S3_SAFE_BOX_PREFIX': 'agent-007',
               'AWS_DEFAULT_REGION': 'eu-west-3', }


class TestS3SafeBox(TestCase):

    def setUp(self):
        self.s3_safe_box = S3SafeBox(ENVIRONMENT)

    def test_upload_should_upload_the_picture_file_to_s3_bucket(self):
        # Given
        s3 = Mock()
        with patch('boto3.resource', return_value=s3):
            s3_bucket = Mock()
            s3.Bucket.return_value = s3_bucket
            # When
            self.s3_safe_box.upload(PICTURE_PATH)

            # Then
            s3_bucket.upload_file.assert_called_once_with(PICTURE_PATH, ANY)

    def test_upload_should_return_the_url_of_the_created_resource_based_on_env_variables(self):
        # Given
        with patch('boto3.resource'):
            # When
            created_resource_url = self.s3_safe_box.upload(PICTURE_PATH)

            # Then
            self.assertRegex(created_resource_url,
                             r'^https://s3.eu-west-3.amazonaws.com/secure_bucket/agent-007/.*$')
