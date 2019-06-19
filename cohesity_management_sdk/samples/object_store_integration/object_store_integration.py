#!/usr/bin/env python
# Copyright 2019 Cohesity Inc.
#
# Python example to List, get Objects and stream them s3 buckets hosted on
# cohesity. Primarily using s3 boto API client in conjuction with cohesity
# client to show the integration. Initialize the CONSTANTS in top of this file.
# Usage: python s3_cohesity.py

import boto3
import os

from pprint import pprint
import urllib3
urllib3.disable_warnings()

from cohesity_management_sdk.cohesity_client import CohesityClient
from cohesity_management_sdk.models.reset_s_3_secret_key_parameters import \
    ResetS3SecretKeyParameters
from cohesity_management_sdk.models.view import View
from cohesity_management_sdk.models.protocol_access_enum import ProtocolAccessEnum

CLUSTER_USERNAME = 'cluster_username'
CLUSTER_PASSWORD = 'cluster_password'
CLUSTER_VIP = 'prod-cluster.cohesity.com'
DOMAIN = 'LOCAL'
COHESITY_S3_PORT = '3000'

BUCKET_NAME = 'test_bucket'
FILENAME = 'file.txt'
DOWNLOAD_FILENAME = 'download-file.txt'

class S3Integration(object):

    def __init__(self):
        self.cohesity_client = self.init_cohesity_client()
        key_id, access_key = self._get_keys()
        self.s3_client = self.init_s3_client(key_id, access_key)

    def _get_keys(self):
        """
        Method to return the secret keys to the user
        :return: key_id(str), secret_key_access(str)
        """
        user = self.cohesity_client.principals.get_users(
            usernames=CLUSTER_USER)[0]
        if not user.s_3_secret_key:
             self._generate_keys()
             self._get_keys()
        return user.s_3_access_key_id, user.s_3_secret_key

    def _generate_keys(self):
        """
        Method to generate the keys if doesn't exist.
        :return: None
        """
        body = ResetS3SecretKeyParameters()
        body.username = CLUSTER_USER
        self.cohesity_client.principals.create_reset_s_3_secret_key(body)

    def _get_s3_url(self):
        """
        Method to construct the s3 Endpoint URL from cohesity.
        :return url(str): eg:  https://cluster.eng.cohesity.com:3000
        """
        return 'https://' + CLUSTER_VIP + ':' + COHESITY_S3_PORT

    def _get_storage_domain_id(self):
        resp = self.cohesity_client.view_boxes.get_view_boxes()
        return resp[0].id

    def init_cohesity_client(self):
        return CohesityClient(CLUSTER_VIP, CLUSTER_USER, CLUSTER_PASSWORD, DOMAIN)

    def init_s3_client(self, key_id, secret_access_key):
        """
         Method to initialize the AWS s3 client.
        :param key_id(str): Cohesity User's S3 ACCESS KEY ID.
        :param secret_access_key(str): Cohesity User's S3 SECRET ACCESS KEY.
        :return:
        """
        session = boto3.session.Session()
        s3_client = session.client(
            service_name='s3',
            aws_access_key_id=key_id,
            aws_secret_access_key=secret_access_key,
            endpoint_url= self._get_s3_url(),
            verify=False
        )
        return s3_client

    def list_buckets(self):
        """
        Method to list the buckets in cohesity
        :return: None
        """
        response = self.s3_client.list_buckets()
        bucket_list = [bucket['Name'] for bucket in response['Buckets']]
        pprint(bucket_list)

    def create_bucket(self):
        """
        Method to create a bucket natively.
        :return:
        """
        # Cohesity doesn't allow to create a bucket natively from s3 client.
        # response = s3_client.create_bucket(Bucket='my-bucket')

        # We create a view with s3Only access, since if it's multiprotocol,
        # bucket becomes readonly access for s3.
        body = View()
        body.view_box_id = self._get_storage_domain_id()
        body.name = BUCKET_NAME
        body.protocol_access = ProtocolAccessEnum.KS3ONLY
        self.cohesity_client.views.create_view(body)
        print("Bucket %s created on Cohesity." % BUCKET_NAME)

    def list_bucket_objects(self):
        """
        Method to list the objects in a bucket.
        :return:
        """
        response = self.s3_client.list_objects_v2(
            Bucket=BUCKET_NAME)
        for content in response.get('Contents', []):
            print("Bucket content: ", content.get('Key'))

    def upload_file_to_bucket(self):
        """"
        Method to upload file to the bucket.
        """
        fp = open(FILENAME, 'wb')
        size = 1024*1024
        fp.write("\0" * size)
        fp.close()
        self.s3_client.upload_file(FILENAME, BUCKET_NAME, FILENAME)
        print("Uploaded File %s of size %s to Bucket: %s" % (FILENAME, size,
                                                             BUCKET_NAME))

    def download_file_from_bucket(self):
        """
        Method to download the file from the bucket.
        :return: None.
        """
        self.s3_client.download_file(BUCKET_NAME, FILENAME, DOWNLOAD_FILENAME)
        print("File downloaded to : %s/%s" % (os.getcwd(), DOWNLOAD_FILENAME))

    def delete_file_from_bucket(self):
        """
        Method to delete the file from the bucket.
        :return: None.
        """
        self.s3_client.delete_object(Bucket=BUCKET_NAME, Key=FILENAME)
        print("File %s deleted from Bucket: %s" % (FILENAME, BUCKET_NAME))

    def delete_bucket(self):
        """
        Method to delete the bucket.
        :return: None.
        """
        self.s3_client.delete_bucket(Bucket=BUCKET_NAME)
        print("Deleted Bucket: %s" % BUCKET_NAME)

def main():
    integration = S3Integration()
    integration.create_bucket()
    integration.list_buckets()

    integration.upload_file_to_bucket()
    integration.list_bucket_objects()
    integration.download_file_from_bucket()

    integration.delete_file_from_bucket()
    integration.delete_bucket()

if __name__ == '__main__':
    main()
