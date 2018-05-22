# RemoteRestoreSnapshotStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archive_task_uid** | [**RemoteRestoreSnapshotStatusArchiveTaskUid**](RemoteRestoreSnapshotStatusArchiveTaskUid.md) |  | [optional] 
**error** | **str** | Specifies the error message if the indexing task fails. | [optional] 
**expiry_time_usecs** | **int** | Specifies the time when the Snapshot expires on the remote Vault. This field is recorded as a Unix epoch Timestamp (in microseconds). | [optional] 
**job_run_id** | **int** | Specifies the id of the Job Run that originally captured the Snapshot. | [optional] 
**progress_monitor_task** | **str** | Specifies the path to the progress monitor task that tracks the progress of building the index. | [optional] 
**snapshot_task_status** | **str** | Specifies the status of the indexing task. &#39;kJobRunning&#39; indicates that the Job/task is currently running. &#39;kJobFinished&#39; indicates that the Job/task completed and finished. &#39;kJobFailed&#39; indicates that the Job/task failed and did not complete. &#39;kJobCanceled&#39; indicates that the Job/task was canceled. &#39;kJobPaused&#39; indicates the Job/task is paused. | [optional] 
**snapshot_task_uid** | [**RemoteRestoreSnapshotStatusSnapshotTaskUid**](RemoteRestoreSnapshotStatusSnapshotTaskUid.md) |  | [optional] 
**snapshot_time_usecs** | **int** | Specify the time the Snapshot was captured. This time is recorded as a Unix epoch Timestamp (in microseconds). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


