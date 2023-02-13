# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class EbsVolumeInfo(object):

    """Implementation of the 'EbsVolumeInfo' model.

    Specifies information about an AWS volume attached to an EC2 instance.

    Attributes:
        device_name (string): Specifies the name of the device. Eg - /dev/sdb.
        id (string): Specifies the ID of the volume.
        is_root_device (bool): Specifies if the volume is attached as root device.
        name (string): Specifies the name of the volume.
        size_bytes (long|int): Specifies the size of the volume in bytes.
        mtype (string): Specifies the type of the volume. Eg - gp2, io1.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "device_name": 'deviceName',
        "id": 'id',
        "is_root_device":'isRootDevice',
        "name":'name',
        "size_bytes":'sizeBytes',
        "mtype":'type'
    }

    def __init__(self,
                 device_name=None,
                 id=None,
                 is_root_device=None,
                 name=None,
                 size_bytes=None,
                 mtype=None
                 ):
        """Constructor for the EbsVolumeInfo class"""

        # Initialize members of the class
        self.device_name = device_name
        self.id = id
        self.is_root_device = is_root_device
        self.name = name
        self.size_bytes = size_bytes
        self.mtype = mtype

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
        device_name = dictionary.get('deviceName')
        id = dictionary.get('id')
        is_root_device = dictionary.get('isRootDevice')
        name = dictionary.get('name')
        size_bytes = dictionary.get('sizeBytes')
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(device_name,
                   id,
                   is_root_device,
                   name,
                   size_bytes,
                   mtype)


