# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.request_error
import cohesity_management_sdk.models.virtual_disk_restore_response

class VirtualDiskRecoverTaskState(object):

    """Implementation of the 'VirtualDiskRecoverTaskState' model.

    Specifies the complete information about a recover virtual disk task
    state.

    Attributes:
        error (RequestError): The error encountered by task (if any). Only
            valid if the task has finished.
        is_instant_recovery_finished (bool): Specifies if instant recovery of
            the virtual disk is complete.
        task_state (TaskStateEnum): Specifies the current state of the restore
            virtual disks task. Specifies the current state of the restore
            virtual disks task. 'kDetachDisksDone' indicates the detached
            state of disks. 'kSetupDisksDone' indicates that disks setup is
            completed. 'kMigrateDisksStarted' indicates that disks are being
            migrated. 'kMigrateDisksDone' indicates that disk migration is
            completed. 'kUnMountDatastoreDone' indicates that disk has
            unmounted the datastore.
        virtual_disk_restore_response (VirtualDiskRestoreResponse): Specifies
            the response for recovery of virtual disks of a vm.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "error":'error',
        "is_instant_recovery_finished":'isInstantRecoveryFinished',
        "task_state":'taskState',
        "virtual_disk_restore_response":'virtualDiskRestoreResponse'
    }

    def __init__(self,
                 error=None,
                 is_instant_recovery_finished=None,
                 task_state=None,
                 virtual_disk_restore_response=None):
        """Constructor for the VirtualDiskRecoverTaskState class"""

        # Initialize members of the class
        self.error = error
        self.is_instant_recovery_finished = is_instant_recovery_finished
        self.task_state = task_state
        self.virtual_disk_restore_response = virtual_disk_restore_response


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
        error = cohesity_management_sdk.models.request_error.RequestError.from_dictionary(dictionary.get('error')) if dictionary.get('error') else None
        is_instant_recovery_finished = dictionary.get('isInstantRecoveryFinished')
        task_state = dictionary.get('taskState')
        virtual_disk_restore_response = cohesity_management_sdk.models.virtual_disk_restore_response.VirtualDiskRestoreResponse.from_dictionary(dictionary.get('virtualDiskRestoreResponse')) if dictionary.get('virtualDiskRestoreResponse') else None

        # Return an object of this model
        return cls(error,
                   is_instant_recovery_finished,
                   task_state,
                   virtual_disk_restore_response)


