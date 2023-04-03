# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class RestoreO365TeamsParams_TargetChannel(object):

    """Implementation of the 'RestoreO365TeamsParams_TargetChannel' model.

    Target channel for teams granular restore to alternate loc. At least one of
    id or name must be specified. name must be specified if create_new_channel
    is true.


    Attributes:

        create_new_channel (bool): Whether to create a new channel. Name must
            be provided for this case.
        id (string): Id of the target channel.
        name (string): Name of the target channel.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "create_new_channel":'createNewChannel',
        "id":'id',
        "name":'name',
    }
    def __init__(self,
                 create_new_channel=None,
                 id=None,
                 name=None,
            ):

        """Constructor for the RestoreO365TeamsParams_TargetChannel class"""

        # Initialize members of the class
        self.create_new_channel = create_new_channel
        self.id = id
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
        create_new_channel = dictionary.get('createNewChannel')
        id = dictionary.get('id')
        name = dictionary.get('name')

        # Return an object of this model
        return cls(
            create_new_channel,
            id,
            name
)