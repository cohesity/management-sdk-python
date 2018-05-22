# MapReduceInstanceRunInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_time** | **int** | Time when map redcue job completed. | [optional] 
**error_message** | **str** | If this run failed, then error message for failure. | [optional] 
**execution_start_time_usecs** | **int** | Time (in usecs) when job was picked up for execution. | [optional] 
**files_processed** | **int** | Number of files processed in this run. | [optional] 
**map_done_time_usecs** | **int** | Time (in usecs) when map tasks were done. | [optional] 
**map_input_bytes** | **int** | Total size of data processed by this run in bytes. | [optional] 
**mappers_spawned** | **int** | Number of mappers spawned till now. | [optional] 
**num_map_outputs** | **int** | Number of outputs from mappers. | [optional] 
**num_reduce_outputs** | **int** | Number of outputs from reducers. | [optional] 
**percentage_completion** | **float** | Percentage completion of this run so far. | [optional] 
**percentage_mapper_completion** | **float** | Percentage of mapper phase completed. | [optional] 
**percentage_reducer_completion** | **float** | Percentage of reducer phase completed. | [optional] 
**reducers_spawned** | **int** | Number of reducers spawned till now. | [optional] 
**remaining_time_mins** | **int** | Expected remaining time in minutes for completion of this run. | [optional] 
**start_time** | **int** | Time when map reduce job was started by user. | [optional] 
**status** | **int** | Status of this run. | [optional] 
**total_num_mappers** | **int** | Total number of mappers to be spawned. | [optional] 
**total_num_reducers** | **int** | Total number of reducers to be spawned. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


