# cohesity.RolesApi

All URIs are relative to *https://localhost/irisservices/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_role**](RolesApi.md#create_role) | **POST** /public/roles | Create a new custom role.
[**delete_roles**](RolesApi.md#delete_roles) | **DELETE** /public/roles | Delete one or more custom Roles.
[**get_roles**](RolesApi.md#get_roles) | **GET** /public/roles | List the roles defined on the Cohesity Cluster.
[**update_role**](RolesApi.md#update_role) | **PUT** /public/roles/{name} | Update a user-defined custom role.


# **create_role**
> Role create_role(body=body)

Create a new custom role.

Returns the new custom role that was created. A custom role is a user-defined role that is created using the REST API, the Cohesity Cluster or the CLI.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.RolesApi()
body = cohesity.RoleCreateParameters() # RoleCreateParameters | Request to create a new custom Role. (optional)

try: 
    # Create a new custom role.
    api_response = api_instance.create_role(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RolesApi->create_role: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RoleCreateParameters**](RoleCreateParameters.md)| Request to create a new custom Role. | [optional] 

### Return type

[**Role**](Role.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_roles**
> delete_roles(body=body)

Delete one or more custom Roles.

Returns Success if all the specified Roles are deleted.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.RolesApi()
body = cohesity.RoleDeleteParameters() # RoleDeleteParameters | Request to delete one or more Roles. (optional)

try: 
    # Delete one or more custom Roles.
    api_instance.delete_roles(body=body)
except ApiException as e:
    print "Exception when calling RolesApi->delete_roles: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RoleDeleteParameters**](RoleDeleteParameters.md)| Request to delete one or more Roles. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_roles**
> list[Role] get_roles(name=name)

List the roles defined on the Cohesity Cluster.

If the 'name' parameter is not specified, all roles defined on the Cohesity Cluster are returned. In addition, information about each role is returned such as the name, description, assigned privileges, etc. If an exact role name (such as COHESITY_VIEWER) is specified in the 'name' parameter, only information about that single role is returned.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.RolesApi()
name = 'name_example' # str | Specifies the name of the role. (optional)

try: 
    # List the roles defined on the Cohesity Cluster.
    api_response = api_instance.get_roles(name=name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RolesApi->get_roles: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Specifies the name of the role. | [optional] 

### Return type

[**list[Role]**](Role.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role**
> Role update_role(name, body=body)

Update a user-defined custom role.

For example, you could update the privileges assigned to a Role. Returns the updated role.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.RolesApi()
name = 'name_example' # str | Specifies the name of the role to update.
body = cohesity.RoleUpdateParameters() # RoleUpdateParameters | Request to update a custom role. (optional)

try: 
    # Update a user-defined custom role.
    api_response = api_instance.update_role(name, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RolesApi->update_role: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Specifies the name of the role to update. | 
 **body** | [**RoleUpdateParameters**](RoleUpdateParameters.md)| Request to update a custom role. | [optional] 

### Return type

[**Role**](Role.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

