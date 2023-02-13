# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class FileStubbingParams_TargetViewData(object):

    """Implementation of the 'FileStubbingParams_TargetViewData' model.

    Attributes:
        nfs_mount_path (string): Mount path where the Cohesity target view
            must be mounted on all NFS clients for accessing the migrated data.
        target_view_name (string): The target view name to which the data will
            be migrated.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "nfs_mount_path": 'nfsMountPath',
        "target_view_name": 'targetViewName'
    }

    def __init__(self,
                 nfs_mount_path=None,
                 target_view_name=None):
        """Constructor for the FileStubbingParams_TargetViewData class"""

        # Initialize members of the class
        self.nfs_mount_path = nfs_mount_path
        self.target_view_name = target_view_name


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
        nfs_mount_path = dictionary.get('nfsMountPath', None)
        target_view_name = dictionary.get('targetViewName', None)

        # Return an object of this model
        return cls(nfs_mount_path,
                   target_view_name)


