# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.additional_oracle_db_params

class OracleSourceParams(object):

    """Implementation of the 'OracleSourceParams' model.

    Message to capture additional backup/restore params for a Oracle source.

    Attributes:
        additional_oracle_db_params_vec (list of AdditionalOracleDBParams):
            Backup channel information for each Oracle database. NOTE: Size of
            this vector will be 1 for DG.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "additional_oracle_db_params_vec":'additionalOracleDbParamsVec'
    }

    def __init__(self,
                 additional_oracle_db_params_vec=None):
        """Constructor for the OracleSourceParams class"""

        # Initialize members of the class
        self.additional_oracle_db_params_vec = additional_oracle_db_params_vec


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
        additional_oracle_db_params_vec = None
        if dictionary.get('additionalOracleDbParamsVec') != None:
            additional_oracle_db_params_vec = list()
            for structure in dictionary.get('additionalOracleDbParamsVec'):
                additional_oracle_db_params_vec.append(cohesity_management_sdk.models.additional_oracle_db_params.AdditionalOracleDBParams.from_dictionary(structure))

        # Return an object of this model
        return cls(additional_oracle_db_params_vec)


