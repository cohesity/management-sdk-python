# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.device_tree

class VolumeInfoLogicalVolumeInfo(object):

    """Implementation of the 'VolumeInfo_LogicalVolumeInfo' model.

    This is extra attribute which uniquely identifies a logical volume in LVM
    or LDM.

    Attributes:
        device_tree (DeviceTree): The tree defining how to combine partitions
            to create this logical volume.
        logical_volume_name (string): Logical volume name.
        logical_volume_uuid (string): Logical volume uuid.
        volume_group_name (string): Volume group name.
        volume_group_uuid (string): Volume group uuid.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "device_tree":'deviceTree',
        "logical_volume_name":'logicalVolumeName',
        "logical_volume_uuid":'logicalVolumeUuid',
        "volume_group_name":'volumeGroupName',
        "volume_group_uuid":'volumeGroupUuid'
    }

    def __init__(self,
                 device_tree=None,
                 logical_volume_name=None,
                 logical_volume_uuid=None,
                 volume_group_name=None,
                 volume_group_uuid=None):
        """Constructor for the VolumeInfoLogicalVolumeInfo class"""

        # Initialize members of the class
        self.device_tree = device_tree
        self.logical_volume_name = logical_volume_name
        self.logical_volume_uuid = logical_volume_uuid
        self.volume_group_name = volume_group_name
        self.volume_group_uuid = volume_group_uuid


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
        device_tree = cohesity_management_sdk.models.device_tree.DeviceTree.from_dictionary(dictionary.get('deviceTree')) if dictionary.get('deviceTree') else None
        logical_volume_name = dictionary.get('logicalVolumeName')
        logical_volume_uuid = dictionary.get('logicalVolumeUuid')
        volume_group_name = dictionary.get('volumeGroupName')
        volume_group_uuid = dictionary.get('volumeGroupUuid')

        # Return an object of this model
        return cls(device_tree,
                   logical_volume_name,
                   logical_volume_uuid,
                   volume_group_name,
                   volume_group_uuid)


