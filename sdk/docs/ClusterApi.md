# cohesity.ClusterApi

All URIs are relative to *https://localhost/irisservices/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_basic_cluster_info**](ClusterApi.md#get_basic_cluster_info) | **GET** /public/basicClusterInfo | List details about the Cohesity Cluster such as the name, type, version, language, locale and domains. This operation does not require authentication.
[**get_cluster**](ClusterApi.md#get_cluster) | **GET** /public/cluster | List details about this Cohesity Cluster.
[**update_cluster_params**](ClusterApi.md#update_cluster_params) | **PUT** /public/cluster | Update the configuration of this Cohesity Cluster.


# **get_basic_cluster_info**
> BasicClusterInfo get_basic_cluster_info()

List details about the Cohesity Cluster such as the name, type, version, language, locale and domains. This operation does not require authentication.

All Active Directory domains that are currently joined to the Cohesity Cluster are returned. In addition, the default LOCAL domain on the Cohesity Cluster is returned as the first element of the domains array in the response.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ClusterApi()

try: 
    # List details about the Cohesity Cluster such as the name, type, version, language, locale and domains. This operation does not require authentication.
    api_response = api_instance.get_basic_cluster_info()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ClusterApi->get_basic_cluster_info: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BasicClusterInfo**](BasicClusterInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster**
> Cluster get_cluster(fetch_stats=fetch_stats)

List details about this Cohesity Cluster.

Returns information about this Cohesity Cluster.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ClusterApi()
fetch_stats = true # bool | If 'true', also get statistics about the Cohesity Cluster. (optional)

try: 
    # List details about this Cohesity Cluster.
    api_response = api_instance.get_cluster(fetch_stats=fetch_stats)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ClusterApi->get_cluster: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fetch_stats** | **bool**| If &#39;true&#39;, also get statistics about the Cohesity Cluster. | [optional] 

### Return type

[**Cluster**](Cluster.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_params**
> Cluster update_cluster_params(body=body)

Update the configuration of this Cohesity Cluster.

Returns the updated Cluster configuration.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ClusterApi()
body = cohesity.UpdateClusterParams() # UpdateClusterParams | Update Cluster Parameter. (optional)

try: 
    # Update the configuration of this Cohesity Cluster.
    api_response = api_instance.update_cluster_params(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ClusterApi->update_cluster_params: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateClusterParams**](UpdateClusterParams.md)| Update Cluster Parameter. | [optional] 

### Return type

[**Cluster**](Cluster.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

