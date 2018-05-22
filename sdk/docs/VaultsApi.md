# cohesity.VaultsApi

All URIs are relative to *https://localhost/irisservices/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_vault**](VaultsApi.md#create_vault) | **POST** /public/vaults | Create a new Vault (External Target).
[**delete_vault**](VaultsApi.md#delete_vault) | **DELETE** /public/vaults/{id} | Delete a Vault (External Target).
[**get_archive_media_info**](VaultsApi.md#get_archive_media_info) | **GET** /public/vaults/archiveMediaInfo | List the media information for the specified archive service.
[**get_vault_by_id**](VaultsApi.md#get_vault_by_id) | **GET** /public/vaults/{id} | List details about a single Vault (External Target).
[**get_vault_encryption_key_info**](VaultsApi.md#get_vault_encryption_key_info) | **GET** /public/vaults/encryptionKey/{id} | Get encryption information for a Vault (External Target). A Vault is equivalent to an External Target in the Cohesity Dashboard.
[**get_vaults**](VaultsApi.md#get_vaults) | **GET** /public/vaults | List the Vaults (External Targets) registered on the Cohesity Cluster filtered by the specified parameters.
[**update_vault**](VaultsApi.md#update_vault) | **PUT** /public/vaults/{id} | Update a Vault (External Target).


# **create_vault**
> Vault create_vault(body)

Create a new Vault (External Target).

Returns the created Vault. A Vault is equivalent to an External Target in the Cohesity Dashboard.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.VaultsApi()
body = cohesity.Vault() # Vault | Request to create a new Vault.

try: 
    # Create a new Vault (External Target).
    api_response = api_instance.create_vault(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling VaultsApi->create_vault: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Vault**](Vault.md)| Request to create a new Vault. | 

### Return type

[**Vault**](Vault.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_vault**
> delete_vault(id)

Delete a Vault (External Target).

Returns delete status upon completion. A Vault is equivalent to an External Target in the Cohesity Dashboard.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.VaultsApi()
id = 789 # int | Specifies a unique id of the Vault.

try: 
    # Delete a Vault (External Target).
    api_instance.delete_vault(id)
except ApiException as e:
    print "Exception when calling VaultsApi->delete_vault: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a unique id of the Vault. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_archive_media_info**
> list[TapeMediaInformation] get_archive_media_info(cluster_id, cluster_incarnation_id, qstar_archive_job_id, entity_ids=entity_ids, qstar_restore_task_id=qstar_restore_task_id)

List the media information for the specified archive service.

Returns the media information about the specified archive service uid (such as a QStar tape archive service).  An archive service uid is uniquely identified using a combination of the following fields: clusterIncarnationId, entityIds and clusterId. These are all required fields.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.VaultsApi()
cluster_id = 789 # int | Specifies the id of the Cohesity Cluster that archived to a QStar media Vault.
cluster_incarnation_id = 789 # int | Specifies the incarnation id of the Cohesity Cluster that archived to a QStar media Vault.
qstar_archive_job_id = 789 # int | Specifies the id of the Job that archived to a QStar media Vault.
entity_ids = [56] # list[int] | Specifies an array of entityIds to optionally filter by. An entityId is a unique id for a VM assigned by the Cohesity Cluster. (optional)
qstar_restore_task_id = 789 # int | Specifies the id of the restore task to optionally filter by. The restore task that is restoring data from the specified media Vault. (optional)

try: 
    # List the media information for the specified archive service.
    api_response = api_instance.get_archive_media_info(cluster_id, cluster_incarnation_id, qstar_archive_job_id, entity_ids=entity_ids, qstar_restore_task_id=qstar_restore_task_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling VaultsApi->get_archive_media_info: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**| Specifies the id of the Cohesity Cluster that archived to a QStar media Vault. | 
 **cluster_incarnation_id** | **int**| Specifies the incarnation id of the Cohesity Cluster that archived to a QStar media Vault. | 
 **qstar_archive_job_id** | **int**| Specifies the id of the Job that archived to a QStar media Vault. | 
 **entity_ids** | [**list[int]**](int.md)| Specifies an array of entityIds to optionally filter by. An entityId is a unique id for a VM assigned by the Cohesity Cluster. | [optional] 
 **qstar_restore_task_id** | **int**| Specifies the id of the restore task to optionally filter by. The restore task that is restoring data from the specified media Vault. | [optional] 

### Return type

[**list[TapeMediaInformation]**](TapeMediaInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vault_by_id**
> Vault get_vault_by_id(id)

List details about a single Vault (External Target).

Returns the Vault corresponding to the specified Vault Id. A Vault is equivalent to an External Target in the Cohesity Dashboard.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.VaultsApi()
id = 789 # int | Specifies a unique id of the Vault.

try: 
    # List details about a single Vault (External Target).
    api_response = api_instance.get_vault_by_id(id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling VaultsApi->get_vault_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a unique id of the Vault. | 

### Return type

[**Vault**](Vault.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vault_encryption_key_info**
> VaultEncryptionKey get_vault_encryption_key_info(id)

Get encryption information for a Vault (External Target). A Vault is equivalent to an External Target in the Cohesity Dashboard.

Get encryption information (such as the encryption key) for the specified Vault (External Target). To restore data to a remote Cluster (for example to support a disaster recovery scenario), you must get the encryption key of the Vault and store it outside the local source Cluster, before disaster strikes. If you have the encryption key and the local source Cluster goes down, you can restore the data to a remote Cluster from the Vault. The local source Cluster is the Cluster that archived the data on the Vault.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.VaultsApi()
id = 789 # int | Specifies a unique id of the Vault.

try: 
    # Get encryption information for a Vault (External Target). A Vault is equivalent to an External Target in the Cohesity Dashboard.
    api_response = api_instance.get_vault_encryption_key_info(id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling VaultsApi->get_vault_encryption_key_info: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a unique id of the Vault. | 

### Return type

[**VaultEncryptionKey**](VaultEncryptionKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vaults**
> list[Vault] get_vaults(include_marked_for_removal=include_marked_for_removal, id=id, name=name)

List the Vaults (External Targets) registered on the Cohesity Cluster filtered by the specified parameters.

If no parameters are specified, all Vaults (External Targets) currently registered on the Cohesity Cluster are returned. Specifying parameters filters the results that are returned. A Vault is equivalent to an External Target in the Cohesity Dashboard.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.VaultsApi()
include_marked_for_removal = true # bool | Specifies if Vaults that are marked for removal should be returned. (optional)
id = 789 # int | Specifies the id of Vault to return. If empty, all Vaults are returned. (optional)
name = 'name_example' # str | Specifies the name of the Vault to return. If empty, all Vaults are returned. (optional)

try: 
    # List the Vaults (External Targets) registered on the Cohesity Cluster filtered by the specified parameters.
    api_response = api_instance.get_vaults(include_marked_for_removal=include_marked_for_removal, id=id, name=name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling VaultsApi->get_vaults: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_marked_for_removal** | **bool**| Specifies if Vaults that are marked for removal should be returned. | [optional] 
 **id** | **int**| Specifies the id of Vault to return. If empty, all Vaults are returned. | [optional] 
 **name** | **str**| Specifies the name of the Vault to return. If empty, all Vaults are returned. | [optional] 

### Return type

[**list[Vault]**](Vault.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vault**
> Vault update_vault(id, body)

Update a Vault (External Target).

Update the settings of a Vault. A Vault is equivalent to an External Target in the Cohesity Dashboard. Returns the updated Vault.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.VaultsApi()
id = 789 # int | Specifies a unique id of the Vault.
body = cohesity.Vault() # Vault | Request to update a Vault's settings.

try: 
    # Update a Vault (External Target).
    api_response = api_instance.update_vault(id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling VaultsApi->update_vault: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a unique id of the Vault. | 
 **body** | [**Vault**](Vault.md)| Request to update a Vault&#39;s settings. | 

### Return type

[**Vault**](Vault.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

