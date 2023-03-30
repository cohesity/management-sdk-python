# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class AcropolisDiskFilterProto(object):

    """Implementation of the 'AcropolisDiskFilterProto' model.

    This message contains basic info of the disk to be filtered from backup.


    Attributes:

        bus_type (string): Bus type (SCSI, IDE, PCI, SATA, SPAPR, NVME).
        index (int): Index/Unit number of the disk.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "bus_type":'busType',
        "index":'index',
    }
    def __init__(self,
                 bus_type=None,
                 index=None,
            ):

        """Constructor for the AcropolisDiskFilterProto class"""

        # Initialize members of the class
        self.bus_type = bus_type
        self.index = index

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
        bus_type = dictionary.get('busType')
        index = dictionary.get('index')

        # Return an object of this model
        return cls(
            bus_type,
            index
)