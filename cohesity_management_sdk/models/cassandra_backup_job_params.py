# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.cassandra_additional_params

class CassandraBackupJobParams(object):

    """Implementation of the 'CassandraBackupJobParams' model.

    Contains any additional cassandra environment specific backup params at
    the
    job level.

    Attributes:
        cassandra_additional_info (CassandraAdditionalParams): Additional
            parameters required for Cassandra backup.
        selected_data_center_vec (list of string):  The data centers selected
            for backup.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cassandra_additional_info": 'cassandraAdditionalInfo',
        "selected_data_center_vec": 'selectedDataCenterVec'
    }

    def __init__(self,
                 cassandra_additional_info=None,
                 selected_data_center_vec=None):
        """Constructor for the CassandraBackupJobParams class"""

        # Initialize members of the class
        self.cassandra_additional_info = cassandra_additional_info
        self.selected_data_center_vec = selected_data_center_vec


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
        cassandra_additional_info = cohesity_management_sdk.models.cassandra_additional_params.CassandraAdditionalParams.from_dictionary(dictionary.get('cassandraAdditionalInfo')) if dictionary.get('cassandraAdditionalInfo') else None
        selected_data_center_vec = dictionary.get('selectedDataCenterVec', None)

        # Return an object of this model
        return cls(cassandra_additional_info,
                   selected_data_center_vec)


