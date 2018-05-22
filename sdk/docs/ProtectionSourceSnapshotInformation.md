# ProtectionSourceSnapshotInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**copy_tasks** | [**list[SnapshotCopyTask]**](SnapshotCopyTask.md) | Specifies a list of copy tasks (such as replication and archival tasks). | [optional] 
**job_id** | **int** | Specifies the id of the Protection Job. | [optional] 
**job_name** | **str** | Specifies the name of the Protection Job. | [optional] 
**job_run_id** | **int** | Specifies the id of the Job Run. | [optional] 
**last_run_end_time_usecs** | **int** | Specifies the end time of the last Job Run. The time is specified in Unix epoch Timestamp (in microseconds). | [optional] 
**last_run_start_time_usecs** | **int** | Specifies the start time of the last Job Run. The time is specified in Unix epoch Timestamp (in microseconds). | [optional] 
**message** | **str** | Specifies warning or error information when the Job Run is not successful. | [optional] 
**num_bytes_read** | **int** | Specifies the total number of bytes read. | [optional] 
**num_logical_bytes_protected** | **int** | Specifies the total number of logical bytes that are protected. The logical size is when the data is fully hydrated or expanded. | [optional] 
**pagination_cookie** | **int** | Specifies an opaque string to pass into the next request to get the next set of Snapshots for pagination purposes. If null, this is the last set of Snapshots or the number of Snapshots returned is equal to or less than the specified pageCount. | [optional] 
**run_status** | **str** | Specifies the type of the Job Run. &#39;kSuccess&#39; indicates that the Job Run was successful. &#39;kRunning&#39; indicates that the Job Run is currently running. &#39;kWarning&#39; indicates that the Job Run was successful but warnings were issued. &#39;kCancelled&#39; indicates that the Job Run was canceled. &#39;kError&#39; indicates the Job Run encountered an error and did not run to completion. | [optional] 
**run_type** | **str** | Specifies the status of the Job Run. &#39;kRegular&#39; indicates an incremental (CBT) backup. Incremental backups utilizing CBT (if supported) are captured of the target protection objects. The first run of a kRegular schedule captures all the blocks. &#39;kFull&#39; indicates a full (no CBT) backup. A complete backup (all blocks) of the target protection objects are always captured and Change Block Tracking (CBT) is not utilized. &#39;kLog&#39; indicates a Database Log backup. Capture the database transaction logs to allow rolling back to a specific point in time. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


