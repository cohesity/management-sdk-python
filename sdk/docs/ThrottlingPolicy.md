# ThrottlingPolicy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enforce_max_streams** | **bool** | Specifies whether datastore streams are configured for all datastores that are part of the registered entity. If set to true, number of streams from Cohesity cluster to the registered entity will be limited to the value set for maxConcurrentStreams. If not set or set to false, there is no max limit for the number of concurrent streams. | [optional] 
**is_enabled** | **bool** | Indicates whether read operations to the datastores, which are part of the registered Protection Source, are throttled. | [optional] 
**latency_thresholds** | [**LatencyThresholds**](LatencyThresholds.md) | Specifies the thresholds that should be applied to all datastores that are part of the registered Object. | [optional] 
**max_concurrent_streams** | **int** | Specifies the limit on the number of streams Cohesity cluster will make concurrently to the datastores of the registered entity. This limit is enforced only when the flag enforceMaxStreams is set to true. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


