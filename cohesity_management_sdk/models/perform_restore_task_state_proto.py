# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.restore_task_state_base_proto
import cohesity_management_sdk.models.perform_restore_task_state_proto
import cohesity_management_sdk.models.clone_app_view_info_proto
import cohesity_management_sdk.models.cloud_deploy_info_proto
import cohesity_management_sdk.models.entity_proto
import cohesity_management_sdk.models.deploy_v_ms_to_cloud_task_state_proto
import cohesity_management_sdk.models.mount_volumes_task_state_proto
import cohesity_management_sdk.models.no_sql_connect_params
import cohesity_management_sdk.models.no_sql_recover_job_params
import cohesity_management_sdk.models.restore_object
import cohesity_management_sdk.models.restore_site_params
import cohesity_management_sdk.models.power_state_config_proto
import cohesity_management_sdk.models.recover_disks_task_state_proto
import cohesity_management_sdk.models.recover_volumes_task_state_proto
import cohesity_management_sdk.models.rename_object_param_proto
import cohesity_management_sdk.models.restore_acropolis_v_ms_params
import cohesity_management_sdk.models.restore_app_task_state_proto
import cohesity_management_sdk.models.restore_files_task_state_proto
import cohesity_management_sdk.models.restore_hyperv_vm_params
import cohesity_management_sdk.models.restore_info_proto
import cohesity_management_sdk.models.restore_kubernetes_namespaces_params
import cohesity_management_sdk.models.restore_kvmv_ms_params
import cohesity_management_sdk.models.restore_one_drive_params
import cohesity_management_sdk.models.restore_outlook_params
import cohesity_management_sdk.models.restore_vmware_vm_params
import cohesity_management_sdk.models.restored_object_network_config_proto
import cohesity_management_sdk.models.universal_id_proto
import cohesity_management_sdk.models.retrieve_archive_task_state_proto
import cohesity_management_sdk.models.vault_params_restore_params
import cohesity_management_sdk.models.restored_object_vcd_config_proto
import cohesity_management_sdk.models.view_params
import cohesity_management_sdk.models.volume_info

