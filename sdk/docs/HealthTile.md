# HealthTile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity_bytes** | **int** | Raw Cluster Capacity in Bytes. This is not usable capacity and does not take replication factor into account. | [optional] 
**cluster_cloud_usage_bytes** | **int** | Usage in Bytes on the cloud. | [optional] 
**last_day_alerts** | [**list[Alert]**](Alert.md) |  | [optional] 
**last_day_num_criticals** | **int** | Number of Critical Alerts. | [optional] 
**last_day_num_warnings** | **int** | Number of Warning Alerts. | [optional] 
**num_nodes** | **int** | Number of nodes in the cluster. | [optional] 
**num_nodes_with_issues** | **int** | Number of nodes in the cluster that are unhealthy. | [optional] 
**percent_full** | **float** | Percent the cluster is full. | [optional] 
**raw_used_bytes** | **int** | Raw Bytes used in the cluster. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


