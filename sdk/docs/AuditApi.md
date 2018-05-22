# cohesity.AuditApi

All URIs are relative to *https://localhost/irisservices/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_cluster_audit_logs**](AuditApi.md#search_cluster_audit_logs) | **GET** /public/auditLogs/cluster | List the cluster audit logs on the Cohesity Cluster that match the filter criteria specified using parameters.


# **search_cluster_audit_logs**
> ClusterAuditLogsSearchResult search_cluster_audit_logs(search=search, start_index=start_index, user_names=user_names, entity_types=entity_types, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, page_count=page_count, output_format=output_format, domains=domains, actions=actions)

List the cluster audit logs on the Cohesity Cluster that match the filter criteria specified using parameters.

When actions (such as a login or a Job being paused) occur on the Cohesity Cluster, the Cluster generates Audit Logs. If no parameters are specified, all logs currently on the Cohesity Cluster are returned. Specifying parameters filters the results that are returned.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.AuditApi()
search = 'search_example' # str | Filter by matching a substring in entity name or details of the Cluster audit log. (optional)
start_index = 789 # int | Specifies an index number that can be used to return subsets of items in multiple requests. Break up the items to return into multiple requests by setting pageCount and startIndex to return a subsets of items in the search result. For example, set startIndex to 0 to get the first set of pageCount items for the first request. Increment startIndex by pageCount to get the next set of pageCount items for a next request. Continue until all items are returned and therefore the total number of returned items is equal to totalCount. Default value is 0. (optional)
user_names = ['user_names_example'] # list[str] | Filter by user names who cause the actions that generate Cluster Audit Logs. (optional)
entity_types = ['entity_types_example'] # list[str] | Filter by entity types involved in the actions that generate the Cluster audit logs, such as User, Protection Job, View, etc. For a complete list, see the Category drop-down in the Admin > Audit Logs page of the Cohesity Dashboard. (optional)
start_time_usecs = 789 # int | Filter by a start time. Only Cluster audit logs that were generated after the specified time are returned. Specify the start time as a Unix epoch Timestamp (in microseconds). (optional)
end_time_usecs = 789 # int | Filter by a end time specified as a Unix epoch Timestamp (in microseconds). Only Cluster audit logs that were generated before the specified end time are returned. (optional)
page_count = 789 # int | Limit the number of items to return in the response for pagination purposes. Default value is 1000. (optional)
output_format = 'output_format_example' # str | Specifies the format of the output such as csv and json. If not specified, the json format is returned. If csv is specified, a comma-separated list with a heading row is returned. (optional)
domains = ['domains_example'] # list[str] | Filter by domains of users who cause the actions that trigger Cluster audit logs. (optional)
actions = ['actions_example'] # list[str] | Filter by the actions that generate Cluster audit logs such as Activate, Cancel, Clone, Create, etc. For a complete list, see the Actions drop-down in the Admin > Audit Logs page of the Cohesity Dashboard. (optional)

try: 
    # List the cluster audit logs on the Cohesity Cluster that match the filter criteria specified using parameters.
    api_response = api_instance.search_cluster_audit_logs(search=search, start_index=start_index, user_names=user_names, entity_types=entity_types, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, page_count=page_count, output_format=output_format, domains=domains, actions=actions)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuditApi->search_cluster_audit_logs: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Filter by matching a substring in entity name or details of the Cluster audit log. | [optional] 
 **start_index** | **int**| Specifies an index number that can be used to return subsets of items in multiple requests. Break up the items to return into multiple requests by setting pageCount and startIndex to return a subsets of items in the search result. For example, set startIndex to 0 to get the first set of pageCount items for the first request. Increment startIndex by pageCount to get the next set of pageCount items for a next request. Continue until all items are returned and therefore the total number of returned items is equal to totalCount. Default value is 0. | [optional] 
 **user_names** | [**list[str]**](str.md)| Filter by user names who cause the actions that generate Cluster Audit Logs. | [optional] 
 **entity_types** | [**list[str]**](str.md)| Filter by entity types involved in the actions that generate the Cluster audit logs, such as User, Protection Job, View, etc. For a complete list, see the Category drop-down in the Admin &gt; Audit Logs page of the Cohesity Dashboard. | [optional] 
 **start_time_usecs** | **int**| Filter by a start time. Only Cluster audit logs that were generated after the specified time are returned. Specify the start time as a Unix epoch Timestamp (in microseconds). | [optional] 
 **end_time_usecs** | **int**| Filter by a end time specified as a Unix epoch Timestamp (in microseconds). Only Cluster audit logs that were generated before the specified end time are returned. | [optional] 
 **page_count** | **int**| Limit the number of items to return in the response for pagination purposes. Default value is 1000. | [optional] 
 **output_format** | **str**| Specifies the format of the output such as csv and json. If not specified, the json format is returned. If csv is specified, a comma-separated list with a heading row is returned. | [optional] 
 **domains** | [**list[str]**](str.md)| Filter by domains of users who cause the actions that trigger Cluster audit logs. | [optional] 
 **actions** | [**list[str]**](str.md)| Filter by the actions that generate Cluster audit logs such as Activate, Cancel, Clone, Create, etc. For a complete list, see the Actions drop-down in the Admin &gt; Audit Logs page of the Cohesity Dashboard. | [optional] 

### Return type

[**ClusterAuditLogsSearchResult**](ClusterAuditLogsSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

