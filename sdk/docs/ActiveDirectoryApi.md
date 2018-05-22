# cohesity.ActiveDirectoryApi

All URIs are relative to *https://localhost/irisservices/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_active_directory_principals**](ActiveDirectoryApi.md#add_active_directory_principals) | **POST** /public/activeDirectory/principals | Add multiple groups or users on the Cohesity Cluster for the specified Active Directory principals. In addition, assign Cohesity roles to the users or groups to define their Cohesity privileges.
[**create_active_directory_entry**](ActiveDirectoryApi.md#create_active_directory_entry) | **POST** /public/activeDirectory | Join the Cohesity Cluster to the specified Active Directory.
[**delete_active_directory_entry**](ActiveDirectoryApi.md#delete_active_directory_entry) | **DELETE** /public/activeDirectory | Deletes the join with the Active Directory.
[**get_active_directory_entry**](ActiveDirectoryApi.md#get_active_directory_entry) | **GET** /public/activeDirectory | Lists the Active Directories that the Cohesity Cluster has joined.
[**list_centrify_zones**](ActiveDirectoryApi.md#list_centrify_zones) | **GET** /public/activeDirectory/centrifyZones | Fetches the list centrify zones of an active directory domain.
[**search_active_directory_principals**](ActiveDirectoryApi.md#search_active_directory_principals) | **GET** /public/activeDirectory/principals | List the user and group principals in the Active Directory that match the filter criteria specified using parameters.
[**update_active_directory_id_mapping**](ActiveDirectoryApi.md#update_active_directory_id_mapping) | **PUT** /public/activeDirectory/{name}/idMappingInfo | Updates the user id mapping info of an Active Directory.
[**update_active_directory_machine_accounts**](ActiveDirectoryApi.md#update_active_directory_machine_accounts) | **POST** /public/activeDirectory/{name}/machineAccounts | Updates the machine accounts of an Active Directory.


# **add_active_directory_principals**
> list[AddedActiveDirectoryPrincipal] add_active_directory_principals(body=body)

Add multiple groups or users on the Cohesity Cluster for the specified Active Directory principals. In addition, assign Cohesity roles to the users or groups to define their Cohesity privileges.

After a group or user has been added to a Cohesity Cluster, the referenced Active Directory principal can be used by the Cohesity Cluster. In addition, this operation maps Cohesity roles with a group or user and this mapping defines the privileges allowed on the Cohesity Cluster for the group or user. For example if an 'management' group is created on the Cohesity Cluster for the Active Directory 'management' principal group and is associated with the Cohesity 'View' role, all users in the referenced Active Directory 'management' principal group can log in to the Cohesity Dashboard but will only have view-only privileges. These users cannot create new Protection Jobs, Policies, Views, etc.  NOTE: Local Cohesity users and groups cannot be created by this operation. Local Cohesity users or groups do not have an associated Active Directory principals and are created directly in the default LOCAL domain.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ActiveDirectoryApi()
body = [cohesity.ActiveDirectoryPrincipalsAddParameters()] # list[ActiveDirectoryPrincipalsAddParameters] | Request to add groups or users to the Cohesity Cluster. (optional)

try: 
    # Add multiple groups or users on the Cohesity Cluster for the specified Active Directory principals. In addition, assign Cohesity roles to the users or groups to define their Cohesity privileges.
    api_response = api_instance.add_active_directory_principals(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ActiveDirectoryApi->add_active_directory_principals: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ActiveDirectoryPrincipalsAddParameters]**](ActiveDirectoryPrincipalsAddParameters.md)| Request to add groups or users to the Cohesity Cluster. | [optional] 

### Return type

[**list[AddedActiveDirectoryPrincipal]**](AddedActiveDirectoryPrincipal.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_active_directory_entry**
> ActiveDirectoryEntry create_active_directory_entry(body)

Join the Cohesity Cluster to the specified Active Directory.

After a Cohesity Cluster has been joined to an Active Directory domain, the users and groups in the domain can be authenticated on the Cohesity Cluster using their Active Directory credentials.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ActiveDirectoryApi()
body = cohesity.ActiveDirectoryEntry() # ActiveDirectoryEntry | Request to join an Active Directory.

try: 
    # Join the Cohesity Cluster to the specified Active Directory.
    api_response = api_instance.create_active_directory_entry(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ActiveDirectoryApi->create_active_directory_entry: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ActiveDirectoryEntry**](ActiveDirectoryEntry.md)| Request to join an Active Directory. | 

### Return type

[**ActiveDirectoryEntry**](ActiveDirectoryEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_active_directory_entry**
> delete_active_directory_entry(body)

Deletes the join with the Active Directory.

Deletes the join of the Cohesity Cluster to the specified Active Directory domain. After the deletion, the Cohesity Cluster no longer has access to the principals on the Active Directory. For example, you can no longer log in to the Cohesity Cluster with a user defined in a principal group of the Active Directory domain.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ActiveDirectoryApi()
body = cohesity.ActiveDirectoryEntry() # ActiveDirectoryEntry | Request to delete a join with an Active Directory.

try: 
    # Deletes the join with the Active Directory.
    api_instance.delete_active_directory_entry(body)
except ApiException as e:
    print "Exception when calling ActiveDirectoryApi->delete_active_directory_entry: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ActiveDirectoryEntry**](ActiveDirectoryEntry.md)| Request to delete a join with an Active Directory. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_active_directory_entry**
> list[ActiveDirectoryEntry] get_active_directory_entry()

Lists the Active Directories that the Cohesity Cluster has joined.

After a Cohesity Cluster has been joined to an Active Directory domain, the users and groups in the domain can be authenticated on the Cohesity Cluster using their Active Directory credentials.  NOTE: The userName and password fields are not populated by this operation.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ActiveDirectoryApi()

try: 
    # Lists the Active Directories that the Cohesity Cluster has joined.
    api_response = api_instance.get_active_directory_entry()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ActiveDirectoryApi->get_active_directory_entry: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ActiveDirectoryEntry]**](ActiveDirectoryEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_centrify_zones**
> list[ListCentrifyZone] list_centrify_zones(domain_name=domain_name)

Fetches the list centrify zones of an active directory domain.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ActiveDirectoryApi()
domain_name = 'domain_name_example' # str | Specifies the fully qualified domain name (FQDN) of an Active Directory. (optional)

try: 
    # Fetches the list centrify zones of an active directory domain.
    api_response = api_instance.list_centrify_zones(domain_name=domain_name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ActiveDirectoryApi->list_centrify_zones: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**| Specifies the fully qualified domain name (FQDN) of an Active Directory. | [optional] 

### Return type

[**list[ListCentrifyZone]**](ListCentrifyZone.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_active_directory_principals**
> list[ActiveDirectoryPrincipal] search_active_directory_principals(domain=domain, object_class=object_class, search=search, sids=sids)

List the user and group principals in the Active Directory that match the filter criteria specified using parameters.

Optionally limit the search results by specifying security identifiers (SIDs), an object class (user or group) or a substring. You can specify SIDs or a substring but not both.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ActiveDirectoryApi()
domain = 'domain_example' # str | Specifies the domain name of the principals to search. If specified the principals in that domain are searched. Domain could be an Active Directory domain joined by the Cluster or any one of the trusted domains of the Active Directory domain or the LOCAL domain. If not specified, all the domains are searched. (optional)
object_class = 'object_class_example' # str | Optionally filter by a principal object class such as 'kGroup' or 'kUser'. If 'kGroup' is specified, only group principals are returned. If 'kUser' is specified, only user principals are returned. If not specified, both group and user principals are returned. 'kUser' specifies a user object class. 'kGroup' specifies a group object class. (optional)
search = 'search_example' # str | Optionally filter by matching a substring. Only principals in the with a name or sAMAccountName that matches part or all of the specified substring are returned. If specified, a 'sids' parameter should not be specified. (optional)
sids = ['sids_example'] # list[str] | Optionally filter by a list of security identifiers (SIDs) found in the specified domain. Only principals matching the specified SIDs are returned. If specified, a 'search' parameter should not be specified. (optional)

try: 
    # List the user and group principals in the Active Directory that match the filter criteria specified using parameters.
    api_response = api_instance.search_active_directory_principals(domain=domain, object_class=object_class, search=search, sids=sids)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ActiveDirectoryApi->search_active_directory_principals: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Specifies the domain name of the principals to search. If specified the principals in that domain are searched. Domain could be an Active Directory domain joined by the Cluster or any one of the trusted domains of the Active Directory domain or the LOCAL domain. If not specified, all the domains are searched. | [optional] 
 **object_class** | **str**| Optionally filter by a principal object class such as &#39;kGroup&#39; or &#39;kUser&#39;. If &#39;kGroup&#39; is specified, only group principals are returned. If &#39;kUser&#39; is specified, only user principals are returned. If not specified, both group and user principals are returned. &#39;kUser&#39; specifies a user object class. &#39;kGroup&#39; specifies a group object class. | [optional] 
 **search** | **str**| Optionally filter by matching a substring. Only principals in the with a name or sAMAccountName that matches part or all of the specified substring are returned. If specified, a &#39;sids&#39; parameter should not be specified. | [optional] 
 **sids** | [**list[str]**](str.md)| Optionally filter by a list of security identifiers (SIDs) found in the specified domain. Only principals matching the specified SIDs are returned. If specified, a &#39;search&#39; parameter should not be specified. | [optional] 

### Return type

[**list[ActiveDirectoryPrincipal]**](ActiveDirectoryPrincipal.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_active_directory_id_mapping**
> ActiveDirectoryEntry update_active_directory_id_mapping(body, name)

Updates the user id mapping info of an Active Directory.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ActiveDirectoryApi()
body = cohesity.IdMappingInfo() # IdMappingInfo | Request to update user id mapping of an Active Directory.
name = 'name_example' # str | Specifies the Active Directory Domain Name.

try: 
    # Updates the user id mapping info of an Active Directory.
    api_response = api_instance.update_active_directory_id_mapping(body, name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ActiveDirectoryApi->update_active_directory_id_mapping: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdMappingInfo**](IdMappingInfo.md)| Request to update user id mapping of an Active Directory. | 
 **name** | **str**| Specifies the Active Directory Domain Name. | 

### Return type

[**ActiveDirectoryEntry**](ActiveDirectoryEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_active_directory_machine_accounts**
> ActiveDirectoryEntry update_active_directory_machine_accounts(body, name)

Updates the machine accounts of an Active Directory.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ActiveDirectoryApi()
body = cohesity.UpdateMachineAccountsParams() # UpdateMachineAccountsParams | Request to update machine accounts of an Active Directory.
name = 'name_example' # str | Specifies the Active Directory Domain Name.

try: 
    # Updates the machine accounts of an Active Directory.
    api_response = api_instance.update_active_directory_machine_accounts(body, name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ActiveDirectoryApi->update_active_directory_machine_accounts: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateMachineAccountsParams**](UpdateMachineAccountsParams.md)| Request to update machine accounts of an Active Directory. | 
 **name** | **str**| Specifies the Active Directory Domain Name. | 

### Return type

[**ActiveDirectoryEntry**](ActiveDirectoryEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

