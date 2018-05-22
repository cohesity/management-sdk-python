# UserDeleteParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Specifies the domain associated with the users to delete. Only users associated with the same domain can be deleted by a single request. If no domain is specified, the specified users are deleted from the LOCAL domain on the Cohesity Cluster. If a non-LOCAL domain is specified, the specified users are deleted on the Cohesity Cluster. However, the referenced user principals on the Active Directory are not deleted. | [optional] 
**users** | **list[str]** | Specifies the list of users to delete on Cohesity Cluster. Only users from the same domain can be deleted by a single request. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


