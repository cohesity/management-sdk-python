# ViewProtectionInfoView

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_sids** | **list[str]** | Specifies the list of security identifiers (SIDs) for the restricted Principals who have access to this View. | [optional] 
**aliases** | [**list[ViewAliasInfo]**](ViewAliasInfo.md) | Aliases created for the view. A view alias allows a directory path inside a view to be mounted using the alias name. | [optional] 
**all_smb_mount_paths** | **list[str]** | Specifies the possible paths that can be used to mount this View as a SMB share. If Active Directory has multiple account names; each machine account has its own path. | [optional] 
**basic_mount_path** | **str** | Specifies the NFS mount path of the View (without the hostname information). This path is used to support NFS mounting of the paths specified in the nfsExportPathList on Windows systems. | [optional] 
**case_insensitive_names_enabled** | **bool** | Specifies whether to support case insensitive file/folder names. This parameter can only be set during create and cannot be changed. | [optional] 
**create_time_msecs** | **int** | Specifies the time that the View was created in milliseconds. | [optional] 
**data_lock_expiry_usecs** | **int** | DataLock (Write Once Read Many) lock expiry epoch time in microseconds. If a view is marked as a DataLock view, only a Data Security Officer (a user having Data Security Privilege) can delete the view until the lock expiry time. | [optional] 
**description** | **str** | Specifies an optional text description about the View. | [optional] 
**enable_filer_audit_logging** | **bool** | Specifies if Filer Audit Logging is enabled for this view. | [optional] 
**enable_mixed_mode_permissions** | **bool** | If set, mixed mode (NFS and SMB) access is enabled for this view. | [optional] 
**enable_smb_access_based_enumeration** | **bool** | Specifies if access-based enumeration should be enabled. If &#39;true&#39;, only files and folders that the user has permissions to access are visible on the SMB share for that user. | [optional] 
**enable_smb_view_discovery** | **bool** | If set, it enables discovery of view for SMB. | [optional] 
**file_extension_filter** | [**FileExtensionFilter**](FileExtensionFilter.md) | Optional filtering criteria that should be satisfied by all the files created in this view. It does not affect existing files. | [optional] 
**logical_quota** | [**CloneTaskRequestCloneViewParametersLogicalQuota**](CloneTaskRequestCloneViewParametersLogicalQuota.md) |  | [optional] 
**logical_usage_bytes** | **int** | LogicalUsageBytes is the logical usage in bytes for the view. | [optional] 
**name** | **str** | Specifies the name of the View. | [optional] 
**nfs_mount_path** | **str** | Specifies the path for mounting this View as an NFS share. | [optional] 
**protocol_access** | **str** | Specifies the supported Protocols for the View. | [optional] 
**qos** | [**QoS**](QoS.md) | Specifies the Quality of Service (QoS) Policy for the View. | [optional] 
**smb_mount_path** | **str** | Specifies the main path for mounting this View as an SMB share. | [optional] 
**smb_permissions_info** | [**SmbPermissionsInfo**](SmbPermissionsInfo.md) | Specifies the SMB permissions for the View. | [optional] 
**storage_policy_override** | [**StoragePolicyOverride**](StoragePolicyOverride.md) | Specifies if inline deduplication and compression settings inherited from the Storage Domain (View Box) should be disabled for this View. | [optional] 
**subnet_whitelist** | [**list[Subnet]**](Subnet.md) | Specifies a list of Subnets with IP addresses that have permissions to access the View. (Overrides the Subnets specified at the global Cohesity Cluster level.) | [optional] 
**view_box_id** | **int** | Specifies the id of the Storage Domain (View Box) where the View is stored. | [optional] 
**view_box_name** | **str** | Specifies the name of the Storage Domain (View Box) where the View is stored. | [optional] 
**view_id** | **int** | Specifies an id of the View assigned by the Cohesity Cluster. | [optional] 
**view_protection** | [**ViewProtection**](ViewProtection.md) | Specifies information about the Protection Jobs protecting this View. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


