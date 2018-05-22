# RemoteProtectionJobRunInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archive_task_uid** | [**RemoteProtectionJobRunInstanceArchiveTaskUid**](RemoteProtectionJobRunInstanceArchiveTaskUid.md) |  | [optional] 
**archive_version** | **int** | Specifies the version of the archive. | [optional] 
**expiry_time_usecs** | **int** | Specifies the time when the archive expires. This time is recorded as a Unix epoch Timestamp (in microseconds). | [optional] 
**index_size_bytes** | **int** | Specifies the size of the index for the archive. | [optional] 
**job_run_id** | **int** | Specifies the instance id of the Job Run task capturing the Snapshot. | [optional] 
**metadata_complete** | **bool** | Specifies whether a full set of metadata is available now. | [optional] 
**snapshot_time_usecs** | **int** | Specify the time the Snapshot was captured as a Unix epoch Timestamp (in microseconds). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


