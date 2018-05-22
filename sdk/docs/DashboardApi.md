# cohesity.DashboardApi

All URIs are relative to *https://localhost/irisservices/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dashboard**](DashboardApi.md#get_dashboard) | **GET** /public/dashboard | Returns the dashboard that match the filter criteria specified using parameters.


# **get_dashboard**
> DashboardResponse get_dashboard(cluster_id=cluster_id, all_clusters=all_clusters)

Returns the dashboard that match the filter criteria specified using parameters.

If no parameters are specified, dashboard for the local cluster is returned.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.DashboardApi()
cluster_id = 789 # int | Id of the remote cluster for which to fetch the data. If value is not specified, it is assumed to be local cluster. (optional)
all_clusters = true # bool | Summary data for all clusters. If this is set to true, ClusterId will be ignored. (optional)

try: 
    # Returns the dashboard that match the filter criteria specified using parameters.
    api_response = api_instance.get_dashboard(cluster_id=cluster_id, all_clusters=all_clusters)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DashboardApi->get_dashboard: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**| Id of the remote cluster for which to fetch the data. If value is not specified, it is assumed to be local cluster. | [optional] 
 **all_clusters** | **bool**| Summary data for all clusters. If this is set to true, ClusterId will be ignored. | [optional] 

### Return type

[**DashboardResponse**](DashboardResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

