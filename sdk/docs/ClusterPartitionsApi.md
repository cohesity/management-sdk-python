# cohesity.ClusterPartitionsApi

All URIs are relative to *https://localhost/irisservices/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cluster_partition_by_id**](ClusterPartitionsApi.md#get_cluster_partition_by_id) | **GET** /public/clusterPartitions/{id} | List details about a single Cluster Partition.
[**get_cluster_partitions**](ClusterPartitionsApi.md#get_cluster_partitions) | **GET** /public/clusterPartitions | List Cluster Partitions filtered by the specified parameters.


# **get_cluster_partition_by_id**
> ClusterPartition get_cluster_partition_by_id(id)

List details about a single Cluster Partition.

Returns the Cluster Partition corresponding to the specified Cluster Partition Id.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ClusterPartitionsApi()
id = 789 # int | Specifies a unique id of the Cluster Partition to return.

try: 
    # List details about a single Cluster Partition.
    api_response = api_instance.get_cluster_partition_by_id(id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ClusterPartitionsApi->get_cluster_partition_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a unique id of the Cluster Partition to return. | 

### Return type

[**ClusterPartition**](ClusterPartition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_partitions**
> list[ClusterPartition] get_cluster_partitions(ids=ids, names=names)

List Cluster Partitions filtered by the specified parameters.

If no parameters are specified, all Cluster Partitions currently on the Cohesity Cluster are returned. Specifying parameters filters the results that are returned.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ClusterPartitionsApi()
ids = [56] # list[int] | Array of Cluster Partition Ids.  Filter by a list of Cluster Partition ids. If empty, the Cluster Partitions are not filtered by id. (optional)
names = ['names_example'] # list[str] | Array of Cluster Partition Names.  Filter by a list of Cluster Partition Names. If empty, the Cluster Partitions are not filtered by names. (optional)

try: 
    # List Cluster Partitions filtered by the specified parameters.
    api_response = api_instance.get_cluster_partitions(ids=ids, names=names)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ClusterPartitionsApi->get_cluster_partitions: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)| Array of Cluster Partition Ids.  Filter by a list of Cluster Partition ids. If empty, the Cluster Partitions are not filtered by id. | [optional] 
 **names** | [**list[str]**](str.md)| Array of Cluster Partition Names.  Filter by a list of Cluster Partition Names. If empty, the Cluster Partitions are not filtered by names. | [optional] 

### Return type

[**list[ClusterPartition]**](ClusterPartition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

