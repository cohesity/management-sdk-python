# IdMappingInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fallback_user_id_mapping_info** | [**UserIdMapping**](UserIdMapping.md) | Specifies the fallback id mapping info which is used when an ID mapping for a user is not found via the above IdMappingInfo. Only supported for two types of fallback mapping types - &#39;kRid&#39; and &#39;kFixed&#39;. | [optional] 
**unix_root_sid** | **str** | Specifies the SID of the Active Directory domain user to be mapped to Unix root user. | [optional] 
**user_id_mapping_info** | [**UserIdMapping**](UserIdMapping.md) | Specifies the information about how the Unix and Windows users are mapped for this domain. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


