# ViewProtection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inactive** | **bool** | Specifies if this View is an inactive View that was created on this Remote Cluster to store the Snapshots created by replication. This inactive View cannot be NFS or SMB mounted. | [optional] 
**magneto_entity_id** | **int** | Specifies the id of the Protection Source that is using this View. | [optional] 
**protection_jobs** | [**list[ProtectionJobInfo]**](ProtectionJobInfo.md) | Specifies the Protection Jobs that are protecting the View. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


