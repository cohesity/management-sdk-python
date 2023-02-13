# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.clone_app_view_info_oracle

class CloneAppViewInfoProto(object):

    """Implementation of the 'CloneAppViewInfoProto' model.

    This message encapsulates the information of Clone operation of backup
    view
    of an App.

    Attributes:
        oracle_app_view_restore_info (CloneAppViewInfoOracle): This message
            encapsulates backup view Clone operation information of a Oracle
            DB.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "oracle_app_view_restore_info":'oracleAppViewRestoreInfo'
    }

    def __init__(self,
                 oracle_app_view_restore_info=None):
        """Constructor for the CloneAppViewInfoProto class"""

        # Initialize members of the class
        self.oracle_app_view_restore_info = oracle_app_view_restore_info


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
        oracle_app_view_restore_info = cohesity_management_sdk.models.clone_app_view_info_oracle.CloneAppViewInfoOracle.from_dictionary(dictionary.get('oracleAppViewRestoreInfo')) if dictionary.get('oracleAppViewRestoreInfo') else None

        # Return an object of this model
        return cls(oracle_app_view_restore_info)


