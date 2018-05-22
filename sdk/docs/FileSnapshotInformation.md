# FileSnapshotInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_archival_copy** | **bool** | If true, this snapshot is located on an archival target (such as a tape or AWS). | [optional] 
**has_local_copy** | **bool** | If true, this snapshot is located on a local Cohesity Cluster. | [optional] 
**has_remote_copy** | **bool** | If true, this snapshot is located on a Remote Cohesity Cluster. | [optional] 
**modified_time_usecs** | **int** | Specifies the time when the file or folder was last modified. Specified as a Unix epoch Timestamp (in microseconds). | [optional] 
**size_bytes** | **int** | Specifies the size of the file or folder in bytes. | [optional] 
**snapshot** | [**SnapshotAttempt**](SnapshotAttempt.md) | Specifies the snapshot that contains the specified file or folder. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


