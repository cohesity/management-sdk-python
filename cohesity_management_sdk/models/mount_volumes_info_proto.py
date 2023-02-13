# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.error_proto
import cohesity_management_sdk.models.mount_volume_result
import cohesity_management_sdk.models.setup_restore_disk_task_info_proto

class MountVolumesInfoProto(object):

    """Implementation of the 'MountVolumesInfoProto' model.

    Each available extension is listed below along with the location of the
    proto file (relative to magneto/connectors) where it is defined.
    MountVolumesInfoProto extension                     Location
    ===========================================================================
    ==
    vmware::MountVolumesInfoProto::vmware_mount_volumes_info
    vmware/vmware.proto
    ===========================================================================
    ==

    Attributes:
        cleanup_error (ErrorProto): TODO: type description here.
        error (ErrorProto): TODO: type description here.
        finished (bool): This will be set to true if the task is complete on
            the slave.
        mount_volume_result_vec (list of MountVolumeResult): Contains the
            result information of the mounted volumes.
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
        mtype (int): The type of environment this mount volumes info pertains
            to.
        vm_online_disks_error (ErrorProto): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cleanup_error":'cleanupError',
        "error":'error',
        "finished":'finished',
        "mount_volume_result_vec":'mountVolumeResultVec',
        "restore_disks_task_info_proto":'restoreDisksTaskInfoProto',
        "slave_task_start_time_usecs":'slaveTaskStartTimeUsecs',
        "mtype":'type',
        "vm_online_disks_error":'vmOnlineDisksError'
    }

    def __init__(self,
                 cleanup_error=None,
                 error=None,
                 finished=None,
                 mount_volume_result_vec=None,
                 restore_disks_task_info_proto=None,
                 slave_task_start_time_usecs=None,
                 mtype=None,
                 vm_online_disks_error=None):
        """Constructor for the MountVolumesInfoProto class"""

        # Initialize members of the class
        self.cleanup_error = cleanup_error
        self.error = error
        self.finished = finished
        self.mount_volume_result_vec = mount_volume_result_vec
        self.restore_disks_task_info_proto = restore_disks_task_info_proto
        self.slave_task_start_time_usecs = slave_task_start_time_usecs
        self.mtype = mtype
        self.vm_online_disks_error = vm_online_disks_error


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
        error = cohesity_management_sdk.models.error_proto.ErrorProto.from_dictionary(dictionary.get('error')) if dictionary.get('error') else None
        finished = dictionary.get('finished')
        mount_volume_result_vec = None
        if dictionary.get('mountVolumeResultVec') != None:
            mount_volume_result_vec = list()
            for structure in dictionary.get('mountVolumeResultVec'):
                mount_volume_result_vec.append(cohesity_management_sdk.models.mount_volume_result.MountVolumeResult.from_dictionary(structure))
        restore_disks_task_info_proto = cohesity_management_sdk.models.setup_restore_disk_task_info_proto.SetupRestoreDiskTaskInfoProto.from_dictionary(dictionary.get('restoreDisksTaskInfoProto')) if dictionary.get('restoreDisksTaskInfoProto') else None
        slave_task_start_time_usecs = dictionary.get('slaveTaskStartTimeUsecs')
        mtype = dictionary.get('type')
        vm_online_disks_error = cohesity_management_sdk.models.error_proto.ErrorProto.from_dictionary(dictionary.get('vmOnlineDisksError')) if dictionary.get('vmOnlineDisksError') else None

        # Return an object of this model
        return cls(cleanup_error,
                   error,
                   finished,
                   mount_volume_result_vec,
                   restore_disks_task_info_proto,
                   slave_task_start_time_usecs,
                   mtype,
                   vm_online_disks_error)


