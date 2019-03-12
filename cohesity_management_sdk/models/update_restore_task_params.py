# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.


class UpdateRestoreTaskParams(object):

    """Implementation of the 'UpdateRestoreTaskParams' model.

    UpdateRestoreTaskParams holds the information to update a Restore Task in
    Magneto.

    Attributes:
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
        "restore_task_id":'restoreTaskId',
        "sql_options":'sqlOptions'
    }

    def __init__(self,
                 restore_task_id=None,
                 sql_options=None):
        """Constructor for the UpdateRestoreTaskParams class"""

        # Initialize members of the class
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
        restore_task_id = dictionary.get('restoreTaskId')
        sql_options = dictionary.get('sqlOptions')

        # Return an object of this model
        return cls(restore_task_id,
                   sql_options)


