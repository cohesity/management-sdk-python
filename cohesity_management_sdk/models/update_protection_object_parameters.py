# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.source_special_parameter
import cohesity_management_sdk.models.universal_id


class UpdateProtectionObjectParameters(object):

    """Implementation of the 'UpdateProtectionObjectParameters' model.

    Specifies the parameters to update a Protection Object.


    Attributes:

        pause_backup (bool): Specifies if the protection for the Protection
            Object is to be paused.
        protected_source_uid (UniversalId, required): Specifies the unique id
            of the Protected Source to be updated.
        rpo_policy_id (string): Specifies the unique id of the new RPO policy
            to assign to the object.
        source_parameters (list of SourceSpecialParameter): Specifies the
            additional special settings for a Protected Source.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "pause_backup":'pauseBackup',
        "protected_source_uid":'protectedSourceUid',
        "rpo_policy_id":'rpoPolicyId',
        "source_parameters":'sourceParameters',
    }
    def __init__(self,
                 pause_backup=None,
                 protected_source_uid=None,
                 rpo_policy_id=None,
                 source_parameters=None,
            ):

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
        pause_backup = dictionary.get('pauseBackup')
        protected_source_uid = cohesity_management_sdk.models.universal_id.UniversalId.from_dictionary(dictionary.get('protectedSourceUid')) if dictionary.get('protectedSourceUid') else None
        rpo_policy_id = dictionary.get('rpoPolicyId')
        source_parameters = None
        if dictionary.get('sourceParameters') != None:
            source_parameters = list()
            for structure in dictionary.get('sourceParameters'):
                source_parameters.append(cohesity_management_sdk.models.source_special_parameter.SourceSpecialParameter.from_dictionary(structure))

        # Return an object of this model
        return cls(
            pause_backup,
            protected_source_uid,
            rpo_policy_id,
            source_parameters
)