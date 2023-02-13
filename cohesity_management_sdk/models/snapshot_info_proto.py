# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.script_execution_status
import cohesity_management_sdk.models.object_snapshot_type
import cohesity_management_sdk.models.storage_snapshot_provider_params
import cohesity_management_sdk.models.error_proto
import cohesity_management_sdk.models.size_info

class SnapshotInfoProto(object):

    """Implementation of the 'SnapshotInfoProto' model.

    Each available extension is listed below along with the location of the
    proto file (relative to magneto/connectors) where it is defined. The only
    exception is view.proto and physical.proto which reside in magneto/base.
    SnapshotInfoProto extension                     Location
    Extn
    ===========================================================================
    ==
    vmware::SnapshotInfo::vmware_snapshot_info     vmware/vmware.proto
    100
    sql::SnapshotInfo::sql_snapshot_info           sql/sql.proto
    101
    view::SnapshotInfo::view_snapshot_info         base/view.proto
    102
    physical::SnapshotInfo::physical_snapshot_info base/physical.proto
    103
    san::SnapshotInfo::san_snapshot_info           san/san.proto
    104
    file::SnapshotInfo::file_snapshot_info         file/file.proto
    105
    hyperv::SnapshotInfo::hyperv_snapshot_info     hyperv/hyperv.proto
    106
    acropolis::SnapshotInfo::
    acropolis_snapshot_info                        acropolis/acropolis.proto
    107
    kvm::SnapshotInfo::kvm_snapshot_info           kvm/kvm.proto
    108
    app_file::SnapshotInfo::app_file_snapshot_info app_file/app_file.proto
    109
    oracle::SnapshotInfo::oracle_snapshot_info     oracle/oracle.proto
    110
    aws::SnapshotInfo::aws_snapshot_info           aws/aws.proto
    111
    outlook::SnapshotInfo::outlook_snapshot_info   outlook/outlook.proto
    112
    azure::SnapshotInfo::azure_snapshot_info       azure/azure.proto
    113
    gcp::SnapshotInfo::gcp_snapshot_info           gcp/gcp.proto
    114
    ad::SnapshotInfo::ad_snapshot_info             ad/ad.proto
    115
    MSGraph::SnapshotInfo::one_drive_snapshot_info ms_graph/graph.proto
    116
    kubernetes::SnapshotInfo:: kubernetes_snapshot_info
    kubernetes/kubernetes.proto
    117
    aws::RDSSnapshotInfo::rds_snapshot_info        aws/aws.proto
    118
    o365::SnapshotInfo::o365_snapshot_info         o365/o365.proto
    119
    exchange::SnapshotInfo::exchange_snapshot_info exchange/exchange.proto
    120
    o365::SharepointSnapshotInfo::sharepoint_snapshot_info
    o365/o365.proto           121
    MSGraph::SharepointListSnapshotInfo::sharepoint_list_snapshot_info
    ms_graph/graph.proto      122
    cdp::SnapshotInfo::cdp_snapshot_info           base/cdp.proto
    123
    imanis::SnapshotInfo::nosql_snapshot_info      imanis/nosql.proto
    124
    o365::PublicFolderSnapshotInfo::public_folder_snapshot_info
    o365/o365.proto           125
    SnapshotInfo::uda_snapshot_info                uda.proto                 126
    o365::TeamsSnapshotInfo::teams_snapshot_info   o365/o365.proto           127
    o365::O365GroupSnapshotInfo::o365_group_snapshot_info
    o365/o365.proto           128
    ===========================================================================
    ==

    Attributes:
        change_rocksdb_name (string): The name of the rocksdb directory for
            writing high change directories.
            It is stored in 'config' directory of the current view.
        error_rocksdb_name (string): The name of the rocksdb directory for
            errors seen during this backup, stored in 'config' directory of
            the current view.
        file_walk_done (bool): This field is only applicable for NAS and file
            backup jobs. It indicates whether the file walk portion of the
            backup has completed.
        front_end_size_info (SizeInfo): Front end size information. An example
            use case is for billing purposes in "[Backup | Data Management] as
            a Service" offering.
        metadata_view_name (string): The metadata view name in which the backup
            metadata was created.
            NOTE: This is populated only for CADv2 NAS backup.
        num_app_instances (int): Number of application instances backed up by
            this task. For example, if the environment type is kSQL, this
            number is for the SQL server instances.
        num_app_objects (int): Number of application objects in total backed
            up by this task. For example, if the environment type is kSQL,
            this number is for all of the SQL server databases
        post_backup_script_status (ScriptExecutionStatus): Captures the
            execution status of post backup script.
        pre_backup_script_status (ScriptExecutionStatus): Captures the
            execution status of pre backup script.
        relative_snapshot_dir (string): This is the path relative to
            'root_path' under which the snapshot lives. This does not begin
            with a '/' and is of the form foo/bar/baz.
        root_path (string): The root path under which the snapshot is stored.
            This is of the form "/ViewBox/ViewName/fs".
        scribe_table_column (string): If this backup task stores any auxiliary
            state in Scribe table, this field will be populated with the
            column key in that table where such state is stored. Data stored
            in the column is extension of SnapshotScribeInfoProto message.
        scribe_table_row (string): If this backup task stores any auxiliary
            state in Scribe table, this field will be populated with the row
            key in that table where such state is stored.
        slave_task_start_time_usecs (long|int): This is the timestamp at which
            the slave task started.
        snapshot_expiry_time (long|int): Snapshot expirty time
        snapshot_type (ObjectSnapshotType): Captures the snapshot type for
            some objects such as VM.
        source_snapshot_create_time_usecs (long|int): The source snapshot
            create time.
        source_snapshot_name (string): This filed is only applicable for NAS
            when we do backup from Readonly/DataProtect volume where we use
            already created snapshot on the source.
        source_snapshot_status (int): Indicates the state of the source
            snapshot if it is being managed by the master op.
            'source_snapshot_name' will be set to indicate the snapshot name.
            At the moment, this feature is enabled only for Netapp & Isilon
            adapters to support continuous snapshotting feature.
        storage_snapshot_provider (StorageSnapshotProviderParams): Specifies
            the parameters required for Storage Snapshot provider.
        target_type (int): Specifies the target type for the task. The field
            is only valid if the task has got a permit.
        total_bytes_read_from_source (long|int): Contains the information
            regarding number of bytes that are read from the source (such as
            VM) so far.
        total_bytes_tiered (long|int): Total amount of data successfully
            tiered from the NAS source.
        total_bytes_to_read_from_source (long|int): Contains the total number
            of bytes that will be read from the source (such as VM) for this
            snapshot.
        total_changed_entity_count (long|int): The total number of file and
            directory entities that have changed since last backup. Only
            applicable to file based backups.
        total_entity_count (long|int): The total number of file and directory
            entities visited in this backup. Only applicable to file based
            backups.
        total_logical_backup_size_bytes (long|int): Logical size of the source
            whose snapshot is being taken. This is the amount of data we would
            have read from the source had this been a full backup.
        total_primary_physical_size_bytes (long|int): Contains the information
            regarding number of bytes that the source (such as VM) has taken
            up on the primary storage.
        mtype (int): The type of environment this snapshot info pertains to.
        view_case_insensitivity_altered (bool): Whether during the backup, the
            backup view's case insensitivity property has been altered. If so,
            Madrox needs to take corresponding actions during replication.
        view_name (string): The data view name under which the snapshot was
            created. NOTE: This is populated only for View, Puppeteer, NAS and
            Oracle backup.
        view_name_to_gc (string): The view name under which the snapshot of
            the migrated data was created. NOTE: This is populated only for
            data migration tasks.
        warnings (list of ErrorProto): Warnings if any. These warnings will be
            propogated to the UI by master.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "change_rocksdb_name":'changeRocksdbName',
        "error_rocksdb_name":'errorRocksdbName',
        "file_walk_done":'fileWalkDone',
        "front_end_size_info":'frontEndSizeInfo',
        "metadata_view_name":'metadataViewName',
        "num_app_instances":'numAppInstances',
        "num_app_objects":'numAppObjects',
        "post_backup_script_status":'postBackupScriptStatus',
        "pre_backup_script_status":'preBackupScriptStatus',
        "relative_snapshot_dir":'relativeSnapshotDir',
        "root_path":'rootPath',
        "scribe_table_column":'scribeTableColumn',
        "scribe_table_row":'scribeTableRow',
        "slave_task_start_time_usecs":'slaveTaskStartTimeUsecs',
        "snapshot_expiry_time":'snapshotExpiryTime',
        "snapshot_type":'snapshotType',
        "source_snapshot_create_time_usecs":'sourceSnapshotCreateTimeUsecs',
        "source_snapshot_name":'sourceSnapshotName',
        "source_snapshot_status":'sourceSnapshotStatus',
        "storage_snapshot_provider":'storageSnapshotProvider',
        "target_type":'targetType',
        "total_bytes_read_from_source":'totalBytesReadFromSource',
        "total_bytes_tiered":'totalBytesTiered',
        "total_bytes_to_read_from_source":'totalBytesToReadFromSource',
        "total_changed_entity_count":'totalChangedEntityCount',
        "total_entity_count":'totalEntityCount',
        "total_logical_backup_size_bytes":'totalLogicalBackupSizeBytes',
        "total_primary_physical_size_bytes":'totalPrimaryPhysicalSizeBytes',
        "mtype":'type',
        "view_case_insensitivity_altered":'viewCaseInsensitivityAltered',
        "view_name":'viewName',
        "view_name_to_gc":'viewNameToGc',
        "warnings":'warnings'
    }

    def __init__(self,
                 change_rocksdb_name=None,
                 error_rocksdb_name=None,
                 file_walk_done=None,
                 front_end_size_info=None,
                 metadata_view_name=None,
                 num_app_instances=None,
                 num_app_objects=None,
                 post_backup_script_status=None,
                 pre_backup_script_status=None,
                 relative_snapshot_dir=None,
                 root_path=None,
                 scribe_table_column=None,
                 scribe_table_row=None,
                 slave_task_start_time_usecs=None,
                 snapshot_expiry_time=None,
                 snapshot_type=None,
                 source_snapshot_create_time_usecs=None,
                 source_snapshot_name=None,
                 source_snapshot_status=None,
                 storage_snapshot_provider=None,
                 target_type=None,
                 total_bytes_read_from_source=None,
                 total_bytes_tiered=None,
                 total_bytes_to_read_from_source=None,
                 total_changed_entity_count=None,
                 total_entity_count=None,
                 total_logical_backup_size_bytes=None,
                 total_primary_physical_size_bytes=None,
                 mtype=None,
                 view_case_insensitivity_altered=None,
                 view_name=None,
                 view_name_to_gc=None,
                 warnings=None):
        """Constructor for the SnapshotInfoProto class"""

        # Initialize members of the class
        self.change_rocksdb_name = change_rocksdb_name
        self.error_rocksdb_name = error_rocksdb_name
        self.file_walk_done = file_walk_done
        self.front_end_size_info = front_end_size_info
        self.metadata_view_name = metadata_view_name
        self.num_app_instances = num_app_instances
        self.num_app_objects = num_app_objects
        self.post_backup_script_status = post_backup_script_status
        self.pre_backup_script_status = pre_backup_script_status
        self.relative_snapshot_dir = relative_snapshot_dir
        self.root_path = root_path
        self.scribe_table_column = scribe_table_column
        self.scribe_table_row = scribe_table_row
        self.slave_task_start_time_usecs = slave_task_start_time_usecs
        self.snapshot_expiry_time = snapshot_expiry_time
        self.snapshot_type = snapshot_type
        self.source_snapshot_create_time_usecs = source_snapshot_create_time_usecs
        self.source_snapshot_name = source_snapshot_name
        self.source_snapshot_status = source_snapshot_status
        self.storage_snapshot_provider = storage_snapshot_provider
        self.target_type = target_type
        self.total_bytes_read_from_source = total_bytes_read_from_source
        self.total_bytes_tiered = total_bytes_tiered
        self.total_bytes_to_read_from_source = total_bytes_to_read_from_source
        self.total_changed_entity_count = total_changed_entity_count
        self.total_entity_count = total_entity_count
        self.total_logical_backup_size_bytes = total_logical_backup_size_bytes
        self.total_primary_physical_size_bytes = total_primary_physical_size_bytes
        self.mtype = mtype
        self.view_case_insensitivity_altered = view_case_insensitivity_altered
        self.view_name = view_name
        self.view_name_to_gc = view_name_to_gc
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
        change_rocksdb_name = dictionary.get('changeRocksdbName')
        error_rocksdb_name = dictionary.get('errorRocksdbName')
        file_walk_done = dictionary.get('fileWalkDone')
        front_end_size_info = cohesity_management_sdk.models.size_info.SizeInfo.from_dictionary(dictionary.get('frontEndSizeInfo')) if dictionary.get('frontEndSizeInfo') else None
        metadata_view_name = dictionary.get('metadataViewName')
        num_app_instances = dictionary.get('numAppInstances')
        num_app_objects = dictionary.get('numAppObjects')
        post_backup_script_status = cohesity_management_sdk.models.script_execution_status.ScriptExecutionStatus.from_dictionary(dictionary.get('postBackupScriptStatus')) if dictionary.get('postBackupScriptStatus') else None
        pre_backup_script_status = cohesity_management_sdk.models.script_execution_status.ScriptExecutionStatus.from_dictionary(dictionary.get('preBackupScriptStatus')) if dictionary.get('preBackupScriptStatus') else None
        relative_snapshot_dir = dictionary.get('relativeSnapshotDir')
        root_path = dictionary.get('rootPath')
        scribe_table_column = dictionary.get('scribeTableColumn')
        scribe_table_row = dictionary.get('scribeTableRow')
        snapshot_expiry_time = dictionary.get('snapshotExpiryTime')
        slave_task_start_time_usecs = dictionary.get('slaveTaskStartTimeUsecs')
        snapshot_type = cohesity_management_sdk.models.object_snapshot_type.ObjectSnapshotType.from_dictionary(dictionary.get('snapshotType')) if dictionary.get('snapshotType') else None
        source_snapshot_create_time_usecs = dictionary.get('sourceSnapshotCreateTimeUsecs')
        source_snapshot_name = dictionary.get('sourceSnapshotName')
        source_snapshot_status = dictionary.get('sourceSnapshotStatus')
        storage_snapshot_provider = cohesity_management_sdk.models.storage_snapshot_provider_params.StorageSnapshotProviderParams.from_dictionary(dictionary.get('storageSnapshotProvider')) if dictionary.get('storageSnapshotProvider') else None
        target_type = dictionary.get('targetType')
        total_bytes_read_from_source = dictionary.get('totalBytesReadFromSource')
        total_bytes_tiered = dictionary.get('totalBytesTiered')
        total_bytes_to_read_from_source = dictionary.get('totalBytesToReadFromSource')
        total_changed_entity_count = dictionary.get('totalChangedEntityCount')
        total_entity_count = dictionary.get('totalEntityCount')
        total_logical_backup_size_bytes = dictionary.get('totalLogicalBackupSizeBytes')
        total_primary_physical_size_bytes = dictionary.get('totalPrimaryPhysicalSizeBytes')
        mtype = dictionary.get('type')
        view_case_insensitivity_altered = dictionary.get('viewCaseInsensitivityAltered')
        view_name = dictionary.get('viewName')
        view_name_to_gc = dictionary.get('viewNameToGc')
        warnings = None
        if dictionary.get('warnings') != None:
            warnings = list()
            for structure in dictionary.get('warnings'):
                warnings.append(cohesity_management_sdk.models.error_proto.ErrorProto.from_dictionary(structure))

        # Return an object of this model
        return cls(change_rocksdb_name,
                   error_rocksdb_name,
                   file_walk_done,
                   front_end_size_info,
                   metadata_view_name,
                   num_app_instances,
                   num_app_objects,
                   post_backup_script_status,
                   pre_backup_script_status,
                   relative_snapshot_dir,
                   root_path,
                   scribe_table_column,
                   scribe_table_row,
                   slave_task_start_time_usecs,
                   snapshot_expiry_time,
                   snapshot_type,
                   source_snapshot_create_time_usecs,
                   source_snapshot_name,
                   source_snapshot_status,
                   storage_snapshot_provider,
                   target_type,
                   total_bytes_read_from_source,
                   total_bytes_tiered,
                   total_bytes_to_read_from_source,
                   total_changed_entity_count,
                   total_entity_count,
                   total_logical_backup_size_bytes,
                   total_primary_physical_size_bytes,
                   mtype,
                   view_case_insensitivity_altered,
                   view_name,
                   view_name_to_gc,
                   warnings)


