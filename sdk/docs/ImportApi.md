# cohesity.ImportApi

All URIs are relative to *https://localhost/irisservices/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**import_config**](ImportApi.md#import_config) | **PUT** /public/import/config | Import config into local cluster.


# **import_config**
> import_config(body)

Import config into local cluster.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ImportApi()
body = cohesity.ImportConfigurations() # ImportConfigurations | Request to import configurations from an exported file.

try: 
    # Import config into local cluster.
    api_instance.import_config(body)
except ApiException as e:
    print "Exception when calling ImportApi->import_config: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ImportConfigurations**](ImportConfigurations.md)| Request to import configurations from an exported file. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

