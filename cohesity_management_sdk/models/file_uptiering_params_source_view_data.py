# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class FileUptieringParams_SourceViewData(object):

    """Implementation of the 'FileUptieringParams_SourceViewData' model.

    Attributes:
        nfs_mount_path (string): Mount path where the Cohesity view must be
            mounted on all NFS clients while migrating the data.

        source_view_name (string): The source view name from which the data
            will be uptiered.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "nfs_mount_path": 'nfsMountPath',
        "source_view_name": 'sourceViewName'
    }

    def __init__(self,
                 nfs_mount_path=None,
                 source_view_name=None):
        """Constructor for the FileUptieringParams_SourceViewData class"""

        # Initialize members of the class
        self.nfs_mount_path = nfs_mount_path
        self.source_view_name = source_view_name


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
        source_view_name = dictionary.get('sourceViewName', None)

        # Return an object of this model
        return cls(nfs_mount_path,
                   source_view_name)


