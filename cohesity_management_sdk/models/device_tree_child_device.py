# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.device_tree
import cohesity_management_sdk.models.device_tree_partition_slice


class DeviceTree_ChildDevice(object):

    """Implementation of the 'DeviceTree_ChildDevice' model.

    TODO: type description here.


    Attributes:

        device (DeviceTree): Recursion: This device is defined recursively.
        device_type (int): This specifies how the parent device is using this
            child device.
        partition_slice (DeviceTree_PartitionSlice): Base case: this is a
            partition slice.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "device":'device',
        "device_type":'deviceType',
        "partition_slice":'partitionSlice',
    }
    def __init__(self,
                 device=None,
                 device_type=None,
                 partition_slice=None,
            ):

        """Constructor for the DeviceTree_ChildDevice class"""

        # Initialize members of the class
        self.device = device
        self.device_type = device_type
        self.partition_slice = partition_slice

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
        device = cohesity_management_sdk.models.device_tree.DeviceTree.from_dictionary(dictionary.get('device')) if dictionary.get('device') else None
        device_type = dictionary.get('deviceType')
        partition_slice = cohesity_management_sdk.models.device_tree_partition_slice.DeviceTree_PartitionSlice.from_dictionary(dictionary.get('partitionSlice')) if dictionary.get('partitionSlice') else None

        # Return an object of this model
        return cls(
            device,
            device_type,
            partition_slice
)