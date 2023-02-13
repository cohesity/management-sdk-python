# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.universal_id
import cohesity_management_sdk.models.source_special_parameter

class UpdateProtectionObjectParameters(object):

    """Implementation of the 'UpdateProtectionObjectParameters' model.

    Specifies the parameters to update a Protection Object.

    Attributes:
        pause_backup (bool): Specifies if the protection for the Protection
            Object is to be paused.
        protected_source_uid (UniversalId): Specifies an id for an object that
            is unique across Cohesity Clusters. The id is composite of all the
            ids listed below.
        rpo_policy_id (string): Specifies the unique id of the new RPO policy
            to assign to the object.
        source_parameters (list of SourceSpecialParameter): Specifies the
            additional special settings for a Protected Source.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "protected_source_uid":'protectedSourceUid',
        "pause_backup":'pauseBackup',
        "rpo_policy_id":'rpoPolicyId',
        "source_parameters":'sourceParameters'
    }

    def __init__(self,
                 protected_source_uid=None,
                 pause_backup=None,
                 rpo_policy_id=None,
                 source_parameters=None):
        """Constructor for the UpdateProtectionObjectParameters class"""

        # Initialize members of the class
        self.pause_backup = pause_backup
        self.protected_source_uid = protected_source_uid
        self.rpo_policy_id = rpo_policy_id
        self.source_parameters = source_parameters


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
        protected_source_uid = cohesity_management_sdk.models.universal_id.UniversalId.from_dictionary(dictionary.get('protectedSourceUid')) if dictionary.get('protectedSourceUid') else None
        pause_backup = dictionary.get('pauseBackup')
        rpo_policy_id = dictionary.get('rpoPolicyId')
        source_parameters = None
        if dictionary.get('sourceParameters') != None:
            source_parameters = list()
            for structure in dictionary.get('sourceParameters'):
                source_parameters.append(cohesity_management_sdk.models.source_special_parameter.SourceSpecialParameter.from_dictionary(structure))

        # Return an object of this model
        return cls(protected_source_uid,
                   pause_backup,
                   rpo_policy_id,
                   source_parameters)


