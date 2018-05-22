# UpdateProtectionJobRun

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**copy_run_targets** | [**list[RunJobSnapshotTarget]**](RunJobSnapshotTarget.md) | Specifies the retention for archival, replication or extended local retention. | [optional] 
**expiry_time_usecs** | **int** | Specifies a new expiration time as a Unix epoch Timestamp (in microseconds). This expiration time defines the retention period for the snapshot. After an expiration time for a Job Run is reached, the Job Run and the snapshot captured by this Job Run are deleted. If 0 is specified, the Job Run and the snapshot are immediately deleted. | [optional] 
**job_uid** | [**UpdateProtectionJobRunJobUid**](UpdateProtectionJobRunJobUid.md) |  | [optional] 
**run_start_time_usecs** | **int** | Specifies the start time of the Job Run to update. The start time is specified as a Unix epoch Timestamp (in microseconds). This uniquely identifies a snapshot. This parameter is required. | [optional] 
**source_ids** | **list[int]** | Ids of the Protection Sources. If this is specified, retention time will only be updated for the sources specified. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


