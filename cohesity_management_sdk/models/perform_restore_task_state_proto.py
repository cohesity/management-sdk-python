# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.backup_run_id
import cohesity_management_sdk.models.clone_app_view_info_proto
import cohesity_management_sdk.models.cloud_deploy_info_proto
import cohesity_management_sdk.models.deploy_vms_to_cloud_task_state_proto
import cohesity_management_sdk.models.entity_proto
import cohesity_management_sdk.models.mount_volumes_task_state_proto
import cohesity_management_sdk.models.multi_stage_restore_task_state_proto
import cohesity_management_sdk.models.no_sql_connect_params
import cohesity_management_sdk.models.no_sql_recover_job_params
import cohesity_management_sdk.models.perform_restore_task_state_proto
import cohesity_management_sdk.models.power_state_config_proto
import cohesity_management_sdk.models.recover_disks_task_state_proto
import cohesity_management_sdk.models.recover_volumes_task_state_proto
import cohesity_management_sdk.models.rename_object_param_proto
import cohesity_management_sdk.models.restore_acropolis_vms_params
import cohesity_management_sdk.models.restore_app_task_state_proto
import cohesity_management_sdk.models.restore_files_task_state_proto
import cohesity_management_sdk.models.restore_hyperv_vm_params
import cohesity_management_sdk.models.restore_info_proto
import cohesity_management_sdk.models.restore_kubernetes_namespaces_params
import cohesity_management_sdk.models.restore_kvm_vms_params
import cohesity_management_sdk.models.restore_o_365_groups_params
import cohesity_management_sdk.models.restore_o_365_public_folders_params
import cohesity_management_sdk.models.restore_o_365_teams_params
import cohesity_management_sdk.models.restore_object
import cohesity_management_sdk.models.restore_one_drive_params
import cohesity_management_sdk.models.restore_outlook_params
import cohesity_management_sdk.models.restore_site_params
import cohesity_management_sdk.models.restore_standby_task_state_proto
import cohesity_management_sdk.models.restore_task_state_base_proto
import cohesity_management_sdk.models.restore_vmware_vm_params
import cohesity_management_sdk.models.restored_object_network_config_proto
import cohesity_management_sdk.models.restored_object_vcd_config_proto
import cohesity_management_sdk.models.retrieve_archive_task_state_proto
import cohesity_management_sdk.models.sfdc_recover_job_params
import cohesity_management_sdk.models.uda_recover_job_params
import cohesity_management_sdk.models.universal_id_proto
import cohesity_management_sdk.models.vault_params_restore_params
import cohesity_management_sdk.models.view_params
import cohesity_management_sdk.models.volume_info


