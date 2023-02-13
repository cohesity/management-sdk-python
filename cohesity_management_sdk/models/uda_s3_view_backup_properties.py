# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.s3_bucket_config_proto

class UdaS3ViewBackupProperties(object):

    """Implementation of the 'UdaS3ViewBackupProperties' model.

    // -----------------------------------------------------------------------------

    Attributes:
        access_key (string): Access key for the buckets which will be created
            for the source initiated jobs. This needs to be passed to UDA for
            doing all s3 communications.
        s3_config (S3BucketConfigProto): For source initiated backup the target
            is s3 view. This captures the configuration needed to create the s3
            view.
        secret_key (string): Secret key for the buckets will be created for the
            source initiated jobs. This secret key needed to be sent to UDA for
            writing data to our S3 views.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "access_key":'accessKey',
        "s3_config":'s3Config',
        "secret_key":'secretKey'
    }

    def __init__(self,
                 access_key=None,
                 s3_config=None,
                 secret_key=None):
        """Constructor for the UdaS3ViewBackupProperties class"""

        # Initialize members of the class
        self.access_key = access_key
        self.s3_config = s3_config
        self.secret_key = secret_key


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
        access_key = dictionary.get('accessKey')
        s3_config = cohesity_management_sdk.models.s3_bucket_config_proto.S3BucketConfigProto.from_dictionary(dictionary.get('s3Config')) if dictionary.get('s3Config') else None
        secret_key = dictionary.get('secretKey')

        # Return an object of this model
        return cls(access_key,
                   s3_config,
                   secret_key)


