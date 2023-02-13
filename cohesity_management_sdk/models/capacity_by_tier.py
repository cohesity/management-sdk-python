# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class CapacityByTier(object):

    """Implementation of the 'CapacityByTier' model.

    CapacityByTier provides the physical capacity in bytes of each storage
    tier.

    Attributes:
        storage_tier (StorageTierEnum): StorageTier is the type of
            StorageTier. StorageTierType represents the various values for the
            Storage Tier. 'kPCIeSSD' indicates storage tier type of Pci Solid
            State Drive. 'kSATAHDD' indicates storage tier type of SATA Solid
            State Drive. 'kSATAHDD' indicates storage tier type of SATA Hard
            Disk Drive. 'kCLOUD' indicates storage tier type of Cloud.
        tier_max_physical_capacity_bytes (long|int):
            TierMaxPhysicalCapacityBytes is the maximum physical capacity in
            bytes of the storage tier.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "storage_tier":'storageTier',
        "tier_max_physical_capacity_bytes":'tierMaxPhysicalCapacityBytes'
    }

    def __init__(self,
                 storage_tier=None,
                 tier_max_physical_capacity_bytes=None):
        """Constructor for the CapacityByTier class"""

        # Initialize members of the class
        self.storage_tier = storage_tier
        self.tier_max_physical_capacity_bytes = tier_max_physical_capacity_bytes


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
        storage_tier = dictionary.get('storageTier')
        tier_max_physical_capacity_bytes = dictionary.get('tierMaxPhysicalCapacityBytes')

        # Return an object of this model
        return cls(storage_tier,
                   tier_max_physical_capacity_bytes)


