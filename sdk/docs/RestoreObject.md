# RestoreObject

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archival_target** | [**RestoreFilesTaskRequestSourceObjectInfoArchivalTarget**](RestoreFilesTaskRequestSourceObjectInfoArchivalTarget.md) |  | [optional] 
**job_id** | **int** | Protection Job Id.  Specifies id of the Protection Job that backed up the objects to be restored. | [optional] 
**job_run_id** | **int** | Specifies the id of the Job Run that captured the snapshot. | [optional] 
**job_uid** | [**RestoreFilesTaskRequestSourceObjectInfoJobUid**](RestoreFilesTaskRequestSourceObjectInfoJobUid.md) |  | [optional] 
**protection_source_id** | **int** | Specifies the id of the leaf object to recover, clone or recover files/folders from. | [optional] 
**started_time_usecs** | **int** | Specifies the time when the Job Run starts capturing a snapshot. Specified as a Unix epoch Timestamp (in microseconds). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


