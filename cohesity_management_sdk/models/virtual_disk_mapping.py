# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.virtual_disk_id_information

class VirtualDiskMapping(object):

    """Implementation of the 'VirtualDiskMapping' model.

    Specifies the request data struct for virtual disk mapping with only the
    disk ids.

    Attributes:
        disk_to_overwrite (VirtualDiskIdInformation): Specifies information
            about disk which user wants to overwrite. If specified, then
            powerOffVmBeforeRecovery must be true.
        source_disk (VirtualDiskIdInformation): Specifies information about
            the source disk.
        target_location_id (long|int): Specifies the target location
            information, for e.g. a datastore in VMware environment. If
            diskToOverwrite is specified then the target location is
            automatically deduced.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "disk_to_overwrite":'diskToOverwrite',
        "source_disk":'sourceDisk',
        "target_location_id":'targetLocationId'
    }

    def __init__(self,
                 disk_to_overwrite=None,
                 source_disk=None,
                 target_location_id=None):
        """Constructor for the VirtualDiskMapping class"""

        # Initialize members of the class
        self.disk_to_overwrite = disk_to_overwrite
        self.source_disk = source_disk
        self.target_location_id = target_location_id


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
        disk_to_overwrite = cohesity_management_sdk.models.virtual_disk_id_information.VirtualDiskIdInformation.from_dictionary(dictionary.get('diskToOverwrite')) if dictionary.get('diskToOverwrite') else None
        source_disk = cohesity_management_sdk.models.virtual_disk_id_information.VirtualDiskIdInformation.from_dictionary(dictionary.get('sourceDisk')) if dictionary.get('sourceDisk') else None
        target_location_id = dictionary.get('targetLocationId')

        # Return an object of this model
        return cls(disk_to_overwrite,
                   source_disk,
                   target_location_id)


