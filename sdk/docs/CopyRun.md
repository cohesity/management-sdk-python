# CopyRun

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**copy_snapshot_tasks** | [**list[CopySnapshotTaskStatus]**](CopySnapshotTaskStatus.md) | Specifies the status information of each task that copies the snapshot taken for a Protection Source. | [optional] 
**error** | **str** | Specifies if an error occurred (if any) while running this task. This field is populated when the status is equal to &#39;kFailure&#39;. | [optional] 
**expiry_time_usecs** | **int** | Specifies expiry time of the copies of the snapshots in this Protection Run. | [optional] 
**run_start_time_usecs** | **int** | Specifies start time of the copy run. | [optional] 
**stats** | [**CopyRunStats**](CopyRunStats.md) | Specifies the aggregated information of all the copy tasks. | [optional] 
**status** | **str** | Specifies the aggregated status of copy tasks such as &#39;kRunning&#39;, &#39;kSuccess&#39;, &#39;kFailure&#39; etc. &#39;kAccepted&#39; indicates the task is queued to run but not yet running. &#39;kRunning&#39; indicates the task is running. &#39;kCanceling&#39; indicates a request to cancel the task has occurred but the task is not yet canceled. &#39;kCanceled&#39; indicates the task has been canceled. &#39;kSuccess&#39; indicates the task was successful. &#39;kFailure&#39; indicates the task failed. | [optional] 
**target** | [**SnapshotTarget**](SnapshotTarget.md) | Specifies the target of the copy task such as an external target or a Remote Cohesity Cluster. | [optional] 
**task_uid** | [**CopyRunTaskUid**](CopyRunTaskUid.md) |  | [optional] 
**user_action_message** | **str** | Specifies a message to the user if any manual intervention is needed to make forward progress for the archival task. This message is mainly relevant for tape based archival tasks where a backup admin might be asked to load a new media when the tape library does not have any more media to use. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


