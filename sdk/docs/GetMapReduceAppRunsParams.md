# GetMapReduceAppRunsParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **int** | ApplicationId is the Id of the map reduce application. | [optional] 
**app_instance_id** | **int** | ApplicationInstanceId is the Id of the map reduce application instance. | [optional] 
**include_details** | **bool** | If this flag is true, then send details of instance, else send only RunInfo. | [optional] 
**last_num_instances** | **int** | Give last N instance of an app based on end time. | [optional] 
**max_run_end_time_in_secs** | **int** | MaxRunEndTimestampInSecs specifies the maximum job run end timestamp in seconds. App run instances with end time less than equal to MaxRunEndTimestampInSecs will be selected. Default is LONG_MAX (inf). | [optional] 
**max_run_start_time_in_secs** | **int** | MaxRunStartTimestampInSecs specifies the maximum job run start timestamp in seconds. App run instances with start time less than equal to MaxRunStartTimestampInSecs will be selected. Default is LONG_MAX (inf). | [optional] 
**min_run_end_time_in_secs** | **int** | MinRunEndTimestampInSecs specifies the minimum job run end timestamp in seconds. App run instances with end time greater than equal to MinRunEndTimestampInSecs will be selected. Default is 0, i.e. beginning of time. | [optional] 
**min_run_start_time_in_secs** | **int** | MinRunStartTimestampInSecs specifies the minimum job run start timestamp in seconds. App run instances with start time greater than equal to MinRunStartTimestampInSecs will be selected. Default is 0, i.e. beginning of time. | [optional] 
**page_size** | **int** | Number of results to be displayed on a page. | [optional] 
**run_status** | **str** | Filter instances based on the map reduce application run status. | [optional] 
**start_offset** | **int** | Start offset for pagination from where result needs to be fetched. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


