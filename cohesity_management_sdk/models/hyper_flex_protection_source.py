# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class HyperFlexProtectionSource(object):

    """Implementation of the 'HyperFlexProtectionSource' model.

    Specifies a Storage Snapshot Provider in a HyperFlex environment.

    Attributes:
        name (string): Specifies a unique name of the Protection Source
        product_version (string): Specifies the product version of the
            protection source.
        mtype (TypeHyperFlexProtectionSourceEnum): Specifies the type of
            managed Object in a HyperFlex protection source like kServer.
            Examples of a HyperFlex types include 'kServer'. 'kServer'
            indicates HyperFlex server entity.
        uuid (string): Specifies the uuid of the protection source.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "product_version":'productVersion',
        "mtype":'type',
        "uuid":'uuid'
    }

    def __init__(self,
                 name=None,
                 product_version=None,
                 mtype=None,
                 uuid=None):
        """Constructor for the HyperFlexProtectionSource class"""

        # Initialize members of the class
        self.name = name
        self.product_version = product_version
        self.mtype = mtype
        self.uuid = uuid


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
        product_version = dictionary.get('productVersion')
        mtype = dictionary.get('type')
        uuid = dictionary.get('uuid')

        # Return an object of this model
        return cls(name,
                   product_version,
                   mtype,
                   uuid)


