# -*- coding: utf-8 -*-
# Copyright 2021 Cohesity Inc.

import cohesity_management_sdk.models.antivirus_scan_config
import cohesity_management_sdk.models.file_extension_filter
import cohesity_management_sdk.models.file_level_data_lock_config
import cohesity_management_sdk.models.quota_policy
import cohesity_management_sdk.models.nfs_squash
import cohesity_management_sdk.models.nfs_root_permissions
import cohesity_management_sdk.models.nis_netgroup
import cohesity_management_sdk.models.qo_s
import cohesity_management_sdk.models.smb_permission
import cohesity_management_sdk.models.smb_permissions_info
import cohesity_management_sdk.models.storage_policy_override
import cohesity_management_sdk.models.subnet

class CloneViewRequest(object):

    """Implementation of the 'CloneViewRequest' model.

    Specifies the settings for cloning an existing View.

    Attributes:
        access_sids (list of string): Array of Security Identifiers (SIDs)
            Specifies the list of security identifiers (SIDs) for the
            restricted Principals who have access to this View.
        antivirus_scan_config (AntivirusScanConfig): Specifies the antivirus
            scan config settings for this View.
        clone_view_name (string): Specifies the name of the new View that is
            cloned from the source View.
        data_lock_expiry_usecs (long|int): DataLock (Write Once Read Many)
            lock expiry epoch time in microseconds. If specified, a view will
            be marked as a DataLock view. If a view is marked as a DataLock
            view, only a Data Security Officer (a user having Data Security
            Privilege) can delete the view until the lock expiry time.
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
        enable_mixed_mode_permissions (bool): If set, mixed mode (NFS and SMB)
            access is enabled for this view. This field is deprecated. Use the
            field SecurityMode. deprecated: true
        enable_nfs_view_discovery (bool): If set, it enables discovery of view
            for NFS.
        enable_offline_caching (bool): Specifies whether to enable offline
            file caching of the view.
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
        enforce_smb_encryption (bool): Specifies the SMB encryption for all
            the sessions for the View. If set, encryption is enforced for all
            the sessions for the View. When enabled all future and existing
            unencrypted sessions are disallowed.
        file_extension_filter (FileExtensionFilter): TODO: type description
            here.
        file_lock_config (FileLevelDataLockConfig): Specifies a config to lock
            files in a view - to protect from malicious or an accidental
            attempt to delete or modify the files in this view.
        is_externally_triggered_backup_target (bool): Specifies whether view
            is for externally triggered backup target.
        is_read_only (bool): Specifies if the view is a read only view. User
            will no longer be able to write to this view if this is set to true.
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
        netgroup_whitelist (list of NisNetgroup): Array of Netgroups.

          Specifies a list of Netgroups that have permissions to access the
          View. (Overrides the Netgroups specified at the global Cohesity
          Cluster level.)
        nfs_all_squash (NfsSquash): TODO: type description here.
        nfs_root_permissions (NfsRootPermissions): Specifies the config of NFS
            root permission of a view file system.
        nfs_root_squash (NfsSquash): TODO: type description here.
        override_global_netgroup_whitelist (bool): Specifies whether view
            level client netgroup whitelist overrides cluster and global
            setting.
        override_global_whitelist (bool): Specifies whether view level client
            subnet whitelist overrides cluster and global setting.
        protocol_access (ProtocolAccessEnum): Specifies the supported
            Protocols for the View. 'kAll' enables protocol access to
            following three views: NFS, SMB and S3. 'kNFSOnly' enables
            protocol access to NFS only. 'kSMBOnly' enables protocol access to
            SMB only. 'kS3Only' enables protocol access to S3 only.
            'kSwiftOnly' enables protocol access to Swift only.
        qos (QoS): Specifies the Quality of Service (QoS) Policy for the
            View.
        security_mode (SecurityModeEnum): Specifies the security mode used for
            this view. Currently we support the following modes: Native,
            Unified and NTFS style. 'kNativeMode' indicates a native security
            mode. 'kUnifiedMode' indicates a unified security mode.
            'kNtfsMode' indicates a NTFS style security mode.
        share_permissions (list of SmbPermission): Specifies a list of share
            level permissions.
        smb_permissions_info (SmbPermissionsInfo): Specifies information about
            SMB permissions.
        source_view_name (string): Specifies the name of the source View that
            will be cloned.
        storage_policy_override (StoragePolicyOverride): Specifies if inline
            deduplication and compression settings inherited from Storage
            Domain (View Box) should be disabled for this View.
        subnet_whitelist (list of Subnet): Array of Subnets.  Specifies a list
            of Subnets with IP addresses that have permissions to access the
            View. (Overrides the Subnets specified at the global Cohesity
            Cluster level.)
        super_user_sids (list of string): Specifies a list of user sids who
            have Superuser access to this view.
        swift_project_domain (string, optional): Specifies the Keystone
            project domain.
        swift_project_name (string, optional): Specifies the Keystone
            project name.
        tenant_id (string): Optional tenant id who has access to this View.
        view_lock_enabled (bool): Specifies whether view lock is enabled. If
            enabled the view cannot be modified or deleted until unlock. By
            default it is disabled.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "access_sids":'accessSids',
        "antivirus_scan_config":'antivirusScanConfig',
        "clone_view_name":'cloneViewName',
        "data_lock_expiry_usecs":'dataLockExpiryUsecs',
        "description":'description',
        "enable_fast_durable_handle":'enableFastDurableHandle',
        "enable_filer_audit_logging":'enableFilerAuditLogging',
        "enable_live_indexing":'enableLiveIndexing',
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
        "is_externally_triggered_backup_target":'isExternallyTriggeredBackupTarget',
        "is_read_only":'isReadOnly',
        "logical_quota":'logicalQuota',
        "netgroup_whitelist":'netgroupWhitelist',
        "nfs_all_squash":'nfsAllSquash',
        "nfs_root_permissions":'nfsRootPermissions',
        "nfs_root_squash":'nfsRootSquash',
        "override_global_netgroup_whitelist":'overrideGlobalNetgroupWhitelist',
        "override_global_whitelist":'overrideGlobalWhitelist',
        "protocol_access":'protocolAccess',
        "qos":'qos',
        "security_mode":'securityMode',
        "share_permissions":'sharePermissions',
        "smb_permissions_info":'smbPermissionsInfo',
        "source_view_name":'sourceViewName',
        "storage_policy_override":'storagePolicyOverride',
        "subnet_whitelist":'subnetWhitelist',
        "super_user_sids":'superUserSids',
        "swift_project_domain":'swiftProjectDomain',
        "swift_project_name":'swiftProjectName',
        "tenant_id":'tenantId',
        "view_lock_enabled":'viewLockEnabled'
    }

    def __init__(self,
                 access_sids=None,
                 antivirus_scan_config=None,
                 clone_view_name=None,
                 data_lock_expiry_usecs=None,
                 description=None,
                 enable_fast_durable_handle=None,
                 enable_filer_audit_logging=None,
                 enable_live_indexing=None,
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
                 is_externally_triggered_backup_target=None,
                 is_read_only=None,
                 logical_quota=None,
                 netgroup_whitelist=None,
                 nfs_all_squash=None,
                 nfs_root_permissions=None,
                 nfs_root_squash=None,
                 override_global_netgroup_whitelist=None,
                 override_global_whitelist=None,
                 protocol_access=None,
                 qos=None,
                 security_mode=None,
                 share_permissions=None,
                 smb_permissions_info=None,
                 source_view_name=None,
                 storage_policy_override=None,
                 subnet_whitelist=None,
                 super_user_sids=None,
                 swift_project_domain=None,
                 swift_project_name=None,
                 tenant_id=None,
                 view_lock_enabled=None):
        """Constructor for the CloneViewRequest class"""

        # Initialize members of the class
        self.access_sids = access_sids
        self.antivirus_scan_config = antivirus_scan_config
        self.clone_view_name = clone_view_name
        self.data_lock_expiry_usecs = data_lock_expiry_usecs
        self.description = description
        self.enable_fast_durable_handle = enable_fast_durable_handle
        self.enable_filer_audit_logging = enable_filer_audit_logging
        self.enable_live_indexing = enable_live_indexing
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
        self.is_externally_triggered_backup_target = is_externally_triggered_backup_target
        self.is_read_only = is_read_only
        self.logical_quota = logical_quota
        self.netgroup_whitelist = netgroup_whitelist
        self.nfs_all_squash = nfs_all_squash
        self.nfs_root_permissions = nfs_root_permissions
        self.nfs_root_squash = nfs_root_squash
        self.override_global_netgroup_whitelist = override_global_netgroup_whitelist
        self.override_global_whitelist = override_global_whitelist
        self.protocol_access = protocol_access
        self.qos = qos
        self.security_mode = security_mode
        self.share_permissions = share_permissions
        self.smb_permissions_info = smb_permissions_info
        self.source_view_name = source_view_name
        self.storage_policy_override = storage_policy_override
        self.subnet_whitelist = subnet_whitelist
        self.super_user_sids = super_user_sids
        self.swift_project_domain = swift_project_domain
        self.swift_project_name = swift_project_name
        self.tenant_id = tenant_id
        self.view_lock_enabled = view_lock_enabled


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
        antivirus_scan_config = cohesity_management_sdk.models.antivirus_scan_config.AntivirusScanConfig.from_dictionary(dictionary.get('antivirusScanConfig')) if dictionary.get('antivirusScanConfig') else None
        clone_view_name = dictionary.get('cloneViewName')
        data_lock_expiry_usecs = dictionary.get('dataLockExpiryUsecs')
        description = dictionary.get('description')
        enable_fast_durable_handle = dictionary.get('enableFastDurableHandle')
        enable_filer_audit_logging = dictionary.get('enableFilerAuditLogging')
        enable_live_indexing = dictionary.get('enableLiveIndexing')
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
        is_externally_triggered_backup_target = dictionary.get('isExternallyTriggeredBackupTarget')
        is_read_only = dictionary.get('isReadOnly')
        logical_quota = cohesity_management_sdk.models.quota_policy.QuotaPolicy.from_dictionary(dictionary.get('logicalQuota')) if dictionary.get('logicalQuota') else None
        netgroup_whitelist = None
        if dictionary.get('netgroupWhitelist') != None:
            netgroup_whitelist = list()
            for structure in dictionary.get('netgroupWhitelist'):
                netgroup_whitelist.append(cohesity_management_sdk.models.nis_netgroup.NisNetgroup.from_dictionary(structure))
        nfs_all_squash = cohesity_management_sdk.models.nfs_squash.NfsSquash.from_dictionary(dictionary.get('nfsAllSquash')) if dictionary.get('nfsAllSquash') else None
        nfs_root_permissions = cohesity_management_sdk.models.nfs_root_permissions.NfsRootPermissions.from_dictionary(dictionary.get('nfsRootPermissions')) if dictionary.get('nfsRootPermissions') else None
        nfs_root_squash = cohesity_management_sdk.models.nfs_squash.NfsSquash.from_dictionary(dictionary.get('nfsRootSquash')) if dictionary.get('nfsRootSquash') else None
        override_global_netgroup_whitelist = dictionary.get('overrideGlobalNetgroupWhitelist')
        override_global_whitelist = dictionary.get('overrideGlobalWhitelist')
        protocol_access = dictionary.get('protocolAccess')
        qos = cohesity_management_sdk.models.qo_s.QoS.from_dictionary(dictionary.get('qos')) if dictionary.get('qos') else None
        security_mode = dictionary.get('securityMode')
        share_permissions = None
        if dictionary.get('sharePermissions') != None:
            share_permissions = list()
            for structure in dictionary.get('sharePermissions'):
                share_permissions.append(cohesity_management_sdk.models.smb_permission.SmbPermission.from_dictionary(structure))
        smb_permissions_info = cohesity_management_sdk.models.smb_permissions_info.SmbPermissionsInfo.from_dictionary(dictionary.get('smbPermissionsInfo')) if dictionary.get('smbPermissionsInfo') else None
        source_view_name = dictionary.get('sourceViewName')
        storage_policy_override = cohesity_management_sdk.models.storage_policy_override.StoragePolicyOverride.from_dictionary(dictionary.get('storagePolicyOverride')) if dictionary.get('storagePolicyOverride') else None
        subnet_whitelist = None
        if dictionary.get('subnetWhitelist') != None:
            subnet_whitelist = list()
            for structure in dictionary.get('subnetWhitelist'):
                subnet_whitelist.append(cohesity_management_sdk.models.subnet.Subnet.from_dictionary(structure))
        super_user_sids = dictionary.get('superUserSids')
        swift_project_domain = dictionary.get('swiftProjectDomain', None)
        swift_project_name = dictionary.get('swiftProjectName', None)
        tenant_id = dictionary.get('tenantId')
        view_lock_enabled = dictionary.get('viewLockEnabled')

        # Return an object of this model
        return cls(access_sids,
                   antivirus_scan_config,
                   clone_view_name,
                   data_lock_expiry_usecs,
                   description,
                   enable_fast_durable_handle,
                   enable_filer_audit_logging,
                   enable_live_indexing,
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
                   is_externally_triggered_backup_target,
                   is_read_only,
                   logical_quota,
                   netgroup_whitelist,
                   nfs_all_squash,
                   nfs_root_permissions,
                   nfs_root_squash,
                   override_global_netgroup_whitelist,
                   override_global_whitelist,
                   protocol_access,
                   qos,
                   security_mode,
                   share_permissions,
                   smb_permissions_info,
                   source_view_name,
                   storage_policy_override,
                   subnet_whitelist,
                   super_user_sids,
                   swift_project_domain,
                   swift_project_name,
                   tenant_id,
                   view_lock_enabled)


