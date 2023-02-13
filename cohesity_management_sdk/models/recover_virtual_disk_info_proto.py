# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.error_proto
import cohesity_management_sdk.models.mo_ref
import cohesity_management_sdk.models.setup_restore_disk_task_info_proto

class RecoverVirtualDiskInfoProto(object):

    """Implementation of the 'RecoverVirtualDiskInfoProto' model.

    Each available extension is listed below along with the location of the
    proto file (relative to magneto/connectors) where it is defined.
    RecoverVirtualDiskInfoProto extension                     Location
    ===========================================================================
    ==
    ===========================================================================
    ==

    Attributes:
        cleanup_error (ErrorProto): TODO: type description here.
        data_migration_error (ErrorProto): TODO: type description here.
        error (ErrorProto): TODO: type description here.
        finished (bool): This will be set to true if the task is complete on
            the slave.
        instant_recovery_finished (bool): This will be set to true once the
            instant recovery of the virtual disk is complete.
        migrate_task_moref (MORef): TODO: type description here.
        restore_disks_task_info_proto (SetupRestoreDiskTaskInfoProto): Each
            available extension is listed below along with the location of the
            proto file (relative to magneto/connectors) where it is defined.
            SetupRestoreDiskTaskInfoProto extension, extension_number Location
            ===================================================================
            ========== vmware::SetupRestoreDiskTaskInfo
            vmware_setup_restore_disk_task_info, 100
            connectors/vmware/vmware_setup_restore_disks.proto.proto
            AgentSetupRestoreDiskTaskInfo agent_setup_restore_disk_task_info,
            101 base/agent.proto  app_file::SetupRestoreTaskInfo
            app_file_setup_restore_task_info, 102
            connectors/app_file/app_file_setup_restore.proto
            hyperv::SetupRestoreDiskTaskInfo
            hyperv_setup_restore_disk_task_info, 103
            connectors/hyperv/hyperv_setup_restore_disks.proto
            ===================================================================
            ==========
        slave_task_start_time_usecs (long|int): This is the timestamp at which
            the slave task started.
        task_state (int): The state of the task.
        mtype (int): The type of environment this recover virtual disk info
            pertains to.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cleanup_error":'cleanupError',
        "data_migration_error":'dataMigrationError',
        "error":'error',
        "finished":'finished',
        "instant_recovery_finished":'instantRecoveryFinished',
        "migrate_task_moref":'migrateTaskMoref',
        "restore_disks_task_info_proto":'restoreDisksTaskInfoProto',
        "slave_task_start_time_usecs":'slaveTaskStartTimeUsecs',
        "task_state":'taskState',
        "mtype":'type'
    }

    def __init__(self,
                 cleanup_error=None,
                 data_migration_error=None,
                 error=None,
                 finished=None,
                 instant_recovery_finished=None,
                 migrate_task_moref=None,
                 restore_disks_task_info_proto=None,
                 slave_task_start_time_usecs=None,
                 task_state=None,
                 mtype=None):
        """Constructor for the RecoverVirtualDiskInfoProto class"""

        # Initialize members of the class
        self.cleanup_error = cleanup_error
        self.data_migration_error = data_migration_error
        self.error = error
        self.finished = finished
        self.instant_recovery_finished = instant_recovery_finished
        self.migrate_task_moref = migrate_task_moref
        self.restore_disks_task_info_proto = restore_disks_task_info_proto
        self.slave_task_start_time_usecs = slave_task_start_time_usecs
        self.task_state = task_state
        self.mtype = mtype


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
        cleanup_error = cohesity_management_sdk.models.error_proto.ErrorProto.from_dictionary(dictionary.get('cleanupError')) if dictionary.get('cleanupError') else None
        data_migration_error = cohesity_management_sdk.models.error_proto.ErrorProto.from_dictionary(dictionary.get('dataMigrationError')) if dictionary.get('dataMigrationError') else None
        error = cohesity_management_sdk.models.error_proto.ErrorProto.from_dictionary(dictionary.get('error')) if dictionary.get('error') else None
        finished = dictionary.get('finished')
        instant_recovery_finished = dictionary.get('instantRecoveryFinished')
        migrate_task_moref = cohesity_management_sdk.models.mo_ref.MORef.from_dictionary(dictionary.get('migrateTaskMoref')) if dictionary.get('migrateTaskMoref') else None
        restore_disks_task_info_proto = cohesity_management_sdk.models.setup_restore_disk_task_info_proto.SetupRestoreDiskTaskInfoProto.from_dictionary(dictionary.get('restoreDisksTaskInfoProto')) if dictionary.get('restoreDisksTaskInfoProto') else None
        slave_task_start_time_usecs = dictionary.get('slaveTaskStartTimeUsecs')
        task_state = dictionary.get('taskState')
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(cleanup_error,
                   data_migration_error,
                   error,
                   finished,
                   instant_recovery_finished,
                   migrate_task_moref,
                   restore_disks_task_info_proto,
                   slave_task_start_time_usecs,
                   task_state,
                   mtype)


