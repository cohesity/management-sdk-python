# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.filesystem_volume

class VmVolumesInformation(object):

    """Implementation of the 'VmVolumesInformation' model.

    Specifies information about a logical volume found a VM.

    Attributes:
        filesystem_volumes (list of FilesystemVolume): Array of Filesystem
            Volumes.  Specifies information about the filesystem volumes found
            in a logical volume.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "filesystem_volumes":'filesystemVolumes'
    }

    def __init__(self,
                 filesystem_volumes=None):
        """Constructor for the VmVolumesInformation class"""

        # Initialize members of the class
        self.filesystem_volumes = filesystem_volumes


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
        filesystem_volumes = None
        if dictionary.get('filesystemVolumes') != None:
            filesystem_volumes = list()
            for structure in dictionary.get('filesystemVolumes'):
                filesystem_volumes.append(cohesity_management_sdk.models.filesystem_volume.FilesystemVolume.from_dictionary(structure))

        # Return an object of this model
        return cls(filesystem_volumes)


