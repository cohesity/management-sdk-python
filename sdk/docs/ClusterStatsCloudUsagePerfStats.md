# ClusterStatsCloudUsagePerfStats

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_in_bytes** | **int** | Data brought into the cluster. This is the usage before data reduction if we ignore the zeroes and effects of cloning. | [optional] 
**data_in_bytes_after_reduction** | **int** | Morphed Usage before data is replicated to other nodes as per RF or Erasure Coding policy. | [optional] 
**min_usable_physical_capacity_bytes** | **int** | Specifies the minimum usable capacity available after erasure coding or RF. This will only be populated for cluster. If a cluster has multiple Domains (View Boxes) with different RF or erasure coding, this metric will be computed using the scheme that will provide least saving. | [optional] 
**num_bytes_read** | **int** | Provides the total number of bytes read in the last 30 seconds. | [optional] 
**num_bytes_written** | **int** | Provides the total number of bytes written in the last 30 second. | [optional] 
**physical_capacity_bytes** | **int** | Provides the total physical capacity in bytes as computed by the Cohesity Cluster. | [optional] 
**read_ios** | **int** | Provides the number of Read IOs that occurred in the last 30 seconds. | [optional] 
**read_latency_msecs** | **float** | Provides the Read latency in milliseconds for the Read IOs that occurred during the last 30 seconds. | [optional] 
**system_capacity_bytes** | **int** | Provides the total available capacity as computed by the Linux &#39;statfs&#39; command. | [optional] 
**system_usage_bytes** | **int** | Provides the usage of bytes, as computed by the Linux &#39;statfs&#39; command, after the size of the data is reduced by change-block tracking, compression and deduplication. | [optional] 
**total_physical_raw_usage_bytes** | **int** | Provides the usage of bytes, as computed by the Cohesity Cluster, before the size of the data is reduced by change-block tracking, compression and deduplication. | [optional] 
**total_physical_usage_bytes** | **int** | Provides the total capacity, as computed by the Cohesity Cluster, after the size of the data has been reduced by change-block tracking, compression and deduplication. | [optional] 
**write_ios** | **int** | Provides the number of Write IOs that occurred in the last 30 seconds. | [optional] 
**write_latency_msecs** | **float** | Provides the Write latency in milliseconds for the Write IOs that occurred during the last 30 seconds. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


