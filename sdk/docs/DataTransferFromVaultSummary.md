# DataTransferFromVaultSummary

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_transfer_per_task** | [**list[DataTransferFromVaultPerTask]**](DataTransferFromVaultPerTask.md) | Specifies the transfer of data from this Vault to this Cohesity Cluster for each clone or recover task. | [optional] 
**num_logical_bytes_transferred** | **int** | Specifies the total number of logical bytes that have been transferred from this Vault (External Target) to this Cohesity Cluster. The logical size is when the data is fully hydrated or expanded. | [optional] 
**num_physical_bytes_transferred** | **int** | Specifies the total number of physical bytes that have been transferred from this Vault (External Target) to the Cohesity Cluster. | [optional] 
**num_tasks** | **int** | Specifies the number of recover or clone tasks that have transferred data from this Vault (External Target) to this Cohesity Cluster. | [optional] 
**physical_data_transferred_bytes_during_time_range** | **list[int]** | Specifies the physical data transferred from this Vault to the Cohesity Cluster during the time period specified using the startTimeMsecs and endTimeMsecs parameters. For each day in the time period, an array element is returned, for example if 7 days are specified, 7 array elements are returned. | [optional] 
**vault_name** | **str** | Specifies the name of the Vault (External Target). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


