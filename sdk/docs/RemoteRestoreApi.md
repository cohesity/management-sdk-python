# cohesity.RemoteRestoreApi

All URIs are relative to *https://localhost/irisservices/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_remote_vault_restore_task**](RemoteRestoreApi.md#create_remote_vault_restore_task) | **POST** /public/remoteVaults/restoreTasks | Create a remote Vault restore task. (CloudRetrieve)
[**create_remote_vault_search_job**](RemoteRestoreApi.md#create_remote_vault_search_job) | **POST** /public/remoteVaults/searchJobs | Create a search of a remote Vault. (CloudRetrieve)
[**get_remote_vault_search_job_results**](RemoteRestoreApi.md#get_remote_vault_search_job_results) | **GET** /public/remoteVaults/searchJobResults | List details about the Job Runs of Protection Jobs found by a single search of a remote Vault. (CloudRetrieve)
[**list_remote_vault_restore_tasks**](RemoteRestoreApi.md#list_remote_vault_restore_tasks) | **GET** /public/remoteVaults/restoreTasks | List the remote Vault restore tasks that have completed or are running on this Cohesity Cluster. (CloudRetrieve)
[**list_remote_vault_search_job_by_id**](RemoteRestoreApi.md#list_remote_vault_search_job_by_id) | **GET** /public/remoteVaults/searchJobs/{id} | List details about a single search Job of a remote Vault. (CloudRetrieve)
[**list_remote_vault_search_jobs**](RemoteRestoreApi.md#list_remote_vault_search_jobs) | **GET** /public/remoteVaults/searchJobs | List all the searches of remote Vaults. (CloudRetrieve)
[**stop_remote_vault_search_job**](RemoteRestoreApi.md#stop_remote_vault_search_job) | **DELETE** /public/remoteVaults/searchJobs | Stop a search of a remote Vault (External Target). (CloudRetrieve)
[**upload_vault_encryption_keys**](RemoteRestoreApi.md#upload_vault_encryption_keys) | **PUT** /public/remoteVaults/encryptionKeys/{id} | Upload the encryption keys required to restore data from a remote Vault. (CloudRetrieve)


# **create_remote_vault_restore_task**
> UniversalId create_remote_vault_restore_task(body)

Create a remote Vault restore task. (CloudRetrieve)

Returns the id of the remote Vault restore Task that was created.  After a Vault is searched by a search Job, this operation can be called to create a task that restores the indexes and/or the Snapshots of a Protection Job, which were archived on a remote Vault (External Target). This is part of the CloudRetrieve functionality for finding and restoring archived data from remote Vaults to an alternative (non-original) Cluster.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.RemoteRestoreApi()
body = cohesity.CreateRemoteVaultRestoreTaskParameters() # CreateRemoteVaultRestoreTaskParameters | Request to create a remote Vault restore task.

try: 
    # Create a remote Vault restore task. (CloudRetrieve)
    api_response = api_instance.create_remote_vault_restore_task(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RemoteRestoreApi->create_remote_vault_restore_task: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRemoteVaultRestoreTaskParameters**](CreateRemoteVaultRestoreTaskParameters.md)| Request to create a remote Vault restore task. | 

### Return type

[**UniversalId**](UniversalId.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_remote_vault_search_job**
> CreatedRemoteVaultSearchJobUid create_remote_vault_search_job(body)

Create a search of a remote Vault. (CloudRetrieve)

A search Job finds Protection Jobs that archived data to a Vault (External Target) which also match the specified search criteria. The results can be optionally filtered by specifying a Cluster match string, a Protection Job match string, a start time and an end time. This is part of the CloudRetrieve functionality for finding and restoring archived data from remote Vaults to an alternative (non-original) Cluster.  NOTE: A Vault is equivalent to an External Target in the Cohesity Dashboard. A search Job is equivalent to a search task in the Cohesity Dashboard.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.RemoteRestoreApi()
body = cohesity.CreateRemoteVaultSearchJobParameters() # CreateRemoteVaultSearchJobParameters | Request to create a search of a remote Vault.

try: 
    # Create a search of a remote Vault. (CloudRetrieve)
    api_response = api_instance.create_remote_vault_search_job(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RemoteRestoreApi->create_remote_vault_search_job: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRemoteVaultSearchJobParameters**](CreateRemoteVaultSearchJobParameters.md)| Request to create a search of a remote Vault. | 

### Return type

[**CreatedRemoteVaultSearchJobUid**](CreatedRemoteVaultSearchJobUid.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_remote_vault_search_job_results**
> RemoteVaultSearchJobResults get_remote_vault_search_job_results(search_job_id, cluster_id, cluster_incarnation_id, page_count=page_count, cluster_name=cluster_name, cookie=cookie)

List details about the Job Runs of Protection Jobs found by a single search of a remote Vault. (CloudRetrieve)

Specify a unique id of the search Job using a combination of the searchJobId, clusterId, and clusterIncarnationId parameters, which are all required.  The results can be optionally filtered by the remote Cluster name. This is part of the CloudRetrieve functionality for finding and restoring archived data from a remote Vault.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.RemoteRestoreApi()
search_job_id = 789 # int | Specifies the id of the remote Vault search Job assigned by the Cohesity Cluster. Used in combination with the clusterId and clusterIncarnationId to uniquely identify the search Job.
cluster_id = 789 # int | Specifies the Cohesity Cluster id where the search Job was created. Used in combination with the searchJobId and clusterIncarnationId to uniquely identify the search Job.
cluster_incarnation_id = 789 # int | Specifies the incarnation id of the Cohesity Cluster where the search Job was created. Used in combination with the searchJobId and clusterId to uniquely identify the search Job.
page_count = 56 # int | Specifies the number of Protection Jobs to return in the response to support pagination. (optional)
cluster_name = 'cluster_name_example' # str | Optionally filter the result by the remote Cohesity Cluster name. (optional)
cookie = 'cookie_example' # str | Specifies the opaque string cookie returned by the previous response, to get next set of results. Used in combination with pageCount to support pagination. (optional)

try: 
    # List details about the Job Runs of Protection Jobs found by a single search of a remote Vault. (CloudRetrieve)
    api_response = api_instance.get_remote_vault_search_job_results(search_job_id, cluster_id, cluster_incarnation_id, page_count=page_count, cluster_name=cluster_name, cookie=cookie)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RemoteRestoreApi->get_remote_vault_search_job_results: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_job_id** | **int**| Specifies the id of the remote Vault search Job assigned by the Cohesity Cluster. Used in combination with the clusterId and clusterIncarnationId to uniquely identify the search Job. | 
 **cluster_id** | **int**| Specifies the Cohesity Cluster id where the search Job was created. Used in combination with the searchJobId and clusterIncarnationId to uniquely identify the search Job. | 
 **cluster_incarnation_id** | **int**| Specifies the incarnation id of the Cohesity Cluster where the search Job was created. Used in combination with the searchJobId and clusterId to uniquely identify the search Job. | 
 **page_count** | **int**| Specifies the number of Protection Jobs to return in the response to support pagination. | [optional] 
 **cluster_name** | **str**| Optionally filter the result by the remote Cohesity Cluster name. | [optional] 
 **cookie** | **str**| Specifies the opaque string cookie returned by the previous response, to get next set of results. Used in combination with pageCount to support pagination. | [optional] 

### Return type

[**RemoteVaultSearchJobResults**](RemoteVaultSearchJobResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_remote_vault_restore_tasks**
> list[RemoteVaultRestoreTaskStatus] list_remote_vault_restore_tasks()

List the remote Vault restore tasks that have completed or are running on this Cohesity Cluster. (CloudRetrieve)

A remote Vault restore task can restore archived data from a Vault (External Target) to this local Cluster. This is part of the CloudRetrieve functionality for finding and restoring archived data from remote Vaults to an alternative (non-original) Cluster.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.RemoteRestoreApi()

try: 
    # List the remote Vault restore tasks that have completed or are running on this Cohesity Cluster. (CloudRetrieve)
    api_response = api_instance.list_remote_vault_restore_tasks()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RemoteRestoreApi->list_remote_vault_restore_tasks: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[RemoteVaultRestoreTaskStatus]**](RemoteVaultRestoreTaskStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_remote_vault_search_job_by_id**
> RemoteVaultSearchJobInformation list_remote_vault_search_job_by_id(id)

List details about a single search Job of a remote Vault. (CloudRetrieve)

Specify an id for a completed or running search Job. A search Job finds data that has been archived to a Vault (External Target). The returned results do not include Job Run (Snapshot) information. It is part of the CloudRetrieve functionality for finding and restoring archived data from remote Vaults to an alternative (non-original) Cluster.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.RemoteRestoreApi()
id = 789 # int | Specifies the id of the remote Vault search Job to return.

try: 
    # List details about a single search Job of a remote Vault. (CloudRetrieve)
    api_response = api_instance.list_remote_vault_search_job_by_id(id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RemoteRestoreApi->list_remote_vault_search_job_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies the id of the remote Vault search Job to return. | 

### Return type

[**RemoteVaultSearchJobInformation**](RemoteVaultSearchJobInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_remote_vault_search_jobs**
> list[RemoteVaultSearchJobInformation] list_remote_vault_search_jobs()

List all the searches of remote Vaults. (CloudRetrieve)

List all the searches of remote Vaults (External Targets) that have run or are running on this Cohesity Cluster. A search finds Protection Jobs that have archived to a Vault (External Target). This is part of the CloudRetrieve functionality for finding and restoring archived data from remote Vaults to an alternative (non-original) Cluster.  NOTE: A Vault is equivalent to an External Target in the Cohesity Dashboard. A search Job is equivalent to a search task in the Cohesity Dashboard.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.RemoteRestoreApi()

try: 
    # List all the searches of remote Vaults. (CloudRetrieve)
    api_response = api_instance.list_remote_vault_search_jobs()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RemoteRestoreApi->list_remote_vault_search_jobs: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[RemoteVaultSearchJobInformation]**](RemoteVaultSearchJobInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_remote_vault_search_job**
> stop_remote_vault_search_job(body)

Stop a search of a remote Vault (External Target). (CloudRetrieve)

This is part of the CloudRetrieve functionality for finding and restoring archived data from remote Vaults to an alternative (non-original) Cluster.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.RemoteRestoreApi()
body = cohesity.StopRemoteVaultSearchJobParameters() # StopRemoteVaultSearchJobParameters | Request to stop a Remote Vault Search Job.

try: 
    # Stop a search of a remote Vault (External Target). (CloudRetrieve)
    api_instance.stop_remote_vault_search_job(body)
except ApiException as e:
    print "Exception when calling RemoteRestoreApi->stop_remote_vault_search_job: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StopRemoteVaultSearchJobParameters**](StopRemoteVaultSearchJobParameters.md)| Request to stop a Remote Vault Search Job. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_vault_encryption_keys**
> upload_vault_encryption_keys(id, body=body)

Upload the encryption keys required to restore data from a remote Vault. (CloudRetrieve)

This request contains multiple files stored as multipart mime data. Each file has a key used to encrypt data between a remote Cluster and the remote Vault. Content of the file should be same as the file downloaded from the remote Cluster.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.RemoteRestoreApi()
id = 789 # int | Specifies a unique id of the Vault.
body = [cohesity.VaultEncryptionKey()] # list[VaultEncryptionKey] | Request to upload encryption keys of a remote Vault. (optional)

try: 
    # Upload the encryption keys required to restore data from a remote Vault. (CloudRetrieve)
    api_instance.upload_vault_encryption_keys(id, body=body)
except ApiException as e:
    print "Exception when calling RemoteRestoreApi->upload_vault_encryption_keys: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a unique id of the Vault. | 
 **body** | [**list[VaultEncryptionKey]**](VaultEncryptionKey.md)| Request to upload encryption keys of a remote Vault. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

