# cohesity.ProtectionPoliciesApi

All URIs are relative to *https://localhost/irisservices/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_protection_policy**](ProtectionPoliciesApi.md#create_protection_policy) | **POST** /public/protectionPolicies | Create a Protection Policy.
[**delete_protection_policy**](ProtectionPoliciesApi.md#delete_protection_policy) | **DELETE** /public/protectionPolicies/{id} | Delete a Protection Policy.
[**get_protection_policies**](ProtectionPoliciesApi.md#get_protection_policies) | **GET** /public/protectionPolicies | List Protection Policies filtered by some parameters.
[**get_protection_policy_by_id**](ProtectionPoliciesApi.md#get_protection_policy_by_id) | **GET** /public/protectionPolicies/{id} | List details about a single Protection Policy.
[**update_protection_policy**](ProtectionPoliciesApi.md#update_protection_policy) | **PUT** /public/protectionPolicies/{id} | Update a Protection Policy.


# **create_protection_policy**
> ProtectionPolicy create_protection_policy(body)

Create a Protection Policy.

Returns the created Protection Policy.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ProtectionPoliciesApi()
body = cohesity.ProtectionPolicyRequest() # ProtectionPolicyRequest | Request to create a Protection Policy.

try: 
    # Create a Protection Policy.
    api_response = api_instance.create_protection_policy(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProtectionPoliciesApi->create_protection_policy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProtectionPolicyRequest**](ProtectionPolicyRequest.md)| Request to create a Protection Policy. | 

### Return type

[**ProtectionPolicy**](ProtectionPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_protection_policy**
> delete_protection_policy(id)

Delete a Protection Policy.

Returns Success if the Protection Policy is deleted.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ProtectionPoliciesApi()
id = 'id_example' # str | Specifies a unique id of the Protection Policy to return.

try: 
    # Delete a Protection Policy.
    api_instance.delete_protection_policy(id)
except ApiException as e:
    print "Exception when calling ProtectionPoliciesApi->delete_protection_policy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the Protection Policy to return. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_protection_policies**
> list[ProtectionPolicy] get_protection_policies(ids=ids, names=names, environments=environments)

List Protection Policies filtered by some parameters.

If no parameters are specified, all Protection Policies currently on the Cohesity Cluster are returned. Specifying parameters filters the results that are returned.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ProtectionPoliciesApi()
ids = ['ids_example'] # list[str] | Filter by a list of Protection Policy ids. (optional)
names = ['names_example'] # list[str] | Filter by a list of Protection Policy names. (optional)
environments = ['environments_example'] # list[str] | Filter by Environment type such as 'kView', 'kSQL', 'kVMware', 'kPuppeteer' 'kPhysical', 'kPure', 'kNetapp', 'kGenericNas', 'kHyperV', 'kAcropolis', or 'kAzure' Only Policies protecting the specified environment type are returned. NOTE: 'kPuppeteer' refers to Cohesity's Remote Adapter. (optional)

try: 
    # List Protection Policies filtered by some parameters.
    api_response = api_instance.get_protection_policies(ids=ids, names=names, environments=environments)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProtectionPoliciesApi->get_protection_policies: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[str]**](str.md)| Filter by a list of Protection Policy ids. | [optional] 
 **names** | [**list[str]**](str.md)| Filter by a list of Protection Policy names. | [optional] 
 **environments** | [**list[str]**](str.md)| Filter by Environment type such as &#39;kView&#39;, &#39;kSQL&#39;, &#39;kVMware&#39;, &#39;kPuppeteer&#39; &#39;kPhysical&#39;, &#39;kPure&#39;, &#39;kNetapp&#39;, &#39;kGenericNas&#39;, &#39;kHyperV&#39;, &#39;kAcropolis&#39;, or &#39;kAzure&#39; Only Policies protecting the specified environment type are returned. NOTE: &#39;kPuppeteer&#39; refers to Cohesity&#39;s Remote Adapter. | [optional] 

### Return type

[**list[ProtectionPolicy]**](ProtectionPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_protection_policy_by_id**
> ProtectionPolicy get_protection_policy_by_id(id)

List details about a single Protection Policy.

Returns the Protection Policy corresponding to the specified Policy Id.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ProtectionPoliciesApi()
id = 'id_example' # str | Specifies a unique id of the Protection Policy to return.

try: 
    # List details about a single Protection Policy.
    api_response = api_instance.get_protection_policy_by_id(id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProtectionPoliciesApi->get_protection_policy_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies a unique id of the Protection Policy to return. | 

### Return type

[**ProtectionPolicy**](ProtectionPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_protection_policy**
> ProtectionPolicy update_protection_policy(body, id)

Update a Protection Policy.

Returns the updated Protection Policy.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ProtectionPoliciesApi()
body = cohesity.ProtectionPolicyRequest() # ProtectionPolicyRequest | Request to update a Protection Policy.
id = 'id_example' # str | Specifies a unique id of the Protection Policy to return.

try: 
    # Update a Protection Policy.
    api_response = api_instance.update_protection_policy(body, id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProtectionPoliciesApi->update_protection_policy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProtectionPolicyRequest**](ProtectionPolicyRequest.md)| Request to update a Protection Policy. | 
 **id** | **str**| Specifies a unique id of the Protection Policy to return. | 

### Return type

[**ProtectionPolicy**](ProtectionPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

