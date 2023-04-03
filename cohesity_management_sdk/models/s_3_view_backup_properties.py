# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.s_3_bucket_config_proto


class S3ViewBackupProperties(object):

    """Implementation of the 'S3ViewBackupProperties' model.

    TODO: type description here.


    Attributes:

        access_key (string): Access key for the buckets which will be created
            for the source initiated jobs. This needs to be passed to Netapp
            for it to for doing all s3 communications.
        s_3_config (S3BucketConfigProto): For source initiated backup the
            target is s3 view. This captures the configuration needed to create
            the s3 view.
        secret_key (string): Secret key for the buckets will be created for the
            source initiated jobs. This secret key needed to be sent to Netapp
            for writing data to our S3 views.
        snapshot_prefix_name (string): The snapshot prefix which is needed at
            the time of incremental for backups. This is only needed for case
            of DP volume.
        view_id (long|int): The id of the S3 view.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "access_key":'accessKey',
        "s_3_config":'s3Config',
        "secret_key":'secretKey',
        "snapshot_prefix_name":'snapshotPrefixName',
        "view_id":'viewId',
    }
    def __init__(self,
                 access_key=None,
                 s_3_config=None,
                 secret_key=None,
                 snapshot_prefix_name=None,
                 view_id=None,
            ):

        """Constructor for the S3ViewBackupProperties class"""

        # Initialize members of the class
        self.access_key = access_key
        self.s_3_config = s_3_config
        self.secret_key = secret_key
        self.snapshot_prefix_name = snapshot_prefix_name
        self.view_id = view_id

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
        s_3_config = cohesity_management_sdk.models.s_3_bucket_config_proto.S3BucketConfigProto.from_dictionary(dictionary.get('s3Config')) if dictionary.get('s3Config') else None
        secret_key = dictionary.get('secretKey')
        snapshot_prefix_name = dictionary.get('snapshotPrefixName')
        view_id = dictionary.get('viewId')

        # Return an object of this model
        return cls(
            access_key,
            s_3_config,
            secret_key,
            snapshot_prefix_name,
            view_id
)