class PerformRestoreTaskStateProto(object):

    """Implementation of the 'PerformRestoreTaskStateProto' model.

    TODO: type description here.


    Attributes:

        action_executor_target_type (int): Denotes the target for action
            executor(Bridge / BridgeProxy) on which task on slave should
            execute actions.
        backup_run_lock_vec (list of BackupRunId): Information about the backup
            runs to lock during this restore.
        base (RestoreTaskStateBaseProto): Contains basic information about the
            restore task.
        can_teardown (bool): This is set if the clone operation has created any
            objects on the primary environment and teardown operation is
            possible. UI will disable the teardown button only if this is not
            set or set to false. NOTE: This won't be reset if the teardown
            operation subsequently completes as teardown state is managed
            separately.
        cdp_restore_progress_monitor_task_path (string): The path of the
            progress monitor for the task that is responsible for creating the
            CDP hydrated view.
        cdp_restore_task (PerformRestoreTaskStateProto): The CDP restore helper
            task which creates the hydrated views for the other restores.
        cdp_restore_task_id (long|int): The id of the task that will create the
            CDP hydrated view.
        cdp_restore_view_name (string): The temporary view where the hydrated
            disks of the CDP restores are kept.
        child_clone_task_id (long|int): The id of the child clone task
            triggered by refresh op.
        child_destroy_task_id (long|int): The following fields are used by
            clone refresh op. These will be present only in case of refresh
            task op.  The id of the child destroy clone task triggered by
            refresh op.
        clone_app_view_info (CloneAppViewInfoProto): The information about
            cloned backup view of an App [ ex. Oracle,SQL]. Currently this only
            contains the clone view information for Oracle, which contains the
            vector of mount-paths where the cloned view got mounted on the
            Oracle Host.
        cloud_deploy_info (CloudDeployInfoProto): This is set only when the
            restore task is of type kDeployVMs. It contains information about
            the kDeployVMs restore task that is populated by the slave.
        continue_restore_on_error (bool): Whether to continue with the restore
            operation if restore of any object fails.
        create_view (bool): True iff the target view needs to be created.
        datastore_entity_vec (list of EntityProto): Please refer to comments
            for the field CreateRestoreTaskArg.datastore_entity_vec for more
            details.
        deploy_vms_to_cloud_task_state (DeployVMsToCloudTaskStateProto): This
            contains information regarding deploy vm to cloud task state. This
            is set for restore type kConvertAndDeployVMs.
        folder_entity (EntityProto): Semantics for a restore task of type
            kCloneVMs: For a successful restore task, it will be always set.
            For a failed task, it may or may not be set.  Semantics for a
            restore task of type kRecoverVMs: Folder entity will be set only if
            objects were restored to a different source.
        full_view_name (string): The full view name (internal or external).
            This is composed of an optional Cohesity specific prefix and the
            user provided view name.
        include_vm_config (bool): This is set to true if the vm-config.xml need
            to be copied in the target view/folder.
        is_multi_stage_restore (bool): Whether this task is a multi-stage
            restore task.
        mount_volumes_task_state (MountVolumesTaskStateProto): This contains
            information regarding mount volumes task state. This is set for
            restore type kMountVolumes.
        multi_restore_task_id (long|int): The id of the task that is created to
            restore multiple apps. For e.g., user requested to restore multiple
            databases or multiple AD objects. When the user requests to restore
            'n' objects, we will create 'n+1' restore tasks with 'n' child
            tasks and one multi restore task. The relationship is maintained by
            stamping the id of the multi restore task on all the child tasks
            using this parameter.
        multi_stage_restore_task_state (MultiStageRestoreTaskStateProto): Note
            that this information can be used inside a subtask created by a
            multi-stage restore task, where the subtask itself is not a
            multi-stage restore task.
        nosql_connect_params (NoSqlConnectParams): Parameters to connect to
            destination nosql parent entity.
        nosql_recover_job_params (NoSqlRecoverJobParams): Additional parameters
            for the recovery job to send to imanis server.
        object_name_deprecated (string): An optional name to give to the
            restored object.
        objects (list of RestoreObject): Information on the exact set of
            objects being restored (along with snapshots they are being
            recovered from). Even if the user wanted to restore an entire job
            from the latest snapshot, this will have individual objects and the
            exact snapshot they are being restored from. If specified, this can
            only have leaf-level entities.
        objects_progress_monitor_task_paths (list of string): Vector containing
            the relative task path of progress monitors of the objects in the
            above field 'objects' to be restored. There is one to one
            correspondence between elements in 'objects' and
            'objects_progress_monitor_task_paths'.  Please note that this field
            will be set only after progress monitor is created for this restore
            task.
        parent_restore_job_id (long|int): If this a child restore task, this
            field will contain the id of the parent restore job that spawned
            this task.  List of env and action type for which this field is
            applicable are: Acropolis: kRecoverVMs.
        parent_restore_task_id (long|int): The id of the parent restore task if
            this is a restore sub-task.  List of environments that use this
            field: kSQL : Used for multi-stage SQL restore that supports a
            hot-standby. kVMware: Used for multi-stage restore that supports a
            hot-standby.  This will also be used by refresh op to mark the new
            clone as internal sub-task.
        path_prefix_deprecated (string): TODO: Type description here.
        physical_flr_parallel_restore (bool): If enabled, magneto physical file
            restore will be enabled via job framework
        physical_flr_use_new_locking_method (bool): If enabled, magneto
            physical file restore will be enabled via job framework
        power_state_config (PowerStateConfigProto): The power state
            configuration to be applied to the restored object. Please refer to
            comments for the field CreateRestoreTaskArg.power_state_config for
            more details.
        preserve_tags (bool): This field is currently used by HyperV and
            VMWare.
        progress_monitor_task_path (string): Root path of a Pulse task tracking
            the progress of the restore task.
        recover_disks_task_state (RecoverDisksTaskStateProto): Contains
            information pertinent to a virtual disk recovery task. This is set
            for restore type kRecoverDisks.
        recover_volumes_task_state (RecoverVolumesTaskStateProto): Contains
            information pertinent to a volume recovery task. This is set for
            restore type kRecoverVolumes.
        related_restore_task_id (long|int): The task id of a related restore
            task. For example, a SQL restore operation may involve restoring a
            VM first and then restoring SQL databases after that. So the
            corresponding VM restore and SQL database restore tasks will be
            related, and they will each have their 'related_restore_task_id'
            set to the id of the other task.
        rename_restored_object_param (RenameObjectParamProto): An optional
            parameter to specify how restored objects are renamed. Please refer
            to comments for the field
            CreateRestoreTaskArg.rename_restored_object_param for more details.
        rename_restored_vapp_param (RenameObjectParamProto): An optional
            parameter to specify how restored vApps(kVirtualApp) are renamed.
            Please refer to comments for the field
            CreateRestoreTaskArg.rename_restored_vapp_param for more details.
        resource_pool_entity (EntityProto): The resource pool entity where the
            restored objects will be attached. Please refer to comments for the
            field CreateRestoreTaskArg.resource_pool_entity for more details.
        restore_acropolis_vms_params (RestoreAcropolisVMsParams): This field
            defines the Acropolis specific params for restore task of type
            kRecoverVMs.
        restore_app_task_state (RestoreAppTaskStateProto): This contains
            information about application restore task state. This is set for
            restore types kRecoverApp/kCloneApp/kCloneRefreshApp.
        restore_files_task_state (RestoreFilesTaskStateProto): This contains
            information regarding restore files task state. This is set for
            restore type kRestoreFiles and kDownloadFiles. Restore type
            kConvertToPst also sets this for download zip file path.
        restore_groups_params (RestoreO365GroupsParams): This field defines the
            O365 groups specific params for restore task of type
            kRecoverO365Groups.
        restore_hyperv_vm_params (RestoreHyperVVMParams): This field defines
            the HyperV specific params for restore tasks of type kCloneVMs and
            kRecoverVMs.
        restore_info (RestoreInfoProto): Contains information about this
            restore task that is populated by the slave.
        restore_kubernetes_namespaces_params
            (RestoreKubernetesNamespacesParams): This field defines the
            Kubernetes specific params for restore task of type
            kRecoverNamespaces.
        restore_kvm_vms_params (RestoreKVMVMsParams): This field defines the
            KVM specific params for restore task of type kRecoverVMs.
        restore_one_drive_params (RestoreOneDriveParams): This field defines
            the one drive specific params for restore task of type
            kRecoverO365Drive.
        restore_outlook_params (RestoreOutlookParams): This field defines the
            O365 specific params for restore task of type kRecoverEmails.
        restore_parent_source (EntityProto): An optional registered parent
            source to which objects are to be restored. If not specified,
            objects are restored back to the original source that was managing
            the objects. If 'restored_to_different_source' is set to true, then
            this field must be specified.
        restore_public_folders_params (RestoreO365PublicFoldersParams): This
            field defines the O365 Public Folders specific params for restore
            task of type kRecoverO365PublicFolders.
        restore_site_params (RestoreSiteParams): This field defines the O365
            site specific params for restore task of type kRecoverSites.
        restore_standby_task_state (RestoreStandbyTaskStateProto): This
            contains information regarding standby restore task state. This is
            currently only set for kRecoverVMs restore type for kVMware
            environment.
        restore_sub_task_vec (list of long|int): Inside Magneto, these are
            represented as regular restore tasks with their own
            PerformRestoreTaskStateProto. Each restore sub-task will have its
            parent_restore_task_id field set.  List of environments that use
            this field: kSQL : Used for multi-stage SQL restore that supports a
            hot-standby. kVMware : User for standby restore to store
            CDPLogApplyRestoreOp id. kOracle : Used for Instant restore for
            clone.
        restore_task_purged (bool): Whether the restore task is purged. During
            WAL recovery, purged restore tasks are ignored.
        restore_teams_params (RestoreO365TeamsParams): This field defines team
            specific params for restore task of type kRecoverO365Teams.
        restore_view_datastore_entity (EntityProto): Please note that this
            field will be set only for the restore task of type kCloneVMs.
        restore_vmware_vm_params (RestoreVMwareVMParams): This field defines
            the VMware specific params for restore tasks of type kCloneVMs and
            kRecoverVMs.
        restored_data_storage_domain_id (long|int): The storage domain id to
            which the data is restored.  E.g.: For folder download tasks, this
            denotes the storage domain (view box) id in which the zip file
            created by yoda is stored - in case of CAD jobs this could be the
            auxiliary view box corresponding to the CAD view box, and for
            regular jobs, this is most likely same as the view box used by that
            job.
        restored_objects_network_config (RestoredObjectNetworkConfigProto): The
            network configuration to be applied to the restored object. Please
            refer to comments for the field
            CreateRestoreTaskArg.restored_objects_network_config for more
            details.
        restored_to_different_source (bool): Whether restore is being performed
            to a different parent source.
        retrieve_archive_progress_monitor_task_path (string): The path of the
            progress monitor for the task that is responsible for retrieving
            the objects from the archive.
        retrieve_archive_stub_view_name (string): The stub view created by
            Icebox corresponding to the archive. The stub view is used to
            selectively retrieve files and folders.
        retrieve_archive_task_uid_vec (list of UniversalIdProto): The uid of
            the tasks that will retrieve the objects from the archive.
            Typically we only retrieve one snapshot for an enity but for point
            in time restores for SQL/Oracle database, we may need to retrieve
            multiple snapshots typically one full, and few logs. Hence we may
            need multiple uids to start retrieval task.
        retrieve_archive_task_vec (list of RetrieveArchiveTaskStateProto):
            Proto that contains all the information about the retrieve archive
            task. Typically we only retrieve one snapshot for an enity but for
            point in time restores for SQL/Oracle database, we may need to
            retrieve multiple snapshots typically one full, and few logs. As we
            may start the multiple retrieval tasks, we need vector of
            RetrieveArchiveTaskStateProto for storing information of retrieved
            archive tasks.
        retrieve_archive_view_name (string): The temporary view where the
            entities that have been retrieved from an archive have been placed
            in by Icebox.
        selected_datastore_idx (long|int): In case of restore job with multi-vm
            multi-datastore this field denotes the specific datastore index in
            datastore_entity_vec to be selected for the task. Not going for
            specific datastore allocation in datastore_entity_vec so that we
            have required information in case of extensibility for task level
            retries with different datastore
        sfdc_recover_job_params (SfdcRecoverJobParams): This field defines the
            sfdc specific params for restore task of type kRecoverSfdc.
        skip_cloning_retrieve_archive_view (bool): Whether Magneto should use
            the 'retrieve_archive_stub_view' above for restore without cloning
            it. We are currently setting it for Direct archive restores using
            stub views.
        skip_image_deploy (bool): This flag can be set to true to just create
            the image and not deploy the VM. This flag is set to true during
            the DR operation that is invoked via runbooks, the creation of
            image(AMI in case of AWS) and snapshots of the data disk is
            achieved by invoking a restore of type kConvertAndDeployVMs and
            orchestration of the VMs is achieved by runbooks.
        skip_rigel_for_restore (bool): Whether to skip Rigel for restore or
            not. This field is applicable only for DMaaS. This field is
            currently being used in DRaaS workflows only.
        stub_view_relative_dir_name (string): Relative directory inside the
            stub view that corresponds with the archive.
        uda_recover_job_params (UdaRecoverJobParams): This field defines the
            uda specific params for restore task of type kRecoverUda.
        vault_restore_params (VaultParams_RestoreParams): Params to be passed
            to Icebox while restoring data from an archive.
        vcd_config (RestoredObjectVCDConfigProto): VApp config for the restored
            object.
        vcd_storage_profile_datastore_moref_vec (list of string): This field is
            applicable for VCD type recovery. It defines the compatible
            datastores for recovery to alternate location. This field is
            inferred using the storage profile in restore_vmware_vm_params
            below.
        view_box_id (long|int): The view box id to which 'view_name' belongs
            to. In case the restore task corresponds to a backup job, this view
            box corresponds to the view box of the backup job.
        view_name_deprecated (string): The view name as provided by the user
            for this restore operation.
        view_params (ViewParams): The params to use when cloning the view.
        vm_restore_reuse_cdp_view (bool): Whether VM restore should reuse the
            cdp restore view while VM recovery.
        volume_info_vec (list of VolumeInfo): Information regarding volumes
            that are required for the restore task. This is populated for
            restore files and mount virtual disk ops.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "action_executor_target_type":'actionExecutorTargetType',
        "backup_run_lock_vec":'backupRunLockVec',
        "base":'base',
        "can_teardown":'canTeardown',
        "cdp_restore_progress_monitor_task_path":'cdpRestoreProgressMonitorTaskPath',
        "cdp_restore_task":'cdpRestoreTask',
        "cdp_restore_task_id":'cdpRestoreTaskId',
        "cdp_restore_view_name":'cdpRestoreViewName',
        "child_clone_task_id":'childCloneTaskId',
        "child_destroy_task_id":'childDestroyTaskId',
        "clone_app_view_info":'cloneAppViewInfo',
        "cloud_deploy_info":'cloudDeployInfo',
        "continue_restore_on_error":'continueRestoreOnError',
        "create_view":'createView',
        "datastore_entity_vec":'datastoreEntityVec',
        "deploy_vms_to_cloud_task_state":'deployVmsToCloudTaskState',
        "folder_entity":'folderEntity',
        "full_view_name":'fullViewName',
        "include_vm_config":'includeVmConfig',
        "is_multi_stage_restore":'isMultiStageRestore',
        "mount_volumes_task_state":'mountVolumesTaskState',
        "multi_restore_task_id":'multiRestoreTaskId',
        "multi_stage_restore_task_state":'multiStageRestoreTaskState',
        "nosql_connect_params":'nosqlConnectParams',
        "nosql_recover_job_params":'nosqlRecoverJobParams',
        "object_name_deprecated":'objectName_DEPRECATED',
        "objects":'objects',
        "objects_progress_monitor_task_paths":'objectsProgressMonitorTaskPaths',
        "parent_restore_job_id":'parentRestoreJobId',
        "parent_restore_task_id":'parentRestoreTaskId',
        "path_prefix_deprecated":'pathPrefix_DEPRECATED',
        "physical_flr_parallel_restore":'physicalFlrParallelRestore',
        "physical_flr_use_new_locking_method":'physicalFlrUseNewLockingMethod',
        "power_state_config":'powerStateConfig',
        "preserve_tags":'preserveTags',
        "progress_monitor_task_path":'progressMonitorTaskPath',
        "recover_disks_task_state":'recoverDisksTaskState',
        "recover_volumes_task_state":'recoverVolumesTaskState',
        "related_restore_task_id":'relatedRestoreTaskId',
        "rename_restored_object_param":'renameRestoredObjectParam',
        "rename_restored_vapp_param":'renameRestoredVappParam',
        "resource_pool_entity":'resourcePoolEntity',
        "restore_acropolis_vms_params":'restoreAcropolisVmsParams',
        "restore_app_task_state":'restoreAppTaskState',
        "restore_files_task_state":'restoreFilesTaskState',
        "restore_groups_params":'restoreGroupsParams',
        "restore_hyperv_vm_params":'restoreHypervVmParams',
        "restore_info":'restoreInfo',
        "restore_kubernetes_namespaces_params":'restoreKubernetesNamespacesParams',
        "restore_kvm_vms_params":'restoreKvmVmsParams',
        "restore_one_drive_params":'restoreOneDriveParams',
        "restore_outlook_params":'restoreOutlookParams',
        "restore_parent_source":'restoreParentSource',
        "restore_public_folders_params":'restorePublicFoldersParams',
        "restore_site_params":'restoreSiteParams',
        "restore_standby_task_state":'restoreStandbyTaskState',
        "restore_sub_task_vec":'restoreSubTaskVec',
        "restore_task_purged":'restoreTaskPurged',
        "restore_teams_params":'restoreTeamsParams',
        "restore_view_datastore_entity":'restoreViewDatastoreEntity',
        "restore_vmware_vm_params":'restoreVmwareVmParams',
        "restored_data_storage_domain_id":'restoredDataStorageDomainId',
        "restored_objects_network_config":'restoredObjectsNetworkConfig',
        "restored_to_different_source":'restoredToDifferentSource',
        "retrieve_archive_progress_monitor_task_path":'retrieveArchiveProgressMonitorTaskPath',
        "retrieve_archive_stub_view_name":'retrieveArchiveStubViewName',
        "retrieve_archive_task_uid_vec":'retrieveArchiveTaskUidVec',
        "retrieve_archive_task_vec":'retrieveArchiveTaskVec',
        "retrieve_archive_view_name":'retrieveArchiveViewName',
        "selected_datastore_idx":'selectedDatastoreIdx',
        "sfdc_recover_job_params":'sfdcRecoverJobParams',
        "skip_cloning_retrieve_archive_view":'skipCloningRetrieveArchiveView',
        "skip_image_deploy":'skipImageDeploy',
        "skip_rigel_for_restore":'skipRigelForRestore',
        "stub_view_relative_dir_name":'stubViewRelativeDirName',
        "uda_recover_job_params":'udaRecoverJobParams',
        "vault_restore_params":'vaultRestoreParams',
        "vcd_config":'vcdConfig',
        "vcd_storage_profile_datastore_moref_vec":'vcdStorageProfileDatastoreMorefVec',
        "view_box_id":'viewBoxId',
        "view_name_deprecated":'viewName_DEPRECATED',
        "view_params":'viewParams',
        "vm_restore_reuse_cdp_view":'vmRestoreReuseCdpView',
        "volume_info_vec":'volumeInfoVec',
    }
    def __init__(self,
                 action_executor_target_type=None,
                 backup_run_lock_vec=None,
                 base=None,
                 can_teardown=None,
                 cdp_restore_progress_monitor_task_path=None,
                 cdp_restore_task=None,
                 cdp_restore_task_id=None,
                 cdp_restore_view_name=None,
                 child_clone_task_id=None,
                 child_destroy_task_id=None,
                 clone_app_view_info=None,
                 cloud_deploy_info=None,
                 continue_restore_on_error=None,
                 create_view=None,
                 datastore_entity_vec=None,
                 deploy_vms_to_cloud_task_state=None,
                 folder_entity=None,
                 full_view_name=None,
                 include_vm_config=None,
                 is_multi_stage_restore=None,
                 mount_volumes_task_state=None,
                 multi_restore_task_id=None,
                 multi_stage_restore_task_state=None,
                 nosql_connect_params=None,
                 nosql_recover_job_params=None,
                 object_name_deprecated=None,
                 objects=None,
                 objects_progress_monitor_task_paths=None,
                 parent_restore_job_id=None,
                 parent_restore_task_id=None,
                 path_prefix_deprecated=None,
                 physical_flr_parallel_restore=None,
                 physical_flr_use_new_locking_method=None,
                 power_state_config=None,
                 preserve_tags=None,
                 progress_monitor_task_path=None,
                 recover_disks_task_state=None,
                 recover_volumes_task_state=None,
                 related_restore_task_id=None,
                 rename_restored_object_param=None,
                 rename_restored_vapp_param=None,
                 resource_pool_entity=None,
                 restore_acropolis_vms_params=None,
                 restore_app_task_state=None,
                 restore_files_task_state=None,
                 restore_groups_params=None,
                 restore_hyperv_vm_params=None,
                 restore_info=None,
                 restore_kubernetes_namespaces_params=None,
                 restore_kvm_vms_params=None,
                 restore_one_drive_params=None,
                 restore_outlook_params=None,
                 restore_parent_source=None,
                 restore_public_folders_params=None,
                 restore_site_params=None,
                 restore_standby_task_state=None,
                 restore_sub_task_vec=None,
                 restore_task_purged=None,
                 restore_teams_params=None,
                 restore_view_datastore_entity=None,
                 restore_vmware_vm_params=None,
                 restored_data_storage_domain_id=None,
                 restored_objects_network_config=None,
                 restored_to_different_source=None,
                 retrieve_archive_progress_monitor_task_path=None,
                 retrieve_archive_stub_view_name=None,
                 retrieve_archive_task_uid_vec=None,
                 retrieve_archive_task_vec=None,
                 retrieve_archive_view_name=None,
                 selected_datastore_idx=None,
                 sfdc_recover_job_params=None,
                 skip_cloning_retrieve_archive_view=None,
                 skip_image_deploy=None,
                 skip_rigel_for_restore=None,
                 stub_view_relative_dir_name=None,
                 uda_recover_job_params=None,
                 vault_restore_params=None,
                 vcd_config=None,
                 vcd_storage_profile_datastore_moref_vec=None,
                 view_box_id=None,
                 view_name_deprecated=None,
                 view_params=None,
                 vm_restore_reuse_cdp_view=None,
                 volume_info_vec=None,
            ):

        """Constructor for the PerformRestoreTaskStateProto class"""

        # Initialize members of the class
        self.action_executor_target_type = action_executor_target_type
        self.backup_run_lock_vec = backup_run_lock_vec
        self.base = base
        self.can_teardown = can_teardown
        self.cdp_restore_progress_monitor_task_path = cdp_restore_progress_monitor_task_path
        self.cdp_restore_task = cdp_restore_task
        self.cdp_restore_task_id = cdp_restore_task_id
        self.cdp_restore_view_name = cdp_restore_view_name
        self.child_clone_task_id = child_clone_task_id
        self.child_destroy_task_id = child_destroy_task_id
        self.clone_app_view_info = clone_app_view_info
        self.cloud_deploy_info = cloud_deploy_info
        self.continue_restore_on_error = continue_restore_on_error
        self.create_view = create_view
        self.datastore_entity_vec = datastore_entity_vec
        self.deploy_vms_to_cloud_task_state = deploy_vms_to_cloud_task_state
        self.folder_entity = folder_entity
        self.full_view_name = full_view_name
        self.include_vm_config = include_vm_config
        self.is_multi_stage_restore = is_multi_stage_restore
        self.mount_volumes_task_state = mount_volumes_task_state
        self.multi_restore_task_id = multi_restore_task_id
        self.multi_stage_restore_task_state = multi_stage_restore_task_state
        self.nosql_connect_params = nosql_connect_params
        self.nosql_recover_job_params = nosql_recover_job_params
        self.object_name_deprecated = object_name_deprecated
        self.objects = objects
        self.objects_progress_monitor_task_paths = objects_progress_monitor_task_paths
        self.parent_restore_job_id = parent_restore_job_id
        self.parent_restore_task_id = parent_restore_task_id
        self.path_prefix_deprecated = path_prefix_deprecated
        self.physical_flr_parallel_restore = physical_flr_parallel_restore
        self.physical_flr_use_new_locking_method = physical_flr_use_new_locking_method
        self.power_state_config = power_state_config
        self.preserve_tags = preserve_tags
        self.progress_monitor_task_path = progress_monitor_task_path
        self.recover_disks_task_state = recover_disks_task_state
        self.recover_volumes_task_state = recover_volumes_task_state
        self.related_restore_task_id = related_restore_task_id
        self.rename_restored_object_param = rename_restored_object_param
        self.rename_restored_vapp_param = rename_restored_vapp_param
        self.resource_pool_entity = resource_pool_entity
        self.restore_acropolis_vms_params = restore_acropolis_vms_params
        self.restore_app_task_state = restore_app_task_state
        self.restore_files_task_state = restore_files_task_state
        self.restore_groups_params = restore_groups_params
        self.restore_hyperv_vm_params = restore_hyperv_vm_params
        self.restore_info = restore_info
        self.restore_kubernetes_namespaces_params = restore_kubernetes_namespaces_params
        self.restore_kvm_vms_params = restore_kvm_vms_params
        self.restore_one_drive_params = restore_one_drive_params
        self.restore_outlook_params = restore_outlook_params
        self.restore_parent_source = restore_parent_source
        self.restore_public_folders_params = restore_public_folders_params
        self.restore_site_params = restore_site_params
        self.restore_standby_task_state = restore_standby_task_state
        self.restore_sub_task_vec = restore_sub_task_vec
        self.restore_task_purged = restore_task_purged
        self.restore_teams_params = restore_teams_params
        self.restore_view_datastore_entity = restore_view_datastore_entity
        self.restore_vmware_vm_params = restore_vmware_vm_params
        self.restored_data_storage_domain_id = restored_data_storage_domain_id
        self.restored_objects_network_config = restored_objects_network_config
        self.restored_to_different_source = restored_to_different_source
        self.retrieve_archive_progress_monitor_task_path = retrieve_archive_progress_monitor_task_path
        self.retrieve_archive_stub_view_name = retrieve_archive_stub_view_name
        self.retrieve_archive_task_uid_vec = retrieve_archive_task_uid_vec
        self.retrieve_archive_task_vec = retrieve_archive_task_vec
        self.retrieve_archive_view_name = retrieve_archive_view_name
        self.selected_datastore_idx = selected_datastore_idx
        self.sfdc_recover_job_params = sfdc_recover_job_params
        self.skip_cloning_retrieve_archive_view = skip_cloning_retrieve_archive_view
        self.skip_image_deploy = skip_image_deploy
        self.skip_rigel_for_restore = skip_rigel_for_restore
        self.stub_view_relative_dir_name = stub_view_relative_dir_name
        self.uda_recover_job_params = uda_recover_job_params
        self.vault_restore_params = vault_restore_params
        self.vcd_config = vcd_config
        self.vcd_storage_profile_datastore_moref_vec = vcd_storage_profile_datastore_moref_vec
        self.view_box_id = view_box_id
        self.view_name_deprecated = view_name_deprecated
        self.view_params = view_params
        self.vm_restore_reuse_cdp_view = vm_restore_reuse_cdp_view
        self.volume_info_vec = volume_info_vec

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
        backup_run_lock_vec = None
        if dictionary.get('backupRunLockVec') != None:
            backup_run_lock_vec = list()
            for structure in dictionary.get('backupRunLockVec'):
                backup_run_lock_vec.append(cohesity_management_sdk.models.backup_run_id.BackupRunId.from_dictionary(structure))
        base = cohesity_management_sdk.models.restore_task_state_base_proto.RestoreTaskStateBaseProto.from_dictionary(dictionary.get('base')) if dictionary.get('base') else None
        can_teardown = dictionary.get('canTeardown')
        cdp_restore_progress_monitor_task_path = dictionary.get('cdpRestoreProgressMonitorTaskPath')
        cdp_restore_task = cohesity_management_sdk.models.perform_restore_task_state_proto.PerformRestoreTaskStateProto.from_dictionary(dictionary.get('cdpRestoreTask')) if dictionary.get('cdpRestoreTask') else None
        cdp_restore_task_id = dictionary.get('cdpRestoreTaskId')
        cdp_restore_view_name = dictionary.get('cdpRestoreViewName')
        child_clone_task_id = dictionary.get('childCloneTaskId')
        child_destroy_task_id = dictionary.get('childDestroyTaskId')
        clone_app_view_info = cohesity_management_sdk.models.clone_app_view_info_proto.CloneAppViewInfoProto.from_dictionary(dictionary.get('cloneAppViewInfo')) if dictionary.get('cloneAppViewInfo') else None
        cloud_deploy_info = cohesity_management_sdk.models.cloud_deploy_info_proto.CloudDeployInfoProto.from_dictionary(dictionary.get('cloudDeployInfo')) if dictionary.get('cloudDeployInfo') else None
        continue_restore_on_error = dictionary.get('continueRestoreOnError')
        create_view = dictionary.get('createView')
        datastore_entity_vec = None
        if dictionary.get('datastoreEntityVec') != None:
            datastore_entity_vec = list()
            for structure in dictionary.get('datastoreEntityVec'):
                datastore_entity_vec.append(cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(structure))
        deploy_vms_to_cloud_task_state = cohesity_management_sdk.models.deploy_vms_to_cloud_task_state_proto.DeployVMsToCloudTaskStateProto.from_dictionary(dictionary.get('deployVmsToCloudTaskState')) if dictionary.get('deployVmsToCloudTaskState') else None
        folder_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('folderEntity')) if dictionary.get('folderEntity') else None
        full_view_name = dictionary.get('fullViewName')
        include_vm_config = dictionary.get('includeVmConfig')
        is_multi_stage_restore = dictionary.get('isMultiStageRestore')
        mount_volumes_task_state = cohesity_management_sdk.models.mount_volumes_task_state_proto.MountVolumesTaskStateProto.from_dictionary(dictionary.get('mountVolumesTaskState')) if dictionary.get('mountVolumesTaskState') else None
        multi_restore_task_id = dictionary.get('multiRestoreTaskId')
        multi_stage_restore_task_state = cohesity_management_sdk.models.multi_stage_restore_task_state_proto.MultiStageRestoreTaskStateProto.from_dictionary(dictionary.get('multiStageRestoreTaskState')) if dictionary.get('multiStageRestoreTaskState') else None
        nosql_connect_params = cohesity_management_sdk.models.no_sql_connect_params.NoSqlConnectParams.from_dictionary(dictionary.get('nosqlConnectParams')) if dictionary.get('nosqlConnectParams') else None
        nosql_recover_job_params = cohesity_management_sdk.models.no_sql_recover_job_params.NoSqlRecoverJobParams.from_dictionary(dictionary.get('nosqlRecoverJobParams')) if dictionary.get('nosqlRecoverJobParams') else None
        object_name_deprecated = dictionary.get('objectName_DEPRECATED')
        objects = None
        if dictionary.get('objects') != None:
            objects = list()
            for structure in dictionary.get('objects'):
                objects.append(cohesity_management_sdk.models.restore_object.RestoreObject.from_dictionary(structure))
        objects_progress_monitor_task_paths = dictionary.get("objectsProgressMonitorTaskPaths")
        parent_restore_job_id = dictionary.get('parentRestoreJobId')
        parent_restore_task_id = dictionary.get('parentRestoreTaskId')
        path_prefix_deprecated = dictionary.get('pathPrefix_DEPRECATED')
        physical_flr_parallel_restore = dictionary.get('physicalFlrParallelRestore')
        physical_flr_use_new_locking_method = dictionary.get('physicalFlrUseNewLockingMethod')
        power_state_config = cohesity_management_sdk.models.power_state_config_proto.PowerStateConfigProto.from_dictionary(dictionary.get('powerStateConfig')) if dictionary.get('powerStateConfig') else None
        preserve_tags = dictionary.get('preserveTags')
        progress_monitor_task_path = dictionary.get('progressMonitorTaskPath')
        recover_disks_task_state = cohesity_management_sdk.models.recover_disks_task_state_proto.RecoverDisksTaskStateProto.from_dictionary(dictionary.get('recoverDisksTaskState')) if dictionary.get('recoverDisksTaskState') else None
        recover_volumes_task_state = cohesity_management_sdk.models.recover_volumes_task_state_proto.RecoverVolumesTaskStateProto.from_dictionary(dictionary.get('recoverVolumesTaskState')) if dictionary.get('recoverVolumesTaskState') else None
        related_restore_task_id = dictionary.get('relatedRestoreTaskId')
        rename_restored_object_param = cohesity_management_sdk.models.rename_object_param_proto.RenameObjectParamProto.from_dictionary(dictionary.get('renameRestoredObjectParam')) if dictionary.get('renameRestoredObjectParam') else None
        rename_restored_vapp_param = cohesity_management_sdk.models.rename_object_param_proto.RenameObjectParamProto.from_dictionary(dictionary.get('renameRestoredVappParam')) if dictionary.get('renameRestoredVappParam') else None
        resource_pool_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('resourcePoolEntity')) if dictionary.get('resourcePoolEntity') else None
        restore_acropolis_vms_params = cohesity_management_sdk.models.restore_acropolis_vms_params.RestoreAcropolisVMsParams.from_dictionary(dictionary.get('restoreAcropolisVmsParams')) if dictionary.get('restoreAcropolisVmsParams') else None
        restore_app_task_state = cohesity_management_sdk.models.restore_app_task_state_proto.RestoreAppTaskStateProto.from_dictionary(dictionary.get('restoreAppTaskState')) if dictionary.get('restoreAppTaskState') else None
        restore_files_task_state = cohesity_management_sdk.models.restore_files_task_state_proto.RestoreFilesTaskStateProto.from_dictionary(dictionary.get('restoreFilesTaskState')) if dictionary.get('restoreFilesTaskState') else None
        restore_groups_params = cohesity_management_sdk.models.restore_o_365_groups_params.RestoreO365GroupsParams.from_dictionary(dictionary.get('restoreGroupsParams')) if dictionary.get('restoreGroupsParams') else None
        restore_hyperv_vm_params = cohesity_management_sdk.models.restore_hyperv_vm_params.RestoreHyperVVMParams.from_dictionary(dictionary.get('restoreHypervVmParams')) if dictionary.get('restoreHypervVmParams') else None
        restore_info = cohesity_management_sdk.models.restore_info_proto.RestoreInfoProto.from_dictionary(dictionary.get('restoreInfo')) if dictionary.get('restoreInfo') else None
        restore_kubernetes_namespaces_params = cohesity_management_sdk.models.restore_kubernetes_namespaces_params.RestoreKubernetesNamespacesParams.from_dictionary(dictionary.get('restoreKubernetesNamespacesParams')) if dictionary.get('restoreKubernetesNamespacesParams') else None
        restore_kvm_vms_params = cohesity_management_sdk.models.restore_kvm_vms_params.RestoreKVMVMsParams.from_dictionary(dictionary.get('restoreKvmVmsParams')) if dictionary.get('restoreKvmVmsParams') else None
        restore_one_drive_params = cohesity_management_sdk.models.restore_one_drive_params.RestoreOneDriveParams.from_dictionary(dictionary.get('restoreOneDriveParams')) if dictionary.get('restoreOneDriveParams') else None
        restore_outlook_params = cohesity_management_sdk.models.restore_outlook_params.RestoreOutlookParams.from_dictionary(dictionary.get('restoreOutlookParams')) if dictionary.get('restoreOutlookParams') else None
        restore_parent_source = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('restoreParentSource')) if dictionary.get('restoreParentSource') else None
        restore_public_folders_params = cohesity_management_sdk.models.restore_o_365_public_folders_params.RestoreO365PublicFoldersParams.from_dictionary(dictionary.get('restorePublicFoldersParams')) if dictionary.get('restorePublicFoldersParams') else None
        restore_site_params = cohesity_management_sdk.models.restore_site_params.RestoreSiteParams.from_dictionary(dictionary.get('restoreSiteParams')) if dictionary.get('restoreSiteParams') else None
        restore_standby_task_state = cohesity_management_sdk.models.restore_standby_task_state_proto.RestoreStandbyTaskStateProto.from_dictionary(dictionary.get('restoreStandbyTaskState')) if dictionary.get('restoreStandbyTaskState') else None
        restore_sub_task_vec = dictionary.get("restoreSubTaskVec")
        restore_task_purged = dictionary.get('restoreTaskPurged')
        restore_teams_params = cohesity_management_sdk.models.restore_o_365_teams_params.RestoreO365TeamsParams.from_dictionary(dictionary.get('restoreTeamsParams')) if dictionary.get('restoreTeamsParams') else None
        restore_view_datastore_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('restoreViewDatastoreEntity')) if dictionary.get('restoreViewDatastoreEntity') else None
        restore_vmware_vm_params = cohesity_management_sdk.models.restore_vmware_vm_params.RestoreVMwareVMParams.from_dictionary(dictionary.get('restoreVmwareVmParams')) if dictionary.get('restoreVmwareVmParams') else None
        restored_data_storage_domain_id = dictionary.get('restoredDataStorageDomainId')
        restored_objects_network_config = cohesity_management_sdk.models.restored_object_network_config_proto.RestoredObjectNetworkConfigProto.from_dictionary(dictionary.get('restoredObjectsNetworkConfig')) if dictionary.get('restoredObjectsNetworkConfig') else None
        restored_to_different_source = dictionary.get('restoredToDifferentSource')
        retrieve_archive_progress_monitor_task_path = dictionary.get('retrieveArchiveProgressMonitorTaskPath')
        retrieve_archive_stub_view_name = dictionary.get('retrieveArchiveStubViewName')
        retrieve_archive_task_uid_vec = None
        if dictionary.get('retrieveArchiveTaskUidVec') != None:
            retrieve_archive_task_uid_vec = list()
            for structure in dictionary.get('retrieveArchiveTaskUidVec'):
                retrieve_archive_task_uid_vec.append(cohesity_management_sdk.models.universal_id_proto.UniversalIdProto.from_dictionary(structure))
        retrieve_archive_task_vec = None
        if dictionary.get('retrieveArchiveTaskVec') != None:
            retrieve_archive_task_vec = list()
            for structure in dictionary.get('retrieveArchiveTaskVec'):
                retrieve_archive_task_vec.append(cohesity_management_sdk.models.retrieve_archive_task_state_proto.RetrieveArchiveTaskStateProto.from_dictionary(structure))
        retrieve_archive_view_name = dictionary.get('retrieveArchiveViewName')
        selected_datastore_idx = dictionary.get('selectedDatastoreIdx')
        sfdc_recover_job_params = cohesity_management_sdk.models.sfdc_recover_job_params.SfdcRecoverJobParams.from_dictionary(dictionary.get('sfdcRecoverJobParams')) if dictionary.get('sfdcRecoverJobParams') else None
        skip_cloning_retrieve_archive_view = dictionary.get('skipCloningRetrieveArchiveView')
        skip_image_deploy = dictionary.get('skipImageDeploy')
        skip_rigel_for_restore = dictionary.get('skipRigelForRestore')
        stub_view_relative_dir_name = dictionary.get('stubViewRelativeDirName')
        uda_recover_job_params = cohesity_management_sdk.models.uda_recover_job_params.UdaRecoverJobParams.from_dictionary(dictionary.get('udaRecoverJobParams')) if dictionary.get('udaRecoverJobParams') else None
        vault_restore_params = cohesity_management_sdk.models.vault_params_restore_params.VaultParams_RestoreParams.from_dictionary(dictionary.get('vaultRestoreParams')) if dictionary.get('vaultRestoreParams') else None
        vcd_config = cohesity_management_sdk.models.restored_object_vcd_config_proto.RestoredObjectVCDConfigProto.from_dictionary(dictionary.get('vcdConfig')) if dictionary.get('vcdConfig') else None
        vcd_storage_profile_datastore_moref_vec = dictionary.get("vcdStorageProfileDatastoreMorefVec")
        view_box_id = dictionary.get('viewBoxId')
        view_name_deprecated = dictionary.get('viewName_DEPRECATED')
        view_params = cohesity_management_sdk.models.view_params.ViewParams.from_dictionary(dictionary.get('viewParams')) if dictionary.get('viewParams') else None
        vm_restore_reuse_cdp_view = dictionary.get('vmRestoreReuseCdpView')
        volume_info_vec = None
        if dictionary.get('volumeInfoVec') != None:
            volume_info_vec = list()
            for structure in dictionary.get('volumeInfoVec'):
                volume_info_vec.append(cohesity_management_sdk.models.volume_info.VolumeInfo.from_dictionary(structure))

        # Return an object of this model
        return cls(
            action_executor_target_type,
            backup_run_lock_vec,
            base,
            can_teardown,
            cdp_restore_progress_monitor_task_path,
            cdp_restore_task,
            cdp_restore_task_id,
            cdp_restore_view_name,
            child_clone_task_id,
            child_destroy_task_id,
            clone_app_view_info,
            cloud_deploy_info,
            continue_restore_on_error,
            create_view,
            datastore_entity_vec,
            deploy_vms_to_cloud_task_state,
            folder_entity,
            full_view_name,
            include_vm_config,
            is_multi_stage_restore,
            mount_volumes_task_state,
            multi_restore_task_id,
            multi_stage_restore_task_state,
            nosql_connect_params,
            nosql_recover_job_params,
            object_name_deprecated,
            objects,
            objects_progress_monitor_task_paths,
            parent_restore_job_id,
            parent_restore_task_id,
            path_prefix_deprecated,
            physical_flr_parallel_restore,
            physical_flr_use_new_locking_method,
            power_state_config,
            preserve_tags,
            progress_monitor_task_path,
            recover_disks_task_state,
            recover_volumes_task_state,
            related_restore_task_id,
            rename_restored_object_param,
            rename_restored_vapp_param,
            resource_pool_entity,
            restore_acropolis_vms_params,
            restore_app_task_state,
            restore_files_task_state,
            restore_groups_params,
            restore_hyperv_vm_params,
            restore_info,
            restore_kubernetes_namespaces_params,
            restore_kvm_vms_params,
            restore_one_drive_params,
            restore_outlook_params,
            restore_parent_source,
            restore_public_folders_params,
            restore_site_params,
            restore_standby_task_state,
            restore_sub_task_vec,
            restore_task_purged,
            restore_teams_params,
            restore_view_datastore_entity,
            restore_vmware_vm_params,
            restored_data_storage_domain_id,
            restored_objects_network_config,
            restored_to_different_source,
            retrieve_archive_progress_monitor_task_path,
            retrieve_archive_stub_view_name,
            retrieve_archive_task_uid_vec,
            retrieve_archive_task_vec,
            retrieve_archive_view_name,
            selected_datastore_idx,
            sfdc_recover_job_params,
            skip_cloning_retrieve_archive_view,
            skip_image_deploy,
            skip_rigel_for_restore,
            stub_view_relative_dir_name,
            uda_recover_job_params,
            vault_restore_params,
            vcd_config,
            vcd_storage_profile_datastore_moref_vec,
            view_box_id,
            view_name_deprecated,
            view_params,
            vm_restore_reuse_cdp_view,
            volume_info_vec
)