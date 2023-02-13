# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class VmwareDiskExclusionProto(object):

    """Implementation of the 'VMwareDiskExclusionProto' model.

    This message contains basic info of the disk to be excluded from backup.
    The info contained here:
    1. should be enough to identify the disk during the backup job.
    2. is a subset of the message fetched to be displayed to the end user.
    Example: entities/vmware.proto.
    Note: Currently this is only implemented for VMware type source.

    Attributes:
        controller_bus_number (long|int): Controller's bus-id controlling the
            virtual disk in question.
        controller_type (string): Controller's type (SCSI, IDE etc).
        unit_number (long|int): Disk unit number to identify the virtual disk
            within a controller.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "controller_bus_number":'controllerBusNumber',
        "controller_type":'controllerType',
        "unit_number":'unitNumber'
    }

    def __init__(self,
                 controller_bus_number=None,
                 controller_type=None,
                 unit_number=None):
        """Constructor for the VmwareDiskExclusionProto class"""

        # Initialize members of the class
        self.controller_bus_number = controller_bus_number
        self.controller_type = controller_type
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
        unit_number = dictionary.get('unitNumber')

        # Return an object of this model
        return cls(controller_bus_number,
                   controller_type,
                   unit_number)


