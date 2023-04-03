# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.restore_o_365_teams_params_source_channel
import cohesity_management_sdk.models.restore_object


class RestoreO365TeamsParams_MSTeamInfo(object):

    """Implementation of the 'RestoreO365TeamsParams_MSTeamInfo' model.

    TODO: type description here.


    Attributes:

        is_full_team_required (bool): Specify if the entire Team is to be
            restored.
        object (RestoreObject): Todo(prann) : deprecate this and only keep the
            necessary info. This will store the details of the MS team to be
            restored.
        source_channel_vec (list of RestoreO365TeamsParams_SourceChannel):
            Channel items that have to be restored. This will be empty iff
            is_full_team_required is false.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "is_full_team_required":'isFullTeamRequired',
        "object":'object',
        "source_channel_vec":'sourceChannelVec',
    }
    def __init__(self,
                 is_full_team_required=None,
                 object=None,
                 source_channel_vec=None,
            ):

        """Constructor for the RestoreO365TeamsParams_MSTeamInfo class"""

        # Initialize members of the class
        self.is_full_team_required = is_full_team_required
        self.object = object
        self.source_channel_vec = source_channel_vec

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
        object = cohesity_management_sdk.models.restore_object.RestoreObject.from_dictionary(dictionary.get('object')) if dictionary.get('object') else None
        source_channel_vec = None
        if dictionary.get('sourceChannelVec') != None:
            source_channel_vec = list()
            for structure in dictionary.get('sourceChannelVec'):
                source_channel_vec.append(cohesity_management_sdk.models.restore_o_365_teams_params_source_channel.RestoreO365TeamsParams_SourceChannel.from_dictionary(structure))

        # Return an object of this model
        return cls(
            is_full_team_required,
            object,
            source_channel_vec
)