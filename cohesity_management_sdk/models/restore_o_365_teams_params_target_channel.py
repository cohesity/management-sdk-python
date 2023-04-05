# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.entity_proto


class RestoreO365TeamsParams_TargetChannel(object):

    """Implementation of the 'RestoreO365TeamsParams_TargetChannel' model.

    Target channel for teams granular restore to alternate loc. At least one of
    id or name must be specified. name must be specified if create_new_channel
    is true.


    Attributes:

        channel_owner_vec (list of EntityProto): Owners for the private
            channel. This is needed only if we are creating private channel.
        channel_type (int): TODO: Type description here.
        create_new_channel (bool): Whether to create a new channel. Name must
            be provided for this case.
        id (string): Id of the target channel.
        name (string): Name of the target channel.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "channel_owner_vec":'channelOwnerVec',
        "channel_type":'channelType',
        "create_new_channel":'createNewChannel',
        "id":'id',
        "name":'name',
    }
    def __init__(self,
                 channel_owner_vec=None,
                 channel_type=None,
                 create_new_channel=None,
                 id=None,
                 name=None,
            ):

        """Constructor for the RestoreO365TeamsParams_TargetChannel class"""

        # Initialize members of the class
        self.channel_owner_vec = channel_owner_vec
        self.channel_type = channel_type
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
        channel_owner_vec = None
        if dictionary.get('channelOwnerVec') != None:
            channel_owner_vec = list()
            for structure in dictionary.get('channelOwnerVec'):
                channel_owner_vec.append(cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(structure))
        channel_type = dictionary.get('channelType')
        create_new_channel = dictionary.get('createNewChannel')
        id = dictionary.get('id')
        name = dictionary.get('name')

        # Return an object of this model
        return cls(
            channel_owner_vec,
            channel_type,
            create_new_channel,
            id,
            name
)