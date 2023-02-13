# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.backup_job_proto_remote_view_params_remote_view_params_per_view

class BackupJobProto_RemoteViewParams_RemoteViewMapEntry(object):

    """Implementation of the 'BackupJobProto_RemoteViewParams_RemoteViewMapEntry' model.


    Attributes:
        key (long|int): TODO:Type description here.
        value (BackupJobProto_RemoteViewParams_RemoteViewParamsPerView):
            TODO:Type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "key": 'key',
        "value": 'value'
    }

    def __init__(self,
                 key=None,
                 value=None):
        """Constructor for the BackupJobProto_RemoteViewParams_RemoteViewMapEntry class"""

        # Initialize members of the class
        self.key = key
        self.value = value


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
        key = dictionary.get('key')
        value = cohesity_management_sdk.models.backup_job_proto_remote_view_params_remote_view_params_per_view.BackupJobProto_RemoteViewParams_RemoteViewParamsPerView.from_dictionary(dictionary.get('value')) if dictionary.get('value') else None

        # Return an object of this model
        return cls(key,
                   value)


