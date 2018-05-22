# cohesity.VlanApi

All URIs are relative to *https://localhost/irisservices/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_vlan_by_id**](VlanApi.md#get_vlan_by_id) | **GET** /public/vlans/{id} | List the details about a single VLAN.
[**get_vlans**](VlanApi.md#get_vlans) | **GET** /public/vlans | List the VLANs for the Cohesity Cluster.
[**remove_vlan**](VlanApi.md#remove_vlan) | **DELETE** /public/vlans/{id} | Remove the specified VLAN from the Cohesity Cluster.
[**update_vlan**](VlanApi.md#update_vlan) | **PUT** /public/vlans/{id} | Creates or updates a VLAN of the Cohesity Cluster.


# **get_vlan_by_id**
> Vlan get_vlan_by_id(id)

List the details about a single VLAN.

Returns the VLAN corresponding to the specified VLAN ID.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.VlanApi()
id = 56 # int | Specifies the id of the VLAN.

try: 
    # List the details about a single VLAN.
    api_response = api_instance.get_vlan_by_id(id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling VlanApi->get_vlan_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the VLAN. | 

### Return type

[**Vlan**](Vlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vlans**
> list[Vlan] get_vlans()

List the VLANs for the Cohesity Cluster.

Returns the VLANs for the Cohesity Cluster.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.VlanApi()

try: 
    # List the VLANs for the Cohesity Cluster.
    api_response = api_instance.get_vlans()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling VlanApi->get_vlans: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Vlan]**](Vlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_vlan**
> remove_vlan(id)

Remove the specified VLAN from the Cohesity Cluster.

Returns the delete status upon completion.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.VlanApi()
id = 56 # int | Specifies the id of the VLAN.

try: 
    # Remove the specified VLAN from the Cohesity Cluster.
    api_instance.remove_vlan(id)
except ApiException as e:
    print "Exception when calling VlanApi->remove_vlan: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the VLAN. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vlan**
> Vlan update_vlan(id, body=body)

Creates or updates a VLAN of the Cohesity Cluster.

Returns the created or updated VLAN on the Cohesity Cluster.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.VlanApi()
id = 56 # int | Specifies the id of the VLAN.
body = cohesity.Vlan() # Vlan |  (optional)

try: 
    # Creates or updates a VLAN of the Cohesity Cluster.
    api_response = api_instance.update_vlan(id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling VlanApi->update_vlan: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the VLAN. | 
 **body** | [**Vlan**](Vlan.md)|  | [optional] 

### Return type

[**Vlan**](Vlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

