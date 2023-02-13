# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.hdfs_connect_params

class HiveBackupJobParams(object):

    """Implementation of the 'HiveBackupJobParams' model.

    Contains any additional hive environment specific backup params at the
    job level.

    Attributes:
    hdfs_connect_params (HdfsConnectParams): Additional hdfs connection params
        required for Hive Backup.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "hdfs_connect_params":'hdfsConnectParams'
    }

    def __init__(self,
                 hdfs_connect_params=None):
        """Constructor for the HiveBackupJobParams class"""

        # Initialize members of the class
        self.hdfs_connect_params = hdfs_connect_params


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
        hdfs_connect_params = cohesity_management_sdk.models.hdfs_connect_params.HdfsConnectParams.from_dictionary(dictionary.get('hdfsConnectParams')) if dictionary.get('hdfsConnectParams') else None

        # Return an object of this model
        return cls(hdfs_connect_params)


