# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.backup_job_proto_remote_view_params_remote_view_map_entry

class BackupJobProto_RemoteViewParams(object):

    """Implementation of the 'BackupJobProto_RemoteViewParams' model.

    From 6.6 onwards, we always create remote view for view backups if policy
    has replication, hence 'create_remote_view' bool is not added here.

    Attributes:
        remote_view_map (list of BackupJobProto_RemoteViewParams_RemoteViewMapEntry):
            A map from view id on source cluster to the view name params on remote
            cluster. This is applicable for view backups with replication configured
            in the policy.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "remote_view_map":'remoteViewMap'
    }

    def __init__(self,
                 remote_view_map=None):
        """Constructor for the BackupJobProto_RemoteViewParams class"""

        # Initialize members of the class
        self.remote_view_map = remote_view_map


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
        remote_view_map = None
        if dictionary.get('remoteViewMap') != None:
            remote_view_map = list()
            for structure in dictionary.get('remoteViewMap'):
                remote_view_map.append(backup_job_proto_remote_view_params_remote_view_map_entry.BackupJobProto_RemoteViewParams_RemoteViewMapEntry.from_dictionary(structure))

        # Return an object of this model
        return cls(remote_view_map)


