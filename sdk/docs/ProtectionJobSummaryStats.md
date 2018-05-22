# ProtectionJobSummaryStats

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average_run_time_usecs** | **int** | Specifies the average run time of all successful Protection Runs. It is specified as a Unix epoch Timestamp (in microseconds). | [optional] 
**fastest_run_time_usecs** | **int** | Specifies the time taken for a fastest successful Protection Run so far. It is specified as a Unix epoch Timestamp (in microseconds). | [optional] 
**num_canceled_runs** | **int** | Specifies the number of runs that were canceled. | [optional] 
**num_failed_runs** | **int** | Specifies the number of runs that failed to finish. | [optional] 
**num_sla_violations** | **int** | Specifies the number of runs having SLA violations. | [optional] 
**num_successful_runs** | **int** | Specifies the number of runs that finished successfully. | [optional] 
**slowest_run_time_usecs** | **int** | Specifies the time taken for a slowest successful Protection Run so far. It is specified as a Unix epoch Timestamp (in microseconds). | [optional] 
**total_bytes_read_from_source** | **int** | Specifies the total amount of data read from the source (so far). | [optional] 
**total_logical_backup_size_bytes** | **int** | Specifies the size of the source object (such as a VM) protected by this task on the primary storage after the snapshot is taken. The logical size of the data on the source if the data is fully hydrated or expanded and not reduced by change-block tracking, compression and deduplication. | [optional] 
**total_physical_backup_size_bytes** | **int** | Specifies the total amount of physical space used on the Cohesity Cluster to store the protected object after being reduced by change-block tracking, compression and deduplication. For example, if the logical backup size is 1GB, but only 1MB was used on the Cohesity Cluster to store it, this field be equal to 1MB. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


