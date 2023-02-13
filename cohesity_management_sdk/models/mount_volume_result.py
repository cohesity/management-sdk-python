# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.error_proto

class MountVolumeResult(object):

    """Implementation of the 'MountVolumeResult' model.

    TODO: type model description here.

    Attributes:
        error (ErrorProto): TODO: type description here.
        filesystem_type (string): Filesystem on this volume.
        mount_point (string): This is populated with the mount point where the
            volume corresponding to the newly attached volume is mounted.
            NOTE: This may not be present in the VM environments if onlining
            of disks is not requested or if the there was any issue during
            onlining.
        original_volume_name (string): This is the name or mount point of the
            original volume.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "error":'error',
        "filesystem_type":'filesystemType',
        "mount_point":'mountPoint',
        "original_volume_name":'originalVolumeName'
    }

    def __init__(self,
                 error=None,
                 filesystem_type=None,
                 mount_point=None,
                 original_volume_name=None):
        """Constructor for the MountVolumeResult class"""

        # Initialize members of the class
        self.error = error
        self.filesystem_type = filesystem_type
        self.mount_point = mount_point
        self.original_volume_name = original_volume_name


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
        error = cohesity_management_sdk.models.error_proto.ErrorProto.from_dictionary(dictionary.get('error')) if dictionary.get('error') else None
        filesystem_type = dictionary.get('filesystemType')
        mount_point = dictionary.get('mountPoint')
        original_volume_name = dictionary.get('originalVolumeName')

        # Return an object of this model
        return cls(error,
                   filesystem_type,
                   mount_point,
                   original_volume_name)


