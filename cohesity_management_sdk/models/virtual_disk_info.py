# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class VirtualDiskInfo(object):

    """Implementation of the 'VirtualDiskInfo' model.

    Virtual Disk Information.

    Attributes:
        bus_number (long|int): Specifies the Id of the controller bus that
            controls the disk.
        controller_type (string): Specifies the controller type like SCSI, or
            IDE etc.
        filename (string): Specifies the host file name used as the virtual
            disk.
        logical_size_bytes (long|int): Virtual disk size.
        unit_number (long|int): Specifies the disk file name. This is the VMDK
            name and not the flat file name.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bus_number":'busNumber',
        "controller_type":'controllerType',
        "filename":'filename',
        "logical_size_bytes":'logicalSizeBytes',
        "unit_number":'unitNumber'
    }

    def __init__(self,
                 bus_number=None,
                 controller_type=None,
                 filename=None,
                 logical_size_bytes=None,
                 unit_number=None):
        """Constructor for the VirtualDiskInfo class"""

        # Initialize members of the class
        self.bus_number = bus_number
        self.controller_type = controller_type
        self.filename = filename
        self.logical_size_bytes = logical_size_bytes
        self.unit_number = unit_number


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
        bus_number = dictionary.get('busNumber')
        controller_type = dictionary.get('controllerType')
        filename = dictionary.get('filename')
        logical_size_bytes = dictionary.get('logicalSizeBytes')
        unit_number = dictionary.get('unitNumber')

        # Return an object of this model
        return cls(bus_number,
                   controller_type,
                   filename,
                   logical_size_bytes,
                   unit_number)


