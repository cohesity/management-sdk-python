# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class UuidConfigProto(object):

    """Implementation of the 'UuidConfigProto' model.

    TODO: type model description here.

    Attributes:
        preserve_uuid (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "preserve_uuid":'preserveUuid'
    }

    def __init__(self,
                 preserve_uuid=None):
        """Constructor for the UuidConfigProto class"""

        # Initialize members of the class
        self.preserve_uuid = preserve_uuid


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
        preserve_uuid = dictionary.get('preserveUuid')

        # Return an object of this model
        return cls(preserve_uuid)


