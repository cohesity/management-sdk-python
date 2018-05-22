# IndexAndSnapshots

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archive_task_uid** | [**IndexAndSnapshotsArchiveTaskUid**](IndexAndSnapshotsArchiveTaskUid.md) |  | [optional] 
**end_time_usecs** | **int** | Specifies the end time as a Unix epoch Timestamp (in microseconds). If set, only index and Snapshots for Protection Job Runs that started before the specified end time are restored. | [optional] 
**remote_protection_job_uid** | [**IndexAndSnapshotsRemoteProtectionJobUid**](IndexAndSnapshotsRemoteProtectionJobUid.md) |  | [optional] 
**start_time_usecs** | **int** | Specifies the start time as a Unix epoch Timestamp (in microseconds). If set, only the index and Snapshots for Protection Job Runs that started after the specified start time are restored. | [optional] 
**view_box_id** | **int** | Specifies the id of the local Storage Domain (View Box) where the index and the Snapshot will be restored to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


