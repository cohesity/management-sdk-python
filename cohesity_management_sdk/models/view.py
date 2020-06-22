# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.view_alias_info
import cohesity_management_sdk.models.antivirus_scan_config
import cohesity_management_sdk.models.file_extension_filter
import cohesity_management_sdk.models.file_level_data_lock_config
import cohesity_management_sdk.models.quota_policy
import cohesity_management_sdk.models.qo_s
import cohesity_management_sdk.models.smb_permissions_info
import cohesity_management_sdk.models.view_stats
import cohesity_management_sdk.models.storage_policy_override
import cohesity_management_sdk.models.subnet
import cohesity_management_sdk.models.view_protection

class View(object):

    """Implementation of the 'View' model.

    Specifies settings for defining a storage location (called a View)
    with NFS and SMB mount paths in a Storage Domain (View Box) on the
    Cohesity
    Cluster.

    Attributes:
        access_sids (list of string): Array of Security Identifiers (SIDs)
            Specifies the list of security identifiers (SIDs) for the
            restricted Principals who have access to this View.
        aliases (list of ViewAliasInfo): Aliases created for the view. A view
            alias allows a directory path inside a view to be mounted using
            the alias name.
        all_smb_mount_paths (list of string): Array of SMB Paths.  Specifies
            the possible paths that can be used to mount this View as a SMB
            share. If Active Directory has multiple account names; each
            machine account has its own path.
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
        data_lock_expiry_usecs (long|int): DataLock (Write Once Read Many)
            lock expiry epoch time in microseconds. If a view is marked as a
            DataLock view, only a Data Security Officer (a user having Data
            Security Privilege) can delete the view until the lock expiry
            time.
        description (string): Specifies an optional text description about the
            View.
        enable_filer_audit_logging (bool): Specifies if Filer Audit Logging is
            enabled for this view.
        enable_mixed_mode_permissions (bool): If set, mixed mode (NFS and SMB)
            access is enabled for this view. This field is deprecated. Use the
            field SecurityMode. deprecated: true
        enable_nfs_view_discovery (bool): If set, it enables discovery of view
            for NFS.
        enable_smb_access_based_enumeration (bool): Specifies if access-based
            enumeration should be enabled. If 'true', only files and folders
            that the user has permissions to access are visible on the SMB
            share for that user.
        enable_smb_encryption (bool): Specifies the SMB encryption for the
            View. If set, it enables the SMB encryption for the View.
            Encryption is supported only by SMB 3.x dialects. Dialects that do
            not support would still access data in unencrypted format.
        enable_smb_view_discovery (bool): If set, it enables discovery of view
            for SMB.
        enforce_smb_encryption (bool): Specifies the SMB encryption for all
            the sessions for the View. If set, encryption is enforced for all
            the sessions for the View. When enabled all future and existing
            unencrypted sessions are disallowed.
        file_extension_filter (FileExtensionFilter): TODO: type description
            here.
        file_lock_config (FileLevelDataLockConfig): Specifies a config to lock
            files in a view - to protect from malicious or an accidental
            attempt to delete or modify the files in this view.
        is_target_for_migrated_data (bool): Specifies if a view contains
            migrated data.
        logical_quota (QuotaPolicy): Specifies an optional logical quota limit
            (in bytes) for the usage allowed on this View. (Logical data is
            when the data is fully hydrated and expanded.) This limit
            overrides the limit inherited from the Storage Domain (View Box)
            (if set). If logicalQuota is nil, the limit is inherited from the
            Storage Domain (View Box) (if set). A new write is not allowed if
            the Storage Domain (View Box) will exceed the specified quota.
            However, it takes time for the Cohesity Cluster to calculate the
            usage across Nodes, so the limit may be exceeded by a small
            amount. In addition, if the limit is increased or data is removed,
            there may be a delay before the Cohesity Cluster allows more data
            to be written to the View, as the Cluster is calculating the usage
            across Nodes.
        logical_usage_bytes (long|int): LogicalUsageBytes is the logical usage
            in bytes for the view.
        name (string): Specifies the name of the View.
        nfs_mount_path (string): Specifies the path for mounting this View as
            an NFS share.
        protocol_access (ProtocolAccessEnum): Specifies the supported
            Protocols for the View. 'kAll' enables protocol access to all
            three views: NFS, SMB and S3. 'kNFSOnly' enables protocol access
            to NFS only. 'kSMBOnly' enables protocol access to SMB only.
            'kS3Only' enables protocol access to S3 only.
        qos (QoS): Specifies the Quality of Service (QoS) Policy for the
            View.
        s_3_access_path (string): Specifies the path to access this View as an
            S3 share.
        security_mode (SecurityModeEnum): Specifies the security mode used for
            this view. Currently we support the following modes: Native,
            Unified and NTFS style. 'kNativeMode' indicates a native security
            mode. 'kUnifiedMode' indicates a unified security mode.
            'kNtfsMode' indicates a NTFS style security mode.
        smb_mount_path (string): Specifies the main path for mounting this
            View as an SMB share.
        smb_permissions_info (SmbPermissionsInfo): Specifies information about
            SMB permissions.
        stats (ViewStats): Provides statistics about the View.
        storage_policy_override (StoragePolicyOverride): Specifies if inline
            deduplication and compression settings inherited from Storage
            Domain (View Box) should be disabled for this View.
        subnet_whitelist (list of Subnet): Array of Subnets.  Specifies a list
            of Subnets with IP addresses that have permissions to access the
            View. (Overrides the Subnets specified at the global Cohesity
            Cluster level.)
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
            Protection Jobs that are protecting the View.

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
        "enable_filer_audit_logging":'enableFilerAuditLogging',
        "enable_mixed_mode_permissions":'enableMixedModePermissions',
        "enable_nfs_view_discovery":'enableNfsViewDiscovery',
        "enable_smb_access_based_enumeration":'enableSmbAccessBasedEnumeration',
        "enable_smb_encryption":'enableSmbEncryption',
        "enable_smb_view_discovery":'enableSmbViewDiscovery',
        "enforce_smb_encryption":'enforceSmbEncryption',
        "file_extension_filter":'fileExtensionFilter',
        "file_lock_config":'fileLockConfig',
        "is_target_for_migrated_data":'isTargetForMigratedData',
        "logical_quota":'logicalQuota',
        "logical_usage_bytes":'logicalUsageBytes',
        "name":'name',
        "nfs_mount_path":'nfsMountPath',
        "protocol_access":'protocolAccess',
        "qos":'qos',
        "s_3_access_path":'s3AccessPath',
        "security_mode":'securityMode',
        "smb_mount_path":'smbMountPath',
        "smb_permissions_info":'smbPermissionsInfo',
        "stats":'stats',
        "storage_policy_override":'storagePolicyOverride',
        "subnet_whitelist":'subnetWhitelist',
        "tenant_id":'tenantId',
        "view_box_id":'viewBoxId',
        "view_box_name":'viewBoxName',
        "view_id":'viewId',
        "view_lock_enabled":'viewLockEnabled',
        "view_protection":'viewProtection'
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
                 enable_filer_audit_logging=None,
                 enable_mixed_mode_permissions=None,
                 enable_nfs_view_discovery=None,
                 enable_smb_access_based_enumeration=None,
                 enable_smb_encryption=None,
                 enable_smb_view_discovery=None,
                 enforce_smb_encryption=None,
                 file_extension_filter=None,
                 file_lock_config=None,
                 is_target_for_migrated_data=None,
                 logical_quota=None,
                 logical_usage_bytes=None,
                 name=None,
                 nfs_mount_path=None,
                 protocol_access=None,
                 qos=None,
                 s_3_access_path=None,
                 security_mode=None,
                 smb_mount_path=None,
                 smb_permissions_info=None,
                 stats=None,
                 storage_policy_override=None,
                 subnet_whitelist=None,
                 tenant_id=None,
                 view_box_id=None,
                 view_box_name=None,
                 view_id=None,
                 view_lock_enabled=None,
                 view_protection=None):
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
        self.enable_filer_audit_logging = enable_filer_audit_logging
        self.enable_mixed_mode_permissions = enable_mixed_mode_permissions
        self.enable_nfs_view_discovery = enable_nfs_view_discovery
        self.enable_smb_access_based_enumeration = enable_smb_access_based_enumeration
        self.enable_smb_encryption = enable_smb_encryption
        self.enable_smb_view_discovery = enable_smb_view_discovery
        self.enforce_smb_encryption = enforce_smb_encryption
        self.file_extension_filter = file_extension_filter
        self.file_lock_config = file_lock_config
        self.is_target_for_migrated_data = is_target_for_migrated_data
        self.logical_quota = logical_quota
        self.logical_usage_bytes = logical_usage_bytes
        self.name = name
        self.nfs_mount_path = nfs_mount_path
        self.protocol_access = protocol_access
        self.qos = qos
        self.s_3_access_path = s_3_access_path
        self.security_mode = security_mode
        self.smb_mount_path = smb_mount_path
        self.smb_permissions_info = smb_permissions_info
        self.stats = stats
        self.storage_policy_override = storage_policy_override
        self.subnet_whitelist = subnet_whitelist
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
        access_sids = dictionary.get('accessSids')
        aliases = None
        if dictionary.get('aliases') != None:
            aliases = list()
            for structure in dictionary.get('aliases'):
                aliases.append(cohesity_management_sdk.models.view_alias_info.ViewAliasInfo.from_dictionary(structure))
        all_smb_mount_paths = dictionary.get('allSmbMountPaths')
        antivirus_scan_config = cohesity_management_sdk.models.antivirus_scan_config.AntivirusScanConfig.from_dictionary(dictionary.get('antivirusScanConfig')) if dictionary.get('antivirusScanConfig') else None
        basic_mount_path = dictionary.get('basicMountPath')
        case_insensitive_names_enabled = dictionary.get('caseInsensitiveNamesEnabled')
        create_time_msecs = dictionary.get('createTimeMsecs')
        data_lock_expiry_usecs = dictionary.get('dataLockExpiryUsecs')
        description = dictionary.get('description')
        enable_filer_audit_logging = dictionary.get('enableFilerAuditLogging')
        enable_mixed_mode_permissions = dictionary.get('enableMixedModePermissions')
        enable_nfs_view_discovery = dictionary.get('enableNfsViewDiscovery')
        enable_smb_access_based_enumeration = dictionary.get('enableSmbAccessBasedEnumeration')
        enable_smb_encryption = dictionary.get('enableSmbEncryption')
        enable_smb_view_discovery = dictionary.get('enableSmbViewDiscovery')
        enforce_smb_encryption = dictionary.get('enforceSmbEncryption')
        file_extension_filter = cohesity_management_sdk.models.file_extension_filter.FileExtensionFilter.from_dictionary(dictionary.get('fileExtensionFilter')) if dictionary.get('fileExtensionFilter') else None
        file_lock_config = cohesity_management_sdk.models.file_level_data_lock_config.FileLevelDataLockConfig.from_dictionary(dictionary.get('fileLockConfig')) if dictionary.get('fileLockConfig') else None
        is_target_for_migrated_data = dictionary.get('isTargetForMigratedData')
        logical_quota = cohesity_management_sdk.models.quota_policy.QuotaPolicy.from_dictionary(dictionary.get('logicalQuota')) if dictionary.get('logicalQuota') else None
        logical_usage_bytes = dictionary.get('logicalUsageBytes')
        name = dictionary.get('name')
        nfs_mount_path = dictionary.get('nfsMountPath')
        protocol_access = dictionary.get('protocolAccess')
        qos = cohesity_management_sdk.models.qo_s.QoS.from_dictionary(dictionary.get('qos')) if dictionary.get('qos') else None
        s_3_access_path = dictionary.get('s3AccessPath')
        security_mode = dictionary.get('securityMode')
        smb_mount_path = dictionary.get('smbMountPath')
        smb_permissions_info = cohesity_management_sdk.models.smb_permissions_info.SmbPermissionsInfo.from_dictionary(dictionary.get('smbPermissionsInfo')) if dictionary.get('smbPermissionsInfo') else None
        stats = cohesity_management_sdk.models.view_stats.ViewStats.from_dictionary(dictionary.get('stats')) if dictionary.get('stats') else None
        storage_policy_override = cohesity_management_sdk.models.storage_policy_override.StoragePolicyOverride.from_dictionary(dictionary.get('storagePolicyOverride')) if dictionary.get('storagePolicyOverride') else None
        subnet_whitelist = None
        if dictionary.get('subnetWhitelist') != None:
            subnet_whitelist = list()
            for structure in dictionary.get('subnetWhitelist'):
                subnet_whitelist.append(cohesity_management_sdk.models.subnet.Subnet.from_dictionary(structure))
        tenant_id = dictionary.get('tenantId')
        view_box_id = dictionary.get('viewBoxId')
        view_box_name = dictionary.get('viewBoxName')
        view_id = dictionary.get('viewId')
        view_lock_enabled = dictionary.get('viewLockEnabled')
        view_protection = cohesity_management_sdk.models.view_protection.ViewProtection.from_dictionary(dictionary.get('viewProtection')) if dictionary.get('viewProtection') else None

        # Return an object of this model
        return cls(access_sids,
                   aliases,
                   all_smb_mount_paths,
                   antivirus_scan_config,
                   basic_mount_path,
                   case_insensitive_names_enabled,
                   create_time_msecs,
                   data_lock_expiry_usecs,
                   description,
                   enable_filer_audit_logging,
                   enable_mixed_mode_permissions,
                   enable_nfs_view_discovery,
                   enable_smb_access_based_enumeration,
                   enable_smb_encryption,
                   enable_smb_view_discovery,
                   enforce_smb_encryption,
                   file_extension_filter,
                   file_lock_config,
                   is_target_for_migrated_data,
                   logical_quota,
                   logical_usage_bytes,
                   name,
                   nfs_mount_path,
                   protocol_access,
                   qos,
                   s_3_access_path,
                   security_mode,
                   smb_mount_path,
                   smb_permissions_info,
                   stats,
                   storage_policy_override,
                   subnet_whitelist,
                   tenant_id,
                   view_box_id,
                   view_box_name,
                   view_id,
                   view_lock_enabled,
                   view_protection)


