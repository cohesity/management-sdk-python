# ActiveDirectoryEntry

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_name** | **str** | Specifies the fully qualified domain name (FQDN) of an Active Directory. | [optional] 
**fallback_user_id_mapping_info** | [**UserIdMapping**](UserIdMapping.md) | Specifies the fallback id mapping info which is used when an ID mapping for a user is not found via the above IdMappingInfo. Only supported for two types of fallback mapping types - &#39;kRid&#39; and &#39;kFixed&#39;. | [optional] 
**machine_accounts** | **list[str]** | Specifies an array of computer names used to identify the Cohesity Cluster on the domain. | [optional] 
**ou_name** | **str** | Specifies an optional Organizational Unit name. | [optional] 
**password** | **str** | Specifies the password for the specified userName. | [optional] 
**trusted_domains** | **list[str]** |  | [optional] 
**unix_root_sid** | **str** | Specifies the SID of the Active Directory domain user to be mapped to Unix root user. | [optional] 
**user_id_mapping_info** | [**UserIdMapping**](UserIdMapping.md) | Specifies the information about how the Unix and Windows users are mapped for this domain. | [optional] 
**user_name** | **str** | Specifies a userName that has administrative privileges in the domain. | [optional] 
**workgroup** | **str** | Specifies an optional Workgroup name. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


