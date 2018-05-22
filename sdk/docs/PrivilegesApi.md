# cohesity.PrivilegesApi

All URIs are relative to *https://localhost/irisservices/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_privileges**](PrivilegesApi.md#get_privileges) | **GET** /public/privileges | List the privileges defined on the Cohesity Cluster.


# **get_privileges**
> list[PrivilegeInfo] get_privileges(name=name)

List the privileges defined on the Cohesity Cluster.

If the 'name' parameter is not specified, all privileges defined on the Cohesity Cluster are returned. In addition, information about each privilege is returned such as the associated category, description, name,  etc. If an exact privilege name (such as PRINCIPAL_VIEW) is specified in the 'name' parameter, only information about that single privilege is returned.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.PrivilegesApi()
name = 'name_example' # str | Specifies the name of the privilege. (optional)

try: 
    # List the privileges defined on the Cohesity Cluster.
    api_response = api_instance.get_privileges(name=name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PrivilegesApi->get_privileges: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Specifies the name of the privilege. | [optional] 

### Return type

[**list[PrivilegeInfo]**](PrivilegeInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

