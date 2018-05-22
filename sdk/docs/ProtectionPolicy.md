# ProtectionPolicy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blackout_periods** | [**list[BlackoutPeriod]**](BlackoutPeriod.md) | If specified, this field defines black periods when new Job Runs are not started. If a Job Run has been scheduled but not yet executed and the blackout period starts, the behavior depends on the policy field AbortInBlackoutPeriod. | [optional] 
**cloud_deploy_policies** | [**list[SnapshotCloudCopyPolicy]**](SnapshotCloudCopyPolicy.md) | Specifies settings for copying Snapshots to Cloud. CloudDeploy target where backup snapshots may be converted and stored. It also defines the retention of copied Snapshots on the Cloud. | [optional] 
**days_to_keep** | **int** | Specifies how many days to retain Snapshots on the Cohesity Cluster. | [optional] 
**days_to_keep_log** | **int** | Specifies the number of days to retain log run if Log Schedule exists. | [optional] 
**days_to_keep_system** | **int** | Specifies the number of days to retain system backups made for bare metal recovery. This field is applicable if systemSchedulingPolicy is specified. | [optional] 
**description** | **str** | Description of the Protection Policy. | [optional] 
**extended_retention_policies** | [**list[ExtendedRetentionPolicy]**](ExtendedRetentionPolicy.md) | Specifies additional retention policies that should be applied to the backup snapshots. A backup snapshot will be retained up to a time that is the maximum of all retention policies that are applicable to it. | [optional] 
**full_scheduling_policy** | [**ProtectionPolicyFullSchedulingPolicy**](ProtectionPolicyFullSchedulingPolicy.md) |  | [optional] 
**id** | **str** | Specifies a unique Policy id assigned by the Cohesity Cluster. | [optional] 
**incremental_scheduling_policy** | [**ProtectionPolicyIncrementalSchedulingPolicy**](ProtectionPolicyIncrementalSchedulingPolicy.md) |  | [optional] 
**last_modified_time_msecs** | **int** | Specifies the epoch time (in milliseconds) when the Protection Policy was last modified. | [optional] 
**log_scheduling_policy** | [**SchedulingPolicy**](SchedulingPolicy.md) | Specifies the Log backup schedule of a Protection Job and how long log files captured by this schedule are retained on the Cohesity Cluster. | [optional] 
**name** | **str** | Specifies the name of the Protection Policy. | [optional] 
**retries** | **int** | Specifies the number of times to retry capturing Snapshots before the Job Run fails. | [optional] 
**retry_interval_mins** | **int** | Specifies the number of minutes before retrying a failed Protection Job. | [optional] 
**skip_interval_mins** | **int** | Specifies the period of time before skipping the execution of new Job Runs if an existing queued Job Run of the same Protection Job has not started. For example if this field is set to 30 minutes and a Job Run is scheduled to start at 5:00 AM every day but does not start due to conflicts (such as too many Jobs are running). If the new Job Run does not start by 5:30AM, the Cohesity Cluster will skip the new Job Run. If the original Job Run completes before 5:30AM the next day, a new Job Run is created and starts executing. This field is optional. | [optional] 
**snapshot_archival_copy_policies** | [**list[SnapshotArchivalCopyPolicy]**](SnapshotArchivalCopyPolicy.md) | Specifies settings for copying Snapshots to  Archival External Targets (such as AWS or Tape). It also defines the retention of copied Snapshots on an External Targets such as AWS and Tape. | [optional] 
**snapshot_replication_copy_policies** | [**list[SnapshotReplicationCopyPolicy]**](SnapshotReplicationCopyPolicy.md) | Specifies settings for copying Snapshots to Remote Clusters. It also defines the retention of copied Snapshots on a Remote Cluster. | [optional] 
**system_scheduling_policy** | [**SchedulingPolicy**](SchedulingPolicy.md) | Specifies the system backup schedule for agents running on servers to run low frequency backup jobs. Images created as part of the backup can be used to perform a \&quot;bare metal\&quot; recovery. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


