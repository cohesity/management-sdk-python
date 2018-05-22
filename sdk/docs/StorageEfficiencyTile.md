# StorageEfficiencyTile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_in_bytes** | **int** | Data brought into the cluster. This is the usage before data reduction if we ignore the zeroes and effects of cloning. | [optional] 
**data_in_deduped_bytes** | **int** | Morphed Usage before data is replicated to other nodes as per RF or Erasure Coding policy. | [optional] 
**data_reduction** | **int** | Data Reduction is the ratio of DataInBytes to DataInDedupBytes. | [optional] 
**last_week_data_in_bytes** | **list[int]** |  | [optional] 
**last_week_data_in_deduped_bytes** | **list[int]** | Morphed usage before data is replicated in last 7 days in descening order of time. | [optional] 
**last_week_data_reduction** | **list[int]** |  | [optional] 
**last_week_logical_used_bytes** | **list[int]** |  | [optional] 
**last_week_physical_used_bytes** | **list[int]** |  | [optional] 
**last_week_storage_efficiency** | **list[int]** |  | [optional] 
**logical_used_bytes** | **int** | Logical Data used on the cluster. | [optional] 
**storage_efficiency** | **int** | Storage Efficiency is the ratio of LogicalUsedBytes / RawUsedBytes. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


