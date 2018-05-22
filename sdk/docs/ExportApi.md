# cohesity.ExportApi

All URIs are relative to *https://localhost/irisservices/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_config**](ExportApi.md#export_config) | **POST** /public/export/config | 


# **export_config**
> export_config(body)



Export metadata into Json files

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ExportApi()
body = cohesity.ExportParameters() # ExportParameters | Request to open an exported config file to prepare for importing.

try: 
    api_instance.export_config(body)
except ApiException as e:
    print "Exception when calling ExportApi->export_config: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExportParameters**](ExportParameters.md)| Request to open an exported config file to prepare for importing. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

