# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class VirtualDiskId(object):

    """Implementation of the 'VirtualDiskId' model.

    This message defines the proto that can be used to identify the disks in
    different environments.

    Attributes:
        controller_bus_number (long|int): Controller's bus-id controlling the
            virtual disk in question.
        controller_type (string): Controller's type (SCSI, IDE etc).
        disk_id (string): Original disk id. This is sufficient to identify the
            disk information, but in some scenarios, user's may specify the
            controller option instead.
        unit_number (long|int): Disk unit number to identify the virtual disk
            within a controller.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "controller_bus_number":'controllerBusNumber',
        "controller_type":'controllerType',
        "disk_id":'diskId',
        "unit_number":'unitNumber'
    }

    def __init__(self,
                 controller_bus_number=None,
                 controller_type=None,
                 disk_id=None,
                 unit_number=None):
        """Constructor for the VirtualDiskId class"""

        # Initialize members of the class
        self.controller_bus_number = controller_bus_number
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
        controller_bus_number = dictionary.get('controllerBusNumber')
        controller_type = dictionary.get('controllerType')
        disk_id = dictionary.get('diskId')
        unit_number = dictionary.get('unitNumber')

        # Return an object of this model
        return cls(controller_bus_number,
                   controller_type,
                   disk_id,
                   unit_number)


