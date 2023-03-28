# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.ad_restore_options
import cohesity_management_sdk.models.oracle_update_restore_task_options
import cohesity_management_sdk.models.update_restore_task_options


class UpdateRestoreTaskParams(object):

    """Implementation of the 'UpdateRestoreTaskParams' model.

    UpdateRestoreTaskParams holds the information to update a Restore Task in
    Magneto.


    Attributes:

        ad_options (AdRestoreOptions): Specifies the Active Directory options
            to update the Restore Task with.
        child_restore_task_ids (list of long|int): Specifies the ID of the
            child restore tasks of 'RestoreTaskId' to which the update is
            meant.
        enable_auto_sync (bool): Enables Auto Sync feature for SQL Multi-stage
            Restore task.
        options (UpdateRestoreTaskOptions): Specifies generic options to update
            the restore task.
        oracle_options (OracleUpdateRestoreTaskOptions): Specifies the oracle
            options to update the Restore Task with.
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
        "child_restore_task_ids":'childRestoreTaskIds',
        "enable_auto_sync":'enableAutoSync',
        "options":'options',
        "oracle_options":'oracleOptions',
        "restore_task_id":'restoreTaskId',
        "sql_options":'sqlOptions',
    }
    def __init__(self,
                 ad_options=None,
                 child_restore_task_ids=None,
                 enable_auto_sync=None,
                 options=None,
                 oracle_options=None,
                 restore_task_id=None,
                 sql_options=None,
            ):

        """Constructor for the UpdateRestoreTaskParams class"""

        # Initialize members of the class
        self.ad_options = ad_options
        self.child_restore_task_ids = child_restore_task_ids
        self.enable_auto_sync = enable_auto_sync
        self.options = options
        self.oracle_options = oracle_options
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
        child_restore_task_ids = dictionary.get("childRestoreTaskIds")
        enable_auto_sync = dictionary.get('enableAutoSync')
        options = cohesity_management_sdk.models.update_restore_task_options.UpdateRestoreTaskOptions.from_dictionary(dictionary.get('options')) if dictionary.get('options') else None
        oracle_options = cohesity_management_sdk.models.oracle_update_restore_task_options.OracleUpdateRestoreTaskOptions.from_dictionary(dictionary.get('oracleOptions')) if dictionary.get('oracleOptions') else None
        restore_task_id = dictionary.get('restoreTaskId')
        sql_options = dictionary.get('sqlOptions')

        # Return an object of this model
        return cls(
            ad_options,
            child_restore_task_ids,
            enable_auto_sync,
            options,
            oracle_options,
            restore_task_id,
            sql_options
)