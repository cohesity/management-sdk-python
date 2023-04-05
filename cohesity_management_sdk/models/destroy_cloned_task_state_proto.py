# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.connector_params
import cohesity_management_sdk.models.deploy_vms_to_cloud_task_state_proto
import cohesity_management_sdk.models.destroy_clone_app_task_info_proto
import cohesity_management_sdk.models.destroy_cloned_vm_task_info_proto
import cohesity_management_sdk.models.destroy_mount_volumes_task_info_proto
import cohesity_management_sdk.models.entity_proto
import cohesity_management_sdk.models.error_proto
import cohesity_management_sdk.models.restored_object_vcd_config_proto
import cohesity_management_sdk.models.user_information


class DestroyClonedTaskStateProto(object):

    """Implementation of the 'DestroyClonedTaskStateProto' model.

    TODO: type description here.


    Attributes:

        action_executor_target_type (int): Denotes the target for action
            executor(Bridge/Bridge_Proxy) on which task on slave should execute
            actions.
        clone_task_name (string): The name of the clone task.
        datastore_entity (EntityProto): The EntityProto of the datastore that
            corresponds to the above 'view_name'. This field will be empty if
            no datastore is associated with the clone view.
        deploy_vms_to_cloud_task_state (DeployVMsToCloudTaskStateProto): Master
            populates information regarding deploy vm to cloud task state. This
            is needed during restore task of type kConvertAndDeployVMs. We use
            it during destroy clone to delete VMs, network entities and storage
            blobs.
        destroy_clone_app_task_info (DestroyCloneAppTaskInfoProto): Master
            populates the information about the destroy clone application task.
            Slave populates the progress and status of the task.
        destroy_clone_vm_task_info (DestroyClonedVMTaskInfoProto): Master
            populates the information about the destroy clone task. Slave
            populates the progress and status of the task.
        destroy_mount_volumes_task_info (DestroyMountVolumesTaskInfoProto):
            Master populates the information about the destroy mount volumes
            task, Slave populate the progress and status of the task.
        end_time_usecs (long|int): If the destroy clone task has finished, this
            field contains the end time of the task.
        error (ErrorProto): The error encountered by task (if any). Only valid
            if the task has finished.
        folder_entity (EntityProto): A folder entity where the cloned objects
            are placed. This folder will be deleted after all cloned entity are
            destroyed.
        force_delete (bool): flag used to perform force delete, ignore error on
            delete steps
        full_view_name (string): The full external view name where cloned
            objects are placed.
        parent_source_connection_params (ConnectorParams): Note: In case of
            kConvertAndDeployVMs to Azure, we need the original ConnectorParams
            of the corresponding deploy to Azure task (i.e. original Azure
            subscription id).
        parent_task_id (long|int): The id of the task that triggered the
            destroy task. This will be used by refresh task to mark the destroy
            task as internal sub-task.
        perform_clone_task_id (long|int): The unique id of the task that
            performed the clone operation.
        restore_type (int): The type of the restore/clone operation that is
            being destroyed.
        scheduled_constituent_id (long|int): Constituent id (and the gandalf
            session id) where this task has been scheduled. If -1, the task is
            not running at any slave. It's possible that the task was
            previously scheduled, but is now being re-scheduled.
        scheduled_gandalf_session_id (long|int): TODO: Type description here.
        start_time_usecs (long|int): The start time of this destroy clone task.
        status (int): Status of the destroy clone task.
        task_id (long|int): A globally unique id of this destroy clone task.
        mtype (int): The type of environment that is being operated on.
        user (string): The user who requested this destroy clone task.
        user_info (UserInformation): Specifies information about the user who
            made the request.
        vcd_config (RestoredObjectVCDConfigProto): VCD config for the restored
            object.
        view_box_id (long|int): The view box id to which 'view_name' belongs
            to.
        view_name_deprecated (string): The view name as provided by the user
            for the clone operation.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "action_executor_target_type":'actionExecutorTargetType',
        "clone_task_name":'cloneTaskName',
        "datastore_entity":'datastoreEntity',
        "deploy_vms_to_cloud_task_state":'deployVmsToCloudTaskState',
        "destroy_clone_app_task_info":'destroyCloneAppTaskInfo',
        "destroy_clone_vm_task_info":'destroyCloneVmTaskInfo',
        "destroy_mount_volumes_task_info":'destroyMountVolumesTaskInfo',
        "end_time_usecs":'endTimeUsecs',
        "error":'error',
        "folder_entity":'folderEntity',
        "force_delete":'forceDelete',
        "full_view_name":'fullViewName',
        "parent_source_connection_params":'parentSourceConnectionParams',
        "parent_task_id":'parentTaskId',
        "perform_clone_task_id":'performCloneTaskId',
        "restore_type":'restoreType',
        "scheduled_constituent_id":'scheduledConstituentId',
        "scheduled_gandalf_session_id":'scheduledGandalfSessionId',
        "start_time_usecs":'startTimeUsecs',
        "status":'status',
        "task_id":'taskId',
        "mtype":'type',
        "user":'user',
        "user_info":'userInfo',
        "vcd_config":'vcdConfig',
        "view_box_id":'viewBoxId',
        "view_name_deprecated":'viewName_DEPRECATED',
    }
    def __init__(self,
                 action_executor_target_type=None,
                 clone_task_name=None,
                 datastore_entity=None,
                 deploy_vms_to_cloud_task_state=None,
                 destroy_clone_app_task_info=None,
                 destroy_clone_vm_task_info=None,
                 destroy_mount_volumes_task_info=None,
                 end_time_usecs=None,
                 error=None,
                 folder_entity=None,
                 force_delete=None,
                 full_view_name=None,
                 parent_source_connection_params=None,
                 parent_task_id=None,
                 perform_clone_task_id=None,
                 restore_type=None,
                 scheduled_constituent_id=None,
                 scheduled_gandalf_session_id=None,
                 start_time_usecs=None,
                 status=None,
                 task_id=None,
                 mtype=None,
                 user=None,
                 user_info=None,
                 vcd_config=None,
                 view_box_id=None,
                 view_name_deprecated=None,
            ):

        """Constructor for the DestroyClonedTaskStateProto class"""

        # Initialize members of the class
        self.action_executor_target_type = action_executor_target_type
        self.clone_task_name = clone_task_name
        self.datastore_entity = datastore_entity
        self.deploy_vms_to_cloud_task_state = deploy_vms_to_cloud_task_state
        self.destroy_clone_app_task_info = destroy_clone_app_task_info
        self.destroy_clone_vm_task_info = destroy_clone_vm_task_info
        self.destroy_mount_volumes_task_info = destroy_mount_volumes_task_info
        self.end_time_usecs = end_time_usecs
        self.error = error
        self.folder_entity = folder_entity
        self.force_delete = force_delete
        self.full_view_name = full_view_name
        self.parent_source_connection_params = parent_source_connection_params
        self.parent_task_id = parent_task_id
        self.perform_clone_task_id = perform_clone_task_id
        self.restore_type = restore_type
        self.scheduled_constituent_id = scheduled_constituent_id
        self.scheduled_gandalf_session_id = scheduled_gandalf_session_id
        self.start_time_usecs = start_time_usecs
        self.status = status
        self.task_id = task_id
        self.mtype = mtype
        self.user = user
        self.user_info = user_info
        self.vcd_config = vcd_config
        self.view_box_id = view_box_id
        self.view_name_deprecated = view_name_deprecated

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
        action_executor_target_type = dictionary.get('actionExecutorTargetType')
        clone_task_name = dictionary.get('cloneTaskName')
        datastore_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('datastoreEntity')) if dictionary.get('datastoreEntity') else None
        deploy_vms_to_cloud_task_state = cohesity_management_sdk.models.deploy_vms_to_cloud_task_state_proto.DeployVMsToCloudTaskStateProto.from_dictionary(dictionary.get('deployVmsToCloudTaskState')) if dictionary.get('deployVmsToCloudTaskState') else None
        destroy_clone_app_task_info = cohesity_management_sdk.models.destroy_clone_app_task_info_proto.DestroyCloneAppTaskInfoProto.from_dictionary(dictionary.get('destroyCloneAppTaskInfo')) if dictionary.get('destroyCloneAppTaskInfo') else None
        destroy_clone_vm_task_info = cohesity_management_sdk.models.destroy_cloned_vm_task_info_proto.DestroyClonedVMTaskInfoProto.from_dictionary(dictionary.get('destroyCloneVmTaskInfo')) if dictionary.get('destroyCloneVmTaskInfo') else None
        destroy_mount_volumes_task_info = cohesity_management_sdk.models.destroy_mount_volumes_task_info_proto.DestroyMountVolumesTaskInfoProto.from_dictionary(dictionary.get('destroyMountVolumesTaskInfo')) if dictionary.get('destroyMountVolumesTaskInfo') else None
        end_time_usecs = dictionary.get('endTimeUsecs')
        error = cohesity_management_sdk.models.error_proto.ErrorProto.from_dictionary(dictionary.get('error')) if dictionary.get('error') else None
        folder_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('folderEntity')) if dictionary.get('folderEntity') else None
        force_delete = dictionary.get('forceDelete')
        full_view_name = dictionary.get('fullViewName')
        parent_source_connection_params = cohesity_management_sdk.models.connector_params.ConnectorParams.from_dictionary(dictionary.get('parentSourceConnectionParams')) if dictionary.get('parentSourceConnectionParams') else None
        parent_task_id = dictionary.get('parentTaskId')
        perform_clone_task_id = dictionary.get('performCloneTaskId')
        restore_type = dictionary.get('restoreType')
        scheduled_constituent_id = dictionary.get('scheduledConstituentId')
        scheduled_gandalf_session_id = dictionary.get('scheduledGandalfSessionId')
        start_time_usecs = dictionary.get('startTimeUsecs')
        status = dictionary.get('status')
        task_id = dictionary.get('taskId')
        mtype = dictionary.get('type')
        user = dictionary.get('user')
        user_info = cohesity_management_sdk.models.user_information.UserInformation.from_dictionary(dictionary.get('userInfo')) if dictionary.get('userInfo') else None
        vcd_config = cohesity_management_sdk.models.restored_object_vcd_config_proto.RestoredObjectVCDConfigProto.from_dictionary(dictionary.get('vcdConfig')) if dictionary.get('vcdConfig') else None
        view_box_id = dictionary.get('viewBoxId')
        view_name_deprecated = dictionary.get('viewName_DEPRECATED')

        # Return an object of this model
        return cls(
            action_executor_target_type,
            clone_task_name,
            datastore_entity,
            deploy_vms_to_cloud_task_state,
            destroy_clone_app_task_info,
            destroy_clone_vm_task_info,
            destroy_mount_volumes_task_info,
            end_time_usecs,
            error,
            folder_entity,
            force_delete,
            full_view_name,
            parent_source_connection_params,
            parent_task_id,
            perform_clone_task_id,
            restore_type,
            scheduled_constituent_id,
            scheduled_gandalf_session_id,
            start_time_usecs,
            status,
            task_id,
            mtype,
            user,
            user_info,
            vcd_config,
            view_box_id,
            view_name_deprecated
)