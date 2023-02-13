# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class CassandraLogRecoverJobParams(object):

    """Implementation of the 'CassandraLogRecoverJobParams' model.

    Attributes:
        end_time_for_log_replay_in_usecs (long|int): This is the end time from
            when logs should be replayed.
        log_backup_view_box_name (string): The view box name where commit logs
            are present.
        log_backup_view_name (string): The view name from where commit logs
            should be restored.
        object_names (list of string): Objects are of the form keyspace.table.
            If a full keyspace is selected to be restored, it is expanded
            before passing to imanis.
        start_time_for_log_replay_in_usecs (long|int):  This is the start time
            from when logs should be replayed.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "end_time_for_log_replay_in_usecs":'endTimeForLogReplayInUsecs',
        "log_backup_view_box_name":'logBackupViewBoxName',
        "log_backup_view_name":'logBackupViewName',
        "object_names":'objectNames',
        "start_time_for_log_replay_in_usecs":'startTimeForLogReplayInUsecs'
    }

    def __init__(self,
                 end_time_for_log_replay_in_usecs=None,
                 log_backup_view_box_name=None,
                 log_backup_view_name=None,
                 object_names=None,
                 start_time_for_log_replay_in_usecs=None):
        """Constructor for the CassandraLogRecoverJobParams class"""

        # Initialize members of the class
        self.end_time_for_log_replay_in_usecs = end_time_for_log_replay_in_usecs
        self.log_backup_view_box_name = log_backup_view_box_name
        self.log_backup_view_name = log_backup_view_name
        self.object_names = object_names
        self.start_time_for_log_replay_in_usecs = start_time_for_log_replay_in_usecs


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
        end_time_for_log_replay_in_usecs = dictionary.get('endTimeForLogReplayInUsecs')
        log_backup_view_box_name = dictionary.get('logBackupViewBoxName')
        log_backup_view_name = dictionary.get('logBackupViewName')
        start_time_for_log_replay_in_usecs = dictionary.get('startTimeForLogReplayInUsecs')
        object_names = dictionary.get('objectNames')

        # Return an object of this model
        return cls(end_time_for_log_replay_in_usecs,
                   log_backup_view_box_name,
                   log_backup_view_name,
                   object_names,
                   start_time_for_log_replay_in_usecs)


