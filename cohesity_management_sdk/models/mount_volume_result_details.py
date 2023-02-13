# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.request_error

class MountVolumeResultDetails(object):

    """Implementation of the 'MountVolumeResultDetails' model.

    Specifies the result of mounting an individual mount volume in a
    Restore Task.

    Attributes:
        mount_error (RequestError): Specifies the cause of the mount failure
            if the mounting of a volume failed.
        mount_point (string): Specifies the mount point where the volume is
            mounted. NOTE: This field may not be populated for VM environments
            if the onlining of disks is not requested or there was any issue
            during onlining.
        volume_name (string): Specifies the name of the original volume.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mount_error":'mountError',
        "mount_point":'mountPoint',
        "volume_name":'volumeName'
    }

    def __init__(self,
                 mount_error=None,
                 mount_point=None,
                 volume_name=None):
        """Constructor for the MountVolumeResultDetails class"""

        # Initialize members of the class
        self.mount_error = mount_error
        self.mount_point = mount_point
        self.volume_name = volume_name


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
        mount_error = cohesity_management_sdk.models.request_error.RequestError.from_dictionary(dictionary.get('mountError')) if dictionary.get('mountError') else None
        mount_point = dictionary.get('mountPoint')
        volume_name = dictionary.get('volumeName')

        # Return an object of this model
        return cls(mount_error,
                   mount_point,
                   volume_name)


