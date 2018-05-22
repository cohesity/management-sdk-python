# cohesity.ReportsApi

All URIs are relative to *https://localhost/irisservices/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data_transfer_from_vaults_report_request**](ReportsApi.md#get_data_transfer_from_vaults_report_request) | **GET** /public/reports/dataTransferFromVaults | Get summary statistics about transferring data from Vaults (External Targets) to this Cohesity Cluster.
[**get_data_transfer_to_vaults_report_request**](ReportsApi.md#get_data_transfer_to_vaults_report_request) | **GET** /public/reports/dataTransferToVaults | Get summary statistics about transferring data from the Cohesity Cluster to Vaults (External Targets).
[**get_protection_sources_job_runs_report_request**](ReportsApi.md#get_protection_sources_job_runs_report_request) | **GET** /public/reports/protectionSourcesJobRuns | Get protection details about the specified list of leaf Protection Source Objects (such as a VMs).
[**get_protection_sources_jobs_summary_report_request**](ReportsApi.md#get_protection_sources_jobs_summary_report_request) | **GET** /public/reports/protectionSourcesJobsSummary | Get Job Run (Snapshot) summary statistics about the leaf Protection Sources Objects that match the specified filter criteria.
[**get_restore_summary_by_object_type_report**](ReportsApi.md#get_restore_summary_by_object_type_report) | **GET** /public/reports/restoreSummaryByObjectType | 


# **get_data_transfer_from_vaults_report_request**
> DataTransferFromVaultsSummaryResponse get_data_transfer_from_vaults_report_request(start_time_msecs=start_time_msecs, end_time_msecs=end_time_msecs, vault_ids=vault_ids, output_format=output_format)

Get summary statistics about transferring data from Vaults (External Targets) to this Cohesity Cluster.

A Vault can provide an additional Cloud Tier where cold data of the Cohesity Cluster is stored in the Cloud. A Vault can also provide archive storage for backup data. This archive data is stored on Tapes and in Cloud Vaults.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ReportsApi()
start_time_msecs = 789 # int | Filter by a start time. Specify the start time as a Unix epoch Timestamp (in milliseconds). If startTimeMsecs and endTimeMsecs are not specified, the time period is the last 7 days. (optional)
end_time_msecs = 789 # int | Filter by end time. Specify the end time as a Unix epoch Timestamp (in milliseconds). If startTimeMsecs and endTimeMsecs are not specified, the time period is the last 7 days. (optional)
vault_ids = [56] # list[int] | Filter by a list of Vault ids. (optional)
output_format = 'output_format_example' # str | Specifies the format for the output such as 'csv' or 'json'. If not specified, the json format is returned. If 'csv' is specified, a comma-separated list with a heading row is returned. (optional)

try: 
    # Get summary statistics about transferring data from Vaults (External Targets) to this Cohesity Cluster.
    api_response = api_instance.get_data_transfer_from_vaults_report_request(start_time_msecs=start_time_msecs, end_time_msecs=end_time_msecs, vault_ids=vault_ids, output_format=output_format)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ReportsApi->get_data_transfer_from_vaults_report_request: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time_msecs** | **int**| Filter by a start time. Specify the start time as a Unix epoch Timestamp (in milliseconds). If startTimeMsecs and endTimeMsecs are not specified, the time period is the last 7 days. | [optional] 
 **end_time_msecs** | **int**| Filter by end time. Specify the end time as a Unix epoch Timestamp (in milliseconds). If startTimeMsecs and endTimeMsecs are not specified, the time period is the last 7 days. | [optional] 
 **vault_ids** | [**list[int]**](int.md)| Filter by a list of Vault ids. | [optional] 
 **output_format** | **str**| Specifies the format for the output such as &#39;csv&#39; or &#39;json&#39;. If not specified, the json format is returned. If &#39;csv&#39; is specified, a comma-separated list with a heading row is returned. | [optional] 

### Return type

[**DataTransferFromVaultsSummaryResponse**](DataTransferFromVaultsSummaryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_transfer_to_vaults_report_request**
> DataTransferToVaultsSummaryResponse get_data_transfer_to_vaults_report_request(vault_ids=vault_ids, output_format=output_format, start_time_msecs=start_time_msecs, end_time_msecs=end_time_msecs)

Get summary statistics about transferring data from the Cohesity Cluster to Vaults (External Targets).

A Vault can provide an additional Cloud Tier where cold data of the Cohesity Cluster can be stored in the Cloud. A Vault can also provide archive storage for backup data. This archive data is stored on Tapes and in Cloud Vaults.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ReportsApi()
vault_ids = [56] # list[int] | Filter by a list of Vault ids. (optional)
output_format = 'output_format_example' # str | Specifies the format for the output such as 'csv' or 'json'. If not specified, the json format is returned. If 'csv' is specified, a comma-separated list with a heading row is returned. (optional)
start_time_msecs = 789 # int | Filter by a start time. Specify the start time as a Unix epoch Timestamp (in milliseconds). If startTimeMsecs and endTimeMsecs are not specified, the time period is the last 7 days. (optional)
end_time_msecs = 789 # int | Filter by end time. Specify the end time as a Unix epoch Timestamp (in milliseconds). If startTimeMsecs and endTimeMsecs are not specified, the time period is the last 7 days. (optional)

try: 
    # Get summary statistics about transferring data from the Cohesity Cluster to Vaults (External Targets).
    api_response = api_instance.get_data_transfer_to_vaults_report_request(vault_ids=vault_ids, output_format=output_format, start_time_msecs=start_time_msecs, end_time_msecs=end_time_msecs)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ReportsApi->get_data_transfer_to_vaults_report_request: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_ids** | [**list[int]**](int.md)| Filter by a list of Vault ids. | [optional] 
 **output_format** | **str**| Specifies the format for the output such as &#39;csv&#39; or &#39;json&#39;. If not specified, the json format is returned. If &#39;csv&#39; is specified, a comma-separated list with a heading row is returned. | [optional] 
 **start_time_msecs** | **int**| Filter by a start time. Specify the start time as a Unix epoch Timestamp (in milliseconds). If startTimeMsecs and endTimeMsecs are not specified, the time period is the last 7 days. | [optional] 
 **end_time_msecs** | **int**| Filter by end time. Specify the end time as a Unix epoch Timestamp (in milliseconds). If startTimeMsecs and endTimeMsecs are not specified, the time period is the last 7 days. | [optional] 

### Return type

[**DataTransferToVaultsSummaryResponse**](DataTransferToVaultsSummaryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_protection_sources_job_runs_report_request**
> list[ProtectionSourcesJobRunsReportElement] get_protection_sources_job_runs_report_request(protection_source_ids, environments=environments, output_format=output_format, page_count=page_count, run_status=run_status, job_ids=job_ids, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs)

Get protection details about the specified list of leaf Protection Source Objects (such as a VMs).

Returns the Snapshots that contain backups of the specified Protection Source Objects and match the specified filter criteria.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ReportsApi()
protection_source_ids = [56] # list[int] | Filter by a list of leaf Protection Sources Objects (such as VMs). Snapshots of the specified Protection Source Objects are returned.
environments = ['environments_example'] # list[str] | Filter by a list of environment types such as 'kVMware', 'kView', 'kSQL' 'kPuppeteer', 'kPhysical', 'kPure', 'kNetapp', 'kGenericNas', 'kHyperV', 'kAcropolis', or 'kAzure'. Snapshots of leaf Protection Source Objects for the specified environment types are returned. NOTE: 'kPuppeteer' refers to Cohesity's Remote Adapter. (optional)
output_format = 'output_format_example' # str | Specifies the format for the output such as 'cvs' or 'json'. If not specified, the json format is returned. If 'csv' is specified, a comma-separated list with a heading row is returned. (optional)
page_count = 56 # int | Specifies the number of Snapshots to return in the response for pagination purposes. Used in combination with the paginationCookie in the response to return multiple sets of Snapshots. (optional)
run_status = ['run_status_example'] # list[str] | Filter by a list of run statuses such as 'kRunning', 'kSuccess', 'kFailure' etc. Snapshots of Job Runs with the specified run statuses are reported. 'kSuccess' indicates that the Job Run was successful. 'kRunning' indicates that the Job Run is currently running. 'kWarning' indicates that the Job Run was successful but warnings were issued. 'kCancelled' indicates that the Job Run was canceled. 'kError' indicates the Job Run encountered an error and did not run to completion. (optional)
job_ids = [56] # list[int] | Filter by a list of Job ids. Snapshots for the specified Protection Jobs are listed. (optional)
start_time_usecs = 789 # int | Filter by a start time. Snapshots that started after the specified time are returned. Specify the start time as a Unix epoch Timestamp (in microseconds). (optional)
end_time_usecs = 789 # int | Filter by a end time. Snapshots that ended before the specified time are returned. Specify the end time as a Unix epoch Timestamp (in microseconds). (optional)

try: 
    # Get protection details about the specified list of leaf Protection Source Objects (such as a VMs).
    api_response = api_instance.get_protection_sources_job_runs_report_request(protection_source_ids, environments=environments, output_format=output_format, page_count=page_count, run_status=run_status, job_ids=job_ids, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ReportsApi->get_protection_sources_job_runs_report_request: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **protection_source_ids** | [**list[int]**](int.md)| Filter by a list of leaf Protection Sources Objects (such as VMs). Snapshots of the specified Protection Source Objects are returned. | 
 **environments** | [**list[str]**](str.md)| Filter by a list of environment types such as &#39;kVMware&#39;, &#39;kView&#39;, &#39;kSQL&#39; &#39;kPuppeteer&#39;, &#39;kPhysical&#39;, &#39;kPure&#39;, &#39;kNetapp&#39;, &#39;kGenericNas&#39;, &#39;kHyperV&#39;, &#39;kAcropolis&#39;, or &#39;kAzure&#39;. Snapshots of leaf Protection Source Objects for the specified environment types are returned. NOTE: &#39;kPuppeteer&#39; refers to Cohesity&#39;s Remote Adapter. | [optional] 
 **output_format** | **str**| Specifies the format for the output such as &#39;cvs&#39; or &#39;json&#39;. If not specified, the json format is returned. If &#39;csv&#39; is specified, a comma-separated list with a heading row is returned. | [optional] 
 **page_count** | **int**| Specifies the number of Snapshots to return in the response for pagination purposes. Used in combination with the paginationCookie in the response to return multiple sets of Snapshots. | [optional] 
 **run_status** | [**list[str]**](str.md)| Filter by a list of run statuses such as &#39;kRunning&#39;, &#39;kSuccess&#39;, &#39;kFailure&#39; etc. Snapshots of Job Runs with the specified run statuses are reported. &#39;kSuccess&#39; indicates that the Job Run was successful. &#39;kRunning&#39; indicates that the Job Run is currently running. &#39;kWarning&#39; indicates that the Job Run was successful but warnings were issued. &#39;kCancelled&#39; indicates that the Job Run was canceled. &#39;kError&#39; indicates the Job Run encountered an error and did not run to completion. | [optional] 
 **job_ids** | [**list[int]**](int.md)| Filter by a list of Job ids. Snapshots for the specified Protection Jobs are listed. | [optional] 
 **start_time_usecs** | **int**| Filter by a start time. Snapshots that started after the specified time are returned. Specify the start time as a Unix epoch Timestamp (in microseconds). | [optional] 
 **end_time_usecs** | **int**| Filter by a end time. Snapshots that ended before the specified time are returned. Specify the end time as a Unix epoch Timestamp (in microseconds). | [optional] 

### Return type

[**list[ProtectionSourcesJobRunsReportElement]**](ProtectionSourcesJobRunsReportElement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_protection_sources_jobs_summary_report_request**
> list[ProtectionSourcesSummaryStats] get_protection_sources_jobs_summary_report_request(protection_source_ids=protection_source_ids, statuses=statuses, output_format=output_format, registered_source_id=registered_source_id, job_ids=job_ids, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, environments=environments)

Get Job Run (Snapshot) summary statistics about the leaf Protection Sources Objects that match the specified filter criteria.

For example, if two Job ids are passed in, Snapshot summary statistics about all the leaf Objects that have been protected by the two specified Jobs are reported. For example if a top level registered Source id is passed in, summary statistics about all the Snapshots backing up leaf Objects in the specified Source are reported.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ReportsApi()
protection_source_ids = [56] # list[int] | Filter by a list of leaf Protection Sources Objects (such as VMs). Snapshot summary statistics for the listed Protection Source Objects are reported. (optional)
statuses = ['statuses_example'] # list[str] | Filter by a list of run statuses. 'kSuccess' indicates that the Job Run was successful. 'kRunning' indicates that the Job Run is currently running. 'kWarning' indicates that the Job Run was successful but warnings were issued. 'kCancelled' indicates that the Job Run was canceled. 'kError' indicates the Job Run encountered an error and did not run to completion. (optional)
output_format = 'output_format_example' # str | Specifies the format for the output such as 'csv' or 'json'. If not specified, the json format is returned. If 'csv' is specified, a comma-separated list with a heading row is returned. (optional)
registered_source_id = 789 # int | Specifies an id of a top level Registered Source such as a vCenter Server. If specified, Snapshot summary statistics for all the leaf Protection Sources (such as VMs) that are children of this Registered Source are reported. NOTE: If specified, filtering by other fields is not supported. (optional)
job_ids = [56] # list[int] | Filter by a list of Job ids. Snapshots summary statistics for the specified Protection Jobs are reported. (optional)
start_time_usecs = 789 # int | Filter by a start time. Snapshot summary statistics for Job Runs that started after the specified time are reported. Specify the start time as a Unix epoch Timestamp (in microseconds). (optional)
end_time_usecs = 789 # int | Filter by end time. Snapshot summary statistics for Job Runs that ended before the specified time are returned. Specify the end time as a Unix epoch Timestamp (in microseconds). (optional)
environments = ['environments_example'] # list[str] | Filter by a list of environment types such as 'kVMware', 'kView', 'kSQL' 'kPuppeteer', 'kPhysical', 'kPure', or 'kNetapp'. Snapshot summary statistics about the leaf Protection Source Objects of specified environment types are reported. NOTE: 'kPuppeteer' refers to Cohesity's Remote Adapter. (optional)

try: 
    # Get Job Run (Snapshot) summary statistics about the leaf Protection Sources Objects that match the specified filter criteria.
    api_response = api_instance.get_protection_sources_jobs_summary_report_request(protection_source_ids=protection_source_ids, statuses=statuses, output_format=output_format, registered_source_id=registered_source_id, job_ids=job_ids, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, environments=environments)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ReportsApi->get_protection_sources_jobs_summary_report_request: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **protection_source_ids** | [**list[int]**](int.md)| Filter by a list of leaf Protection Sources Objects (such as VMs). Snapshot summary statistics for the listed Protection Source Objects are reported. | [optional] 
 **statuses** | [**list[str]**](str.md)| Filter by a list of run statuses. &#39;kSuccess&#39; indicates that the Job Run was successful. &#39;kRunning&#39; indicates that the Job Run is currently running. &#39;kWarning&#39; indicates that the Job Run was successful but warnings were issued. &#39;kCancelled&#39; indicates that the Job Run was canceled. &#39;kError&#39; indicates the Job Run encountered an error and did not run to completion. | [optional] 
 **output_format** | **str**| Specifies the format for the output such as &#39;csv&#39; or &#39;json&#39;. If not specified, the json format is returned. If &#39;csv&#39; is specified, a comma-separated list with a heading row is returned. | [optional] 
 **registered_source_id** | **int**| Specifies an id of a top level Registered Source such as a vCenter Server. If specified, Snapshot summary statistics for all the leaf Protection Sources (such as VMs) that are children of this Registered Source are reported. NOTE: If specified, filtering by other fields is not supported. | [optional] 
 **job_ids** | [**list[int]**](int.md)| Filter by a list of Job ids. Snapshots summary statistics for the specified Protection Jobs are reported. | [optional] 
 **start_time_usecs** | **int**| Filter by a start time. Snapshot summary statistics for Job Runs that started after the specified time are reported. Specify the start time as a Unix epoch Timestamp (in microseconds). | [optional] 
 **end_time_usecs** | **int**| Filter by end time. Snapshot summary statistics for Job Runs that ended before the specified time are returned. Specify the end time as a Unix epoch Timestamp (in microseconds). | [optional] 
 **environments** | [**list[str]**](str.md)| Filter by a list of environment types such as &#39;kVMware&#39;, &#39;kView&#39;, &#39;kSQL&#39; &#39;kPuppeteer&#39;, &#39;kPhysical&#39;, &#39;kPure&#39;, or &#39;kNetapp&#39;. Snapshot summary statistics about the leaf Protection Source Objects of specified environment types are reported. NOTE: &#39;kPuppeteer&#39; refers to Cohesity&#39;s Remote Adapter. | [optional] 

### Return type

[**list[ProtectionSourcesSummaryStats]**](ProtectionSourcesSummaryStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_restore_summary_by_object_type_report**
> list[RestoreSourceSummaryByObjectTypeElement] get_restore_summary_by_object_type_report(recover_task_name=recover_task_name, status=status, output_format=output_format, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, type=type, user_name=user_name, recovered_from=recovered_from)



### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ReportsApi()
recover_task_name = 'recover_task_name_example' # str | Specifies the recover task name. (optional)
status = 'status_example' # str | Specifies the overall status of the Restore Task to filter. 'kReadyToSchedule' indicates the Restore Task is waiting to be scheduled. 'kProgressMonitorCreated' indicates the progress monitor for the Restore Task has been created. 'kRetrievedFromArchive' indicates that the objects to restore have been retrieved from the specified archive. A Task will only ever transition to this state if a retrieval is necessary. 'kAdmitted' indicates the task has been admitted. After a task has been admitted, its status does not move back to 'kReadyToSchedule' state even if it is rescheduled. 'kInProgress' indicates that the Restore Task is in progress. 'kFinishingProgressMonitor' indicates that the Restore Task is finishing its progress monitoring. 'kFinished' indicates that the Restore Task has finished. The status indicating success or failure is found in the error code that is stored with the Restore Task. (optional)
output_format = 'output_format_example' # str | Specifies the format for the output such as 'csv' or 'json'. If not specified, the json format is returned. If 'csv' is specified, a comma-separated list with a heading row is returned. (optional)
start_time_usecs = 789 # int | Filter by a start time specified as a Unix epoch Timestamp (in microseconds). (optional)
end_time_usecs = 789 # int | Filter by an end time specified as a Unix epoch Timestamp (in microseconds). (optional)
type = 'type_example' # str | Specify the object type to filter with. Specifies the type of Restore Task.  'kRecoverVMs' specifies a Restore Task that recovers VMs. 'kCloneVMs' specifies a Restore Task that clones VMs. 'kCloneView' specifies a Restore Task that clones a View. 'kMountVolumes' specifies a Restore Task that mounts volumes. 'kRestoreFiles' specifies a Restore Task that recovers files and folders. (optional)
user_name = 'user_name_example' # str | Specify the user name to filter with. (optional)
recovered_from = ['recovered_from_example'] # list[str] | Specifies the targets from which the recovery happend. (optional)

try: 
    api_response = api_instance.get_restore_summary_by_object_type_report(recover_task_name=recover_task_name, status=status, output_format=output_format, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, type=type, user_name=user_name, recovered_from=recovered_from)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ReportsApi->get_restore_summary_by_object_type_report: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recover_task_name** | **str**| Specifies the recover task name. | [optional] 
 **status** | **str**| Specifies the overall status of the Restore Task to filter. &#39;kReadyToSchedule&#39; indicates the Restore Task is waiting to be scheduled. &#39;kProgressMonitorCreated&#39; indicates the progress monitor for the Restore Task has been created. &#39;kRetrievedFromArchive&#39; indicates that the objects to restore have been retrieved from the specified archive. A Task will only ever transition to this state if a retrieval is necessary. &#39;kAdmitted&#39; indicates the task has been admitted. After a task has been admitted, its status does not move back to &#39;kReadyToSchedule&#39; state even if it is rescheduled. &#39;kInProgress&#39; indicates that the Restore Task is in progress. &#39;kFinishingProgressMonitor&#39; indicates that the Restore Task is finishing its progress monitoring. &#39;kFinished&#39; indicates that the Restore Task has finished. The status indicating success or failure is found in the error code that is stored with the Restore Task. | [optional] 
 **output_format** | **str**| Specifies the format for the output such as &#39;csv&#39; or &#39;json&#39;. If not specified, the json format is returned. If &#39;csv&#39; is specified, a comma-separated list with a heading row is returned. | [optional] 
 **start_time_usecs** | **int**| Filter by a start time specified as a Unix epoch Timestamp (in microseconds). | [optional] 
 **end_time_usecs** | **int**| Filter by an end time specified as a Unix epoch Timestamp (in microseconds). | [optional] 
 **type** | **str**| Specify the object type to filter with. Specifies the type of Restore Task.  &#39;kRecoverVMs&#39; specifies a Restore Task that recovers VMs. &#39;kCloneVMs&#39; specifies a Restore Task that clones VMs. &#39;kCloneView&#39; specifies a Restore Task that clones a View. &#39;kMountVolumes&#39; specifies a Restore Task that mounts volumes. &#39;kRestoreFiles&#39; specifies a Restore Task that recovers files and folders. | [optional] 
 **user_name** | **str**| Specify the user name to filter with. | [optional] 
 **recovered_from** | [**list[str]**](str.md)| Specifies the targets from which the recovery happend. | [optional] 

### Return type

[**list[RestoreSourceSummaryByObjectTypeElement]**](RestoreSourceSummaryByObjectTypeElement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

