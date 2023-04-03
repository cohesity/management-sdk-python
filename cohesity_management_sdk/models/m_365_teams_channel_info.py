# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class M365TeamsChannelInfo(object):

    """Implementation of the 'M365TeamsChannelInfo' model.

    Specifies information about a M365 Teams Channel.


    Attributes:

        is_private (bool): Specifies if this is a private channel.
        name (string): Specifies the name of a M365 Teams channel.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "is_private":'isPrivate',
        "name":'name',
    }
    def __init__(self,
                 is_private=None,
                 name=None,
            ):

        """Constructor for the M365TeamsChannelInfo class"""

        # Initialize members of the class
        self.is_private = is_private
        self.name = name

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
        is_private = dictionary.get('isPrivate')
        name = dictionary.get('name')

        # Return an object of this model
        return cls(
            is_private,
            name
)