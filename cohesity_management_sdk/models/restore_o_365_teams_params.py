# -*- coding: utf-8 -*-
# Copyright 2021 Cohesity Inc.

import cohesity_management_sdk.models.restore_o_365_teams_params_ms_team_info
import cohesity_management_sdk.models.entity_proto

class RestoreO365TeamsParams(object):

    """Implementation of the 'RestoreO365TeamsParams' model.

    TODO: type model description here.

    Attributes:
        create_new_team (bool): Bool which specifies, if we have to create a
            new team if it doesn't exist.
        ms_teams_vec (list of RestoreO365TeamsParams_MSTeamInfo): List of
            teams getting restored.
        restore_original_owners_members (bool): Bool which specifies, if the
            original members/owners should be part of the newly created target
            team.
        restore_to_original (bool):  Whether or not all teams are restored to
            original location.
        target_ms_team_entity (EntityProto): Specifies the target ms team
            entity info and the team listed in the ms_teams_vec will be
            restored to this team if restore_to_original is false and
            create_new_team is false.
        target_team (string): Target team in case restore_to_original is false.
        target_team_name (string): Target team name in case restore_to_original
            is false. This will be ignored if restoring to alternate existing
            team.
        target_team_owner (string):The string which contains the owner smtp
            address for the target team.
        target_team_owner_entity (EntityProto): The addtional team owner
            entity info for the specified by target team.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "create_new_team":'createNewTeam',
        "ms_teams_vec":'msTeamsVec',
        "restore_original_owners_members":'restoreOriginalOwnersMembers',
        "restore_to_original":'restoreToOriginal',
        "target_ms_team_entity":'targetMsTeamEntity',
        "target_team":'targetTeam',
        "target_team_name":'targetTeamName',
        "target_team_owner":'targetTeamOwner',
        "target_team_owner_entity":'targetTeamOwnerEntity'
    }

    def __init__(self,
                 create_new_team=None,
                 ms_teams_vec=None,
                 restore_original_owners_members=None,
                 restore_to_original=None,
                 target_ms_team_entity=None,
                 target_team=None,
                 target_team_name=None,
                 target_team_owner=None,
                 target_team_owner_entity=None):
        """Constructor for the RestoreO365TeamsParams class"""

        # Initialize members of the class
        self.create_new_team = create_new_team
        self.ms_teams_vec = ms_teams_vec
        self.restore_original_owners_members = restore_original_owners_members
        self.restore_to_original = restore_to_original
        self.target_ms_team_entity = target_ms_team_entity
        self.target_team = target_team
        self.target_team_name = target_team_name
        self.target_team_owner = target_team_owner
        self.target_team_owner_entity = target_team_owner_entity


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
        create_new_team = dictionary.get('createNewTeam')
        ms_teams_vec = None
        if dictionary.get('msTeamsVec') != None:
            ms_teams_vec = list()
            for structure in dictionary.get('msTeamsVec'):
                ms_teams_vec.append(cohesity_management_sdk.models.restore_o_365_teams_params_ms_team_info.RestoreO365TeamsParams_MSTeamInfo.from_dictionary(structure))
        restore_original_owners_members = dictionary.get('restoreOriginalOwnersMembers')
        restore_to_original = dictionary.get('restoreToOriginal')
        target_ms_team_entity = cohesity_management_sdk.models.entity_proto.entity_proto.EntityProto.from_dictionary(dictionary.get('targetMsTeamEntity')) if dictionary.get('targetMsTeamEntity') else None
        target_team = dictionary.get('targetTeam')
        target_team_name = dictionary.get('targetTeamName')
        target_team_owner = dictionary.get('targetTeamOwner')
        target_team_owner_entity = cohesity_management_sdk.models.entity_proto.entity_proto.EntityProto.from_dictionary(dictionary.get('targetTeamOwnerEntity')) if dictionary.get('targetTeamOwnerEntity') else None

        # Return an object of this model
        return cls(create_new_team,
                   ms_teams_vec,
                   restore_original_owners_members,
                   restore_to_original,
                   target_ms_team_entity,
                   target_team,
                   target_team_name,
                   target_team_owner,
                   target_team_owner_entity)


