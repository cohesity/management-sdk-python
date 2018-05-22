# cohesity.RemoteClusterApi

All URIs are relative to *https://localhost/irisservices/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_remote_cluster**](RemoteClusterApi.md#create_remote_cluster) | **POST** /public/remoteClusters | Register a remote Cluster on this local Cluster for replication.
[**delete_remote_cluster**](RemoteClusterApi.md#delete_remote_cluster) | **DELETE** /public/remoteClusters/{id} | Delete a remote Cluster registration connection.
[**get_remote_cluster_by_id**](RemoteClusterApi.md#get_remote_cluster_by_id) | **GET** /public/remoteClusters/{id} | List details about a single remote Cluster registered on this local Cluster.
[**get_remote_clusters**](RemoteClusterApi.md#get_remote_clusters) | **GET** /public/remoteClusters | List the remote Cohesity Clusters that are registered on this local Cohesity Cluster that match the filter criteria specified using parameters.
[**get_replication_encryption_key**](RemoteClusterApi.md#get_replication_encryption_key) | **GET** /public/replicationEncryptionKey | Get the encryption key on this Cluster.
[**update_remote_cluster**](RemoteClusterApi.md#update_remote_cluster) | **PUT** /public/remoteClusters/{id} | Update the connection settings of the registered remote Cluster.


# **create_remote_cluster**
> RemoteCluster create_remote_cluster(body)

Register a remote Cluster on this local Cluster for replication.

For a Protection Job to replicate Snapshots from one Cluster to another Cluster, the Clusters must be paired together by registering each Cluster on the other Cluster. For example, Cluster A must be registered on Cluster B and Cluster B must be registered on Cluster A.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.RemoteClusterApi()
body = cohesity.RegisterRemoteCluster() # RegisterRemoteCluster | Request to register a remote Cluster.

try: 
    # Register a remote Cluster on this local Cluster for replication.
    api_response = api_instance.create_remote_cluster(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RemoteClusterApi->create_remote_cluster: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RegisterRemoteCluster**](RegisterRemoteCluster.md)| Request to register a remote Cluster. | 

### Return type

[**RemoteCluster**](RemoteCluster.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_remote_cluster**
> delete_remote_cluster(id)

Delete a remote Cluster registration connection.

Delete the specified remote Cluster registration connection on this Cluster.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.RemoteClusterApi()
id = 789 # int | id of the remote Cluster

try: 
    # Delete a remote Cluster registration connection.
    api_instance.delete_remote_cluster(id)
except ApiException as e:
    print "Exception when calling RemoteClusterApi->delete_remote_cluster: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of the remote Cluster | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_remote_cluster_by_id**
> list[RemoteCluster] get_remote_cluster_by_id(id)

List details about a single remote Cluster registered on this local Cluster.

Returns the details about the remote Cluster with the specified Cluster id that is registered on this local Cluster.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.RemoteClusterApi()
id = 789 # int | id of the remote Cluster

try: 
    # List details about a single remote Cluster registered on this local Cluster.
    api_response = api_instance.get_remote_cluster_by_id(id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RemoteClusterApi->get_remote_cluster_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of the remote Cluster | 

### Return type

[**list[RemoteCluster]**](RemoteCluster.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_remote_clusters**
> list[RemoteCluster] get_remote_clusters(cluster_ids=cluster_ids, cluster_names=cluster_names, purpose_replication=purpose_replication, purpose_remote_access=purpose_remote_access)

List the remote Cohesity Clusters that are registered on this local Cohesity Cluster that match the filter criteria specified using parameters.

Cohesity Clusters involved in replication, must be registered to each other. For example, if Cluster A is replicating Snapshots to Cluster B, Cluster B must be registered on Cluster A and Cluster B must be registered on Cluster A.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.RemoteClusterApi()
cluster_ids = [56] # list[int] | Filter by a list of Cluster ids. (optional)
cluster_names = ['cluster_names_example'] # list[str] | Filter by a list of Cluster names. (optional)
purpose_replication = true # bool | Filter for purpose as Replication. (optional)
purpose_remote_access = true # bool | Filter for purpose as Remote Access. (optional)

try: 
    # List the remote Cohesity Clusters that are registered on this local Cohesity Cluster that match the filter criteria specified using parameters.
    api_response = api_instance.get_remote_clusters(cluster_ids=cluster_ids, cluster_names=cluster_names, purpose_replication=purpose_replication, purpose_remote_access=purpose_remote_access)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RemoteClusterApi->get_remote_clusters: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_ids** | [**list[int]**](int.md)| Filter by a list of Cluster ids. | [optional] 
 **cluster_names** | [**list[str]**](str.md)| Filter by a list of Cluster names. | [optional] 
 **purpose_replication** | **bool**| Filter for purpose as Replication. | [optional] 
 **purpose_remote_access** | **bool**| Filter for purpose as Remote Access. | [optional] 

### Return type

[**list[RemoteCluster]**](RemoteCluster.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_replication_encryption_key**
> ReplicationEncryptionKeyReponse get_replication_encryption_key()

Get the encryption key on this Cluster.

Get the encryption key that is used for encrypting replication data between this Cluster and a remote Cluster.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.RemoteClusterApi()

try: 
    # Get the encryption key on this Cluster.
    api_response = api_instance.get_replication_encryption_key()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RemoteClusterApi->get_replication_encryption_key: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ReplicationEncryptionKeyReponse**](ReplicationEncryptionKeyReponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_remote_cluster**
> RemoteCluster update_remote_cluster(id, body)

Update the connection settings of the registered remote Cluster.

Update the connection settings of the specified remote Cluster that is registered on this Cluster.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.RemoteClusterApi()
id = 789 # int | id of the remote Cluster
body = cohesity.RegisterRemoteCluster() # RegisterRemoteCluster | Request to update a remote Cluster.

try: 
    # Update the connection settings of the registered remote Cluster.
    api_response = api_instance.update_remote_cluster(id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RemoteClusterApi->update_remote_cluster: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of the remote Cluster | 
 **body** | [**RegisterRemoteCluster**](RegisterRemoteCluster.md)| Request to update a remote Cluster. | 

### Return type

[**RemoteCluster**](RemoteCluster.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

