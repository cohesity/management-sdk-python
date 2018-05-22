# cohesity.StaticRouteApi

All URIs are relative to *https://localhost/irisservices/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_static_routes**](StaticRouteApi.md#get_static_routes) | **GET** /public/staticRoutes | List the Static Routes for the Cohesity Cluster.
[**remove_static_route**](StaticRouteApi.md#remove_static_route) | **DELETE** /public/staticRoutes/{ip} | Remove the specified Static Route from the Cohesity Cluster.
[**update_static_route**](StaticRouteApi.md#update_static_route) | **PUT** /public/staticRoutes/{ip} | Create or update a Static Route on the Cohesity Cluster.


# **get_static_routes**
> list[StaticRoute] get_static_routes()

List the Static Routes for the Cohesity Cluster.

Returns the Static Routes for the Cohesity Cluster.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.StaticRouteApi()

try: 
    # List the Static Routes for the Cohesity Cluster.
    api_response = api_instance.get_static_routes()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling StaticRouteApi->get_static_routes: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[StaticRoute]**](StaticRoute.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_static_route**
> remove_static_route(ip)

Remove the specified Static Route from the Cohesity Cluster.

Returns the delete status upon completion.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.StaticRouteApi()
ip = 'ip_example' # str | Specifies the subnet IP of the route destination network.

try: 
    # Remove the specified Static Route from the Cohesity Cluster.
    api_instance.remove_static_route(ip)
except ApiException as e:
    print "Exception when calling StaticRouteApi->remove_static_route: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**| Specifies the subnet IP of the route destination network. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_static_route**
> StaticRoute update_static_route(ip, body=body)

Create or update a Static Route on the Cohesity Cluster.

Returns the created or updated Static Route on the Cohesity Cluster.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.StaticRouteApi()
ip = 'ip_example' # str | Specifies the subnet IP of the route destination network.
body = cohesity.StaticRoute() # StaticRoute |  (optional)

try: 
    # Create or update a Static Route on the Cohesity Cluster.
    api_response = api_instance.update_static_route(ip, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling StaticRouteApi->update_static_route: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**| Specifies the subnet IP of the route destination network. | 
 **body** | [**StaticRoute**](StaticRoute.md)|  | [optional] 

### Return type

[**StaticRoute**](StaticRoute.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

