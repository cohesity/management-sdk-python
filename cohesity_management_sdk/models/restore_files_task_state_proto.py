# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.restore_files_info_proto
import cohesity_management_sdk.models.restore_files_params


class RestoreFilesTaskStateProto(object):

    """Implementation of the 'RestoreFilesTaskStateProto' model.

    TODO: type description here.


    Attributes:

        restore_files_info (RestoreFilesInfoProto): Contains information about
            this restore files task that is populated by the slave.
        restore_params (RestoreFilesParams): This captures all the necessary
            information required to perform restore to source task.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "restore_files_info":'restoreFilesInfo',
        "restore_params":'restoreParams',
    }
    def __init__(self,
                 restore_files_info=None,
                 restore_params=None,
            ):

        """Constructor for the RestoreFilesTaskStateProto class"""

        # Initialize members of the class
        self.restore_files_info = restore_files_info
        self.restore_params = restore_params

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
        restore_files_info = cohesity_management_sdk.models.restore_files_info_proto.RestoreFilesInfoProto.from_dictionary(dictionary.get('restoreFilesInfo')) if dictionary.get('restoreFilesInfo') else None
        restore_params = cohesity_management_sdk.models.restore_files_params.RestoreFilesParams.from_dictionary(dictionary.get('restoreParams')) if dictionary.get('restoreParams') else None

        # Return an object of this model
        return cls(
            restore_files_info,
            restore_params
)