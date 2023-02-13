# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.migrate_oracle_clone_params

class OracleUpdateRestoreTaskOptions(object):

    """Implementation of the 'OracleUpdateRestoreTaskOptions' model.

    OracleUpdateRestoreTaskOptions holds the information needed for updating
    an Oracle restore task. Currently this contains Oracle clone specific
    details, which would be needed in the migration workflow.

    Attributes:
        migrate_clone_params (MigrateOracleCloneParams): Details needed for
            Oracle Clone migrations.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "migrate_clone_params":'MigrateCloneParams'
    }

    def __init__(self,
                 migrate_clone_params=None):
        """Constructor for the OracleUpdateRestoreTaskOptions class"""

        # Initialize members of the class
        self.migrate_clone_params = migrate_clone_params


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
        migrate_clone_params = cohesity_management_sdk.models.migrate_oracle_clone_params.MigrateOracleCloneParams.from_dictionary(dictionary.get('MigrateCloneParams')) if dictionary.get('MigrateCloneParams') else None

        # Return an object of this model
        return cls(migrate_clone_params)


