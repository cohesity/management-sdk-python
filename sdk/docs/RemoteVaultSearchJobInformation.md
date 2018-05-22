# RemoteVaultSearchJobInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_count** | **int** | Specifies number of Clusters that have archived to the remote Vault and match the search criteria for this job, up to this point in the search. If the search is complete, the total number of Clusters that have archived to the remote Vault and that match the search criteria for this search Job, are reported. If the search is not complete, a partial number is reported. | [optional] 
**end_time_usecs** | **int** | Specifies the end time of the search as a Unix epoch Timestamp (in microseconds) if the search Job has completed. | [optional] 
**error** | **str** | Specifies the error message reported when a search fails. | [optional] 
**job_count** | **int** | Specifies number of Protection Jobs that have archived to the remote Vault and match the search criteria for this search Job, up to this point in the search. If the search is complete, the total number of Protection Jobs that have archived to the remote Vault and that match the search criteria for this search Job, are reported. If the search is not complete, a partial number is reported. | [optional] 
**name** | **str** | Specifies the name of the search Job. | [optional] 
**search_job_status** | **str** | Specifies the status of the search. &#39;kJobRunning&#39; indicates that the Job/task is currently running. &#39;kJobFinished&#39; indicates that the Job/task completed and finished. &#39;kJobFailed&#39; indicates that the Job/task failed and did not complete. &#39;kJobCanceled&#39; indicates that the Job/task was canceled. &#39;kJobPaused&#39; indicates the Job/task is paused. | [optional] 
**search_job_uid** | [**RemoteVaultSearchJobInformationSearchJobUid**](RemoteVaultSearchJobInformationSearchJobUid.md) |  | [optional] 
**start_time_usecs** | **int** | Specifies the start time of the search as a Unix epoch Timestamp (in microseconds). | [optional] 
**vault_id** | **int** | Specifies the id of the remote Vault (External Target) that was searched. | [optional] 
**vault_name** | **str** | Specifies the name of the remote Vault (External Target) that was searched. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


