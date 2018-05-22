# RemoteVaultSearchJobResults

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_count** | **int** | Specifies number of Clusters that have archived to the remote Vault that match the criteria specified in the search Job, up to this point in the search. If the search is complete, the total number of Clusters that have archived to the remote Vault and that match the search criteria for the search Job, are reported. If the search was not complete, a partial number is reported. | [optional] 
**cluster_match_string** | **str** | Specifies the value of the clusterMatchSting if it was set in the original search Job. | [optional] 
**cookie** | **str** | Specifies an opaque string to pass to the next request to get the next set of search results. This is provided to support pagination. If null, this is the last set of search results. | [optional] 
**end_time_usecs** | **int** | Specifies the value of endTimeUsecs if it was set in the original search Job. End time is recorded as a Unix epoch Timestamp (in microseconds). | [optional] 
**error** | **str** | Specifies the error message if the search fails. | [optional] 
**job_count** | **int** | Specifies number of Protection Jobs that have archived to the remote Vault that match the criteria specified in the search Job. If the search is complete, the total number of Protection Jobs that have archived to the remote Vault and match the search criteria for the search Job, are reported. If the search is not complete, a partial number is reported. | [optional] 
**job_match_string** | **str** | Specifies the value of the jobMatchSting if it was set in the original search Job. | [optional] 
**protection_jobs** | [**list[RemoteProtectionJobRunInformation]**](RemoteProtectionJobRunInformation.md) | Specifies a list of Protection Jobs that have archived data to a remote Vault and that also match the filter criteria. | [optional] 
**search_job_status** | **str** | Specifies the status of the search Job. &#39;kJobRunning&#39; indicates that the Job/task is currently running. &#39;kJobFinished&#39; indicates that the Job/task completed and finished. &#39;kJobFailed&#39; indicates that the Job/task failed and did not complete. &#39;kJobCanceled&#39; indicates that the Job/task was canceled. &#39;kJobPaused&#39; indicates the Job/task is paused. | [optional] 
**search_job_uid** | [**RemoteVaultSearchJobResultsSearchJobUid**](RemoteVaultSearchJobResultsSearchJobUid.md) |  | [optional] 
**start_time_usecs** | **int** | Specifies the value of startTimeUsecs if it was set in the original search Job. Start time is recorded as a Unix epoch Timestamp (in microseconds). | [optional] 
**vault_id** | **int** | Specifies the id of the remote Vault that was searched. | [optional] 
**vault_name** | **str** | Specifies the name of the remote Vault that was searched. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


