# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.san_storage_array
import cohesity_management_sdk.models.san_volume

class NimbleProtectionSource(object):

    """Implementation of the 'NimbleProtectionSource' model.

    Specifies a Protection Source in a Nimble environment.

    Attributes:
        name (string): Specifies a unique name of the Protection Source
        storage_array (SanStorageArray): Specifies a SAN Storage Array.
        mtype (TypeNimbleProtectionSourceEnum): Specifies the type of managed
            Object in a SAN/Nimble Protection Source like a kStorageArray or
            kVolume. Examples of SAN Objects include 'kStorageArray' and
            'kVolume'. 'kStorageArray' indicates that entire SAN storage array
            is being protected. 'kVolume' indicates that volume within the
            array is being protected.
        volume (SanVolume): Specifies a SAN Volume in a SAN Storage Array.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "storage_array":'storageArray',
        "mtype":'type',
        "volume":'volume'
    }

    def __init__(self,
                 name=None,
                 storage_array=None,
                 mtype=None,
                 volume=None):
        """Constructor for the NimbleProtectionSource class"""

        # Initialize members of the class
        self.name = name
        self.storage_array = storage_array
        self.mtype = mtype
        self.volume = volume


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
        name = dictionary.get('name')
        storage_array = cohesity_management_sdk.models.san_storage_array.SanStorageArray.from_dictionary(dictionary.get('storageArray')) if dictionary.get('storageArray') else None
        mtype = dictionary.get('type')
        volume = cohesity_management_sdk.models.san_volume.SanVolume.from_dictionary(dictionary.get('volume')) if dictionary.get('volume') else None

        # Return an object of this model
        return cls(name,
                   storage_array,
                   mtype,
                   volume)


