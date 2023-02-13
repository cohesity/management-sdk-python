# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.device_tree_details

class LogicalVolume(object):

    """Implementation of the 'LogicalVolume' model.

    Specifies attributes for a kLVM (Linux) or kLDM (Windows) filesystem.

    Attributes:
        device_root_node (DeviceTreeDetails): Specifies a logical volume
            stored as a tree where the leaves are the blocks of partitions and
            intermediate nodes are assembled by combining nodes using one of
            the following modes: linear layout, striped, mirrored, RAID etc. A
            deviceTree is a block device formed by combining one or more
            Devices using a combining strategy.
        group_name (string): Specifies the group name of the logical volume.
        group_uuid (string): Specifies the group uuid of the logical volume.
        name (string): Specifies the name of the logical volume.
        uuid (string): Specifies the uuid of the logical volume.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "device_root_node":'deviceRootNode',
        "group_name":'groupName',
        "group_uuid":'groupUuid',
        "name":'name',
        "uuid":'uuid'
    }

    def __init__(self,
                 device_root_node=None,
                 group_name=None,
                 group_uuid=None,
                 name=None,
                 uuid=None):
        """Constructor for the LogicalVolume class"""

        # Initialize members of the class
        self.device_root_node = device_root_node
        self.group_name = group_name
        self.group_uuid = group_uuid
        self.name = name
        self.uuid = uuid


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
        device_root_node = cohesity_management_sdk.models.device_tree_details.DeviceTreeDetails.from_dictionary(dictionary.get('deviceRootNode')) if dictionary.get('deviceRootNode') else None
        group_name = dictionary.get('groupName')
        group_uuid = dictionary.get('groupUuid')
        name = dictionary.get('name')
        uuid = dictionary.get('uuid')

        # Return an object of this model
        return cls(device_root_node,
                   group_name,
                   group_uuid,
                   name,
                   uuid)


