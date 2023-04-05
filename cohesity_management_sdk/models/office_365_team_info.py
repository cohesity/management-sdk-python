# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.m_365_teams_channel_info


class Office365TeamInfo(object):

    """Implementation of the 'Office365TeamInfo' model.

    Specifies information about an Office365 Team.


    Attributes:

        channel_count (long|int): Specifies the channel count associated with a
            team.
        channels (list of M365TeamsChannelInfo): Specifies the list of channels
            associated with a team.
        members_count (long|int): Specifies the members count associated with a
            team.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "channel_count":'channelCount',
        "channels":'channels',
        "members_count":'membersCount',
    }
    def __init__(self,
                 channel_count=None,
                 channels=None,
                 members_count=None,
            ):

        """Constructor for the Office365TeamInfo class"""

        # Initialize members of the class
        self.channel_count = channel_count
        self.channels = channels
        self.members_count = members_count

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
        channel_count = dictionary.get('channelCount')
        channels = None
        if dictionary.get('channels') != None:
            channels = list()
            for structure in dictionary.get('channels'):
                channels.append(cohesity_management_sdk.models.m_365_teams_channel_info.M365TeamsChannelInfo.from_dictionary(structure))
        members_count = dictionary.get('membersCount')

        # Return an object of this model
        return cls(
            channel_count,
            channels,
            members_count
)