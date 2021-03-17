# -*- coding: utf-8 -*-
# Copyright 2021 Cohesity Inc.

import cohesity_management_sdk.models.restore_o_365_teams_params_ms_team_info

class RestoreO365TeamsParams(object):

    """Implementation of the 'RestoreO365TeamsParams' model.

    Attributes:
        ms_teams_vec (list of RestoreO365TeamsParams_MSTeamInfo): List of teams
            getting restored.
        restore_to_original (bool): Whether or not all teams are restored to
            original location.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ms_teams_vec": 'msTeamsVec',
        "restore_to_original": 'restoreToOriginal'
    }

    def __init__(self,
                 ms_teams_vec=None,
                 restore_to_original=None):
        """Constructor for the RestoreO365TeamsParams class"""

        # Initialize members of the class
        self.ms_teams_vec = ms_teams_vec
        self.restore_to_original = restore_to_original


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
        ms_teams_vec = None
        if dictionary.get('msTeamsVec') != None:
            ms_teams_vec = list()
            for structure in dictionary.get('msTeamsVec'):
                ms_teams_vec.append(cohesity_management_sdk.models.restore_o_365_teams_params_ms_team_info.RestoreO365TeamsParams_MSTeamInfo.from_dictionary(structure))
        restore_to_original = dictionary.get('restoreToOriginal')

        # Return an object of this model
        return cls(ms_teams_vec,
                   restore_to_original)


