# cohesity.ViewsApi

All URIs are relative to *https://localhost/irisservices/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clone_directory**](ViewsApi.md#clone_directory) | **POST** /public/views/cloneDirectory | Clone a directory of a view.
[**clone_view**](ViewsApi.md#clone_view) | **POST** /public/views/clone | Clone a View.
[**create_view**](ViewsApi.md#create_view) | **POST** /public/views | Create a View.
[**create_view_alias**](ViewsApi.md#create_view_alias) | **POST** /public/viewAliases | Create a View Alias. A View Alias allows a directory inside the view to be mounted without specifying the entire path.
[**create_view_user_quota**](ViewsApi.md#create_view_user_quota) | **POST** /public/viewUserQuotas | Create a new quota policy for a user in a view.
[**delete_view**](ViewsApi.md#delete_view) | **DELETE** /public/views/{name} | Delete a View.
[**delete_view_alias**](ViewsApi.md#delete_view_alias) | **DELETE** /public/viewAliases/{name} | Delete a View Alias.
[**delete_view_users_quota**](ViewsApi.md#delete_view_users_quota) | **DELETE** /public/viewUserQuotas | Delete the quota policy overrides for users in a view.
[**get_view_by_name**](ViewsApi.md#get_view_by_name) | **GET** /public/views/{name} | List details about a single View.
[**get_view_user_quotas**](ViewsApi.md#get_view_user_quotas) | **GET** /public/viewUserQuotas | Get the quota policies, usage and summary for a view for all its users. It can also fetch the quota policies, usage and summary for a user in all his views.
[**get_views**](ViewsApi.md#get_views) | **GET** /public/views | List Views filtered by some parameters.
[**get_views_by_share_name**](ViewsApi.md#get_views_by_share_name) | **GET** /public/shares | List shares filtered by name.
[**overwrite_view**](ViewsApi.md#overwrite_view) | **POST** /public/views/overwrite | Overwrites a Target view with contents of a Source view.
[**rename_view**](ViewsApi.md#rename_view) | **POST** /public/views/rename/{name} | Rename a View.
[**update_user_quota_settings**](ViewsApi.md#update_user_quota_settings) | **PUT** /public/viewUserQuotasSettings | Update the user quota settings in a view.
[**update_view**](ViewsApi.md#update_view) | **PUT** /public/views/{name} | Update a View.
[**update_view_user_quota**](ViewsApi.md#update_view_user_quota) | **PUT** /public/viewUserQuotas | Update a new quota policy for a user in a view.


# **clone_directory**
> clone_directory(body)

Clone a directory of a view.

Returns error if op fails.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ViewsApi()
body = cohesity.CloneDirectoryParams() # CloneDirectoryParams | Request to clone a directory.

try: 
    # Clone a directory of a view.
    api_instance.clone_directory(body)
except ApiException as e:
    print "Exception when calling ViewsApi->clone_directory: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloneDirectoryParams**](CloneDirectoryParams.md)| Request to clone a directory. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clone_view**
> View clone_view(body)

Clone a View.

Returns the cloned View.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ViewsApi()
body = cohesity.CloneViewRequest() # CloneViewRequest | Request to clone a View.

try: 
    # Clone a View.
    api_response = api_instance.clone_view(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ViewsApi->clone_view: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloneViewRequest**](CloneViewRequest.md)| Request to clone a View. | 

### Return type

[**View**](View.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_view**
> View create_view(body)

Create a View.

Returns the created View.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ViewsApi()
body = cohesity.CreateViewRequest() # CreateViewRequest | Request to create a View.

try: 
    # Create a View.
    api_response = api_instance.create_view(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ViewsApi->create_view: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateViewRequest**](CreateViewRequest.md)| Request to create a View. | 

### Return type

[**View**](View.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_view_alias**
> ViewAlias create_view_alias(body)

Create a View Alias. A View Alias allows a directory inside the view to be mounted without specifying the entire path.

Returns the created View Alias.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ViewsApi()
body = cohesity.ViewAlias() # ViewAlias | Request to create a View.

try: 
    # Create a View Alias. A View Alias allows a directory inside the view to be mounted without specifying the entire path.
    api_response = api_instance.create_view_alias(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ViewsApi->create_view_alias: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ViewAlias**](ViewAlias.md)| Request to create a View. | 

### Return type

[**ViewAlias**](ViewAlias.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_view_user_quota**
> UserQuotaAndUsage create_view_user_quota(body=body)

Create a new quota policy for a user in a view.

Returns error if op fails.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ViewsApi()
body = cohesity.ViewUserQuotaParameters() # ViewUserQuotaParameters | update user quota params. (optional)

try: 
    # Create a new quota policy for a user in a view.
    api_response = api_instance.create_view_user_quota(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ViewsApi->create_view_user_quota: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ViewUserQuotaParameters**](ViewUserQuotaParameters.md)| update user quota params. | [optional] 

### Return type

[**UserQuotaAndUsage**](UserQuotaAndUsage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_view**
> delete_view(name)

Delete a View.

Returns delete status upon completion.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ViewsApi()
name = 'name_example' # str | Specifies the View name.

try: 
    # Delete a View.
    api_instance.delete_view(name)
except ApiException as e:
    print "Exception when calling ViewsApi->delete_view: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Specifies the View name. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_view_alias**
> delete_view_alias(name)

Delete a View Alias.

Returns delete status upon completion.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ViewsApi()
name = 'name_example' # str | Specifies the View Alias name.

try: 
    # Delete a View Alias.
    api_instance.delete_view_alias(name)
except ApiException as e:
    print "Exception when calling ViewsApi->delete_view_alias: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Specifies the View Alias name. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_view_users_quota**
> delete_view_users_quota(body=body)

Delete the quota policy overrides for users in a view.

Returns error if op fails.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ViewsApi()
body = cohesity.DeleteViewUsersQuotaParameters() # DeleteViewUsersQuotaParameters | update user quota params. (optional)

try: 
    # Delete the quota policy overrides for users in a view.
    api_instance.delete_view_users_quota(body=body)
except ApiException as e:
    print "Exception when calling ViewsApi->delete_view_users_quota: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteViewUsersQuotaParameters**](DeleteViewUsersQuotaParameters.md)| update user quota params. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_view_by_name**
> View get_view_by_name(name)

List details about a single View.

Returns the View corresponding to the specified View name.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ViewsApi()
name = 'name_example' # str | Specifies the View name.

try: 
    # List details about a single View.
    api_response = api_instance.get_view_by_name(name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ViewsApi->get_view_by_name: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Specifies the View name. | 

### Return type

[**View**](View.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_view_user_quotas**
> ViewUserQuotas get_view_user_quotas(include_usage=include_usage, exclude_users_within_alert_threshold=exclude_users_within_alert_threshold, unix_uid=unix_uid, summary_only=summary_only, cookie=cookie, view_name=view_name, sid=sid, page_count=page_count, max_view_id=max_view_id, output_format=output_format)

Get the quota policies, usage and summary for a view for all its users. It can also fetch the quota policies, usage and summary for a user in all his views.

Returns error if op fails.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ViewsApi()
include_usage = true # bool | If set to true, the logical usage info is included only for users with quota overrides. By default, it is set to false. (optional)
exclude_users_within_alert_threshold = true # bool | This field can be set only when includeUsage is set to true. By default, all the users with logical usage > 0 will be returned in the result. If this field is set to true, only the list of users who has exceeded the alert threshold will be returned. (optional)
unix_uid = 56 # int | If interested in a user via unix-identifier, include UnixUid. Otherwise, If valid unix-id to SID mappings are available (i.e., when mixed mode is enabled) the server will perform the necessary id mapping and return the correct usage irrespective of whether the unix id / SID is provided. (optional)
summary_only = true # bool | Specifies a flag to just return a summary. If set to true, and if ViewName is not nil, it returns the summary of users for a view. Otherwise if UserId not nil, and ViewName is nil then it fetches the summary for a user in his views.  By default, it is set to false. (optional)
cookie = 'cookie_example' # str | Cookie should be used from previous call to list user quota overrides. It resumes (or gives the next set of values) from the result of the previous call. (optional)
view_name = 'view_name_example' # str | Specifies the name of the input view. If given, there could be three scenarios with the viewName input parameter: It gives the user quota overrides for this view, and the user quota settings. Returns 'usersQuotaAndUsage'. If given along with the user id, it returns the quota policy for this user on this view. Returns 'usersQuotaAndUsage'. If given along with SummaryOnly as true, a user quota summary for this view would be returned. Returns 'summaryForView'. If not given, then the user id is checked. (optional)
sid = 'sid_example' # str | If interested in a user via smb_client, include SID. Otherwise, If valid unix-id to SID mappings are available (i.e., when mixed mode is enabled) the server will perform the necessary id mapping and return the correct usage irrespective of whether the unix id / SID is provided. The string is of following format - S-1-IdentifierAuthority-SubAuthority1-SubAuthority2-...-SubAuthorityn. (optional)
page_count = 789 # int | Specifies the max entries that should be returned in the result. (optional)
max_view_id = 789 # int | Related to fetching a particular user's quota and usage in all his views. It only pertains to the scenario where either UnixUid or Sid is specified, and ViewName is nil. Specify the maxViewId for All the views returned would have view_id's less than or equal to the given MaxViewId if it is >= 0. (optional)
output_format = 'output_format_example' # str | OutputFormat is the Output format for the output. If it is not specified, default is json. (optional)

try: 
    # Get the quota policies, usage and summary for a view for all its users. It can also fetch the quota policies, usage and summary for a user in all his views.
    api_response = api_instance.get_view_user_quotas(include_usage=include_usage, exclude_users_within_alert_threshold=exclude_users_within_alert_threshold, unix_uid=unix_uid, summary_only=summary_only, cookie=cookie, view_name=view_name, sid=sid, page_count=page_count, max_view_id=max_view_id, output_format=output_format)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ViewsApi->get_view_user_quotas: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_usage** | **bool**| If set to true, the logical usage info is included only for users with quota overrides. By default, it is set to false. | [optional] 
 **exclude_users_within_alert_threshold** | **bool**| This field can be set only when includeUsage is set to true. By default, all the users with logical usage &gt; 0 will be returned in the result. If this field is set to true, only the list of users who has exceeded the alert threshold will be returned. | [optional] 
 **unix_uid** | **int**| If interested in a user via unix-identifier, include UnixUid. Otherwise, If valid unix-id to SID mappings are available (i.e., when mixed mode is enabled) the server will perform the necessary id mapping and return the correct usage irrespective of whether the unix id / SID is provided. | [optional] 
 **summary_only** | **bool**| Specifies a flag to just return a summary. If set to true, and if ViewName is not nil, it returns the summary of users for a view. Otherwise if UserId not nil, and ViewName is nil then it fetches the summary for a user in his views.  By default, it is set to false. | [optional] 
 **cookie** | **str**| Cookie should be used from previous call to list user quota overrides. It resumes (or gives the next set of values) from the result of the previous call. | [optional] 
 **view_name** | **str**| Specifies the name of the input view. If given, there could be three scenarios with the viewName input parameter: It gives the user quota overrides for this view, and the user quota settings. Returns &#39;usersQuotaAndUsage&#39;. If given along with the user id, it returns the quota policy for this user on this view. Returns &#39;usersQuotaAndUsage&#39;. If given along with SummaryOnly as true, a user quota summary for this view would be returned. Returns &#39;summaryForView&#39;. If not given, then the user id is checked. | [optional] 
 **sid** | **str**| If interested in a user via smb_client, include SID. Otherwise, If valid unix-id to SID mappings are available (i.e., when mixed mode is enabled) the server will perform the necessary id mapping and return the correct usage irrespective of whether the unix id / SID is provided. The string is of following format - S-1-IdentifierAuthority-SubAuthority1-SubAuthority2-...-SubAuthorityn. | [optional] 
 **page_count** | **int**| Specifies the max entries that should be returned in the result. | [optional] 
 **max_view_id** | **int**| Related to fetching a particular user&#39;s quota and usage in all his views. It only pertains to the scenario where either UnixUid or Sid is specified, and ViewName is nil. Specify the maxViewId for All the views returned would have view_id&#39;s less than or equal to the given MaxViewId if it is &gt;&#x3D; 0. | [optional] 
 **output_format** | **str**| OutputFormat is the Output format for the output. If it is not specified, default is json. | [optional] 

### Return type

[**ViewUserQuotas**](ViewUserQuotas.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_views**
> GetViewsResult get_views(include_inactive=include_inactive, job_ids=job_ids, view_box_names=view_box_names, match_partial_names=match_partial_names, max_view_id=max_view_id, sort_by_logical_usage=sort_by_logical_usage, match_alias_names=match_alias_names, view_names=view_names, view_box_ids=view_box_ids, max_count=max_count)

List Views filtered by some parameters.

If no parameters are specified, all Views on the Cohesity Cluster are returned. Specifying parameters filters the results that are returned. NOTE: If maxCount is set and the number of Views returned exceeds the maxCount, there are more Views to return. To get the next set of Views, send another request and specify the id of the last View returned in viewList from the previous response.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ViewsApi()
include_inactive = true # bool | Specifies if inactive Views on this Remote Cluster (which have Snapshots copied by replication) should also be returned. Inactive Views are not counted towards the maxCount. By default, this field is set to false. (optional)
job_ids = [56] # list[int] | Filter by Protection Job ids. Return Views that are being protected by listed Jobs, which are specified by ids. (optional)
view_box_names = ['view_box_names_example'] # list[str] | Filter by a list of View Box names. (optional)
match_partial_names = true # bool | If true, the names in viewNames are matched by prefix rather than exactly matched. (optional)
max_view_id = 789 # int | If the number of Views to return exceeds the maxCount specified in the original request, specify the id of the last View from the viewList in the previous response to get the next set of Views. (optional)
sort_by_logical_usage = true # bool | If set to true, the list is sorted descending by logical usage. (optional)
match_alias_names = true # bool | If true, view aliases are also matched with the names in viewNames. (optional)
view_names = ['view_names_example'] # list[str] | Filter by a list of View names. (optional)
view_box_ids = [56] # list[int] | Filter by a list of Storage Domains (View Boxes) specified by id. (optional)
max_count = 56 # int | Specifies a limit on the number of Views returned. (optional)

try: 
    # List Views filtered by some parameters.
    api_response = api_instance.get_views(include_inactive=include_inactive, job_ids=job_ids, view_box_names=view_box_names, match_partial_names=match_partial_names, max_view_id=max_view_id, sort_by_logical_usage=sort_by_logical_usage, match_alias_names=match_alias_names, view_names=view_names, view_box_ids=view_box_ids, max_count=max_count)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ViewsApi->get_views: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_inactive** | **bool**| Specifies if inactive Views on this Remote Cluster (which have Snapshots copied by replication) should also be returned. Inactive Views are not counted towards the maxCount. By default, this field is set to false. | [optional] 
 **job_ids** | [**list[int]**](int.md)| Filter by Protection Job ids. Return Views that are being protected by listed Jobs, which are specified by ids. | [optional] 
 **view_box_names** | [**list[str]**](str.md)| Filter by a list of View Box names. | [optional] 
 **match_partial_names** | **bool**| If true, the names in viewNames are matched by prefix rather than exactly matched. | [optional] 
 **max_view_id** | **int**| If the number of Views to return exceeds the maxCount specified in the original request, specify the id of the last View from the viewList in the previous response to get the next set of Views. | [optional] 
 **sort_by_logical_usage** | **bool**| If set to true, the list is sorted descending by logical usage. | [optional] 
 **match_alias_names** | **bool**| If true, view aliases are also matched with the names in viewNames. | [optional] 
 **view_names** | [**list[str]**](str.md)| Filter by a list of View names. | [optional] 
 **view_box_ids** | [**list[int]**](int.md)| Filter by a list of Storage Domains (View Boxes) specified by id. | [optional] 
 **max_count** | **int**| Specifies a limit on the number of Views returned. | [optional] 

### Return type

[**GetViewsResult**](GetViewsResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_views_by_share_name**
> GetViewsByShareNameResult get_views_by_share_name(share_name=share_name, max_count=max_count, pagination_cookie=pagination_cookie)

List shares filtered by name.

If no parameters are specified, all shares on the Cohesity Cluster are returned. Specifying share name/prefix filters the results that are returned. NOTE: If maxCount is set and the number of Views returned exceeds the maxCount, there are more Views to return. To get the next set of Views, send another request and specify the pagination cookie from the previous response.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ViewsApi()
share_name = 'share_name_example' # str | The share name(substring) that needs to be searched against existing views and aliases. (optional)
max_count = 56 # int | Specifies a limit on the number of Views returned. (optional)
pagination_cookie = 'pagination_cookie_example' # str | Expected to be empty in the first call to GetViewsByShareName. To get the next set of results, set this value to the pagination cookie value returned  in the response of the previous call. (optional)

try: 
    # List shares filtered by name.
    api_response = api_instance.get_views_by_share_name(share_name=share_name, max_count=max_count, pagination_cookie=pagination_cookie)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ViewsApi->get_views_by_share_name: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **share_name** | **str**| The share name(substring) that needs to be searched against existing views and aliases. | [optional] 
 **max_count** | **int**| Specifies a limit on the number of Views returned. | [optional] 
 **pagination_cookie** | **str**| Expected to be empty in the first call to GetViewsByShareName. To get the next set of results, set this value to the pagination cookie value returned  in the response of the previous call. | [optional] 

### Return type

[**GetViewsByShareNameResult**](GetViewsByShareNameResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **overwrite_view**
> View overwrite_view(body)

Overwrites a Target view with contents of a Source view.

Specifies source and target view names as params. Returns the modified Target View.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ViewsApi()
body = cohesity.OverwriteViewParam() # OverwriteViewParam | Request to overwrite a Target view with contents of a Source view.

try: 
    # Overwrites a Target view with contents of a Source view.
    api_response = api_instance.overwrite_view(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ViewsApi->overwrite_view: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OverwriteViewParam**](OverwriteViewParam.md)| Request to overwrite a Target view with contents of a Source view. | 

### Return type

[**View**](View.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rename_view**
> View rename_view(body, name)

Rename a View.

Specify original name of the View in the 'name' parameter. Returns the renamed View.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ViewsApi()
body = cohesity.RenameViewParam() # RenameViewParam | Request to rename a View.
name = 'name_example' # str | Specifies the View name.

try: 
    # Rename a View.
    api_response = api_instance.rename_view(body, name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ViewsApi->rename_view: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RenameViewParam**](RenameViewParam.md)| Request to rename a View. | 
 **name** | **str**| Specifies the View name. | 

### Return type

[**View**](View.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_quota_settings**
> UserQuotaSettings update_user_quota_settings(body=body)

Update the user quota settings in a view.

Returns error if op fails.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ViewsApi()
body = cohesity.UpdateUserQuotaSettingsForView() # UpdateUserQuotaSettingsForView | update user quota metadata params. (optional)

try: 
    # Update the user quota settings in a view.
    api_response = api_instance.update_user_quota_settings(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ViewsApi->update_user_quota_settings: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateUserQuotaSettingsForView**](UpdateUserQuotaSettingsForView.md)| update user quota metadata params. | [optional] 

### Return type

[**UserQuotaSettings**](UserQuotaSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_view**
> View update_view(name, body)

Update a View.

Returns the updated View.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ViewsApi()
name = 'name_example' # str | Specifies the View name.
body = cohesity.UpdateViewParam() # UpdateViewParam | Request to update a view.

try: 
    # Update a View.
    api_response = api_instance.update_view(name, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ViewsApi->update_view: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Specifies the View name. | 
 **body** | [**UpdateViewParam**](UpdateViewParam.md)| Request to update a view. | 

### Return type

[**View**](View.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_view_user_quota**
> UserQuotaAndUsage update_view_user_quota(body=body)

Update a new quota policy for a user in a view.

Returns error if op fails.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ViewsApi()
body = cohesity.ViewUserQuotaParameters() # ViewUserQuotaParameters | update user quota params. (optional)

try: 
    # Update a new quota policy for a user in a view.
    api_response = api_instance.update_view_user_quota(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ViewsApi->update_view_user_quota: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ViewUserQuotaParameters**](ViewUserQuotaParameters.md)| update user quota params. | [optional] 

### Return type

[**UserQuotaAndUsage**](UserQuotaAndUsage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

