# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.deploy_v_ms_to_cloud_task_state_proto
import cohesity_management_sdk.models.error_proto
import cohesity_management_sdk.models.connector_params
import cohesity_management_sdk.models.no_sql_connect_params
import cohesity_management_sdk.models.no_sql_recover_job_params
import cohesity_management_sdk.models.power_state_config_proto
import cohesity_management_sdk.models.rename_object_param_proto
import cohesity_management_sdk.models.restore_o_365_groups_params
import cohesity_management_sdk.models.restore_acropolis_v_ms_params
import cohesity_management_sdk.models.restore_kubernetes_namespaces_params
import cohesity_management_sdk.models.restore_kvmv_ms_params
import cohesity_management_sdk.models.restore_o_365_teams_params
import cohesity_management_sdk.models.restore_o_365_public_folders_params
import cohesity_management_sdk.models.restore_object
import cohesity_management_sdk.models.restored_object_vcd_config_proto
import cohesity_management_sdk.models.restore_site_params
import cohesity_management_sdk.models.entity_proto
import cohesity_management_sdk.models.perform_restore_job_state_proto_restore_task
import cohesity_management_sdk.models.restore_vmware_vm_params
import cohesity_management_sdk.models.restored_object_network_config_proto
import cohesity_management_sdk.models.perform_restore_task_state_proto
import cohesity_management_sdk.models.user_information
import cohesity_management_sdk.models.view_params

