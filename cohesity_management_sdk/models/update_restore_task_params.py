# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.ad_restore_options

class UpdateRestoreTaskParams(object):

    """Implementation of the 'UpdateRestoreTaskParams' model.

    UpdateRestoreTaskParams holds the information to update a Restore Task in
    Magneto.

    Attributes:
        ad_options (AdRestoreOptions): AdRestoreOptions are the AD specific
            options for the restore task being updated
        restore_task_id (long|int): Specifies the ID of the existing Restore
            Task to update.
        sql_options (SqlOptionsEnum): Specifies the sql options to update the
            Restore Task with. Specifies the action type of multi stage SQL
            restore.  'kCreate' specifies the create action for a restore.
            'kUpdate' specifies the user action to update an ongoing restore.
            'kFinalize' specifies the user action to finalize a restore.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ad_options":'adOptions',
        "restore_task_id":'restoreTaskId',
        "sql_options":'sqlOptions'
    }

    def __init__(self,
                 ad_options=None,
                 restore_task_id=None,
                 sql_options=None):
        """Constructor for the UpdateRestoreTaskParams class"""

        # Initialize members of the class
        self.ad_options = ad_options
        self.restore_task_id = restore_task_id
        self.sql_options = sql_options


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
        ad_options = cohesity_management_sdk.models.ad_restore_options.AdRestoreOptions.from_dictionary(dictionary.get('adOptions')) if dictionary.get('adOptions') else None
        restore_task_id = dictionary.get('restoreTaskId')
        sql_options = dictionary.get('sqlOptions')

        # Return an object of this model
        return cls(ad_options,
                   restore_task_id,
                   sql_options)


