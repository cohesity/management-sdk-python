# cohesity.SchedulerApi

All URIs are relative to *https://localhost/irisservices/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_scheduler_job**](SchedulerApi.md#create_scheduler_job) | **POST** /public/scheduler | Create an email report scheduler job.
[**delete_scheduler_jobs**](SchedulerApi.md#delete_scheduler_jobs) | **DELETE** /public/scheduler | Delete one or more email report schedule jobs.
[**get_scheduler_jobs**](SchedulerApi.md#get_scheduler_jobs) | **GET** /public/scheduler | List the email report schedule jobs that are scheduled to run.
[**update_scheduler_job**](SchedulerApi.md#update_scheduler_job) | **PUT** /public/scheduler | Update an existing email report schedule job.


# **create_scheduler_job**
> SchedulerProtoSchedulerJobScheduleJobParametersReportJobParameter create_scheduler_job(body)

Create an email report scheduler job.

Returns the created email report scheduler job. An email report scheduler job generates a report with the specified parameters and sends that report to the specified email accounts according to the defined schedule. This operation may also be used to send a report once (with no schedule), by setting the EnableRecurring field to false.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.SchedulerApi()
body = cohesity.SchedulerProtoSchedulerJob() # SchedulerProtoSchedulerJob | 

try: 
    # Create an email report scheduler job.
    api_response = api_instance.create_scheduler_job(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SchedulerApi->create_scheduler_job: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SchedulerProtoSchedulerJob**](SchedulerProtoSchedulerJob.md)|  | 

### Return type

[**SchedulerProtoSchedulerJobScheduleJobParametersReportJobParameter**](SchedulerProtoSchedulerJobScheduleJobParametersReportJobParameter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_scheduler_jobs**
> delete_scheduler_jobs(ids=ids)

Delete one or more email report schedule jobs.

Specify a list of email report schedule job ids to unschedule and delete.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.SchedulerApi()
ids = [cohesity.list[int]()] # list[int] | Array of ids (optional)

try: 
    # Delete one or more email report schedule jobs.
    api_instance.delete_scheduler_jobs(ids=ids)
except ApiException as e:
    print "Exception when calling SchedulerApi->delete_scheduler_jobs: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **list[int]**| Array of ids | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scheduler_jobs**
> SchedulerProto get_scheduler_jobs()

List the email report schedule jobs that are scheduled to run.

Returns all the email report scheduler jobs that are scheduled to run. An email report scheduler job generates a report with the specified parameters and sends that report to the specified email accounts according to the defined schedule.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.SchedulerApi()

try: 
    # List the email report schedule jobs that are scheduled to run.
    api_response = api_instance.get_scheduler_jobs()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SchedulerApi->get_scheduler_jobs: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SchedulerProto**](SchedulerProto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_scheduler_job**
> SchedulerProtoSchedulerJob update_scheduler_job(body=body)

Update an existing email report schedule job.

Returns the updated email report scheduler job.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.SchedulerApi()
body = cohesity.SchedulerProtoSchedulerJob() # SchedulerProtoSchedulerJob | Update Job Parameter. (optional)

try: 
    # Update an existing email report schedule job.
    api_response = api_instance.update_scheduler_job(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SchedulerApi->update_scheduler_job: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SchedulerProtoSchedulerJob**](SchedulerProtoSchedulerJob.md)| Update Job Parameter. | [optional] 

### Return type

[**SchedulerProtoSchedulerJob**](SchedulerProtoSchedulerJob.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

