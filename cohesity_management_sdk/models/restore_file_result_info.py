# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.restore_file_copy_stats
import cohesity_management_sdk.models.error_proto
import cohesity_management_sdk.models.restored_file_info

class RestoreFileResultInfo(object):

    """Implementation of the 'RestoreFileResultInfo' model.

    This message captures result of restore of individual file or directory
    as initiated from magneto.
    Note, it is expected that the agents go through the "estimation" phase
    first for the entire batch of restore requests and then start copying.
    These state transitions are reflected in the "status" field here.

    Attributes:
        copy_stats (RestoreFileCopyStats): This message captures the progress
            information regarding restore of file/directory.
        destination_dir (string): This is set to the destination directory
            where the file/directory was copied.
        error (ErrorProto): TODO: type description here.
        restored_file_info (RestoredFileInfo): TODO: type description here.
        status (int): Status of the restore.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "copy_stats":'copyStats',
        "destination_dir":'destinationDir',
        "error":'error',
        "restored_file_info":'restoredFileInfo',
        "status":'status'
    }

    def __init__(self,
                 copy_stats=None,
                 destination_dir=None,
                 error=None,
                 restored_file_info=None,
                 status=None):
        """Constructor for the RestoreFileResultInfo class"""

        # Initialize members of the class
        self.copy_stats = copy_stats
        self.destination_dir = destination_dir
        self.error = error
        self.restored_file_info = restored_file_info
        self.status = status


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
        copy_stats = cohesity_management_sdk.models.restore_file_copy_stats.RestoreFileCopyStats.from_dictionary(dictionary.get('copyStats')) if dictionary.get('copyStats') else None
        destination_dir = dictionary.get('destinationDir')
        error = cohesity_management_sdk.models.error_proto.ErrorProto.from_dictionary(dictionary.get('error')) if dictionary.get('error') else None
        restored_file_info = cohesity_management_sdk.models.restored_file_info.RestoredFileInfo.from_dictionary(dictionary.get('restoredFileInfo')) if dictionary.get('restoredFileInfo') else None
        status = dictionary.get('status')

        # Return an object of this model
        return cls(copy_stats,
                   destination_dir,
                   error,
                   restored_file_info,
                   status)


