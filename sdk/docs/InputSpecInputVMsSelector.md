# InputSpecInputVMsSelector

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_time_filter** | [**InputSpecFileTimeFilter**](InputSpecFileTimeFilter.md) | Time filter for file&#39;s last change time. | [optional] 
**filename_glob** | **list[str]** | After VMDKs are selected as above, the files within them can be selected by using these predicates. | [optional] 
**job_ids** | **list[int]** |  | [optional] 
**max_snapshot_timestamp** | **int** | Exclusive end of snapshot_timestamp range. If missing, inf will be used as the timestamp range. | [optional] 
**min_snapshot_timestamp** | **int** | Inclusive. If missing, 0 will the default lower end of timestamp range | [optional] 
**partition_ids** | **list[int]** |  | [optional] 
**process_latest_only** | **bool** | Boolean flag to indicate if only latest snapshot of each object should be processed. | [optional] 
**root_dir** | **str** | Within each volume, traversal will be rooted at this directory. A typical value here might be /home | [optional] 
**source_entity_ids** | **list[int]** |  | [optional] 
**view_box_ids** | **list[int]** |  | [optional] 
**view_names** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


