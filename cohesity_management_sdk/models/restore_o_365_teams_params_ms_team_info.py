# -*- coding: utf-8 -*-
# Copyright 2021 Cohesity Inc.

import cohesity_management_sdk.models.restore_object

class RestoreO365TeamsParams_MSTeamInfo(object):

    """Implementation of the 'RestoreO365TeamsParams_MSTeamInfo' model.

    IP Range for range of vip address addition.

    Attributes:
        is_full_team_required (bool): Specify if the entire Team is to be
            restored.
        mobject (string): Start IP of the range

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "is_full_team_required": 'isFullTeamRequired',
        "mobject": 'object'
    }

    def __init__(self,
                 is_full_team_required=None,
                 mobject=None):
        """Constructor for the RestoreO365TeamsParams_MSTeamInfo class"""

        # Initialize members of the class
        self.is_full_team_required = is_full_team_required
        self.mobject = mobject


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
        is_full_team_required = dictionary.get('isFullTeamRequired')
        mobject = cohesity_management_sdk.models.restore_object.RestoreObject.from_dictionary(dictionary.get('object')) if dictionary.get('object') else None

        # Return an object of this model
        return cls(is_full_team_required,
                   mobject)


