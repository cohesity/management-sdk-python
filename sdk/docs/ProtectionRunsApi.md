# cohesity.ProtectionRunsApi

All URIs are relative to *https://localhost/irisservices/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_protection_job_run**](ProtectionRunsApi.md#cancel_protection_job_run) | **POST** /public/protectionRuns/cancel/{id} | Cancel a Protection Job run.
[**get_protection_runs**](ProtectionRunsApi.md#get_protection_runs) | **GET** /public/protectionRuns | List Protection Job Runs filtered by the specified parameters.
[**update_protection_runs**](ProtectionRunsApi.md#update_protection_runs) | **PUT** /public/protectionRuns | Update how long Protection Job Runs and their snapshots are retained on the Cohesity Cluster.


# **cancel_protection_job_run**
> cancel_protection_job_run(id, body=body)

Cancel a Protection Job run.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ProtectionRunsApi()
id = 789 # int | Specifies a unique id of the Protection Job.
body = cohesity.CancelProtectionJobRunParam() # CancelProtectionJobRunParam |  (optional)

try: 
    # Cancel a Protection Job run.
    api_instance.cancel_protection_job_run(id, body=body)
except ApiException as e:
    print "Exception when calling ProtectionRunsApi->cancel_protection_job_run: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a unique id of the Protection Job. | 
 **body** | [**CancelProtectionJobRunParam**](CancelProtectionJobRunParam.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_protection_runs**
> list[ProtectionRunInstance] get_protection_runs(job_id=job_id, exclude_tasks=exclude_tasks, exclude_error_runs=exclude_error_runs, exclude_non_restoreable_runs=exclude_non_restoreable_runs, started_time_usecs=started_time_usecs, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, num_runs=num_runs, source_id=source_id, run_types=run_types)

List Protection Job Runs filtered by the specified parameters.

If no parameters are specified, Job Runs currently on the Cohesity Cluster are returned. Both running and completed Job Runs are reported. Specifying parameters filters the results that are returned.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ProtectionRunsApi()
job_id = 789 # int | Filter by a Protection Job that is specified by id. If not specified, all Job Runs for all Protection Jobs are returned. (optional)
exclude_tasks = true # bool | If true, the individual backup status for all the objects protected by the Job Run are not populated in the response. For example in a VMware environment, the status of backing up each VM associated with a Job is not returned. (optional)
exclude_error_runs = true # bool | Filter out Jobs Runs with errors by setting this field to 'true'. If not set or set to 'false', Job Runs with errors are returned. (optional)
exclude_non_restoreable_runs = true # bool | Filter out jobs runs that cannot be restored by setting this field to 'true'. If not set or set to 'false', Runs without any successful object will be returned. The default value is false. (optional)
started_time_usecs = 789 # int | Return a specific Job Run by specifying a time and a jobId. Specify the time when the Job Run started as a Unix epoch Timestamp (in microseconds). If this field is specified, jobId must also be specified. (optional)
start_time_usecs = 789 # int | Filter by a start time. Only Job Runs that started after the specified time are returned. Specify the start time as a Unix epoch Timestamp (in microseconds). (optional)
end_time_usecs = 789 # int | Filter by a end time specified as a Unix epoch Timestamp (in microseconds). Only Job Runs that completed before the specified end time are returned. (optional)
num_runs = 789 # int | Specify the number of Job Runs to return. The newest Job Runs are returned. (optional)
source_id = 789 # int | Filter by source id. Only Job Runs protecting the specified source (such as a VM or View) are returned. The source id is assigned by the Cohesity Cluster. (optional)
run_types = ['run_types_example'] # list[str] | Filter by run type such as 'kFull', 'kRegular' or 'kLog'. If not specified, Job Runs of all types are returned. (optional)

try: 
    # List Protection Job Runs filtered by the specified parameters.
    api_response = api_instance.get_protection_runs(job_id=job_id, exclude_tasks=exclude_tasks, exclude_error_runs=exclude_error_runs, exclude_non_restoreable_runs=exclude_non_restoreable_runs, started_time_usecs=started_time_usecs, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, num_runs=num_runs, source_id=source_id, run_types=run_types)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProtectionRunsApi->get_protection_runs: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| Filter by a Protection Job that is specified by id. If not specified, all Job Runs for all Protection Jobs are returned. | [optional] 
 **exclude_tasks** | **bool**| If true, the individual backup status for all the objects protected by the Job Run are not populated in the response. For example in a VMware environment, the status of backing up each VM associated with a Job is not returned. | [optional] 
 **exclude_error_runs** | **bool**| Filter out Jobs Runs with errors by setting this field to &#39;true&#39;. If not set or set to &#39;false&#39;, Job Runs with errors are returned. | [optional] 
 **exclude_non_restoreable_runs** | **bool**| Filter out jobs runs that cannot be restored by setting this field to &#39;true&#39;. If not set or set to &#39;false&#39;, Runs without any successful object will be returned. The default value is false. | [optional] 
 **started_time_usecs** | **int**| Return a specific Job Run by specifying a time and a jobId. Specify the time when the Job Run started as a Unix epoch Timestamp (in microseconds). If this field is specified, jobId must also be specified. | [optional] 
 **start_time_usecs** | **int**| Filter by a start time. Only Job Runs that started after the specified time are returned. Specify the start time as a Unix epoch Timestamp (in microseconds). | [optional] 
 **end_time_usecs** | **int**| Filter by a end time specified as a Unix epoch Timestamp (in microseconds). Only Job Runs that completed before the specified end time are returned. | [optional] 
 **num_runs** | **int**| Specify the number of Job Runs to return. The newest Job Runs are returned. | [optional] 
 **source_id** | **int**| Filter by source id. Only Job Runs protecting the specified source (such as a VM or View) are returned. The source id is assigned by the Cohesity Cluster. | [optional] 
 **run_types** | [**list[str]**](str.md)| Filter by run type such as &#39;kFull&#39;, &#39;kRegular&#39; or &#39;kLog&#39;. If not specified, Job Runs of all types are returned. | [optional] 

### Return type

[**list[ProtectionRunInstance]**](ProtectionRunInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_protection_runs**
> update_protection_runs(body)

Update how long Protection Job Runs and their snapshots are retained on the Cohesity Cluster.

Update the expiration date (retention period) for the specified Protection Job Runs and their snapshots. After an expiration time is reached, the Job Run and its snapshots are deleted. If an expiration time of 0 is specified, a Job Run and its snapshots are immediately deleted.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ProtectionRunsApi()
body = cohesity.UpdateProtectionJobRunsParam() # UpdateProtectionJobRunsParam | Request to update the expiration time of Protection Job Runs.

try: 
    # Update how long Protection Job Runs and their snapshots are retained on the Cohesity Cluster.
    api_instance.update_protection_runs(body)
except ApiException as e:
    print "Exception when calling ProtectionRunsApi->update_protection_runs: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateProtectionJobRunsParam**](UpdateProtectionJobRunsParam.md)| Request to update the expiration time of Protection Job Runs. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

