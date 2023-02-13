# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class NodeSystemDiskInfo(object):

    """Implementation of the 'NodeSystemDiskInfo' model.

    TODO: type model description here.

    Attributes:
        device_path (string): DevicePath is the device path of the disk.
        id (long|int): Id is the id of the disk.
        offline (bool): Offline specifies whether a disk is marked offline.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "device_path":'devicePath',
        "id":'id',
        "offline":'offline'
    }

    def __init__(self,
                 device_path=None,
                 id=None,
                 offline=None):
        """Constructor for the NodeSystemDiskInfo class"""

        # Initialize members of the class
        self.device_path = device_path
        self.id = id
        self.offline = offline


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
        device_path = dictionary.get('devicePath')
        id = dictionary.get('id')
        offline = dictionary.get('offline')

        # Return an object of this model
        return cls(device_path,
                   id,
                   offline)


