# cohesity.AlertsApi

All URIs are relative to *https://localhost/irisservices/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_resolution**](AlertsApi.md#create_resolution) | **POST** /public/alertResolutions | Create an Alert Resolution.
[**get_alert_by_id**](AlertsApi.md#get_alert_by_id) | **GET** /public/alerts/{id} | List details about a single Alert.
[**get_alerts**](AlertsApi.md#get_alerts) | **GET** /public/alerts | List the Alerts on the Cohesity Cluster.
[**get_resolution_by_id**](AlertsApi.md#get_resolution_by_id) | **GET** /public/alertResolutions/{id} | List details about a single Alert Resolution.
[**get_resolutions**](AlertsApi.md#get_resolutions) | **GET** /public/alertResolutions | List the Alert Resolutions on the Cohesity Cluster.
[**update_resolution**](AlertsApi.md#update_resolution) | **PUT** /public/alertResolutions/{id} | Apply an existing Alert Resolution to additional Alerts.


# **create_resolution**
> AlertResolution create_resolution(body)

Create an Alert Resolution.

Create an Alert Resolution and apply it to one or more Alerts. Mark the Alerts as resolved.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.AlertsApi()
body = cohesity.AlertResolutionRequest() # AlertResolutionRequest | Request to create an Alert Resolution and apply it to the specified Alerts.

try: 
    # Create an Alert Resolution.
    api_response = api_instance.create_resolution(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AlertsApi->create_resolution: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AlertResolutionRequest**](AlertResolutionRequest.md)| Request to create an Alert Resolution and apply it to the specified Alerts. | 

### Return type

[**AlertResolution**](AlertResolution.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_by_id**
> Alert get_alert_by_id(id)

List details about a single Alert.

Returns the Alert object corresponding to the specified id.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.AlertsApi()
id = 'id_example' # str | Unique id of the Alert to return.

try: 
    # List details about a single Alert.
    api_response = api_instance.get_alert_by_id(id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AlertsApi->get_alert_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique id of the Alert to return. | 

### Return type

[**Alert**](Alert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alerts**
> list[Alert] get_alerts(max_alerts, alert_category_list=alert_category_list, end_date_usecs=end_date_usecs, alert_state_list=alert_state_list, resolution_id_list=resolution_id_list, alert_id_list=alert_id_list, start_date_usecs=start_date_usecs, alert_severity_list=alert_severity_list, alert_type_list=alert_type_list)

List the Alerts on the Cohesity Cluster.

Returns all Alert objects found on the Cohesity Cluster that match the filter criteria specified using parameters. The Cohesity Cluster creates an Alert when a potential problem is found or when a threshold has been exceeded on the Cohesity Cluster. If no filter parameters are specified, all Alert objects are returned. Each object provides details about the Alert such as the Status and Severity.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.AlertsApi()
max_alerts = 56 # int | Limit the number of returned Alerts. The newest Alerts are returned.
alert_category_list = ['alert_category_list_example'] # list[str] | Filter by a list of Alert Categories such as 'kDisk', 'kNode', 'kCluster', 'kNodeHealth', 'kClusterHealth', 'kBackupRestore', 'kEncryption' and 'kArchivalRestore'. (optional)
end_date_usecs = 789 # int | Filter by End Date and Time by specifying a Unix epoch time in microseconds. (optional)
alert_state_list = ['alert_state_list_example'] # list[str] | Filter by a list of Alert States such as 'kOpen' and 'kResolved'. (optional)
resolution_id_list = [56] # list[int] | Filter by a list of Resolution Ids. (optional)
alert_id_list = ['alert_id_list_example'] # list[str] | Filter by a list of Alert ids. (optional)
start_date_usecs = 789 # int | Filter by Start Date and Time by specifying a Unix epoch time in microseconds. (optional)
alert_severity_list = ['alert_severity_list_example'] # list[str] | Filter by a list of Alert Severities such as 'kCritical', 'kWarning' and 'kInfo'. (optional)
alert_type_list = [56] # list[int] | Filter by a list of Alert Types. (optional)

try: 
    # List the Alerts on the Cohesity Cluster.
    api_response = api_instance.get_alerts(max_alerts, alert_category_list=alert_category_list, end_date_usecs=end_date_usecs, alert_state_list=alert_state_list, resolution_id_list=resolution_id_list, alert_id_list=alert_id_list, start_date_usecs=start_date_usecs, alert_severity_list=alert_severity_list, alert_type_list=alert_type_list)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AlertsApi->get_alerts: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **max_alerts** | **int**| Limit the number of returned Alerts. The newest Alerts are returned. | 
 **alert_category_list** | [**list[str]**](str.md)| Filter by a list of Alert Categories such as &#39;kDisk&#39;, &#39;kNode&#39;, &#39;kCluster&#39;, &#39;kNodeHealth&#39;, &#39;kClusterHealth&#39;, &#39;kBackupRestore&#39;, &#39;kEncryption&#39; and &#39;kArchivalRestore&#39;. | [optional] 
 **end_date_usecs** | **int**| Filter by End Date and Time by specifying a Unix epoch time in microseconds. | [optional] 
 **alert_state_list** | [**list[str]**](str.md)| Filter by a list of Alert States such as &#39;kOpen&#39; and &#39;kResolved&#39;. | [optional] 
 **resolution_id_list** | [**list[int]**](int.md)| Filter by a list of Resolution Ids. | [optional] 
 **alert_id_list** | [**list[str]**](str.md)| Filter by a list of Alert ids. | [optional] 
 **start_date_usecs** | **int**| Filter by Start Date and Time by specifying a Unix epoch time in microseconds. | [optional] 
 **alert_severity_list** | [**list[str]**](str.md)| Filter by a list of Alert Severities such as &#39;kCritical&#39;, &#39;kWarning&#39; and &#39;kInfo&#39;. | [optional] 
 **alert_type_list** | [**list[int]**](int.md)| Filter by a list of Alert Types. | [optional] 

### Return type

[**list[Alert]**](Alert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resolution_by_id**
> AlertResolution get_resolution_by_id(id)

List details about a single Alert Resolution.

Returns the Alert Resolution object corresponding to passed in Alert Resolution Id.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.AlertsApi()
id = 789 # int | Unique id of the Alert Resolution to return.

try: 
    # List details about a single Alert Resolution.
    api_response = api_instance.get_resolution_by_id(id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AlertsApi->get_resolution_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique id of the Alert Resolution to return. | 

### Return type

[**AlertResolution**](AlertResolution.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resolutions**
> list[AlertResolution] get_resolutions(max_resolutions, start_date_usecs=start_date_usecs, end_date_usecs=end_date_usecs, resolution_id_list=resolution_id_list, alert_id_list=alert_id_list)

List the Alert Resolutions on the Cohesity Cluster.

Returns all Alert Resolution objects found on the Cohesity Cluster that match the filter criteria specified using parameters. If no filter parameters are specified, all Alert Resolution objects are returned. Each object provides details about the Alert Resolution such as the resolution summary and details.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.AlertsApi()
max_resolutions = 56 # int | Limit the number of returned Alert Resolutions. The newest Resolutions are returned.
start_date_usecs = 789 # int | Filter by Start Date and Time by specifying a Unix epoch time in microseconds. (optional)
end_date_usecs = 789 # int | Filter by End Date and Time by specifying a Unix epoch time in microseconds. (optional)
resolution_id_list = [56] # list[int] | Filter by a list of Alert Resolution ids. (optional)
alert_id_list = ['alert_id_list_example'] # list[str] | Filter by a list of Alert ids. (optional)

try: 
    # List the Alert Resolutions on the Cohesity Cluster.
    api_response = api_instance.get_resolutions(max_resolutions, start_date_usecs=start_date_usecs, end_date_usecs=end_date_usecs, resolution_id_list=resolution_id_list, alert_id_list=alert_id_list)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AlertsApi->get_resolutions: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **max_resolutions** | **int**| Limit the number of returned Alert Resolutions. The newest Resolutions are returned. | 
 **start_date_usecs** | **int**| Filter by Start Date and Time by specifying a Unix epoch time in microseconds. | [optional] 
 **end_date_usecs** | **int**| Filter by End Date and Time by specifying a Unix epoch time in microseconds. | [optional] 
 **resolution_id_list** | [**list[int]**](int.md)| Filter by a list of Alert Resolution ids. | [optional] 
 **alert_id_list** | [**list[str]**](str.md)| Filter by a list of Alert ids. | [optional] 

### Return type

[**list[AlertResolution]**](AlertResolution.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_resolution**
> AlertResolution update_resolution(id, body)

Apply an existing Alert Resolution to additional Alerts.

Apply an existing Alert Resolution to one or more additional Alerts. Mark those additional Alerts as resolved.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.AlertsApi()
id = 789 # int | Unique id of the Alert Resolution to return.
body = cohesity.UpdateResolutionParams() # UpdateResolutionParams | Request to apply an existing resolution to the specified Alerts.

try: 
    # Apply an existing Alert Resolution to additional Alerts.
    api_response = api_instance.update_resolution(id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AlertsApi->update_resolution: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique id of the Alert Resolution to return. | 
 **body** | [**UpdateResolutionParams**](UpdateResolutionParams.md)| Request to apply an existing resolution to the specified Alerts. | 

### Return type

[**AlertResolution**](AlertResolution.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

