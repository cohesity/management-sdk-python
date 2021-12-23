# -*- coding: utf-8 -*-
# Copyright 2021 Cohesity Inc.

import cohesity_management_sdk.models.cassandra_additional_params
import cohesity_management_sdk.models.cassandra_log_recover_job_params

class CassandraRecoverJobParams(object):

    """Implementation of the 'CassandraRecoverJobParams' model.

    Contains any additional cassandra environment specific params for the
    recover job.

    Attributes:
        cassandra_additional_info (CassandraAdditionalParams): Additional
            parameters required for Cassandra recovery.
            TODO (faizan.khan) : Remove this.
        selected_data_center_vec (list of string):  The data centers selected
            for recovery.
        staging_directory_vec (list of string): Cassandra staging directory
        suffix (string): A suffix that is to be applied to all recovered
            entities
            TODO (faizan.khan) : Remove this.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cassandra_additional_info": 'cassandraAdditionalInfo',
        "selected_data_center_vec": 'selectedDataCenterVec',
        "staging_directory_vec": 'stagingDirectoryVec',
        "suffix":'suffix'
    }

    def __init__(self,
                 cassandra_additional_info=None,
                 selected_data_center_vec=None,
                 staging_directory_vec=None,
                 suffix=None):
        """Constructor for the CassandraRecoverJobParams class"""

        # Initialize members of the class
        self.cassandra_additional_info = cassandra_additional_info
        self.selected_data_center_vec = selected_data_center_vec
        self.staging_directory_vec = staging_directory_vec
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
        cassandra_additional_info = cohesity_management_sdk.models.cassandra_additional_params.CassandraAdditionalParams.from_dictionary(dictionary.get('cassandraAdditionalInfo')) if dictionary.get('cassandraAdditionalInfo') else None
        selected_data_center_vec = dictionary.get('selectedDataCenterVec')
        staging_directory_vec = dictionary.get('stagingDirectoryVec')
        suffix = dictionary.get('suffix')

        # Return an object of this model
        return cls(cassandra_additional_info,
                   selected_data_center_vec,
                   staging_directory_vec,
                   suffix)


