# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.error_proto

class RecoverVolumesTaskStateProtoTaskResult(object):

    """Implementation of the 'RecoverVolumesTaskStateProto_TaskResult' model.

    TODO: type model description here.

    Attributes:
        dst_guid (string): Volume GUID for the Target Entity (phy host).
        error (ErrorProto): TODO: type description here.
        progress_monitor_task_path (string): The path relative to the root
            path of the restore task progress monitor.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "dst_guid":'dstGuid',
        "error":'error',
        "progress_monitor_task_path":'progressMonitorTaskPath'
    }

    def __init__(self,
                 dst_guid=None,
                 error=None,
                 progress_monitor_task_path=None):
        """Constructor for the RecoverVolumesTaskStateProtoTaskResult class"""

        # Initialize members of the class
        self.dst_guid = dst_guid
        self.error = error
        self.progress_monitor_task_path = progress_monitor_task_path


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
        dst_guid = dictionary.get('dstGuid')
        error = cohesity_management_sdk.models.error_proto.ErrorProto.from_dictionary(dictionary.get('error')) if dictionary.get('error') else None
        progress_monitor_task_path = dictionary.get('progressMonitorTaskPath')

        # Return an object of this model
        return cls(dst_guid,
                   error,
                   progress_monitor_task_path)


