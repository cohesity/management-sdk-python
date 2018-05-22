# cohesity.ViewBoxesApi

All URIs are relative to *https://localhost/irisservices/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_view_box**](ViewBoxesApi.md#create_view_box) | **POST** /public/viewBoxes | Create a Domain (View Box).
[**get_view_box_by_id**](ViewBoxesApi.md#get_view_box_by_id) | **GET** /public/viewBoxes/{id} | List details about a single Domain (View Box).
[**get_view_boxes**](ViewBoxesApi.md#get_view_boxes) | **GET** /public/viewBoxes | List Domains (View Boxes) filtered by the specified parameters.
[**update_view_box**](ViewBoxesApi.md#update_view_box) | **PUT** /public/viewBoxes/{id} | Update a Domain (View Box).


# **create_view_box**
> ViewBox create_view_box(body)

Create a Domain (View Box).

Returns the created Domain (View Box).

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ViewBoxesApi()
body = cohesity.CreateViewBoxParams() # CreateViewBoxParams | Request to create a Storage Domain (View Box) configuration.

try: 
    # Create a Domain (View Box).
    api_response = api_instance.create_view_box(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ViewBoxesApi->create_view_box: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateViewBoxParams**](CreateViewBoxParams.md)| Request to create a Storage Domain (View Box) configuration. | 

### Return type

[**ViewBox**](ViewBox.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_view_box_by_id**
> ViewBox get_view_box_by_id(id)

List details about a single Domain (View Box).

Returns the Domain (View Box) corresponding to the specified Domain (View Box) Id.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ViewBoxesApi()
id = 789 # int | Id of the Storage Domain (View Box)

try: 
    # List details about a single Domain (View Box).
    api_response = api_instance.get_view_box_by_id(id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ViewBoxesApi->get_view_box_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of the Storage Domain (View Box) | 

### Return type

[**ViewBox**](ViewBox.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_view_boxes**
> list[ViewBox] get_view_boxes(ids=ids, names=names, cluster_partition_ids=cluster_partition_ids, fetch_stats=fetch_stats)

List Domains (View Boxes) filtered by the specified parameters.

If no parameters are specified, all Domains (View Boxes) currently on the Cohesity Cluster are returned. Specifying parameters filters the results that are returned.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ViewBoxesApi()
ids = [56] # list[int] | Filter by a list of Storage Domain (View Box) ids. If empty, View Boxes are not filtered by id. (optional)
names = ['names_example'] # list[str] | Filter by a list of Storage Domain (View Box) Names. If empty, Storage Domains (View Boxes) are not filtered by Name. (optional)
cluster_partition_ids = [56] # list[int] | Filter by a list of Cluster Partition Ids. (optional)
fetch_stats = true # bool | Specifies whether to include usage and performance statistics. (optional)

try: 
    # List Domains (View Boxes) filtered by the specified parameters.
    api_response = api_instance.get_view_boxes(ids=ids, names=names, cluster_partition_ids=cluster_partition_ids, fetch_stats=fetch_stats)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ViewBoxesApi->get_view_boxes: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)| Filter by a list of Storage Domain (View Box) ids. If empty, View Boxes are not filtered by id. | [optional] 
 **names** | [**list[str]**](str.md)| Filter by a list of Storage Domain (View Box) Names. If empty, Storage Domains (View Boxes) are not filtered by Name. | [optional] 
 **cluster_partition_ids** | [**list[int]**](int.md)| Filter by a list of Cluster Partition Ids. | [optional] 
 **fetch_stats** | **bool**| Specifies whether to include usage and performance statistics. | [optional] 

### Return type

[**list[ViewBox]**](ViewBox.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_view_box**
> ViewBox update_view_box(id, body)

Update a Domain (View Box).

Returns the updated Domain (View Box).

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ViewBoxesApi()
id = 789 # int | Id of the Storage Domain (View Box)
body = cohesity.CreateViewBoxParams() # CreateViewBoxParams | Request to update a Storage Domain (View Box) configuration.

try: 
    # Update a Domain (View Box).
    api_response = api_instance.update_view_box(id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ViewBoxesApi->update_view_box: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of the Storage Domain (View Box) | 
 **body** | [**CreateViewBoxParams**](CreateViewBoxParams.md)| Request to update a Storage Domain (View Box) configuration. | 

### Return type

[**ViewBox**](ViewBox.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