class PerformRestoreTaskStateProto(object):

    """Implementation of the 'PerformRestoreTaskStateProto' model.

    TODO: type model description here.

    Attributes:
        action_executor_target_type (int): Denotes the target for action
            executor(Bridge / BridgeProxy) on which task on slave should
            execute actions.
        base (RestoreTaskStateBaseProto): TODO: type description here.
        can_teardown (bool): This is set if the clone operation has created
            any objects on the primary environment and teardown operation is
            possible. UI will disable the teardown button only if this is not
            set or set to false. NOTE: This won't be reset if the teardown
            operation subsequently completes as teardown state is managed
            separately.
        cdp_restore_progress_monitor_task_path (string): The path of the
            progress monitor for the task that is responsible for creating the
            CDP hydrated view.
        cdp_restore_task (PerformRestoreTaskStateProto): TODO: type
            description here.
        cdp_restore_task_id (long|int): The id of the task that will create
            the CDP hydrated view.
        cdp_restore_view_name (string): The temporary view where the hydrated
            disks of the CDP restores are kept.
        child_clone_task_id (long|int): The id of the child clone task
            triggered by refresh op.
        child_destroy_task_id (long|int): The following fields are used by
            clone refresh op. These will be present only in case of refresh
            task op.  The id of the child destroy clone task triggered by
            refresh op.
        clone_app_view_info (CloneAppViewInfoProto): This message encapsulates
            the information of Clone operation of backup view of an App.
        cloud_deploy_info (CloudDeployInfoProto): Each available extension is
            listed below along with the location of the proto file (relative
            to magneto/connectors) where it is defined. The extension applies
            to both CloudDeployInfoProto as well as CloudDeployEntity.
            CloudDeployInfoProto extension                  Location
            Extension
            ===================================================================
            ========== aws::CloudDeployInfo::aws_cloud_deploy_info
            aws/aws.proto            100
            azure::CloudDeployInfo::azure_cloud_deploy_info azure/azure.proto
            101 gcp::CloudDeployInfo::gcp_cloud_deploy_info     gcp/gcp.proto
            102 aws::ReplicationInfo::aws_replication_info      aws/aws.proto
            103 azure::ReplicationInfo::azure_replication_info
            azure/azure.proto        104
            ===================================================================
            ==========  CloudDeployInfoProto.CloudDeployEntity extension
            Location         Extension
            ===================================================================
            ==========
            aws::CloudDeployEntityInfo::aws_cloud_deploy_entity_info
            aws/aws.proto          100
            vmware::RestoreEntityInfo::vmware_cloud_deploy_entity_info
            vmware/vmware.proto    101
            azure::CloudDeployEntityInfo::azure_cloud_deploy_entity_info
            azure/azure.proto      102
            gcp::CloudDeployEntityInfo::gcp_cloud_deploy_entity_info
            gcp/gcp.proto          103
            hyperv::RestoreEntityInfo::hyperv_cloud_deploy_entity_info
            hyperv/hyperv.proto    104
            aws::ReplicationEntityInfo::aws_replication_entity_info
            aws/aws.proto          105
            aws::ReplicationEntityInfo::azure_replication_entity_info
            azure/azure.proto      106
            ===================================================================
            ==========
        continue_restore_on_error (bool): Whether to continue with the restore
            operation if restore of any object fails.
        create_view (bool): True iff the target view needs to be created.
        datastore_entity_vec (list of EntityProto): Please refer to comments
            for the field CreateRestoreTaskArg.datastore_entity_vec for more
            details.
        deploy_vms_to_cloud_task_state (DeployVMsToCloudTaskStateProto): TODO:
            type description here.
        folder_entity (EntityProto): Specifies the attributes and the latest
            statistics about an entity.
        full_view_name (string): The full view name (internal or external).
            This is composed of an optional Cohesity specific prefix and the
            user provided view name.
        include_vm_config (bool): This is set to true if the vm-config.xml
            need to be copied in the target view/folder.
        mount_volumes_task_state (MountVolumesTaskStateProto): TODO: type
            description here.
        nosql_connect_params (NoSqlConnectParams): Parameters to connect to
            destination nosql parent entity.
        nosql_recover_job_params (NoSqlRecoverJobParams): Additional
            parameters for the recovery job to send to imanis server.
        object_name_deprecated (string): An optional name to give to the
            restored object.
        objects (list of RestoreObject): Information on the exact set of
            objects being restored (along with snapshots they are being
            recovered from). Even if the user wanted to restore an entire job
            from the latest snapshot, this will have individual objects and
            the exact snapshot they are being restored from. If specified,
            this can only have leaf-level entities.
        objects_progress_monitor_task_paths (list of string): Vector
            containing the relative task path of progress monitors of the
            objects in the above field 'objects' to be restored. There is one
            to one correspondence between elements in 'objects' and
            'objects_progress_monitor_task_paths'.  Please note that this
            field will be set only after progress monitor is created for this
            restore task.
        parent_restore_job_id (long|int): If this a child restore task, this
            field will contain the id of the parent restore job that spawned
            this task.  List of env and action type for which this field is
            applicable are: Acropolis: kRecoverVMs.
        parent_restore_task_id (long|int): The id of the parent restore task
            if this is a restore sub-task.  List of environments that use this
            field: kSQL : Used for multi-stage SQL restore that supports a
            hot-standy.  This will also be used by refresh op to mark the new
            clone as internal sub-task.
        path_prefix_deprecated (string): TODO: type description here.
        physical_flr_parallel_restore (bool): If enabled, magneto physical
            file restore will be enabled via job framework
        physical_flr_use_new_locking_method (bool): If enabled, magneto
            physical file restore will be enabled via job framework
        power_state_config (PowerStateConfigProto): TODO: type description
            here.
        preserve_tags (bool): This field is currently used by HyperV and
            VMWare.
        progress_monitor_task_path (string): Root path of a Pulse task
            tracking the progress of the restore task.
        recover_disks_task_state (RecoverDisksTaskStateProto): TODO: type
            description here.
        recover_volumes_task_state (RecoverVolumesTaskStateProto): TODO: type
            description here.
        related_restore_task_id (long|int): The task id of a related restore
            task. For example, a SQL restore operation may involve restoring a
            VM first and then restoring SQL databases after that. So the
            corresponding VM restore and SQL database restore tasks will be
            related, and they will each have their 'related_restore_task_id'
            set to the id of the other task.
        rename_restored_object_param (RenameObjectParamProto): Message to
            specify the prefix/suffix added to rename an object. At least one
            of prefix or suffix must be specified. Please note that both
            prefix and suffix can be specified.
        rename_restored_vapp_param (RenameObjectParamProto): Message to
            specify the prefix/suffix added to rename an object. At least one
            of prefix or suffix must be specified. Please note that both
            prefix and suffix can be specified.
        resource_pool_entity (EntityProto): Specifies the attributes and the
            latest statistics about an entity.
        restore_acropolis_vms_params (RestoreAcropolisVMsParams): TODO: type
            description here.
        restore_app_task_state (RestoreAppTaskStateProto): TODO: type
            description here.
        restore_files_task_state (RestoreFilesTaskStateProto): TODO: type
            description here.
        restore_hyperv_vm_params (RestoreHypervVMParams): TODO: type
            description here.
        restore_info (RestoreInfoProto): Each available extension is listed
            below along with the location of the proto file (relative to
            magneto/connectors) where it is defined. The extension applies to
            both RestoreInfoProto as well as RestoreEntity.  RestoreInfoProto
            extension                     Location            Extension
            ===================================================================
            ========== vmware::RestoreInfo::vmware_restore_info
            vmware/vmware.proto       100 sql::RestoreInfo::sql_restore_info
            sql/sql.proto             101 pure::RestoreInfo::pure_restore_info
            pure/pure.proto           102
            azure::RestoreInfo::azure_restore_info       azure/azure.proto
            103 file::RestoreInfo::file_restore_info         file/file.proto
            104 hyperv::RestoreInfo::hyperv_restore_info
            hyperv/hyperv.proto       105
            acropolis::RestoreInfo::acropolis_restore_info
            acropolis/acropolis.proto 106 kvm::RestoreInfo::kvm_restore_info
            kvm/kvm.proto             107 aws::RestoreInfo::aws_restore_info
            aws/aws.proto             108
            physical::RestoreInfo::physical_restore_info physical.proto
            109 oracle::RestoreInfo::oracle_restore_info
            oracle/oracle.proto       110
            outlook::RestoreInfo::outlook_restore_info   outlook/outlook.proto
            111 gcp::RestoreInfo::gcp_restore_info           gcp/gcp.proto
            112 ad::RestoreInfo::ad_restore_info             ad/ad.proto
            113 kubernetes::RestoreInfo::kubernetes_restore_info
            kubernetes/kubernetes.proto 114
            one_drive::RestoreInfo::one_drive_restore_info
            ms_graph/graph.proto      115
            ===================================================================
            ==========  RestoreInfoProto.RestoreEntity extension
            Location            Extension
            ===================================================================
            ========== vmware::RestoreEntityInfo::vmware_restore_entity_info
            vmware/vmware.proto        100
            azure::RestoreEntityInfo::azure_restore_entity_info
            azure/azure.proto          101
            hyperv::RestoreEntityInfo::hyperv_restore_entity_info
            hyperv/hyperv.proto        102
            acropolis::RestoreEntityInfo::acropolis_restore_entity_info
            acropolis/acropolis.proto  103
            kvm::RestoreEntityInfo::kvm_restore_entity_info kvm/kvm.proto
            104 aws::RestoreEntityInfo::aws_restore_entity_info aws/aws.proto
            105 outlook::RestoreEntityInfo::outlook_restore_entity_info
            outlook/outlook.proto      106
            gcp::RestoreEntityInfo::gcp_restore_entity_info gcp/gcp.proto
            107 kubernetes::RestoreEntityInfo::kubernetes_restore_entity_info
            kuebrnetes/kubernetes.proto 108
            one_drive::RestoreEntityInfo::one_drive_restore_entity_info
            ms_graph/graph.proto       109
            ===================================================================
            ==========
        restore_kubernetes_namespaces_params
            (RestoreKubernetesNamespacesParams): TODO: type description here.
        restore_kvm_vms_params (RestoreKVMVMsParams): TODO: type description
            here.
        restore_one_drive_params (RestoreOneDriveParams): TODO: type
            description here.
        restore_outlook_params (RestoreOutlookParams): TODO: type description
            here.
        restore_parent_source (EntityProto): Specifies the attributes and the
            latest statistics about an entity.
        restore_site_params (RestoreSiteParams): This field defines the O365
            site specific params for restore task of type kRecoverSites.
        restore_sub_task_vec (list of long|int): Inside Magneto, these are
            represented as regular restore tasks with their own
            PerformRestoreTaskStateProto. Each restore sub-task will have its
            parent_restore_task_id field set.  List of environments that use
            this field: kSQL : Used for multi-stage SQL restore that supports
            a hot-standy.
        restore_task_purged (bool): Whether the restore task is purged. During
            WAL recovery, purged restore tasks are ignored.
        restore_view_datastore_entity (EntityProto): Specifies the attributes
            and the latest statistics about an entity.
        restore_vmware_vm_params (RestoreVmwareVMParams): TODO: type
            description here.
        restored_objects_network_config (RestoredObjectNetworkConfigProto):
            TODO: type description here.
        restored_to_different_source (bool): Whether restore is being
            performed to a different parent source.
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
            retrieve multiple snapshots typically one full, and few logs. As
            we may start the multiple retrieval tasks, we need vector of
            RetrieveArchiveTaskStateProto for storing information of retrieved
            archive tasks.
        retrieve_archive_view_name (string): The temporary view where the
            entities that have been retrieved from an archive have been placed
            in by Icebox.
        selected_datastore_idx (long|int): In case of restore job with
            multi-vm multi-datastore this field denotes the specific datastore
            index in datastore_entity_vec to be selected for the task. Not
            going for specific datastore allocation in datastore_entity_vec so
            that we have required information in case of extensibility for
            task level retries with different datastore
        stub_view_relative_dir_name (string): Relative directory inside the
            stub view that corresponds with the archive.
        vault_restore_params (VaultParamsRestoreParams): TODO: type
            description here.
        vcd_config (RestoredObjectVCDConfigProto): TODO: type description
            here.
        vcd_storage_profile_datastore_moref_vec (list of string): This field
            is applicable for VCD type recovery. It defines the compatible
            datastores for recovery to alternate location. This field is
            inferred using the storage profile in restore_vmware_vm_params
            below.
        view_box_id (long|int): The view box id to which 'view_name' belongs
            to. In case the restore task corresponds to a backup job, this
            view box corresponds to the view box of the backup job.
        view_name_deprecated (string): The view name as provided by the user
            for this restore operation.
        view_params (ViewParams): TODO: type description here.
        volume_info_vec (list of VolumeInfo): Information regarding volumes
            that are required for the restore task. This is populated for
            restore files and mount virtual disk ops.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "action_executor_target_type":'actionExecutorTargetType',
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
        "mount_volumes_task_state":'mountVolumesTaskState',
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
        "restore_hyperv_vm_params":'restoreHypervVmParams',
        "restore_info":'restoreInfo',
        "restore_kubernetes_namespaces_params":'restoreKubernetesNamespacesParams',
        "restore_kvm_vms_params":'restoreKvmVmsParams',
        "restore_one_drive_params":'restoreOneDriveParams',
        "restore_outlook_params":'restoreOutlookParams',
        "restore_parent_source":'restoreParentSource',
        "restore_site_params":'restoreSiteParams',
        "restore_sub_task_vec":'restoreSubTaskVec',
        "restore_task_purged":'restoreTaskPurged',
        "restore_view_datastore_entity":'restoreViewDatastoreEntity',
        "restore_vmware_vm_params":'restoreVmwareVmParams',
        "restored_objects_network_config":'restoredObjectsNetworkConfig',
        "restored_to_different_source":'restoredToDifferentSource',
        "retrieve_archive_progress_monitor_task_path":'retrieveArchiveProgressMonitorTaskPath',
        "retrieve_archive_stub_view_name":'retrieveArchiveStubViewName',
        "retrieve_archive_task_uid_vec":'retrieveArchiveTaskUidVec',
        "retrieve_archive_task_vec":'retrieveArchiveTaskVec',
        "retrieve_archive_view_name":'retrieveArchiveViewName',
        "selected_datastore_idx":'selectedDatastoreIdx',
        "stub_view_relative_dir_name":'stubViewRelativeDirName',
        "vault_restore_params":'vaultRestoreParams',
        "vcd_config":'vcdConfig',
        "vcd_storage_profile_datastore_moref_vec":'vcdStorageProfileDatastoreMorefVec',
        "view_box_id":'viewBoxId',
        "view_name_deprecated":'viewName_DEPRECATED',
        "view_params":'viewParams',
        "volume_info_vec":'volumeInfoVec'
    }

    def __init__(self,
                 action_executor_target_type=None,
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
                 mount_volumes_task_state=None,
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
                 restore_hyperv_vm_params=None,
                 restore_info=None,
                 restore_kubernetes_namespaces_params=None,
                 restore_kvm_vms_params=None,
                 restore_one_drive_params=None,
                 restore_outlook_params=None,
                 restore_parent_source=None,
                 restore_site_params=None,
                 restore_sub_task_vec=None,
                 restore_task_purged=None,
                 restore_view_datastore_entity=None,
                 restore_vmware_vm_params=None,
                 restored_objects_network_config=None,
                 restored_to_different_source=None,
                 retrieve_archive_progress_monitor_task_path=None,
                 retrieve_archive_stub_view_name=None,
                 retrieve_archive_task_uid_vec=None,
                 retrieve_archive_task_vec=None,
                 retrieve_archive_view_name=None,
                 selected_datastore_idx=None,
                 stub_view_relative_dir_name=None,
                 vault_restore_params=None,
                 vcd_config=None,
                 vcd_storage_profile_datastore_moref_vec=None,
                 view_box_id=None,
                 view_name_deprecated=None,
                 view_params=None,
                 volume_info_vec=None):
        """Constructor for the PerformRestoreTaskStateProto class"""

        # Initialize members of the class
        self.action_executor_target_type = action_executor_target_type
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
        self.mount_volumes_task_state = mount_volumes_task_state
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
        self.restore_hyperv_vm_params = restore_hyperv_vm_params
        self.restore_info = restore_info
        self.restore_kubernetes_namespaces_params = restore_kubernetes_namespaces_params
        self.restore_kvm_vms_params = restore_kvm_vms_params
        self.restore_one_drive_params = restore_one_drive_params
        self.restore_outlook_params = restore_outlook_params
        self.restore_parent_source = restore_parent_source
        self.restore_site_params = restore_site_params
        self.restore_sub_task_vec = restore_sub_task_vec
        self.restore_task_purged = restore_task_purged
        self.restore_view_datastore_entity = restore_view_datastore_entity
        self.restore_vmware_vm_params = restore_vmware_vm_params
        self.restored_objects_network_config = restored_objects_network_config
        self.restored_to_different_source = restored_to_different_source
        self.retrieve_archive_progress_monitor_task_path = retrieve_archive_progress_monitor_task_path
        self.retrieve_archive_stub_view_name = retrieve_archive_stub_view_name
        self.retrieve_archive_task_uid_vec = retrieve_archive_task_uid_vec
        self.retrieve_archive_task_vec = retrieve_archive_task_vec
        self.retrieve_archive_view_name = retrieve_archive_view_name
        self.selected_datastore_idx = selected_datastore_idx
        self.stub_view_relative_dir_name = stub_view_relative_dir_name
        self.vault_restore_params = vault_restore_params
        self.vcd_config = vcd_config
        self.vcd_storage_profile_datastore_moref_vec = vcd_storage_profile_datastore_moref_vec
        self.view_box_id = view_box_id
        self.view_name_deprecated = view_name_deprecated
        self.view_params = view_params
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
        deploy_vms_to_cloud_task_state = cohesity_management_sdk.models.deploy_v_ms_to_cloud_task_state_proto.DeployVMsToCloudTaskStateProto.from_dictionary(dictionary.get('deployVmsToCloudTaskState')) if dictionary.get('deployVmsToCloudTaskState') else None
        folder_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('folderEntity')) if dictionary.get('folderEntity') else None
        full_view_name = dictionary.get('fullViewName')
        include_vm_config = dictionary.get('includeVmConfig')
        mount_volumes_task_state = cohesity_management_sdk.models.mount_volumes_task_state_proto.MountVolumesTaskStateProto.from_dictionary(dictionary.get('mountVolumesTaskState')) if dictionary.get('mountVolumesTaskState') else None
        nosql_connect_params = cohesity_management_sdk.models.no_sql_connect_params.NoSqlConnectParams.from_dictionary(dictionary.get('nosqlConnectParams')) if dictionary.get('nosqlConnectParams') else None
        nosql_recover_job_params = cohesity_management_sdk.models.no_sql_recover_job_params.NoSqlRecoverJobParams.from_dictionary(dictionary.get('nosqlRecoverJobParams')) if dictionary.get('nosqlRecoverJobParams') else None
        object_name_deprecated = dictionary.get('objectName_DEPRECATED')
        objects = None
        if dictionary.get('objects') != None:
            objects = list()
            for structure in dictionary.get('objects'):
                objects.append(cohesity_management_sdk.models.restore_object.RestoreObject.from_dictionary(structure))
        objects_progress_monitor_task_paths = dictionary.get('objectsProgressMonitorTaskPaths')
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
        restore_acropolis_vms_params = cohesity_management_sdk.models.restore_acropolis_v_ms_params.RestoreAcropolisVMsParams.from_dictionary(dictionary.get('restoreAcropolisVmsParams')) if dictionary.get('restoreAcropolisVmsParams') else None
        restore_app_task_state = cohesity_management_sdk.models.restore_app_task_state_proto.RestoreAppTaskStateProto.from_dictionary(dictionary.get('restoreAppTaskState')) if dictionary.get('restoreAppTaskState') else None
        restore_files_task_state = cohesity_management_sdk.models.restore_files_task_state_proto.RestoreFilesTaskStateProto.from_dictionary(dictionary.get('restoreFilesTaskState')) if dictionary.get('restoreFilesTaskState') else None
        restore_hyperv_vm_params = cohesity_management_sdk.models.restore_hyperv_vm_params.RestoreHypervVMParams.from_dictionary(dictionary.get('restoreHypervVmParams')) if dictionary.get('restoreHypervVmParams') else None
        restore_info = cohesity_management_sdk.models.restore_info_proto.RestoreInfoProto.from_dictionary(dictionary.get('restoreInfo')) if dictionary.get('restoreInfo') else None
        restore_kubernetes_namespaces_params = cohesity_management_sdk.models.restore_kubernetes_namespaces_params.RestoreKubernetesNamespacesParams.from_dictionary(dictionary.get('restoreKubernetesNamespacesParams')) if dictionary.get('restoreKubernetesNamespacesParams') else None
        restore_kvm_vms_params = cohesity_management_sdk.models.restore_kvmv_ms_params.RestoreKVMVMsParams.from_dictionary(dictionary.get('restoreKvmVmsParams')) if dictionary.get('restoreKvmVmsParams') else None
        restore_one_drive_params = cohesity_management_sdk.models.restore_one_drive_params.RestoreOneDriveParams.from_dictionary(dictionary.get('restoreOneDriveParams')) if dictionary.get('restoreOneDriveParams') else None
        restore_outlook_params = cohesity_management_sdk.models.restore_outlook_params.RestoreOutlookParams.from_dictionary(dictionary.get('restoreOutlookParams')) if dictionary.get('restoreOutlookParams') else None
        restore_parent_source = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('restoreParentSource')) if dictionary.get('restoreParentSource') else None
        restore_site_params = cohesity_management_sdk.models.restore_site_params.RestoreSiteParams.from_dictionary(dictionary.get('restoreSiteParams')) if dictionary.get('restoreSiteParams') else None
        restore_sub_task_vec = dictionary.get('restoreSubTaskVec')
        restore_task_purged = dictionary.get('restoreTaskPurged')
        restore_view_datastore_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('restoreViewDatastoreEntity')) if dictionary.get('restoreViewDatastoreEntity') else None
        restore_vmware_vm_params = cohesity_management_sdk.models.restore_vmware_vm_params.RestoreVmwareVMParams.from_dictionary(dictionary.get('restoreVmwareVmParams')) if dictionary.get('restoreVmwareVmParams') else None
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
        stub_view_relative_dir_name = dictionary.get('stubViewRelativeDirName')
        vault_restore_params = cohesity_management_sdk.models.vault_params_restore_params.VaultParamsRestoreParams.from_dictionary(dictionary.get('vaultRestoreParams')) if dictionary.get('vaultRestoreParams') else None
        vcd_config = cohesity_management_sdk.models.restored_object_vcd_config_proto.RestoredObjectVCDConfigProto.from_dictionary(dictionary.get('vcdConfig')) if dictionary.get('vcdConfig') else None
        vcd_storage_profile_datastore_moref_vec = dictionary.get('vcdStorageProfileDatastoreMorefVec')
        view_box_id = dictionary.get('viewBoxId')
        view_name_deprecated = dictionary.get('viewName_DEPRECATED')
        view_params = cohesity_management_sdk.models.view_params.ViewParams.from_dictionary(dictionary.get('viewParams')) if dictionary.get('viewParams') else None
        volume_info_vec = None
        if dictionary.get('volumeInfoVec') != None:
            volume_info_vec = list()
            for structure in dictionary.get('volumeInfoVec'):
                volume_info_vec.append(cohesity_management_sdk.models.volume_info.VolumeInfo.from_dictionary(structure))

        # Return an object of this model
        return cls(action_executor_target_type,
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
                   mount_volumes_task_state,
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
                   restore_hyperv_vm_params,
                   restore_info,
                   restore_kubernetes_namespaces_params,
                   restore_kvm_vms_params,
                   restore_one_drive_params,
                   restore_outlook_params,
                   restore_parent_source,
                   restore_site_params,
                   restore_sub_task_vec,
                   restore_task_purged,
                   restore_view_datastore_entity,
                   restore_vmware_vm_params,
                   restored_objects_network_config,
                   restored_to_different_source,
                   retrieve_archive_progress_monitor_task_path,
                   retrieve_archive_stub_view_name,
                   retrieve_archive_task_uid_vec,
                   retrieve_archive_task_vec,
                   retrieve_archive_view_name,
                   selected_datastore_idx,
                   stub_view_relative_dir_name,
                   vault_restore_params,
                   vcd_config,
                   vcd_storage_profile_datastore_moref_vec,
                   view_box_id,
                   view_name_deprecated,
                   view_params,
                   volume_info_vec)


