# cohesity.NodesApi

All URIs are relative to *https://localhost/irisservices/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_node_by_id**](NodesApi.md#get_node_by_id) | **GET** /public/nodes/{id} | List details about a single node.
[**get_nodes**](NodesApi.md#get_nodes) | **GET** /public/nodes | List Nodes of the cluster.


# **get_node_by_id**
> list[Node] get_node_by_id(id)

List details about a single node.

Returns the Node corresponding to the specified Node Id.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.NodesApi()
id = 789 # int | Id of the Node

try: 
    # List details about a single node.
    api_response = api_instance.get_node_by_id(id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling NodesApi->get_node_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of the Node | 

### Return type

[**list[Node]**](Node.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nodes**
> list[Node] get_nodes()

List Nodes of the cluster.

If no parameters are specified, all Nodes currently on the Cohesity Cluster are returned. Specifying parameters filters the results that are returned.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.NodesApi()

try: 
    # List Nodes of the cluster.
    api_response = api_instance.get_nodes()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling NodesApi->get_nodes: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Node]**](Node.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

