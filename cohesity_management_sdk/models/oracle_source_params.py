# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.additional_oracle_db_params

class OracleSourceParams(object):

    """Implementation of the 'OracleSourceParams' model.

    Message to capture additional backup/restore params for a Oracle source.

    Attributes:
        additional_oracle_db_params_vec (list of AdditionalOracleDBParams): A
            vector of unique Oracle databases. Each vector entry represents
            the backup/restore parameters for one unique Oracle database.
            Uniqueness is determined by the database unique name.
        persist_mountpoints (bool): This parameter indicates whether or not to
            persist mountpoints. Default is set to true, which was the
            behavior before this option.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "additional_oracle_db_params_vec":'additionalOracleDbParamsVec',
        "persist_mountpoints":'persistMountpoints'
    }

    def __init__(self,
                 additional_oracle_db_params_vec=None,
                 persist_mountpoints=None):
        """Constructor for the OracleSourceParams class"""

        # Initialize members of the class
        self.additional_oracle_db_params_vec = additional_oracle_db_params_vec
        self.persist_mountpoints = persist_mountpoints


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
        persist_mountpoints = dictionary.get('persistMountpoints')

        # Return an object of this model
        return cls(additional_oracle_db_params_vec,
                   persist_mountpoints)