class PerformRestoreJobStateProto(object):

    """Implementation of the 'PerformRestoreJobStateProto' model.

    Proto to define the persistent information of a wrapper restore job that
    spawns multiple child restore tasks.

    Attributes:
        admitted_time_usecs (long|int): The time at which the restore job was
            admitted to run on a Magneto master. This field will be set only
            after the status changes to 'kAdmitted'. Using this field, amount
            of time spent in the waiting/queued state and the amount of time
            taken taken to actually run the job can be determined. wait time =
            admitted_time_usecs - start_time_usecs run time = end_time_usecs -
            admitted_time_usecs
        cancellation_requested (bool): Whether this restore job has a pending
            cancellation request.
        continue_restore_on_error (bool): Whether to continue with the restore
            operation if restore of any object fails.
        deploy_vms_to_cloud_task_state (DeployVMsToCloudTaskStateProto): TODO:
            type description here.
        end_time_usecs (long|int): If the restore job has finished, this field
            contains the end time for the job.
        error (ErrorProto): TODO: type description here.
        name (string): The name of the restore job.
        nosql_connect_params (NoSqlConnectParams): Parameters to connect to
            destination nosql parent entity.
        nosql_recover_job_params (NoSqlRecoverJobParams): Additional
            parameters for the recovery job to send to imanis server.
        objects (list of RestoreObject): Information on the exact set of
            objects being restored (along with snapshots they are being
            recovered from). Even if the user wanted to restore an entire job
            form the latest snapshot, this will have individual objects and
            the exact snapshot they are bein restored from. If specified, this
            can only have leaf-level entities.
        parent_source_connection_params (ConnectorParams): Message that
            encapsulates the various params required to establish a connection
            with a particular environment.
        physical_flr_parallel_restore (bool): If enabled, magneto physical
            file restore will be enabled via job framework
        power_state_config (PowerStateConfigProto): TODO: type description
            here.
        preserve_tags (bool): Whether to preserve tags for the clone op.
          This field is currently used by HyperV and VMWare.
        progress_monitor_task_path (string): Root path of a Pulse task
            tracking the progress of the restore job.
        rename_restored_object_param (RenameObjectParamProto): Message to
            specify the prefix/suffix added to rename an object. At least one
            of prefix or suffix must be specified. Please note that both
            prefix and suffix can be specified.
        rename_restored_vapp_param (RenameObjectParamProto): An optional
            parameter to specify how restored vApps(kVirtualApp) are renamed.
            Please refer to comments for the field
            CreateRestoreTaskARg.rename_restored_vapp_param for more details.
        restore_acropolis_vms_params (RestoreAcropolisVMsParams): TODO: type
            description here.
        restore_groups_params (RestoreO365GroupsParams): This field defines
            o365 groups specific params for restore job of type
            kRecoverO365Groups.
        restore_job_id (long|int): A globally unique id for this restore job.
        restore_kubernetes_namespaces_params
            (RestoreKubernetesNamespacesParams): TODO: type description here.
        restore_kvm_vms_params (RestoreKVMVMsParams): TODO: type description
            here.
        restore_parent_source (EntityProto): Specifies the attributes and the
            latest statistics about an entity.
        restore_public_folders_params (RestoreO365PublicFoldersParams): This
            field defines the O365 Public Folders specific params for restore
            task of type kRecoverO365PublicFolders.
        restore_site_params (RestoreSiteParams): This field defines o365 site
            specific params for restore job of type kRecoverSites.
        restore_task_state_proto_tmpl (PerformRestoreTaskStateProto): This
            will be optionally populated for certain type of restores (FLR for
            now) and can be used as a template proto while creating the actual
            restore task later.
        restore_task_vec (list of PerformRestoreJobStateProtoRestoreTask):
            Even if the user wanted to restore an entire job from the latest
            snapshot, this will have info of all the individual objects.
        restore_teams_params (RestoreO365TeamsParams): This field defines the
            O365 Teams specific params for restore task of type
            kRecoverO365Teams.
        restore_vmware_vm_params (RestoreVmwareVMParams): TODO: type
            description here.
        restored_objects_network_config (RestoredObjectNetworkConfigProto):
            TODO: type description here.
        restored_to_different_source (bool): Whether restore is being
            performed to a different parent source.
        skip_image_deploy (bool): This flag can be set to true to just create
            the image and not deploy the VM. This flag is set to true during
            the DR operation that is invoked via runbooks, the creation of
            image(AMI in case of AWS) and snapshots of the data disk is
            achieved by invoking a restore of type kConvertAndDeployVMs
            and orchestration of the VMs is achieved by runbooks.
        start_time_usecs (long|int): The start time for this restore job.
        status (int): Status of the restore job.
        target_view_name (string): Name of the external view that the user
            specifies for restore operations. This field will be used to
            populate "full_view_name" field in PerformRestoreTaskStateProto so
            that each restore task uses the same view to clone the files into.
            This field currently only used for recovery type of kCloneVMs
            backed up using CDP VMs.
        mtype (int): The type of restore being performed.
        user (string): The user who requested this restore job.
        user_info (UserInformation): A message to encapsulate information
            about the user who made the request. Request should be filtered by
            these fields if specified so that only the objects that the user
            is permissioned for are returned. If both sid_vec & tenant_id are
            specified then an intersection of respective results should be
            returned.
        vcd_config (RestoredObjectVCDConfigProto): The params to use while
            recovering a vcd entity.
        view_box_id (long|int): The view box id to which the restore job
            belongs to.
        view_params (ViewParams): The params to use when cloning the view.
            This contains information about the view that is created when the
            user requests a clone operation. Information such as QoS,
            whitelisting can be provided
        warnings (List of ErrorProto): Populate warnings on the job if any.
            The warning messages are propagated from the child restore tasks
            upon completion of the task.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "admitted_time_usecs":'admittedTimeUsecs',
        "cancellation_requested":'cancellationRequested',
        "continue_restore_on_error":'continueRestoreOnError',
        "deploy_vms_to_cloud_task_state":'deployVmsToCloudTaskState',
        "end_time_usecs":'endTimeUsecs',
        "error":'error',
        "name":'name',
        "nosql_connect_params":'nosqlConnectParams',
        "nosql_recover_job_params":'nosqlRecoverJobParams',
        "objects":'objects',
        "parent_source_connection_params":'parentSourceConnectionParams',
        "physical_flr_parallel_restore":'physicalFlrParallelRestore',
        "power_state_config":'powerStateConfig',
        "preserve_tags":'preserveTags',
        "progress_monitor_task_path":'progressMonitorTaskPath',
        "rename_restored_object_param":'renameRestoredObjectParam',
        "rename_restored_vapp_param":'renameRestoredVappParam',
        "restore_acropolis_vms_params":'restoreAcropolisVmsParams',
        "restore_groups_params":'restoreGroupsParams',
        "restore_job_id":'restoreJobId',
        "restore_kubernetes_namespaces_params":'restoreKubernetesNamespacesParams',
        "restore_kvm_vms_params":'restoreKvmVmsParams',
        "restore_parent_source":'restoreParentSource',
        "restore_public_folders_params":'restorePublicFoldersParams',
        "restore_site_params":'restoreSiteParams',
        "restore_task_state_proto_tmpl":'restoreTaskStateProtoTmpl',
        "restore_task_vec":'restoreTaskVec',
        "restore_teams_params":'restoreTeamsParams',
        "restore_vmware_vm_params":'restoreVmwareVmParams',
        "restored_objects_network_config":'restoredObjectsNetworkConfig',
        "restored_to_different_source":'restoredToDifferentSource',
        "skip_image_deploy":'skipImageDeploy',
        "start_time_usecs":'startTimeUsecs',
        "status":'status',
        "target_view_name":'targetViewName',
        "mtype":'type',
        "user":'user',
        "user_info":'userInfo',
        "vcd_config":'vcdConfig',
        "view_box_id":'viewBoxId',
        "view_params":'viewParams',
        "warnings":'warnings'
    }

    def __init__(self,
                 admitted_time_usecs=None,
                 cancellation_requested=None,
                 continue_restore_on_error=None,
                 deploy_vms_to_cloud_task_state=None,
                 end_time_usecs=None,
                 error=None,
                 name=None,
                 nosql_connect_params=None,
                 nosql_recover_job_params=None,
                 objects=None,
                 parent_source_connection_params=None,
                 physical_flr_parallel_restore=None,
                 power_state_config=None,
                 preserve_tags=None,
                 progress_monitor_task_path=None,
                 rename_restored_object_param=None,
                 rename_restored_vapp_param=None,
                 restore_acropolis_vms_params=None,
                 restore_groups_params=None,
                 restore_job_id=None,
                 restore_kubernetes_namespaces_params=None,
                 restore_kvm_vms_params=None,
                 restore_parent_source=None,
                 restore_public_folders_params=None,
                 restore_site_params=None,
                 restore_task_state_proto_tmpl=None,
                 restore_task_vec=None,
                 restore_teams_params=None,
                 restore_vmware_vm_params=None,
                 restored_objects_network_config=None,
                 restored_to_different_source=None,
                 skip_image_deploy=None,
                 start_time_usecs=None,
                 status=None,
                 target_view_name=None,
                 mtype=None,
                 user=None,
                 user_info=None,
                 vcd_config=None,
                 view_box_id=None,
                 view_params=None,
                 warnings=None):
        """Constructor for the PerformRestoreJobStateProto class"""

        # Initialize members of the class
        self.admitted_time_usecs = admitted_time_usecs
        self.cancellation_requested = cancellation_requested
        self.continue_restore_on_error = continue_restore_on_error
        self.deploy_vms_to_cloud_task_state = deploy_vms_to_cloud_task_state
        self.end_time_usecs = end_time_usecs
        self.error = error
        self.name = name
        self.nosql_connect_params = nosql_connect_params
        self.nosql_recover_job_params = nosql_recover_job_params
        self.objects = objects
        self.parent_source_connection_params = parent_source_connection_params
        self.physical_flr_parallel_restore = physical_flr_parallel_restore
        self.power_state_config = power_state_config
        self.preserve_tags = preserve_tags
        self.progress_monitor_task_path = progress_monitor_task_path
        self.rename_restored_object_param = rename_restored_object_param
        self.rename_restored_vapp_param = rename_restored_vapp_param
        self.restore_acropolis_vms_params = restore_acropolis_vms_params
        self.restore_groups_params = restore_groups_params
        self.restore_job_id = restore_job_id
        self.restore_kubernetes_namespaces_params = restore_kubernetes_namespaces_params
        self.restore_kvm_vms_params = restore_kvm_vms_params
        self.restore_parent_source = restore_parent_source
        self.restore_public_folders_params = restore_public_folders_params
        self.restore_site_params = restore_site_params
        self.restore_task_state_proto_tmpl = restore_task_state_proto_tmpl
        self.restore_task_vec = restore_task_vec
        self.restore_teams_params = restore_teams_params
        self.restore_vmware_vm_params = restore_vmware_vm_params
        self.restored_objects_network_config = restored_objects_network_config
        self.restored_to_different_source = restored_to_different_source
        self.skip_image_deploy = skip_image_deploy
        self.start_time_usecs = start_time_usecs
        self.status = status
        self.target_view_name = target_view_name
        self.mtype = mtype
        self.user = user
        self.user_info = user_info
        self.vcd_config = vcd_config
        self.view_box_id = view_box_id
        self.view_params = view_params
        self.warnings = warnings


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
        admitted_time_usecs = dictionary.get('admittedTimeUsecs')
        cancellation_requested = dictionary.get('cancellationRequested')
        continue_restore_on_error = dictionary.get('continueRestoreOnError')
        deploy_vms_to_cloud_task_state = cohesity_management_sdk.models.deploy_v_ms_to_cloud_task_state_proto.DeployVMsToCloudTaskStateProto.from_dictionary(dictionary.get('deployVmsToCloudTaskState')) if dictionary.get('deployVmsToCloudTaskState') else None
        end_time_usecs = dictionary.get('endTimeUsecs')
        error = cohesity_management_sdk.models.error_proto.ErrorProto.from_dictionary(dictionary.get('error')) if dictionary.get('error') else None
        name = dictionary.get('name')
        nosql_connect_params = cohesity_management_sdk.models.no_sql_connect_params.NoSqlConnectParams.from_dictionary(dictionary.get('nosqlConnectParams')) if dictionary.get('nosqlConnectParams') else None
        nosql_recover_job_params = cohesity_management_sdk.models.no_sql_recover_job_params.NoSqlRecoverJobParams.from_dictionary(dictionary.get('nosqlRecoverJobParams')) if dictionary.get('nosqlRecoverJobParams') else None
        objects = None
        if dictionary.get('objects') != None:
            objects = list()
            for structure in dictionary.get('objects'):
                objects.append(cohesity_management_sdk.models.restore_object.RestoreObject.from_dictionary(structure))
        parent_source_connection_params = cohesity_management_sdk.models.connector_params.ConnectorParams.from_dictionary(dictionary.get('parentSourceConnectionParams')) if dictionary.get('parentSourceConnectionParams') else None
        physical_flr_parallel_restore = dictionary.get('physicalFlrParallelRestore')
        power_state_config = cohesity_management_sdk.models.power_state_config_proto.PowerStateConfigProto.from_dictionary(dictionary.get('powerStateConfig')) if dictionary.get('powerStateConfig') else None
        preserve_tags = dictionary.get('preserveTags', None)
        progress_monitor_task_path = dictionary.get('progressMonitorTaskPath')
        rename_restored_object_param = cohesity_management_sdk.models.rename_object_param_proto.RenameObjectParamProto.from_dictionary(dictionary.get('renameRestoredObjectParam')) if dictionary.get('renameRestoredObjectParam') else None
        rename_restored_vapp_param = cohesity_management_sdk.models.rename_object_param_proto.RenameObjectParamProto.from_dictionary(dictionary.get('renameRestoredVappParam')) if dictionary.get('renameRestoredVappParam') else None
        restore_acropolis_vms_params = cohesity_management_sdk.models.restore_acropolis_v_ms_params.RestoreAcropolisVMsParams.from_dictionary(dictionary.get('restoreAcropolisVmsParams')) if dictionary.get('restoreAcropolisVmsParams') else None
        restore_groups_params = cohesity_management_sdk.models.restore_o_365_groups_params.RestoreO365GroupsParams.from_dictionary(dictionary.get('restoreGroupsParams')) if dictionary.get('restoreGroupsParams') else None
        restore_job_id = dictionary.get('restoreJobId')
        restore_kubernetes_namespaces_params = cohesity_management_sdk.models.restore_kubernetes_namespaces_params.RestoreKubernetesNamespacesParams.from_dictionary(dictionary.get('restoreKubernetesNamespacesParams')) if dictionary.get('restoreKubernetesNamespacesParams') else None
        restore_kvm_vms_params = cohesity_management_sdk.models.restore_kvmv_ms_params.RestoreKVMVMsParams.from_dictionary(dictionary.get('restoreKvmVmsParams')) if dictionary.get('restoreKvmVmsParams') else None
        restore_parent_source = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('restoreParentSource')) if dictionary.get('restoreParentSource') else None
        restore_public_folders_params = cohesity_management_sdk.models.restore_o_365_public_folders_params.RestoreO365PublicFoldersParams.from_dictionary(dictionary.get('restorePublicFoldersParams')) if dictionary.get('restorePublicFoldersParams') else None
        restore_site_params = cohesity_management_sdk.models.restore_site_params.RestoreSiteParams.from_dictionary(dictionary.get('restoreSiteParams')) if dictionary.get('restoreSiteParams') else None
        restore_task_state_proto_tmpl = cohesity_management_sdk.models.perform_restore_task_state_proto.PerformRestoreTaskStateProto.from_dictionary(dictionary.get('restoreTaskStateProtoTmpl')) if dictionary.get('restoreTaskStateProtoTmpl') else None
        restore_task_vec = None
        if dictionary.get('restoreTaskVec') != None:
            restore_task_vec = list()
            for structure in dictionary.get('restoreTaskVec'):
                restore_task_vec.append(cohesity_management_sdk.models.perform_restore_job_state_proto_restore_task.PerformRestoreJobStateProtoRestoreTask.from_dictionary(structure))
        restore_teams_params = cohesity_management_sdk.models.restore_o_365_teams_params.RestoreO365TeamsParams.from_dictionary(dictionary.get('restoreTeamsParams')) if dictionary.get('restoreTeamsParams') else None
        restore_vmware_vm_params = cohesity_management_sdk.models.restore_vmware_vm_params.RestoreVmwareVMParams.from_dictionary(dictionary.get('restoreVmwareVmParams')) if dictionary.get('restoreVmwareVmParams') else None
        restored_objects_network_config = cohesity_management_sdk.models.restored_object_network_config_proto.RestoredObjectNetworkConfigProto.from_dictionary(dictionary.get('restoredObjectsNetworkConfig')) if dictionary.get('restoredObjectsNetworkConfig') else None
        restored_to_different_source = dictionary.get('restoredToDifferentSource')
        skip_image_deploy = dictionary.get('skipImageDeploy')
        start_time_usecs = dictionary.get('startTimeUsecs')
        status = dictionary.get('status')
        target_view_name = dictionary.get('targetViewName')
        mtype = dictionary.get('type')
        user = dictionary.get('user')
        user_info = cohesity_management_sdk.models.user_information.UserInformation.from_dictionary(dictionary.get('userInfo')) if dictionary.get('userInfo') else None
        vcd_config = cohesity_management_sdk.models.restored_object_vcd_config_proto.RestoredObjectVCDConfigProto.from_dictionary(dictionary.get('vcdConfig')) if dictionary.get('vcdConfig') else None
        view_box_id = dictionary.get('viewBoxId')
        view_params = cohesity_management_sdk.models.view_params.ViewParams.from_dictionary(dictionary.get('viewParams')) if dictionary.get('viewParams') else None
        warnings = dictionary.get('warnings')

        # Return an object of this model
        return cls(admitted_time_usecs,
                   cancellation_requested,
                   continue_restore_on_error,
                   deploy_vms_to_cloud_task_state,
                   end_time_usecs,
                   error,
                   name,
                   nosql_connect_params,
                   nosql_recover_job_params,
                   objects,
                   parent_source_connection_params,
                   physical_flr_parallel_restore,
                   power_state_config,
                   preserve_tags,
                   progress_monitor_task_path,
                   rename_restored_object_param,
                   rename_restored_vapp_param,
                   restore_acropolis_vms_params,
                   restore_groups_params,
                   restore_job_id,
                   restore_kubernetes_namespaces_params,
                   restore_kvm_vms_params,
                   restore_parent_source,
                   restore_public_folders_params,
                   restore_site_params,
                   restore_task_state_proto_tmpl,
                   restore_task_vec,
                   restore_teams_params,
                   restore_vmware_vm_params,
                   restored_objects_network_config,
                   restored_to_different_source,
                   skip_image_deploy,
                   start_time_usecs,
                   status,
                   target_view_name,
                   mtype,
                   user,
                   user_info,
                   vcd_config,
                   view_box_id,
                   view_params,
                   warnings)


