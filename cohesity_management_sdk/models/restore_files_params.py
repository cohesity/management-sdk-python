# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.credentials
import cohesity_management_sdk.models.entity_proto
import cohesity_management_sdk.models.file_uptiering_params
import cohesity_management_sdk.models.isilon_env_params
import cohesity_management_sdk.models.nas_backup_params
import cohesity_management_sdk.models.restore_files_params_directory_name_security_style_map_entry
import cohesity_management_sdk.models.restore_files_preferences
import cohesity_management_sdk.models.restored_file_info
import cohesity_management_sdk.models.s3_view_backup_properties


class RestoreFilesParams(object):

    """Implementation of the 'RestoreFilesParams' model.

    This message captures all the necessary arguments specified by the user to
    restore files to the source.


    Attributes:

        blacklisted_ip_addrs (list of string): A list of target IP addresses
            that should not be used.
        destination_ep_uuid (string): Destination endpoint UUID for source s3
            objectstore.
        directory_name_security_style_map (list of
            RestoreFilesParams_DirectoryNameSecurityStyleMapEntry): Directory
            name security style map contains mapping of the directory name to
            security style it supports.  This is needed to restore the same
            permission for the given directory for Qtrees.
        glacier_flr_restore_option (int): Glacier restore option chosen by the
            user.
        is_archive_flr (bool): Whether this is a file restore operation from an
            archive.
        is_file_volume_restore (bool): Whether this is a file based volume
            restore.
        is_mount_based_flr (bool): Whether this is a mount based file restore
            operation
        is_source_initiated_restore (bool): Whether this is a source initiated
            restore.
        isilon_env_params (IsilonEnvParams): This is applicable if target
            entity is of kIsilon type.
        mount_disks_on_vm (bool): Whether this will attach disks or mount disks
            on the VM side OR use Storage Proxy RPCs to stream data.
        nas_backup_params (NasBackupParams): Used to determining
            filtering_policy for NAS Migration uptier operation. Currently this
            is set only if this is NAS Migration uptier operation.
        nas_protocol_type_vec (list of int): The NAS protocol type(s) of this
            restore task. Currently we only support a single restore type. This
            field is only populated for NAS restore tasks.
        objectstore_config_name (string): Object store config name for source
            initiated backup.
        physical_flr_parallel_restore (bool): If enabled, magneto physical file
            restore will be enabled via job framework
        proxy_entity (EntityProto): If the proxy entity is specified, then the
            virtual disks are attached to the proxy server and the file copy
            will be initiated through this server.
        proxy_entity_parent_source (EntityProto): If the proxy entity above is
            specified, then it's parent entity must be specified as well.
        restore_files_preferences (RestoreFilesPreferences): Preferences for
            the restore files operation.
        restore_method (int): Determines the type of method to be used to
            perform FLR.
        restored_file_info_vec (list of RestoredFileInfo): Information
            regarding files and directories.
        s3_viewbackupproperties (S3ViewBackupProperties): This message captures
            all the details of S3 view from where the data is restored.
        source_snapshot_name (string): Snapshot name need by source to start
            the restore.
        target_entity (EntityProto): Target entity where the files are being
            restored to.
        target_entity_credentials (Credentials): Credentials to access the
            target entity such as a VM. In case of physical server, the copy
            process will be launched as this user. NOTE: If proxy entity is
            specified, then this credentials will be used for running
            operations on proxy server as well.
        target_entity_parent_source (EntityProto): The registered source (i.e
            vCenter or ESXi host in VMware environment) under which the target
            entity is present.
        target_host_entity (EntityProto): Host entity where the target entity
            resides. This is only populated for Netapp environments right now
            if target_entity_parent_source is a cluster. For example, the host
            of a target Netapp volume will be the vserver it belongs to.
        target_host_type (int): The host environment type. This is set in
            VMware environment to indicate the OS type of the target entity.
            NOTE: This is expected to be set since magneto does not know the
            host type for VMware entities.
        uptier_params (FileUptieringParams): Set if this is NAS Migration
            uptier operation.
        use_existing_agent (bool): Whether this will use an existing agent on
            the target VM to do the restore. This field is deprecated.
            restore_method should be used for populating use of existing agent.
        view_id (long|int): View ID
        view_name (string): Name of the S3 view
        vpc_connector_entity (EntityProto): Entity of the VPC connector,
            required in case of GCP FLR.
        whitelisted_ip_addrs (list of string): A list of target IP addresses
            that should be used exclusively.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "blacklisted_ip_addrs":'blacklistedIpAddrs',
        "destination_ep_uuid":'destinationEpUuid',
        "directory_name_security_style_map":'directoryNameSecurityStyleMap',
        "glacier_flr_restore_option":'glacierFlrRestoreOption',
        "is_archive_flr":'isArchiveFlr',
        "is_file_volume_restore":'isFileVolumeRestore',
        "is_mount_based_flr":'isMountBasedFlr',
        "is_source_initiated_restore":'isSourceInitiatedRestore',
        "isilon_env_params":'isilonEnvParams',
        "mount_disks_on_vm":'mountDisksOnVm',
        "nas_backup_params":'nasBackupParams',
        "nas_protocol_type_vec":'nasProtocolTypeVec',
        "objectstore_config_name":'objectstoreConfigName',
        "physical_flr_parallel_restore":'physicalFlrParallelRestore',
        "proxy_entity":'proxyEntity',
        "proxy_entity_parent_source":'proxyEntityParentSource',
        "restore_files_preferences":'restoreFilesPreferences',
        "restore_method":'restoreMethod',
        "restored_file_info_vec":'restoredFileInfoVec',
        "s3_viewbackupproperties":'s3Viewbackupproperties',
        "source_snapshot_name":'sourceSnapshotName',
        "target_entity":'targetEntity',
        "target_entity_credentials":'targetEntityCredentials',
        "target_entity_parent_source":'targetEntityParentSource',
        "target_host_entity":'targetHostEntity',
        "target_host_type":'targetHostType',
        "uptier_params":'uptierParams',
        "use_existing_agent":'useExistingAgent',
        "view_id":'viewId',
        "view_name":'viewName',
        "vpc_connector_entity":'vpcConnectorEntity',
        "whitelisted_ip_addrs":'whitelistedIpAddrs',
    }
    def __init__(self,
                 blacklisted_ip_addrs=None,
                 destination_ep_uuid=None,
                 directory_name_security_style_map=None,
                 glacier_flr_restore_option=None,
                 is_archive_flr=None,
                 is_file_volume_restore=None,
                 is_mount_based_flr=None,
                 is_source_initiated_restore=None,
                 isilon_env_params=None,
                 mount_disks_on_vm=None,
                 nas_backup_params=None,
                 nas_protocol_type_vec=None,
                 objectstore_config_name=None,
                 physical_flr_parallel_restore=None,
                 proxy_entity=None,
                 proxy_entity_parent_source=None,
                 restore_files_preferences=None,
                 restore_method=None,
                 restored_file_info_vec=None,
                 s3_viewbackupproperties=None,
                 source_snapshot_name=None,
                 target_entity=None,
                 target_entity_credentials=None,
                 target_entity_parent_source=None,
                 target_host_entity=None,
                 target_host_type=None,
                 uptier_params=None,
                 use_existing_agent=None,
                 view_id=None,
                 view_name=None,
                 vpc_connector_entity=None,
                 whitelisted_ip_addrs=None,
            ):

        """Constructor for the RestoreFilesParams class"""

        # Initialize members of the class
        self.blacklisted_ip_addrs = blacklisted_ip_addrs
        self.destination_ep_uuid = destination_ep_uuid
        self.directory_name_security_style_map = directory_name_security_style_map
        self.glacier_flr_restore_option = glacier_flr_restore_option
        self.is_archive_flr = is_archive_flr
        self.is_file_volume_restore = is_file_volume_restore
        self.is_mount_based_flr = is_mount_based_flr
        self.is_source_initiated_restore = is_source_initiated_restore
        self.isilon_env_params = isilon_env_params
        self.mount_disks_on_vm = mount_disks_on_vm
        self.nas_backup_params = nas_backup_params
        self.nas_protocol_type_vec = nas_protocol_type_vec
        self.objectstore_config_name = objectstore_config_name
        self.physical_flr_parallel_restore = physical_flr_parallel_restore
        self.proxy_entity = proxy_entity
        self.proxy_entity_parent_source = proxy_entity_parent_source
        self.restore_files_preferences = restore_files_preferences
        self.restore_method = restore_method
        self.restored_file_info_vec = restored_file_info_vec
        self.s3_viewbackupproperties = s3_viewbackupproperties
        self.source_snapshot_name = source_snapshot_name
        self.target_entity = target_entity
        self.target_entity_credentials = target_entity_credentials
        self.target_entity_parent_source = target_entity_parent_source
        self.target_host_entity = target_host_entity
        self.target_host_type = target_host_type
        self.uptier_params = uptier_params
        self.use_existing_agent = use_existing_agent
        self.view_id = view_id
        self.view_name = view_name
        self.vpc_connector_entity = vpc_connector_entity
        self.whitelisted_ip_addrs = whitelisted_ip_addrs

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
        blacklisted_ip_addrs = dictionary.get("blacklistedIpAddrs")
        destination_ep_uuid = dictionary.get('destinationEpUuid')
        directory_name_security_style_map = None
        if dictionary.get('directoryNameSecurityStyleMap') != None:
            directory_name_security_style_map = list()
            for structure in dictionary.get('directoryNameSecurityStyleMap'):
                directory_name_security_style_map.append(cohesity_management_sdk.models.restore_files_params_directory_name_security_style_map_entry.RestoreFilesParams_DirectoryNameSecurityStyleMapEntry.from_dictionary(structure))
        glacier_flr_restore_option = dictionary.get('glacierFlrRestoreOption')
        is_archive_flr = dictionary.get('isArchiveFlr')
        is_file_volume_restore = dictionary.get('isFileVolumeRestore')
        is_mount_based_flr = dictionary.get('isMountBasedFlr')
        is_source_initiated_restore = dictionary.get('isSourceInitiatedRestore')
        isilon_env_params = cohesity_management_sdk.models.isilon_env_params.IsilonEnvParams.from_dictionary(dictionary.get('isilonEnvParams')) if dictionary.get('isilonEnvParams') else None
        mount_disks_on_vm = dictionary.get('mountDisksOnVm')
        nas_backup_params = cohesity_management_sdk.models.nas_backup_params.NasBackupParams.from_dictionary(dictionary.get('nasBackupParams')) if dictionary.get('nasBackupParams') else None
        nas_protocol_type_vec = dictionary.get("nasProtocolTypeVec")
        objectstore_config_name = dictionary.get('objectstoreConfigName')
        physical_flr_parallel_restore = dictionary.get('physicalFlrParallelRestore')
        proxy_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('proxyEntity')) if dictionary.get('proxyEntity') else None
        proxy_entity_parent_source = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('proxyEntityParentSource')) if dictionary.get('proxyEntityParentSource') else None
        restore_files_preferences = cohesity_management_sdk.models.restore_files_preferences.RestoreFilesPreferences.from_dictionary(dictionary.get('restoreFilesPreferences')) if dictionary.get('restoreFilesPreferences') else None
        restore_method = dictionary.get('restoreMethod')
        restored_file_info_vec = None
        if dictionary.get('restoredFileInfoVec') != None:
            restored_file_info_vec = list()
            for structure in dictionary.get('restoredFileInfoVec'):
                restored_file_info_vec.append(cohesity_management_sdk.models.restored_file_info.RestoredFileInfo.from_dictionary(structure))
        s3_viewbackupproperties = cohesity_management_sdk.models.s3_view_backup_properties.S3ViewBackupProperties.from_dictionary(dictionary.get('s3Viewbackupproperties')) if dictionary.get('s3Viewbackupproperties') else None
        source_snapshot_name = dictionary.get('sourceSnapshotName')
        target_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('targetEntity')) if dictionary.get('targetEntity') else None
        target_entity_credentials = cohesity_management_sdk.models.credentials.Credentials.from_dictionary(dictionary.get('targetEntityCredentials')) if dictionary.get('targetEntityCredentials') else None
        target_entity_parent_source = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('targetEntityParentSource')) if dictionary.get('targetEntityParentSource') else None
        target_host_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('targetHostEntity')) if dictionary.get('targetHostEntity') else None
        target_host_type = dictionary.get('targetHostType')
        uptier_params = cohesity_management_sdk.models.file_uptiering_params.FileUptieringParams.from_dictionary(dictionary.get('uptierParams')) if dictionary.get('uptierParams') else None
        use_existing_agent = dictionary.get('useExistingAgent')
        view_id = dictionary.get('viewId')
        view_name = dictionary.get('viewName')
        vpc_connector_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('vpcConnectorEntity')) if dictionary.get('vpcConnectorEntity') else None
        whitelisted_ip_addrs = dictionary.get("whitelistedIpAddrs")

        # Return an object of this model
        return cls(
            blacklisted_ip_addrs,
            destination_ep_uuid,
            directory_name_security_style_map,
            glacier_flr_restore_option,
            is_archive_flr,
            is_file_volume_restore,
            is_mount_based_flr,
            is_source_initiated_restore,
            isilon_env_params,
            mount_disks_on_vm,
            nas_backup_params,
            nas_protocol_type_vec,
            objectstore_config_name,
            physical_flr_parallel_restore,
            proxy_entity,
            proxy_entity_parent_source,
            restore_files_preferences,
            restore_method,
            restored_file_info_vec,
            s3_viewbackupproperties,
            source_snapshot_name,
            target_entity,
            target_entity_credentials,
            target_entity_parent_source,
            target_host_entity,
            target_host_type,
            uptier_params,
            use_existing_agent,
            view_id,
            view_name,
            vpc_connector_entity,
            whitelisted_ip_addrs
)