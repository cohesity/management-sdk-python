# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.antivirus_scan_config
import cohesity_management_sdk.models.file_extension_filter
import cohesity_management_sdk.models.file_level_data_lock_config
import cohesity_management_sdk.models.quota_policy
import cohesity_management_sdk.models.qo_s
import cohesity_management_sdk.models.smb_permissions_info
import cohesity_management_sdk.models.storage_policy_override
import cohesity_management_sdk.models.subnet

class CreateViewRequest(object):

    """Implementation of the 'CreateViewRequest' model.

    Specifies the information required for creating a new View.

    Attributes:
        access_sids (list of string): Array of Security Identifiers (SIDs)
            Specifies the list of security identifiers (SIDs) for the
            restricted Principals who have access to this View.
        antivirus_scan_config (AntivirusScanConfig): Specifies the antivirus
            scan config settings for this View.
        case_insensitive_names_enabled (bool): Specifies whether to support
            case insensitive file/folder names. This parameter can only be set
            during create and cannot be changed.
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
        name (string): Specifies the name of the new View to create.
        protocol_access (ProtocolAccessEnum): Specifies the supported
            Protocols for the View. 'kAll' enables protocol access to all
            three views: NFS, SMB and S3. 'kNFSOnly' enables protocol access
            to NFS only. 'kSMBOnly' enables protocol access to SMB only.
            'kS3Only' enables protocol access to S3 only.
        qos (QoS): Specifies the Quality of Service (QoS) Policy for the
            View.
        security_mode (SecurityModeEnum): Specifies the security mode used for
            this view. Currently we support the following modes: Native,
            Unified and NTFS style. 'kNativeMode' indicates a native security
            mode. 'kUnifiedMode' indicates a unified security mode.
            'kNtfsMode' indicates a NTFS style security mode.
        smb_permissions_info (SmbPermissionsInfo): Specifies information about
            SMB permissions.
        storage_policy_override (StoragePolicyOverride): Specifies if inline
            deduplication and compression settings inherited from Storage
            Domain (View Box) should be disabled for this View.
        subnet_whitelist (list of Subnet): Array of Subnets.  Specifies a list
            of Subnets with IP addresses that have permissions to access the
            View. (Overrides the Subnets specified at the global Cohesity
            Cluster level.)
        tenant_id (string): Optional tenant id who has access to this View.
        view_box_id (long|int): Specifies the id of the Storage Domain (View
            Box) where the View will be created.
        view_lock_enabled (bool): Specifies whether view lock is enabled. If
            enabled the view cannot be modified or deleted until unlock. By
            default it is disabled.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "view_box_id":'viewBoxId',
        "access_sids":'accessSids',
        "antivirus_scan_config":'antivirusScanConfig',
        "case_insensitive_names_enabled":'caseInsensitiveNamesEnabled',
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
        "logical_quota":'logicalQuota',
        "protocol_access":'protocolAccess',
        "qos":'qos',
        "security_mode":'securityMode',
        "smb_permissions_info":'smbPermissionsInfo',
        "storage_policy_override":'storagePolicyOverride',
        "subnet_whitelist":'subnetWhitelist',
        "tenant_id":'tenantId',
        "view_lock_enabled":'viewLockEnabled'
    }

    def __init__(self,
                 name=None,
                 view_box_id=None,
                 access_sids=None,
                 antivirus_scan_config=None,
                 case_insensitive_names_enabled=None,
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
                 logical_quota=None,
                 protocol_access=None,
                 qos=None,
                 security_mode=None,
                 smb_permissions_info=None,
                 storage_policy_override=None,
                 subnet_whitelist=None,
                 tenant_id=None,
                 view_lock_enabled=None):
        """Constructor for the CreateViewRequest class"""

        # Initialize members of the class
        self.access_sids = access_sids
        self.antivirus_scan_config = antivirus_scan_config
        self.case_insensitive_names_enabled = case_insensitive_names_enabled
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
        self.logical_quota = logical_quota
        self.name = name
        self.protocol_access = protocol_access
        self.qos = qos
        self.security_mode = security_mode
        self.smb_permissions_info = smb_permissions_info
        self.storage_policy_override = storage_policy_override
        self.subnet_whitelist = subnet_whitelist
        self.tenant_id = tenant_id
        self.view_box_id = view_box_id
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
        name = dictionary.get('name')
        view_box_id = dictionary.get('viewBoxId')
        access_sids = dictionary.get('accessSids')
        antivirus_scan_config = cohesity_management_sdk.models.antivirus_scan_config.AntivirusScanConfig.from_dictionary(dictionary.get('antivirusScanConfig')) if dictionary.get('antivirusScanConfig') else None
        case_insensitive_names_enabled = dictionary.get('caseInsensitiveNamesEnabled')
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
        logical_quota = cohesity_management_sdk.models.quota_policy.QuotaPolicy.from_dictionary(dictionary.get('logicalQuota')) if dictionary.get('logicalQuota') else None
        protocol_access = dictionary.get('protocolAccess')
        qos = cohesity_management_sdk.models.qo_s.QoS.from_dictionary(dictionary.get('qos')) if dictionary.get('qos') else None
        security_mode = dictionary.get('securityMode')
        smb_permissions_info = cohesity_management_sdk.models.smb_permissions_info.SmbPermissionsInfo.from_dictionary(dictionary.get('smbPermissionsInfo')) if dictionary.get('smbPermissionsInfo') else None
        storage_policy_override = cohesity_management_sdk.models.storage_policy_override.StoragePolicyOverride.from_dictionary(dictionary.get('storagePolicyOverride')) if dictionary.get('storagePolicyOverride') else None
        subnet_whitelist = None
        if dictionary.get('subnetWhitelist') != None:
            subnet_whitelist = list()
            for structure in dictionary.get('subnetWhitelist'):
                subnet_whitelist.append(cohesity_management_sdk.models.subnet.Subnet.from_dictionary(structure))
        tenant_id = dictionary.get('tenantId')
        view_lock_enabled = dictionary.get('viewLockEnabled')

        # Return an object of this model
        return cls(name,
                   view_box_id,
                   access_sids,
                   antivirus_scan_config,
                   case_insensitive_names_enabled,
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
                   logical_quota,
                   protocol_access,
                   qos,
                   security_mode,
                   smb_permissions_info,
                   storage_policy_override,
                   subnet_whitelist,
                   tenant_id,
                   view_lock_enabled)


