# -*- coding: utf-8 -*-
# Copyright 2021 Cohesity Inc.


class VirtualDiskIdInformation(object):

    """Implementation of the 'VirtualDiskIdInformation' model.

    Specifies information about virtual disk which includes disk uuid,
    controller type, bus number and unit number.

    Attributes:
        bus_number (long|int): Specifies the Id of the controller bus that
            controls the disk.
        controller_type (string): Specifies the controller type like SCSI, or
            IDE etc.
        disk_id (string): Specfies the uuid of the virtual disk.
        unit_number (long|int): Specifies the disk file name. This is the VMDK
            name and not the flat file name.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bus_number":'busNumber',
        "controller_type":'controllerType',
        "disk_id":'diskId',
        "unit_number":'unitNumber'
    }

    def __init__(self,
                 bus_number=None,
                 controller_type=None,
                 disk_id=None,
                 unit_number=None):
        """Constructor for the VirtualDiskIdInformation class"""

        # Initialize members of the class
        self.bus_number = bus_number
        self.controller_type = controller_type
        self.disk_id = disk_id
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
        disk_id = dictionary.get('diskId')
        unit_number = dictionary.get('unitNumber')

        # Return an object of this model
        return cls(bus_number,
                   controller_type,
                   disk_id,
                   unit_number)


