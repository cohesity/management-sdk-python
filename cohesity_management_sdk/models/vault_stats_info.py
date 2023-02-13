# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class VaultStatsInfo(object):

    """Implementation of the 'VaultStatsInfo' model.

    Specifies the stats for each vault.

    Attributes:
        id (long|int): Specifies the Vault Id.
        name (string): Specifies the Vault name.
        mtype (TypeVaultStatsInfoEnum): Specifies the Vault type.
        usage_bytes (long|int): Specifies the bytes used by the Vault.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "name":'name',
        "mtype":'type',
        "usage_bytes":'usageBytes'
    }

    def __init__(self,
                 id=None,
                 name=None,
                 mtype=None,
                 usage_bytes=None):
        """Constructor for the VaultStatsInfo class"""

        # Initialize members of the class
        self.id = id
        self.name = name
        self.mtype = mtype
        self.usage_bytes = usage_bytes


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
        id = dictionary.get('id')
        name = dictionary.get('name')
        mtype = dictionary.get('type')
        usage_bytes = dictionary.get('usageBytes')

        # Return an object of this model
        return cls(id,
                   name,
                   mtype,
                   usage_bytes)


