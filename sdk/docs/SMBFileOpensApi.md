# cohesity.SMBFileOpensApi

All URIs are relative to *https://localhost/irisservices/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**close_smb_file_open**](SMBFileOpensApi.md#close_smb_file_open) | **POST** /public/smbFileOpens | Closes an active SMB file open.
[**get_smb_file_opens**](SMBFileOpensApi.md#get_smb_file_opens) | **GET** /public/smbFileOpens | List the active SMB file opens that match the filter criteria specified using parameters.


# **close_smb_file_open**
> close_smb_file_open(body)

Closes an active SMB file open.

Returns nothing upon success.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.SMBFileOpensApi()
body = cohesity.CloseSmbFileOpenParameters() # CloseSmbFileOpenParameters | Request to close an active SMB file open.

try: 
    # Closes an active SMB file open.
    api_instance.close_smb_file_open(body)
except ApiException as e:
    print "Exception when calling SMBFileOpensApi->close_smb_file_open: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloseSmbFileOpenParameters**](CloseSmbFileOpenParameters.md)| Request to close an active SMB file open. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_smb_file_opens**
> SmbActiveFileOpensResponse get_smb_file_opens(file_path=file_path, view_name=view_name, page_count=page_count, cookie=cookie)

List the active SMB file opens that match the filter criteria specified using parameters.

If no parameters are specified, all active SMB file opens currently on the Cohesity Cluster are returned. Specifying parameters filters the results that are returned.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.SMBFileOpensApi()
file_path = 'file_path_example' # str | Specifies the filepath in the view relative to the root filesystem. If this field is specified, viewName field must also be specified. (optional)
view_name = 'view_name_example' # str | Specifies the name of the View in which to search. If a view name is not specified, all the views in the Cluster is searched. This field is mandatory if filePath field is specified. (optional)
page_count = 56 # int | Specifies the maximum number of active opens to return in the response. This field cannot be set above 1000. If this is not set, maximum of 1000 entries are returned. (optional)
cookie = 'cookie_example' # str | Specifies the opaque string returned in the previous response. If this is set, next set of active opens just after the previous response are returned. If this is not set, first set of active opens are returned. (optional)

try: 
    # List the active SMB file opens that match the filter criteria specified using parameters.
    api_response = api_instance.get_smb_file_opens(file_path=file_path, view_name=view_name, page_count=page_count, cookie=cookie)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SMBFileOpensApi->get_smb_file_opens: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_path** | **str**| Specifies the filepath in the view relative to the root filesystem. If this field is specified, viewName field must also be specified. | [optional] 
 **view_name** | **str**| Specifies the name of the View in which to search. If a view name is not specified, all the views in the Cluster is searched. This field is mandatory if filePath field is specified. | [optional] 
 **page_count** | **int**| Specifies the maximum number of active opens to return in the response. This field cannot be set above 1000. If this is not set, maximum of 1000 entries are returned. | [optional] 
 **cookie** | **str**| Specifies the opaque string returned in the previous response. If this is set, next set of active opens just after the previous response are returned. If this is not set, first set of active opens are returned. | [optional] 

### Return type

[**SmbActiveFileOpensResponse**](SmbActiveFileOpensResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

