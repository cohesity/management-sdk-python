# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.restore_app_params

class RestoreAppTaskStateProto(object):

    """Implementation of the 'RestoreAppTaskStateProto' model.

    TODO: type model description here.

    Attributes:
        app_restore_progress_monitor_subtask_path (string): The Pulse task
            path to the application restore task sub tree. If the application
            restore has to wait on other tasks (for example, a SQL db restore
            may wait for a tail log backup or a VM restore), then this would
            represent a sub-tree of 'progress_monitor_task_path' in
            PerformRestoreTaskStateProto.
        child_restore_app_params_vec (list of RestoreAppParams): This has list
            of the restore app params for all the child restore tasks. This is
            populated iff the 'is_parent_task' is set to true.
        last_finished_log_backup_start_time_usecs (long|int): The start time
            of the last finished log backup run. For SQL application, this is
            set iff we need to take a tail log backup.
        restore_app_params (RestoreAppParams): This message captures all the
            necessary arguments specified by the user to restore an
            application.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "app_restore_progress_monitor_subtask_path":'appRestoreProgressMonitorSubtaskPath',
        "child_restore_app_params_vec":'childRestoreAppParamsVec',
        "last_finished_log_backup_start_time_usecs":'lastFinishedLogBackupStartTimeUsecs',
        "restore_app_params":'restoreAppParams'
    }

    def __init__(self,
                 app_restore_progress_monitor_subtask_path=None,
                 child_restore_app_params_vec=None,
                 last_finished_log_backup_start_time_usecs=None,
                 restore_app_params=None):
        """Constructor for the RestoreAppTaskStateProto class"""

        # Initialize members of the class
        self.app_restore_progress_monitor_subtask_path = app_restore_progress_monitor_subtask_path
        self.child_restore_app_params_vec = child_restore_app_params_vec
        self.last_finished_log_backup_start_time_usecs = last_finished_log_backup_start_time_usecs
        self.restore_app_params = restore_app_params


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
        app_restore_progress_monitor_subtask_path = dictionary.get('appRestoreProgressMonitorSubtaskPath')
        child_restore_app_params_vec = None
        if dictionary.get('childRestoreAppParamsVec') != None:
            child_restore_app_params_vec = list()
            for structure in dictionary.get('childRestoreAppParamsVec'):
                child_restore_app_params_vec.append(cohesity_management_sdk.models.restore_app_params.RestoreAppParams.from_dictionary(structure))
        last_finished_log_backup_start_time_usecs = dictionary.get('lastFinishedLogBackupStartTimeUsecs')
        restore_app_params = cohesity_management_sdk.models.restore_app_params.RestoreAppParams.from_dictionary(dictionary.get('restoreAppParams')) if dictionary.get('restoreAppParams') else None

        # Return an object of this model
        return cls(app_restore_progress_monitor_subtask_path,
                   child_restore_app_params_vec,
                   last_finished_log_backup_start_time_usecs,
                   restore_app_params)


