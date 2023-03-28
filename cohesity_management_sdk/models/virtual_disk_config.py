# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class VirtualDiskConfig(object):

    """Implementation of the 'VirtualDiskConfig' model.

    Acropolis Virtual Disk


    Attributes:

        device_bus (string): The device bus for the virtual disk device.
        device_index (int): Index of the device on the adapter type.
        disk_size_bytes (long|int): Disk size in Bytes.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "device_bus":'deviceBus',
        "device_index":'deviceIndex',
        "disk_size_bytes":'diskSizeBytes',
    }
    def __init__(self,
                 device_bus=None,
                 device_index=None,
                 disk_size_bytes=None,
            ):

        """Constructor for the VirtualDiskConfig class"""

        # Initialize members of the class
        self.device_bus = device_bus
        self.device_index = device_index
        self.disk_size_bytes = disk_size_bytes

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
        device_bus = dictionary.get('deviceBus')
        device_index = dictionary.get('deviceIndex')
        disk_size_bytes = dictionary.get('diskSizeBytes')

        # Return an object of this model
        return cls(
            device_bus,
            device_index,
            disk_size_bytes
)