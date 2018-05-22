# cohesity.PrincipalsApi

All URIs are relative to *https://localhost/irisservices/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](PrincipalsApi.md#create_user) | **POST** /public/users | Create or add a new user to the Cohesity Cluster.
[**delete_users**](PrincipalsApi.md#delete_users) | **DELETE** /public/users | Delete one or more users on the Cohesity Cluster.
[**get_user_privileges**](PrincipalsApi.md#get_user_privileges) | **GET** /public/users/privileges | List the privileges of the session user.
[**get_users**](PrincipalsApi.md#get_users) | **GET** /public/users | List the users on the Cohesity Cluster that match the filter criteria specified using parameters.
[**list_sources_for_principals**](PrincipalsApi.md#list_sources_for_principals) | **GET** /public/principals/protectionSources | Returns the Protection Sources objects and View names that the principals have permissions to access.
[**reset_s3_secret_key**](PrincipalsApi.md#reset_s3_secret_key) | **POST** /public/users/s3SecretKey | Reset the S3 secret access key for the specified user on the Cohesity Cluster.
[**search_principals**](PrincipalsApi.md#search_principals) | **GET** /public/principals/searchPrincipals | List the user and group principals that match the filter criteria specified using parameters.
[**update_sources_for_principals**](PrincipalsApi.md#update_sources_for_principals) | **PUT** /public/principals/protectionSources | Set the Protection Sources and Views that the specified principal has permissions to access.
[**update_user**](PrincipalsApi.md#update_user) | **PUT** /public/users | Update an existing user on the Cohesity Cluster. Only user settings on the Cohesity Cluster are updated. No changes are made to the referenced user principal on the Active Directory.


# **create_user**
> User create_user(body=body)

Create or add a new user to the Cohesity Cluster.

If an Active Directory domain is specified, a new user is added to the Cohesity Cluster for the specified Active Directory user principal. If the LOCAL domain is specified, a new user is created directly in the default LOCAL domain on the Cohesity Cluster.  Returns the created or added user.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.PrincipalsApi()
body = cohesity.UserParameters() # UserParameters | Request to add or create a new user. (optional)

try: 
    # Create or add a new user to the Cohesity Cluster.
    api_response = api_instance.create_user(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PrincipalsApi->create_user: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserParameters**](UserParameters.md)| Request to add or create a new user. | [optional] 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_users**
> delete_users(body=body)

Delete one or more users on the Cohesity Cluster.

Only users from the same domain can be deleted by a single request. If the Cohesity user was created for an Active Directory user, the referenced principal user on the Active Directory domain is NOT deleted. Only the user on the Cohesity Cluster is deleted. Returns Success if the specified users are deleted.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.PrincipalsApi()
body = cohesity.UserDeleteParameters() # UserDeleteParameters | Request to delete one or more users on the Cohesity Cluster. (optional)

try: 
    # Delete one or more users on the Cohesity Cluster.
    api_instance.delete_users(body=body)
except ApiException as e:
    print "Exception when calling PrincipalsApi->delete_users: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserDeleteParameters**](UserDeleteParameters.md)| Request to delete one or more users on the Cohesity Cluster. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_privileges**
> list[str] get_user_privileges()

List the privileges of the session user.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.PrincipalsApi()

try: 
    # List the privileges of the session user.
    api_response = api_instance.get_user_privileges()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PrincipalsApi->get_user_privileges: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> list[User] get_users(domain=domain, usernames=usernames, email_addresses=email_addresses)

List the users on the Cohesity Cluster that match the filter criteria specified using parameters.

If no parameters are specified, all users currently on the Cohesity Cluster are returned. Specifying parameters filters the results that are returned.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.PrincipalsApi()
domain = 'domain_example' # str | Optionally specify a domain to filter by. If no domain is specified, all users on the Cohesity Cluster are searched. If a domain is specified, only users on the Cohesity Cluster associated with that domain are searched. (optional)
usernames = ['usernames_example'] # list[str] | Optionally specify a list of usernames to filter by. (optional)
email_addresses = ['email_addresses_example'] # list[str] | Optionally specify a list of email addresses to filter by. (optional)

try: 
    # List the users on the Cohesity Cluster that match the filter criteria specified using parameters.
    api_response = api_instance.get_users(domain=domain, usernames=usernames, email_addresses=email_addresses)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PrincipalsApi->get_users: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Optionally specify a domain to filter by. If no domain is specified, all users on the Cohesity Cluster are searched. If a domain is specified, only users on the Cohesity Cluster associated with that domain are searched. | [optional] 
 **usernames** | [**list[str]**](str.md)| Optionally specify a list of usernames to filter by. | [optional] 
 **email_addresses** | [**list[str]**](str.md)| Optionally specify a list of email addresses to filter by. | [optional] 

### Return type

[**list[User]**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sources_for_principals**
> list[SourcesForSid] list_sources_for_principals(sids=sids)

Returns the Protection Sources objects and View names that the principals have permissions to access.

From the passed in list principals (specified by SIDs), return the list of Protection Sources objects and View names that each principal has permission to access.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.PrincipalsApi()
sids = ['sids_example'] # list[str] | Specifies a list of security identifiers (SIDs) that specify user or group principals. (optional)

try: 
    # Returns the Protection Sources objects and View names that the principals have permissions to access.
    api_response = api_instance.list_sources_for_principals(sids=sids)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PrincipalsApi->list_sources_for_principals: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sids** | [**list[str]**](str.md)| Specifies a list of security identifiers (SIDs) that specify user or group principals. | [optional] 

### Return type

[**list[SourcesForSid]**](SourcesForSid.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_s3_secret_key**
> NewS3SecretAccessKey reset_s3_secret_key(body=body)

Reset the S3 secret access key for the specified user on the Cohesity Cluster.

Returns the new key that was generated.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.PrincipalsApi()
body = cohesity.ResetS3SecretKeyParameters() # ResetS3SecretKeyParameters | Request to reset the S3 secret access key for the specified Cohesity user. (optional)

try: 
    # Reset the S3 secret access key for the specified user on the Cohesity Cluster.
    api_response = api_instance.reset_s3_secret_key(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PrincipalsApi->reset_s3_secret_key: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResetS3SecretKeyParameters**](ResetS3SecretKeyParameters.md)| Request to reset the S3 secret access key for the specified Cohesity user. | [optional] 

### Return type

[**NewS3SecretAccessKey**](NewS3SecretAccessKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_principals**
> list[Principal] search_principals(domain=domain, object_class=object_class, search=search, sids=sids)

List the user and group principals that match the filter criteria specified using parameters.

Optionally limit the search results by specifying security identifiers (SIDs), an object class (user or group) or a substring. You can specify SIDs or a substring but not both.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.PrincipalsApi()
domain = 'domain_example' # str | Specifies the domain name of the principals to search. If specified the principals in that domain are searched. Domain could be an Active Directory domain joined by the Cluster or any one of the trusted domains of the Active Directory domain or the LOCAL domain. If not specified, all the domains are searched. (optional)
object_class = 'object_class_example' # str | Optionally filter by a principal object class such as 'kGroup' or 'kUser'. If 'kGroup' is specified, only group principals are returned. If 'kUser' is specified, only user principals are returned. If not specified, both group and user principals are returned. 'kUser' specifies a user object class. 'kGroup' specifies a group object class. (optional)
search = 'search_example' # str | Optionally filter by matching a substring. Only principals in the with a name or sAMAccountName that matches part or all of the specified substring are returned. If specified, a 'sids' parameter should not be specified. (optional)
sids = ['sids_example'] # list[str] | Optionally filter by a list of security identifiers (SIDs) found in the specified domain. Only principals matching the specified SIDs are returned. If specified, a 'search' parameter should not be specified. (optional)

try: 
    # List the user and group principals that match the filter criteria specified using parameters.
    api_response = api_instance.search_principals(domain=domain, object_class=object_class, search=search, sids=sids)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PrincipalsApi->search_principals: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Specifies the domain name of the principals to search. If specified the principals in that domain are searched. Domain could be an Active Directory domain joined by the Cluster or any one of the trusted domains of the Active Directory domain or the LOCAL domain. If not specified, all the domains are searched. | [optional] 
 **object_class** | **str**| Optionally filter by a principal object class such as &#39;kGroup&#39; or &#39;kUser&#39;. If &#39;kGroup&#39; is specified, only group principals are returned. If &#39;kUser&#39; is specified, only user principals are returned. If not specified, both group and user principals are returned. &#39;kUser&#39; specifies a user object class. &#39;kGroup&#39; specifies a group object class. | [optional] 
 **search** | **str**| Optionally filter by matching a substring. Only principals in the with a name or sAMAccountName that matches part or all of the specified substring are returned. If specified, a &#39;sids&#39; parameter should not be specified. | [optional] 
 **sids** | [**list[str]**](str.md)| Optionally filter by a list of security identifiers (SIDs) found in the specified domain. Only principals matching the specified SIDs are returned. If specified, a &#39;search&#39; parameter should not be specified. | [optional] 

### Return type

[**list[Principal]**](Principal.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sources_for_principals**
> update_sources_for_principals(body)

Set the Protection Sources and Views that the specified principal has permissions to access.

Specify the security identifier (SID) of the principal to grant access permissions for.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.PrincipalsApi()
body = cohesity.UpdateSourcesForPrincipalsParams() # UpdateSourcesForPrincipalsParams | Request to set access permissions to Protection Sources and Views for a principal.

try: 
    # Set the Protection Sources and Views that the specified principal has permissions to access.
    api_instance.update_sources_for_principals(body)
except ApiException as e:
    print "Exception when calling PrincipalsApi->update_sources_for_principals: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateSourcesForPrincipalsParams**](UpdateSourcesForPrincipalsParams.md)| Request to set access permissions to Protection Sources and Views for a principal. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> User update_user(body=body)

Update an existing user on the Cohesity Cluster. Only user settings on the Cohesity Cluster are updated. No changes are made to the referenced user principal on the Active Directory.

Returns the user that was updated on the Cohesity Cluster.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.PrincipalsApi()
body = cohesity.UserParameters() # UserParameters | Request to update an existing user. (optional)

try: 
    # Update an existing user on the Cohesity Cluster. Only user settings on the Cohesity Cluster are updated. No changes are made to the referenced user principal on the Active Directory.
    api_response = api_instance.update_user(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PrincipalsApi->update_user: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserParameters**](UserParameters.md)| Request to update an existing user. | [optional] 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

