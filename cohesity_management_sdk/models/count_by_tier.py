# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class CountByTier(object):

    """Implementation of the 'CountByTier' model.

    CountByTier provides the disk count of each storage tier.

    Attributes:
        disk_count (long|int): DiskCount is the disk number of the storage
            tier.
        storage_tier (StorageTierEnum): StorageTier is the type of
            StorageTier. StorageTierType represents the various values for the
            Storage Tier. 'kPCIeSSD' indicates storage tier type of Pci Solid
            State Drive. 'kSATAHDD' indicates storage tier type of SATA Solid
            State Drive. 'kSATAHDD' indicates storage tier type of SATA Hard
            Disk Drive. 'kCLOUD' indicates storage tier type of Cloud.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "disk_count":'diskCount',
        "storage_tier":'storageTier'
    }

    def __init__(self,
                 disk_count=None,
                 storage_tier=None):
        """Constructor for the CountByTier class"""

        # Initialize members of the class
        self.disk_count = disk_count
        self.storage_tier = storage_tier


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
        disk_count = dictionary.get('diskCount')
        storage_tier = dictionary.get('storageTier')

        # Return an object of this model
        return cls(disk_count,
                   storage_tier)


