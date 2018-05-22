# cohesity.GroupsApi

All URIs are relative to *https://localhost/irisservices/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_group**](GroupsApi.md#create_group) | **POST** /public/groups | Create or add a new group to the Cohesity Cluster.
[**delete_groups**](GroupsApi.md#delete_groups) | **DELETE** /public/groups | Delete one or more groups on the Cohesity Cluster.
[**get_groups**](GroupsApi.md#get_groups) | **GET** /public/groups | List the groups that match the filter criteria specified using parameters.
[**update_group**](GroupsApi.md#update_group) | **PUT** /public/groups | Update an existing group on the Cohesity Cluster. Only group settings on the Cohesity Cluster are updated. No changes are made to the referenced group principal on the Active Directory.


# **create_group**
> Group create_group(body=body)

Create or add a new group to the Cohesity Cluster.

If an Active Directory domain is specified, a new group is added to the Cohesity Cluster for the specified Active Directory group principal. If the LOCAL domain is specified, a new group is created directly in the default LOCAL domain on the Cohesity Cluster.  Returns the created or added group.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.GroupsApi()
body = cohesity.GroupParameters() # GroupParameters | Request to add or create a Group. (optional)

try: 
    # Create or add a new group to the Cohesity Cluster.
    api_response = api_instance.create_group(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling GroupsApi->create_group: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupParameters**](GroupParameters.md)| Request to add or create a Group. | [optional] 

### Return type

[**Group**](Group.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_groups**
> delete_groups(body=body)

Delete one or more groups on the Cohesity Cluster.

If the group on the Cohesity Cluster was added for an Active Directory user, the referenced principal group on the Active Directory domain is NOT deleted. Only the group on the Cohesity Cluster is deleted.  Returns Success if the specified groups are deleted.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.GroupsApi()
body = cohesity.GroupDeleteParameters() # GroupDeleteParameters | Request to delete one or more groups on the Cohesity Cluster. (optional)

try: 
    # Delete one or more groups on the Cohesity Cluster.
    api_instance.delete_groups(body=body)
except ApiException as e:
    print "Exception when calling GroupsApi->delete_groups: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupDeleteParameters**](GroupDeleteParameters.md)| Request to delete one or more groups on the Cohesity Cluster. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_groups**
> list[Group] get_groups(name=name, domain=domain)

List the groups that match the filter criteria specified using parameters.

If no parameters are specified, all groups currently on the Cohesity Cluster are returned. Specifying parameters filters the results that are returned.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.GroupsApi()
name = 'name_example' # str | Optionally specify a group name to filter by. (optional)
domain = 'domain_example' # str | If no domain is specified, all groups on the Cohesity Cluster are searched. If a domain is specified, only groups on the Cohesity Cluster associated with that domain are searched. (optional)

try: 
    # List the groups that match the filter criteria specified using parameters.
    api_response = api_instance.get_groups(name=name, domain=domain)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling GroupsApi->get_groups: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Optionally specify a group name to filter by. | [optional] 
 **domain** | **str**| If no domain is specified, all groups on the Cohesity Cluster are searched. If a domain is specified, only groups on the Cohesity Cluster associated with that domain are searched. | [optional] 

### Return type

[**list[Group]**](Group.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group**
> Group update_group(body=body)

Update an existing group on the Cohesity Cluster. Only group settings on the Cohesity Cluster are updated. No changes are made to the referenced group principal on the Active Directory.

Returns the group that was updated on the Cohesity Cluster.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.GroupsApi()
body = cohesity.GroupParameters() # GroupParameters | Request to update a group. (optional)

try: 
    # Update an existing group on the Cohesity Cluster. Only group settings on the Cohesity Cluster are updated. No changes are made to the referenced group principal on the Active Directory.
    api_response = api_instance.update_group(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling GroupsApi->update_group: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupParameters**](GroupParameters.md)| Request to update a group. | [optional] 

### Return type

[**Group**](Group.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

