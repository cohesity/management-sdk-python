# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class VcdStorageProfile(object):

    """Implementation of the 'VcdStorageProfile' model.

    Specifies a storage profile for use while recovering to a VMware VCD.

    Attributes:
        name (string): Specifies the name of the storage profile.
        uuid (string): Specifies the UUID of the storage profile as identified
            by the VCD.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "uuid": 'uuid'
    }

    def __init__(self,
                 name=None,
                 uuid=None):
        """Constructor for the VcdStorageProfile class"""

        # Initialize members of the class
        self.name = name
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
        name = dictionary.get('name', None)
        uuid = dictionary.get('uuid', None)

        # Return an object of this model
        return cls(name,
                   uuid)


