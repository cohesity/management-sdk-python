# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class S3BucketInfo(object):

    """Implementation of the 'S3BucketInfo' model.

    TODO: type description here.


    Attributes:

        aws_region (string): AWS region of the S3 bucket.
        bucket_name (string): Name of the S3 bucket.
        key_prefix (string): Complete path of the sub folder in the s3 bucket.
            This job will create all keys within the given key prefix.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "aws_region":'awsRegion',
        "bucket_name":'bucketName',
        "key_prefix":'keyPrefix',
    }
    def __init__(self,
                 aws_region=None,
                 bucket_name=None,
                 key_prefix=None,
            ):

        """Constructor for the S3BucketInfo class"""

        # Initialize members of the class
        self.aws_region = aws_region
        self.bucket_name = bucket_name
        self.key_prefix = key_prefix

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        aws_region = dictionary.get('awsRegion')
        bucket_name = dictionary.get('bucketName')
        key_prefix = dictionary.get('keyPrefix')

        # Return an object of this model
        return cls(
            aws_region,
            bucket_name,
            key_prefix
)