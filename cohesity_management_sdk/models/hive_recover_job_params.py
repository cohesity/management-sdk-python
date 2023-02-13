# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.hdfs_connect_params

class HiveRecoverJobParams(object):

    """Implementation of the 'HiveRecoverJobParams' model.

    Contains any additional hive environment specific params for the
    recover job.

    Attributes:
        hdfs_connect_params (HdfsConnectParams): Additional hdfs connection
            params required for Hive Backup.
        suffix (string): A suffix that is to be applied to all recovered
            entities

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "hdfs_connect_params": 'hdfsConnectParams',
        "suffix": 'suffix'
    }

    def __init__(self,
                 hdfs_connect_params=None,
                 suffix=None):
        """Constructor for the HiveRecoverJobParams class"""

        # Initialize members of the class
        self.hdfs_connect_params = hdfs_connect_params
        self.suffix = suffix


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
        hdfs_connect_params = cohesity_management_sdk.models.hdfs_connect_params.HdfsConnectParams.from_dictionary(dictionary.get('hdfsConnectParams')) if dictionary.get('hdfsConnectParams', None) else None
        suffix = dictionary.get('suffix', None)

        # Return an object of this model
        return cls(hdfs_connect_params,
                   suffix)


