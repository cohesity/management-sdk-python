# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class GcpDiskInfo(object):

    """Implementation of the 'GcpDiskInfo' model.

    Specified info about the GCP disk.


    Attributes:

        device_name (string): Specifies the name of the device. Eg - /dev/sdb.
        id (long|int): Specified ID of the disk.
        is_root_device (bool): Specifies if the disk is attached as root
            device.
        name (string): Specifies the name of the disk.
        size_gb (long|int): Specifies the size of the device.
        mtype (string): Specifies the type of the disk.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "device_name":'deviceName',
        "id":'id',
        "is_root_device":'isRootDevice',
        "name":'name',
        "size_gb":'sizeGb',
        "mtype":'type',
    }
    def __init__(self,
                 device_name=None,
                 id=None,
                 is_root_device=None,
                 name=None,
                 size_gb=None,
                 mtype=None,
            ):

        """Constructor for the GcpDiskInfo class"""

        # Initialize members of the class
        self.device_name = device_name
        self.id = id
        self.is_root_device = is_root_device
        self.name = name
        self.size_gb = size_gb
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
        size_gb = dictionary.get('sizeGb')
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(
            device_name,
            id,
            is_root_device,
            name,
            size_gb,
            mtype
)