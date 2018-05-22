# cohesity.AnalyticsApi

All URIs are relative to *https://localhost/irisservices/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyze_jar**](AnalyticsApi.md#analyze_jar) | **POST** /public/analytics/analyzeJar | Analyze the uploaded jar.
[**cancel_map_reduce_instance_run**](AnalyticsApi.md#cancel_map_reduce_instance_run) | **PUT** /public/analytics/cancelAppInstanceRun/{id} | Cancel a specific map reduce instance run.
[**create_application**](AnalyticsApi.md#create_application) | **POST** /public/analytics/apps | Create an Application.
[**create_mapper**](AnalyticsApi.md#create_mapper) | **POST** /public/analytics/mappers | Create a Mapper.
[**create_reducer**](AnalyticsApi.md#create_reducer) | **POST** /public/analytics/reducers | Create a Reducer.
[**delete_application**](AnalyticsApi.md#delete_application) | **DELETE** /public/analytics/apps/{id} | Delete an Application.
[**delete_map_reduce_instance_run**](AnalyticsApi.md#delete_map_reduce_instance_run) | **DELETE** /public/analytics/mrAppRun/{id} | Delete a Map-Reduce Application Instance Run.
[**delete_mapper**](AnalyticsApi.md#delete_mapper) | **DELETE** /public/analytics/mappers/{id} | Delete a Mapper.
[**delete_reducer**](AnalyticsApi.md#delete_reducer) | **DELETE** /public/analytics/reducers/{id} | Delete a Reducer.
[**delete_uploaded_jar**](AnalyticsApi.md#delete_uploaded_jar) | **DELETE** /public/analytics/uploadJar | Delete the uploaded jar from temporary locaation.
[**download_mr_base_jar**](AnalyticsApi.md#download_mr_base_jar) | **GET** /public/analytics/mrBaseJar | Downloads the map reduce base jar.
[**download_mr_output_files**](AnalyticsApi.md#download_mr_output_files) | **GET** /public/analytics/mrOutputfiles | Download map reduce base instance run output files from Yoda.
[**get_application_by_id**](AnalyticsApi.md#get_application_by_id) | **GET** /public/analytics/apps/{id} | List details about a single Application.
[**get_applications**](AnalyticsApi.md#get_applications) | **GET** /public/analytics/apps | List Applications filtered by the specified parameters.
[**get_map_reduce_app_runs**](AnalyticsApi.md#get_map_reduce_app_runs) | **GET** /public/analytics/mrAppRuns | List map reduce application runs filtered by the specified parameters.
[**get_mapper_by_id**](AnalyticsApi.md#get_mapper_by_id) | **GET** /public/analytics/mappers/{id} | List details about a single Mapper.
[**get_mappers**](AnalyticsApi.md#get_mappers) | **GET** /public/analytics/mappers | List Mappers filtered by the specified parameters.
[**get_mr_upload_jar_path**](AnalyticsApi.md#get_mr_upload_jar_path) | **GET** /public/analytics/uploadJarPath | Get details about the mounted path to upload Jars.
[**get_reducer_by_id**](AnalyticsApi.md#get_reducer_by_id) | **GET** /public/analytics/reducers/{id} | List details about a single Reducer.
[**get_reducers**](AnalyticsApi.md#get_reducers) | **GET** /public/analytics/reducers | List Reducers filtered by the specified parameters.
[**run_map_reduce_app_instance**](AnalyticsApi.md#run_map_reduce_app_instance) | **PUT** /public/analytics/runAppInstance | Run a map-reduce application instance.
[**update_application**](AnalyticsApi.md#update_application) | **PUT** /public/analytics/apps/{id} | Update an Application.
[**update_mapper**](AnalyticsApi.md#update_mapper) | **PUT** /public/analytics/mappers/{id} | Update a Mapper.
[**update_reducer**](AnalyticsApi.md#update_reducer) | **PUT** /public/analytics/reducers/{id} | Update a Reducer.
[**upload_jar**](AnalyticsApi.md#upload_jar) | **POST** /public/analytics/uploadJar | Upload a jar to pre-specified Yoda internal view.


# **analyze_jar**
> AnalyseJarResult analyze_jar(body=body)

Analyze the uploaded jar.

Returns the result of the jar analysis.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.AnalyticsApi()
body = cohesity.AnalyseJarArg() # AnalyseJarArg |  (optional)

try: 
    # Analyze the uploaded jar.
    api_response = api_instance.analyze_jar(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->analyze_jar: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnalyseJarArg**](AnalyseJarArg.md)|  | [optional] 

### Return type

[**AnalyseJarResult**](AnalyseJarResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_map_reduce_instance_run**
> KillMapReduceInstanceResult cancel_map_reduce_instance_run(id)

Cancel a specific map reduce instance run.

Returns the result.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.AnalyticsApi()
id = 789 # int | 

try: 
    # Cancel a specific map reduce instance run.
    api_response = api_instance.cancel_map_reduce_instance_run(id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->cancel_map_reduce_instance_run: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**KillMapReduceInstanceResult**](KillMapReduceInstanceResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_application**
> MapReduceInfo create_application(body=body)

Create an Application.

Returns the created application.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.AnalyticsApi()
body = cohesity.MapReduceInfo() # MapReduceInfo |  (optional)

try: 
    # Create an Application.
    api_response = api_instance.create_application(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->create_application: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MapReduceInfo**](MapReduceInfo.md)|  | [optional] 

### Return type

[**MapReduceInfo**](MapReduceInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_mapper**
> MapperInfo create_mapper(body=body)

Create a Mapper.

Returns the created mapper.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.AnalyticsApi()
body = cohesity.MapperInfo() # MapperInfo |  (optional)

try: 
    # Create a Mapper.
    api_response = api_instance.create_mapper(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->create_mapper: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MapperInfo**](MapperInfo.md)|  | [optional] 

### Return type

[**MapperInfo**](MapperInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_reducer**
> ReducerInfo create_reducer(body=body)

Create a Reducer.

Returns the created reducer.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.AnalyticsApi()
body = cohesity.ReducerInfo() # ReducerInfo |  (optional)

try: 
    # Create a Reducer.
    api_response = api_instance.create_reducer(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->create_reducer: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReducerInfo**](ReducerInfo.md)|  | [optional] 

### Return type

[**ReducerInfo**](ReducerInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application**
> delete_application(id)

Delete an Application.

Returns delete status upon completion.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.AnalyticsApi()
id = 789 # int | 

try: 
    # Delete an Application.
    api_instance.delete_application(id)
except ApiException as e:
    print "Exception when calling AnalyticsApi->delete_application: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_map_reduce_instance_run**
> delete_map_reduce_instance_run(id)

Delete a Map-Reduce Application Instance Run.

Returns delete status upon completion.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.AnalyticsApi()
id = 789 # int | 

try: 
    # Delete a Map-Reduce Application Instance Run.
    api_instance.delete_map_reduce_instance_run(id)
except ApiException as e:
    print "Exception when calling AnalyticsApi->delete_map_reduce_instance_run: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mapper**
> delete_mapper(id)

Delete a Mapper.

Returns delete status upon completion.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.AnalyticsApi()
id = 789 # int | 

try: 
    # Delete a Mapper.
    api_instance.delete_mapper(id)
except ApiException as e:
    print "Exception when calling AnalyticsApi->delete_mapper: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_reducer**
> delete_reducer(id)

Delete a Reducer.

Returns delete status upon completion.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.AnalyticsApi()
id = 789 # int | 

try: 
    # Delete a Reducer.
    api_instance.delete_reducer(id)
except ApiException as e:
    print "Exception when calling AnalyticsApi->delete_reducer: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_uploaded_jar**
> delete_uploaded_jar(body=body)

Delete the uploaded jar from temporary locaation.

Returns delete status upon completion.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.AnalyticsApi()
body = cohesity.UploadMRJarViewPathWrapper() # UploadMRJarViewPathWrapper |  (optional)

try: 
    # Delete the uploaded jar from temporary locaation.
    api_instance.delete_uploaded_jar(body=body)
except ApiException as e:
    print "Exception when calling AnalyticsApi->delete_uploaded_jar: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UploadMRJarViewPathWrapper**](UploadMRJarViewPathWrapper.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_mr_base_jar**
> ExtractFileRangeResult download_mr_base_jar()

Downloads the map reduce base jar.

Returns a struct containing the map reduce base jar from the cluster.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.AnalyticsApi()

try: 
    # Downloads the map reduce base jar.
    api_response = api_instance.download_mr_base_jar()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->download_mr_base_jar: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ExtractFileRangeResult**](ExtractFileRangeResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_mr_output_files**
> ExtractFileRangeResult download_mr_output_files(is_nfs_file=is_nfs_file, partition_id=partition_id, view_box_id=view_box_id, view_name=view_name, file_path=file_path, start_offset=start_offset, length_bytes=length_bytes)

Download map reduce base instance run output files from Yoda.

Returns a struct containing the map reduce instance run output files from Yoda.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.AnalyticsApi()
is_nfs_file = true # bool | If true, then extracts file from NFS, else from local file system. (optional)
partition_id = 789 # int | Cluster partition id for the file to be read. (optional)
view_box_id = 789 # int | View box id for the file to be read. Required for nfs files only. (optional)
view_name = 'view_name_example' # str | View name for the file to be read. Required for nfs files only. (optional)
file_path = 'file_path_example' # str | filepath of the file on NFS. (optional)
start_offset = 789 # int | start offset from where bytes will be read. (optional)
length_bytes = 789 # int | Number of bytes to be read from start_offset. (optional)

try: 
    # Download map reduce base instance run output files from Yoda.
    api_response = api_instance.download_mr_output_files(is_nfs_file=is_nfs_file, partition_id=partition_id, view_box_id=view_box_id, view_name=view_name, file_path=file_path, start_offset=start_offset, length_bytes=length_bytes)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->download_mr_output_files: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_nfs_file** | **bool**| If true, then extracts file from NFS, else from local file system. | [optional] 
 **partition_id** | **int**| Cluster partition id for the file to be read. | [optional] 
 **view_box_id** | **int**| View box id for the file to be read. Required for nfs files only. | [optional] 
 **view_name** | **str**| View name for the file to be read. Required for nfs files only. | [optional] 
 **file_path** | **str**| filepath of the file on NFS. | [optional] 
 **start_offset** | **int**| start offset from where bytes will be read. | [optional] 
 **length_bytes** | **int**| Number of bytes to be read from start_offset. | [optional] 

### Return type

[**ExtractFileRangeResult**](ExtractFileRangeResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_by_id**
> MapReduceInfo get_application_by_id(id)

List details about a single Application.

Returns the Application corresponding to the specified Application Id.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.AnalyticsApi()
id = 789 # int | 

try: 
    # List details about a single Application.
    api_response = api_instance.get_application_by_id(id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->get_application_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**MapReduceInfo**](MapReduceInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_applications**
> ApplicationsWrapper get_applications()

List Applications filtered by the specified parameters.

If no parameters are specified, all Applications currently on the Cohesity Cluster are returned. Specifying parameters filters the results that are returned.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.AnalyticsApi()

try: 
    # List Applications filtered by the specified parameters.
    api_response = api_instance.get_applications()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->get_applications: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApplicationsWrapper**](ApplicationsWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_map_reduce_app_runs**
> ApplicationsWrapper get_map_reduce_app_runs(body=body)

List map reduce application runs filtered by the specified parameters.

If no parameters are specified, all map reduce application instance runs currently on the Cohesity Cluster are returned. Specifying parameters filters the results that are returned.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.AnalyticsApi()
body = cohesity.GetMapReduceAppRunsParams() # GetMapReduceAppRunsParams |  (optional)

try: 
    # List map reduce application runs filtered by the specified parameters.
    api_response = api_instance.get_map_reduce_app_runs(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->get_map_reduce_app_runs: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetMapReduceAppRunsParams**](GetMapReduceAppRunsParams.md)|  | [optional] 

### Return type

[**ApplicationsWrapper**](ApplicationsWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mapper_by_id**
> MapperInfo get_mapper_by_id(id)

List details about a single Mapper.

Returns the Mapper corresponding to the specified Mapper Id.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.AnalyticsApi()
id = 789 # int | 

try: 
    # List details about a single Mapper.
    api_response = api_instance.get_mapper_by_id(id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->get_mapper_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**MapperInfo**](MapperInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mappers**
> MappersWrapper get_mappers()

List Mappers filtered by the specified parameters.

If no parameters are specified, all Mappers currently on the Cohesity Cluster are returned. Specifying parameters filters the results that are returned.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.AnalyticsApi()

try: 
    # List Mappers filtered by the specified parameters.
    api_response = api_instance.get_mappers()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->get_mappers: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MappersWrapper**](MappersWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mr_upload_jar_path**
> GetMRJarUploadPathResult get_mr_upload_jar_path()

Get details about the mounted path to upload Jars.

Returns the mounted path to upload Jars.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.AnalyticsApi()

try: 
    # Get details about the mounted path to upload Jars.
    api_response = api_instance.get_mr_upload_jar_path()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->get_mr_upload_jar_path: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetMRJarUploadPathResult**](GetMRJarUploadPathResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reducer_by_id**
> ReducerInfo get_reducer_by_id(id)

List details about a single Reducer.

Returns the Reducer corresponding to the specified Reducer Id.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.AnalyticsApi()
id = 789 # int | 

try: 
    # List details about a single Reducer.
    api_response = api_instance.get_reducer_by_id(id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->get_reducer_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ReducerInfo**](ReducerInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reducers**
> ReducersWrapper get_reducers()

List Reducers filtered by the specified parameters.

If no parameters are specified, all Reducers currently on the Cohesity Cluster are returned. Specifying parameters filters the results that are returned.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.AnalyticsApi()

try: 
    # List Reducers filtered by the specified parameters.
    api_response = api_instance.get_reducers()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->get_reducers: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ReducersWrapper**](ReducersWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_map_reduce_app_instance**
> RunMapReduceInstanceResult run_map_reduce_app_instance(body=body)

Run a map-reduce application instance.

Returns the updated Application.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.AnalyticsApi()
body = cohesity.RunMapReduceParams() # RunMapReduceParams |  (optional)

try: 
    # Run a map-reduce application instance.
    api_response = api_instance.run_map_reduce_app_instance(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->run_map_reduce_app_instance: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RunMapReduceParams**](RunMapReduceParams.md)|  | [optional] 

### Return type

[**RunMapReduceInstanceResult**](RunMapReduceInstanceResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_application**
> MapReduceInfo update_application(id, body=body)

Update an Application.

Returns the updated Application.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.AnalyticsApi()
id = 789 # int | 
body = cohesity.MapReduceInfo() # MapReduceInfo |  (optional)

try: 
    # Update an Application.
    api_response = api_instance.update_application(id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->update_application: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**MapReduceInfo**](MapReduceInfo.md)|  | [optional] 

### Return type

[**MapReduceInfo**](MapReduceInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mapper**
> MapperInfo update_mapper(id, body=body)

Update a Mapper.

Returns the updated Mapper.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.AnalyticsApi()
id = 789 # int | 
body = cohesity.MapperInfo() # MapperInfo |  (optional)

try: 
    # Update a Mapper.
    api_response = api_instance.update_mapper(id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->update_mapper: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**MapperInfo**](MapperInfo.md)|  | [optional] 

### Return type

[**MapperInfo**](MapperInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_reducer**
> ReducerInfo update_reducer(id, body=body)

Update a Reducer.

Returns the updated reducer.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.AnalyticsApi()
id = 789 # int | 
body = cohesity.ReducerInfo() # ReducerInfo |  (optional)

try: 
    # Update a Reducer.
    api_response = api_instance.update_reducer(id, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->update_reducer: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**ReducerInfo**](ReducerInfo.md)|  | [optional] 

### Return type

[**ReducerInfo**](ReducerInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_jar**
> UploadMRJarViewPathWrapper upload_jar()

Upload a jar to pre-specified Yoda internal view.

Returns a struct containing the jar name and local mount path where the jar will be uploaded.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.AnalyticsApi()

try: 
    # Upload a jar to pre-specified Yoda internal view.
    api_response = api_instance.upload_jar()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalyticsApi->upload_jar: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UploadMRJarViewPathWrapper**](UploadMRJarViewPathWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

