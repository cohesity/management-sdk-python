# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.antivirus_scan_config
import cohesity_management_sdk.models.file_extension_filter
import cohesity_management_sdk.models.file_level_data_lock_config
import cohesity_management_sdk.models.nfs_root_permissions
import cohesity_management_sdk.models.nfs_squash
import cohesity_management_sdk.models.nis_netgroup
import cohesity_management_sdk.models.qo_s
import cohesity_management_sdk.models.quota_policy
import cohesity_management_sdk.models.smb_permission
import cohesity_management_sdk.models.smb_permissions_info
import cohesity_management_sdk.models.storage_policy_override
import cohesity_management_sdk.models.subnet
import cohesity_management_sdk.models.view_alias
import cohesity_management_sdk.models.view_intent
import cohesity_management_sdk.models.view_protection
import cohesity_management_sdk.models.view_stats


class View(object):

    """Implementation of the 'View' model.

    Specifies settings for defining a storage location (called a View) with NFS
    and SMB mount paths in a Storage Domain (View Box) on the Cohesity Cluster.


    Attributes:

        access_sids (list of string): Array of Security Identifiers (SIDs) 
            Specifies the list of security identifiers (SIDs) for the
            restricted Principals who have access to this View.
        aliases (list of ViewAlias): Aliases created for the view. A view alias
            allows a directory path inside a view to be mounted using the alias
            name.
        all_smb_mount_paths (list of string): Array of SMB Paths.  Specifies
            the possible paths that can be used to mount this View as a SMB
            share. If Active Directory has multiple account names; each machine
            account has its own path.
        antivirus_scan_config (AntivirusScanConfig): Specifies the antivirus
            scan config settings for this View.
        basic_mount_path (string): Specifies the NFS mount path of the View
            (without the hostname information). This path is used to support
            NFS mounting of the paths specified in the nfsExportPathList on
            Windows systems.
        case_insensitive_names_enabled (bool): Specifies whether to support
            case insensitive file/folder names. This parameter can only be set
            during create and cannot be changed.
        create_time_msecs (long|int): Specifies the time that the View was
            created in milliseconds.
        data_lock_expiry_usecs (long|int): DataLock (Write Once Read Many) lock
            expiry epoch time in microseconds. If a view is marked as a
            DataLock view, only a Data Security Officer (a user having Data
            Security Privilege) can delete the view until the lock expiry time.
        description (string): Specifies an optional text description about the
            View.
        enable_fast_durable_handle (bool): Specifies whether fast durable
            handle is enabled. If enabled, view open handle will be kept in
            memory, which results in a higher performance. But the handles
            cannot be recovered if node or service crashes.
        enable_filer_audit_logging (bool): Specifies if Filer Audit Logging is
            enabled for this view.
        enable_live_indexing (bool): Specifies whether to enable live indexing
            for the view.
        enable_metadata_accelerator (bool): Specifies whether view is blur
            enabled.
        enable_mixed_mode_permissions (bool): If set, mixed mode (NFS and SMB)
            access is enabled for this view. This field is deprecated. Use the
            field SecurityMode. deprecated: true
        enable_nfs_view_discovery (bool): If set, it enables discovery of view
            for NFS.
        enable_offline_caching (bool): Specifies whether to enable offline file
            caching of the view.
        enable_smb_access_based_enumeration (bool): Specifies if access-based
            enumeration should be enabled. If 'true', only files and folders
            that the user has permissions to access are visible on the SMB
            share for that user.
        enable_smb_encryption (bool): Specifies the SMB encryption for the
            View. If set, it enables the SMB encryption for the View.
            Encryption is supported only by SMB 3.x dialects. Dialects that do
            not support would still access data in unencrypted format.
        enable_smb_oplock (bool): Specifies whether SMB opportunistic lock is
            enabled.
        enable_smb_view_discovery (bool): If set, it enables discovery of view
            for SMB.
        enforce_smb_encryption (bool): Specifies the SMB encryption for all the
            sessions for the View. If set, encryption is enforced for all the
            sessions for the View. When enabled all future and existing
            unencrypted sessions are disallowed.
        file_extension_filter (FileExtensionFilter): Optional filtering
            criteria that should be satisfied by all the files created in this
            view. It does not affect existing files.
        file_lock_config (FileLevelDataLockConfig): Optional config that
            enables file locking for this view. It cannot be disabled during
            the edit of a view, if it has been enabled during the creation of
            the view. Also, it cannot be enabled if it was disabled during the
            creation of the view.
        intent (ViewIntent): Specifies the Intent of the View. readOnly: true
        is_externally_triggered_backup_target (bool): Specifies whether view is
            for externally triggered backup target.
        is_read_only (bool): Specifies if the view is a read only view. User
            will no longer be able to write to this view if this is set to
            true.
        is_target_for_migrated_data (bool): Specifies if a view contains
            migrated data.
        logical_quota (QuotaPolicy): Specifies an optional logical quota limit
            (in bytes) for the usage allowed on this View. (Logical data is
            when the data is fully hydrated and expanded.) This limit overrides
            the limit inherited from the Storage Domain (View Box) (if set). If
            logicalQuota is nil, the limit is inherited from the Storage Domain
            (View Box) (if set). A new write is not allowed if the Storage
            Domain (View Box) will exceed the specified quota. However, it
            takes time for the Cohesity Cluster to calculate the usage across
            Nodes, so the limit may be exceeded by a small amount. In addition,
            if the limit is increased or data is removed, there may be a delay
            before the Cohesity Cluster allows more data to be written to the
            View, as the Cluster is calculating the usage across Nodes.
        logical_usage_bytes (long|int): LogicalUsageBytes is the logical usage
            in bytes for the view.
        name (string): Specifies the name of the View.
        netgroup_whitelist (list of NisNetgroup): Array of Netgroups. 
            Specifies a list of Netgroups that have permissions to access the
            View. (Overrides the Netgroups specified at the global Cohesity
            Cluster level.)
        nfs_all_squash (NfsSquash): Specifies the NFS all squash config.
        nfs_mount_path (string): Specifies the path for mounting this View as
            an NFS share.
        nfs_root_permissions (NfsRootPermissions): Specifies the NFS root
            permission config of the view file system.
        nfs_root_squash (NfsSquash): Specifies the NFS root squash config.
        override_global_netgroup_whitelist (bool): Specifies whether view level
            client netgroup allowlist overrides cluster and global setting.
        override_global_whitelist (bool): Specifies whether view level client
            subnet allowlist overrides cluster and global setting.
        owner_sid (string): Specifies the Sid of the view owner.
        protocol_access (ProtocolAccessEnum): Specifies the supported Protocols
            for the View. 'kAll' enables protocol access to following three
            views: NFS, SMB and S3. 'kNFSOnly' enables protocol access to NFS
            only. 'kSMBOnly' enables protocol access to SMB only. 'kS3Only'
            enables protocol access to S3 only. 'kSwiftOnly' enables protocol
            access to Swift only. 'kUnknown' indicates that the protocol access
            of a view does not match any of the above. In this case, the
            constant is used as 'catch-all'.
        qos (QoS): Specifies the Quality of Service (QoS) Policy for the View.
        s3_access_path (string): Specifies the path to access this View as an
            S3 share.
        s3_folder_support_enabled (bool): Specifies whether to support s3
            folder support feature on the view. This parameter can only be set
            during create and cannot be changed.
        s3_key_mapping_config (S3KeyMappingConfigEnum): Specifies the S3 key
            mapping config of the view. This parameter can only be set during
            create and cannot be changed. Configuration of S3 key mapping. 
            Specifies the type of S3 key mapping config.
        security_mode (SecurityModeEnum): Specifies the security mode used for
            this view. Currently we support the following modes: Native,
            Unified and NTFS style. 'kNativeMode' indicates a native security
            mode. 'kUnifiedMode' indicates a unified security mode. 'kNtfsMode'
            indicates a NTFS style security mode.
        share_permissions (list of SmbPermission): Specifies a list of share
            level permissions.
        smb_mount_path (string): Specifies the main path for mounting this View
            as an SMB share.
        smb_permissions_info (SmbPermissionsInfo): Specifies the SMB
            permissions for the View.
        stats (ViewStats): Specifies statistics about the View. readOnly: true
        storage_policy_override (StoragePolicyOverride): Specifies if inline
            deduplication and compression settings inherited from the Storage
            Domain (View Box) should be disabled for this View.
        subnet_whitelist (list of Subnet): Array of Subnets.  Specifies a list
            of Subnets with IP addresses that have permissions to access the
            View. (Overrides the Subnets specified at the global Cohesity
            Cluster level.)
        super_user_sids (list of string): Specifies a list of user sids who
            have Superuser access to this view.
        swift_project_domain (string): Specifies the Keystone project domain.
        swift_project_name (string): Specifies the Keystone project name.
        swift_user_domain (string): Specifies the Keystone user domain.
        swift_username (string): Specifies the Keystone username.
        tenant_id (string): Optional tenant id who has access to this View.
        view_box_id (long|int): Specifies the id of the Storage Domain (View
            Box) where the View is stored.
        view_box_name (string): Specifies the name of the Storage Domain (View
            Box) where the View is stored.
        view_id (long|int): Specifies an id of the View assigned by the
            Cohesity Cluster.
        view_lock_enabled (bool): Specifies whether view lock is enabled. If
            enabled the view cannot be modified or deleted until unlock. By
            default it is disabled.
        view_protection (ViewProtection): Specifies information about the
            Protection Jobs protecting this View.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "access_sids":'accessSids',
        "aliases":'aliases',
        "all_smb_mount_paths":'allSmbMountPaths',
        "antivirus_scan_config":'antivirusScanConfig',
        "basic_mount_path":'basicMountPath',
        "case_insensitive_names_enabled":'caseInsensitiveNamesEnabled',
        "create_time_msecs":'createTimeMsecs',
        "data_lock_expiry_usecs":'dataLockExpiryUsecs',
        "description":'description',
        "enable_fast_durable_handle":'enableFastDurableHandle',
        "enable_filer_audit_logging":'enableFilerAuditLogging',
        "enable_live_indexing":'enableLiveIndexing',
        "enable_metadata_accelerator":'enableMetadataAccelerator',
        "enable_mixed_mode_permissions":'enableMixedModePermissions',
        "enable_nfs_view_discovery":'enableNfsViewDiscovery',
        "enable_offline_caching":'enableOfflineCaching',
        "enable_smb_access_based_enumeration":'enableSmbAccessBasedEnumeration',
        "enable_smb_encryption":'enableSmbEncryption',
        "enable_smb_oplock":'enableSmbOplock',
        "enable_smb_view_discovery":'enableSmbViewDiscovery',
        "enforce_smb_encryption":'enforceSmbEncryption',
        "file_extension_filter":'fileExtensionFilter',
        "file_lock_config":'fileLockConfig',
        "intent":'intent',
        "is_externally_triggered_backup_target":'isExternallyTriggeredBackupTarget',
        "is_read_only":'isReadOnly',
        "is_target_for_migrated_data":'isTargetForMigratedData',
        "logical_quota":'logicalQuota',
        "logical_usage_bytes":'logicalUsageBytes',
        "name":'name',
        "netgroup_whitelist":'netgroupWhitelist',
        "nfs_all_squash":'nfsAllSquash',
        "nfs_mount_path":'nfsMountPath',
        "nfs_root_permissions":'nfsRootPermissions',
        "nfs_root_squash":'nfsRootSquash',
        "override_global_netgroup_whitelist":'overrideGlobalNetgroupWhitelist',
        "override_global_whitelist":'overrideGlobalWhitelist',
        "owner_sid":'ownerSid',
        "protocol_access":'protocolAccess',
        "qos":'qos',
        "s3_access_path":'s3AccessPath',
        "s3_folder_support_enabled":'s3FolderSupportEnabled',
        "s3_key_mapping_config":'s3KeyMappingConfig',
        "security_mode":'securityMode',
        "share_permissions":'sharePermissions',
        "smb_mount_path":'smbMountPath',
        "smb_permissions_info":'smbPermissionsInfo',
        "stats":'stats',
        "storage_policy_override":'storagePolicyOverride',
        "subnet_whitelist":'subnetWhitelist',
        "super_user_sids":'superUserSids',
        "swift_project_domain":'swiftProjectDomain',
        "swift_project_name":'swiftProjectName',
        "swift_user_domain":'swiftUserDomain',
        "swift_username":'swiftUsername',
        "tenant_id":'tenantId',
        "view_box_id":'viewBoxId',
        "view_box_name":'viewBoxName',
        "view_id":'viewId',
        "view_lock_enabled":'viewLockEnabled',
        "view_protection":'viewProtection',
    }
    def __init__(self,
                 access_sids=None,
                 aliases=None,
                 all_smb_mount_paths=None,
                 antivirus_scan_config=None,
                 basic_mount_path=None,
                 case_insensitive_names_enabled=None,
                 create_time_msecs=None,
                 data_lock_expiry_usecs=None,
                 description=None,
                 enable_fast_durable_handle=None,
                 enable_filer_audit_logging=None,
                 enable_live_indexing=None,
                 enable_metadata_accelerator=None,
                 enable_mixed_mode_permissions=None,
                 enable_nfs_view_discovery=None,
                 enable_offline_caching=None,
                 enable_smb_access_based_enumeration=None,
                 enable_smb_encryption=None,
                 enable_smb_oplock=None,
                 enable_smb_view_discovery=None,
                 enforce_smb_encryption=None,
                 file_extension_filter=None,
                 file_lock_config=None,
                 intent=None,
                 is_externally_triggered_backup_target=None,
                 is_read_only=None,
                 is_target_for_migrated_data=None,
                 logical_quota=None,
                 logical_usage_bytes=None,
                 name=None,
                 netgroup_whitelist=None,
                 nfs_all_squash=None,
                 nfs_mount_path=None,
                 nfs_root_permissions=None,
                 nfs_root_squash=None,
                 override_global_netgroup_whitelist=None,
                 override_global_whitelist=None,
                 owner_sid=None,
                 protocol_access=None,
                 qos=None,
                 s3_access_path=None,
                 s3_folder_support_enabled=None,
                 s3_key_mapping_config=None,
                 security_mode=None,
                 share_permissions=None,
                 smb_mount_path=None,
                 smb_permissions_info=None,
                 stats=None,
                 storage_policy_override=None,
                 subnet_whitelist=None,
                 super_user_sids=None,
                 swift_project_domain=None,
                 swift_project_name=None,
                 swift_user_domain=None,
                 swift_username=None,
                 tenant_id=None,
                 view_box_id=None,
                 view_box_name=None,
                 view_id=None,
                 view_lock_enabled=None,
                 view_protection=None,
            ):

        """Constructor for the View class"""

        # Initialize members of the class
        self.access_sids = access_sids
        self.aliases = aliases
        self.all_smb_mount_paths = all_smb_mount_paths
        self.antivirus_scan_config = antivirus_scan_config
        self.basic_mount_path = basic_mount_path
        self.case_insensitive_names_enabled = case_insensitive_names_enabled
        self.create_time_msecs = create_time_msecs
        self.data_lock_expiry_usecs = data_lock_expiry_usecs
        self.description = description
        self.enable_fast_durable_handle = enable_fast_durable_handle
        self.enable_filer_audit_logging = enable_filer_audit_logging
        self.enable_live_indexing = enable_live_indexing
        self.enable_metadata_accelerator = enable_metadata_accelerator
        self.enable_mixed_mode_permissions = enable_mixed_mode_permissions
        self.enable_nfs_view_discovery = enable_nfs_view_discovery
        self.enable_offline_caching = enable_offline_caching
        self.enable_smb_access_based_enumeration = enable_smb_access_based_enumeration
        self.enable_smb_encryption = enable_smb_encryption
        self.enable_smb_oplock = enable_smb_oplock
        self.enable_smb_view_discovery = enable_smb_view_discovery
        self.enforce_smb_encryption = enforce_smb_encryption
        self.file_extension_filter = file_extension_filter
        self.file_lock_config = file_lock_config
        self.intent = intent
        self.is_externally_triggered_backup_target = is_externally_triggered_backup_target
        self.is_read_only = is_read_only
        self.is_target_for_migrated_data = is_target_for_migrated_data
        self.logical_quota = logical_quota
        self.logical_usage_bytes = logical_usage_bytes
        self.name = name
        self.netgroup_whitelist = netgroup_whitelist
        self.nfs_all_squash = nfs_all_squash
        self.nfs_mount_path = nfs_mount_path
        self.nfs_root_permissions = nfs_root_permissions
        self.nfs_root_squash = nfs_root_squash
        self.override_global_netgroup_whitelist = override_global_netgroup_whitelist
        self.override_global_whitelist = override_global_whitelist
        self.owner_sid = owner_sid
        self.protocol_access = protocol_access
        self.qos = qos
        self.s3_access_path = s3_access_path
        self.s3_folder_support_enabled = s3_folder_support_enabled
        self.s3_key_mapping_config = s3_key_mapping_config
        self.security_mode = security_mode
        self.share_permissions = share_permissions
        self.smb_mount_path = smb_mount_path
        self.smb_permissions_info = smb_permissions_info
        self.stats = stats
        self.storage_policy_override = storage_policy_override
        self.subnet_whitelist = subnet_whitelist
        self.super_user_sids = super_user_sids
        self.swift_project_domain = swift_project_domain
        self.swift_project_name = swift_project_name
        self.swift_user_domain = swift_user_domain
        self.swift_username = swift_username
        self.tenant_id = tenant_id
        self.view_box_id = view_box_id
        self.view_box_name = view_box_name
        self.view_id = view_id
        self.view_lock_enabled = view_lock_enabled
        self.view_protection = view_protection

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
        access_sids = dictionary.get("accessSids")
        aliases = None
        if dictionary.get('aliases') != None:
            aliases = list()
            for structure in dictionary.get('aliases'):
                aliases.append(cohesity_management_sdk.models.view_alias.ViewAlias.from_dictionary(structure))
        all_smb_mount_paths = dictionary.get("allSmbMountPaths")
        antivirus_scan_config = cohesity_management_sdk.models.antivirus_scan_config.AntivirusScanConfig.from_dictionary(dictionary.get('antivirusScanConfig')) if dictionary.get('antivirusScanConfig') else None
        basic_mount_path = dictionary.get('basicMountPath')
        case_insensitive_names_enabled = dictionary.get('caseInsensitiveNamesEnabled')
        create_time_msecs = dictionary.get('createTimeMsecs')
        data_lock_expiry_usecs = dictionary.get('dataLockExpiryUsecs')
        description = dictionary.get('description')
        enable_fast_durable_handle = dictionary.get('enableFastDurableHandle')
        enable_filer_audit_logging = dictionary.get('enableFilerAuditLogging')
        enable_live_indexing = dictionary.get('enableLiveIndexing')
        enable_metadata_accelerator = dictionary.get('enableMetadataAccelerator')
        enable_mixed_mode_permissions = dictionary.get('enableMixedModePermissions')
        enable_nfs_view_discovery = dictionary.get('enableNfsViewDiscovery')
        enable_offline_caching = dictionary.get('enableOfflineCaching')
        enable_smb_access_based_enumeration = dictionary.get('enableSmbAccessBasedEnumeration')
        enable_smb_encryption = dictionary.get('enableSmbEncryption')
        enable_smb_oplock = dictionary.get('enableSmbOplock')
        enable_smb_view_discovery = dictionary.get('enableSmbViewDiscovery')
        enforce_smb_encryption = dictionary.get('enforceSmbEncryption')
        file_extension_filter = cohesity_management_sdk.models.file_extension_filter.FileExtensionFilter.from_dictionary(dictionary.get('fileExtensionFilter')) if dictionary.get('fileExtensionFilter') else None
        file_lock_config = cohesity_management_sdk.models.file_level_data_lock_config.FileLevelDataLockConfig.from_dictionary(dictionary.get('fileLockConfig')) if dictionary.get('fileLockConfig') else None
        intent = cohesity_management_sdk.models.view_intent.ViewIntent.from_dictionary(dictionary.get('intent')) if dictionary.get('intent') else None
        is_externally_triggered_backup_target = dictionary.get('isExternallyTriggeredBackupTarget')
        is_read_only = dictionary.get('isReadOnly')
        is_target_for_migrated_data = dictionary.get('isTargetForMigratedData')
        logical_quota = cohesity_management_sdk.models.quota_policy.QuotaPolicy.from_dictionary(dictionary.get('logicalQuota')) if dictionary.get('logicalQuota') else None
        logical_usage_bytes = dictionary.get('logicalUsageBytes')
        name = dictionary.get('name')
        netgroup_whitelist = None
        if dictionary.get('netgroupWhitelist') != None:
            netgroup_whitelist = list()
            for structure in dictionary.get('netgroupWhitelist'):
                netgroup_whitelist.append(cohesity_management_sdk.models.nis_netgroup.NisNetgroup.from_dictionary(structure))
        nfs_all_squash = cohesity_management_sdk.models.nfs_squash.NfsSquash.from_dictionary(dictionary.get('nfsAllSquash')) if dictionary.get('nfsAllSquash') else None
        nfs_mount_path = dictionary.get('nfsMountPath')
        nfs_root_permissions = cohesity_management_sdk.models.nfs_root_permissions.NfsRootPermissions.from_dictionary(dictionary.get('nfsRootPermissions')) if dictionary.get('nfsRootPermissions') else None
        nfs_root_squash = cohesity_management_sdk.models.nfs_squash.NfsSquash.from_dictionary(dictionary.get('nfsRootSquash')) if dictionary.get('nfsRootSquash') else None
        override_global_netgroup_whitelist = dictionary.get('overrideGlobalNetgroupWhitelist')
        override_global_whitelist = dictionary.get('overrideGlobalWhitelist')
        owner_sid = dictionary.get('ownerSid')
        protocol_access = dictionary.get('protocolAccess')
        qos = cohesity_management_sdk.models.qo_s.QoS.from_dictionary(dictionary.get('qos')) if dictionary.get('qos') else None
        s3_access_path = dictionary.get('s3AccessPath')
        s3_folder_support_enabled = dictionary.get('s3FolderSupportEnabled')
        s3_key_mapping_config = dictionary.get('s3KeyMappingConfig')
        security_mode = dictionary.get('securityMode')
        share_permissions = None
        if dictionary.get('sharePermissions') != None:
            share_permissions = list()
            for structure in dictionary.get('sharePermissions'):
                share_permissions.append(cohesity_management_sdk.models.smb_permission.SmbPermission.from_dictionary(structure))
        smb_mount_path = dictionary.get('smbMountPath')
        smb_permissions_info = cohesity_management_sdk.models.smb_permissions_info.SmbPermissionsInfo.from_dictionary(dictionary.get('smbPermissionsInfo')) if dictionary.get('smbPermissionsInfo') else None
        stats = cohesity_management_sdk.models.view_stats.ViewStats.from_dictionary(dictionary.get('stats')) if dictionary.get('stats') else None
        storage_policy_override = cohesity_management_sdk.models.storage_policy_override.StoragePolicyOverride.from_dictionary(dictionary.get('storagePolicyOverride')) if dictionary.get('storagePolicyOverride') else None
        subnet_whitelist = None
        if dictionary.get('subnetWhitelist') != None:
            subnet_whitelist = list()
            for structure in dictionary.get('subnetWhitelist'):
                subnet_whitelist.append(cohesity_management_sdk.models.subnet.Subnet.from_dictionary(structure))
        super_user_sids = dictionary.get("superUserSids")
        swift_project_domain = dictionary.get('swiftProjectDomain')
        swift_project_name = dictionary.get('swiftProjectName')
        swift_user_domain = dictionary.get('swiftUserDomain')
        swift_username = dictionary.get('swiftUsername')
        tenant_id = dictionary.get('tenantId')
        view_box_id = dictionary.get('viewBoxId')
        view_box_name = dictionary.get('viewBoxName')
        view_id = dictionary.get('viewId')
        view_lock_enabled = dictionary.get('viewLockEnabled')
        view_protection = cohesity_management_sdk.models.view_protection.ViewProtection.from_dictionary(dictionary.get('viewProtection')) if dictionary.get('viewProtection') else None

        # Return an object of this model
        return cls(
            access_sids,
            aliases,
            all_smb_mount_paths,
            antivirus_scan_config,
            basic_mount_path,
            case_insensitive_names_enabled,
            create_time_msecs,
            data_lock_expiry_usecs,
            description,
            enable_fast_durable_handle,
            enable_filer_audit_logging,
            enable_live_indexing,
            enable_metadata_accelerator,
            enable_mixed_mode_permissions,
            enable_nfs_view_discovery,
            enable_offline_caching,
            enable_smb_access_based_enumeration,
            enable_smb_encryption,
            enable_smb_oplock,
            enable_smb_view_discovery,
            enforce_smb_encryption,
            file_extension_filter,
            file_lock_config,
            intent,
            is_externally_triggered_backup_target,
            is_read_only,
            is_target_for_migrated_data,
            logical_quota,
            logical_usage_bytes,
            name,
            netgroup_whitelist,
            nfs_all_squash,
            nfs_mount_path,
            nfs_root_permissions,
            nfs_root_squash,
            override_global_netgroup_whitelist,
            override_global_whitelist,
            owner_sid,
            protocol_access,
            qos,
            s3_access_path,
            s3_folder_support_enabled,
            s3_key_mapping_config,
            security_mode,
            share_permissions,
            smb_mount_path,
            smb_permissions_info,
            stats,
            storage_policy_override,
            subnet_whitelist,
            super_user_sids,
            swift_project_domain,
            swift_project_name,
            swift_user_domain,
            swift_username,
            tenant_id,
            view_box_id,
            view_box_name,
            view_id,
            view_lock_enabled,
            view_protection
)