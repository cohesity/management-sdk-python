# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.virtual_disk_id
import cohesity_management_sdk.models.entity_proto

class RecoverVirtualDiskParamsVirtualDiskMapping(object):

    """Implementation of the 'RecoverVirtualDiskParams_VirtualDiskMapping' model.

    TODO: type model description here.

    Attributes:
        disk_to_overwrite (VirtualDiskId): This message defines the proto that
            can be used to identify the disks in different environments.
        src_disk (VirtualDiskId): This message defines the proto that can be
            used to identify the disks in different environments.
        target_location (EntityProto): Specifies the attributes and the latest
            statistics about an entity.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "disk_to_overwrite":'diskToOverwrite',
        "src_disk":'srcDisk',
        "target_location":'targetLocation'
    }

    def __init__(self,
                 disk_to_overwrite=None,
                 src_disk=None,
                 target_location=None):
        """Constructor for the RecoverVirtualDiskParamsVirtualDiskMapping class"""

        # Initialize members of the class
        self.disk_to_overwrite = disk_to_overwrite
        self.src_disk = src_disk
        self.target_location = target_location


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
        disk_to_overwrite = cohesity_management_sdk.models.virtual_disk_id.VirtualDiskId.from_dictionary(dictionary.get('diskToOverwrite')) if dictionary.get('diskToOverwrite') else None
        src_disk = cohesity_management_sdk.models.virtual_disk_id.VirtualDiskId.from_dictionary(dictionary.get('srcDisk')) if dictionary.get('srcDisk') else None
        target_location = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('targetLocation')) if dictionary.get('targetLocation') else None

        # Return an object of this model
        return cls(disk_to_overwrite,
                   src_disk,
                   target_location)


