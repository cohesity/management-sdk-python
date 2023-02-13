# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class Office365SiteInfo(object):

    """Implementation of the 'Office365SiteInfo' model.

    Specifies information about an Office365 sharepoint Site.

    Attributes:
        is_group_site (bool): Specifies if the sharepoint site is 
            ssociated with a group.
        is_private_channel_site (bool): Specifies if the sharepoint site is
            associated with a private channel of some team.
        is_team_site (bool): Specifies if the sharepoint site is associated
            with a team.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "is_group_site":'isGroupSite',
        "is_private_channel_site":'isPrivateChannelSite',
        "is_team_site":'isTeamSite'
    }

    def __init__(self,
                 is_group_site=None,
                 is_private_channel_site=None,
                 is_team_site=None):
        """Constructor for the Office365SiteInfo class"""

        # Initialize members of the class
        self.is_group_site = is_group_site
        self.is_private_channel_site = is_private_channel_site
        self.is_team_site = is_team_site


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
        is_group_site = dictionary.get('isGroupSite')
        is_private_channel_site = dictionary.get('isPrivateChannelSite')
        is_team_site = dictionary.get('isTeamSite')

        # Return an object of this model
        return cls(is_group_site,
                   is_private_channel_site,
                   is_team_site)


