# cohesity.StatisticsApi

All URIs are relative to *https://localhost/irisservices/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_entities**](StatisticsApi.md#get_entities) | **GET** /public/statistics/entities | Lists the entities for the specified schema.
[**get_entities_schema**](StatisticsApi.md#get_entities_schema) | **GET** /public/statistics/entitiesSchema | List the entity schemas filtered by the specified parameters.
[**get_entity_schema_by_name**](StatisticsApi.md#get_entity_schema_by_name) | **GET** /public/statistics/entitiesSchema/{schemaName} | Get the entity schema for the specified schema.
[**get_time_series_stats**](StatisticsApi.md#get_time_series_stats) | **GET** /public/statistics/timeSeriesStats | List a series of data points for an entity of a metric in a schema, during the specified time period.


# **get_entities**
> list[EntityProto] get_entities(schema_name, include_aggr_metric_sources=include_aggr_metric_sources, metric_names=metric_names)

Lists the entities for the specified schema.

An entity is an object found on the Cohesity Cluster, such as a disk or a Node. In the Cohesity Dashboard, similar functionality is provided in Advanced Diagnostics.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.StatisticsApi()
schema_name = 'schema_name_example' # str | Specifies the entity schema to search for entities.
include_aggr_metric_sources = true # bool | Specifies whether to include the sources of aggregate metrics of an entity. (optional)
metric_names = ['metric_names_example'] # list[str] | Specifies the list of metric names to return such as 'kRandomIos' which corresponds to 'Random IOs' in Advanced Diagnostics of the Cohesity Dashboard. (optional)

try: 
    # Lists the entities for the specified schema.
    api_response = api_instance.get_entities(schema_name, include_aggr_metric_sources=include_aggr_metric_sources, metric_names=metric_names)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling StatisticsApi->get_entities: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_name** | **str**| Specifies the entity schema to search for entities. | 
 **include_aggr_metric_sources** | **bool**| Specifies whether to include the sources of aggregate metrics of an entity. | [optional] 
 **metric_names** | [**list[str]**](str.md)| Specifies the list of metric names to return such as &#39;kRandomIos&#39; which corresponds to &#39;Random IOs&#39; in Advanced Diagnostics of the Cohesity Dashboard. | [optional] 

### Return type

[**list[EntityProto]**](EntityProto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entities_schema**
> list[EntitySchemaProto] get_entities_schema(schema_names=schema_names, metric_names=metric_names)

List the entity schemas filtered by the specified parameters.

An entity schema specifies the meta-data associated with entity such as the list of attributes and a time series of data. For example for a Disk entity, the entity schema specifies the Node that is using this Disk, the type of the Disk, and Metrics about the Disk such as Space Usage, Read IOs and Write IOs. Metrics define data points (time series data) to track over a period of time for a specific interval. If no parameters are specified, all entity schemas found on the Cohesity Cluster are returned. Specifying parameters filters the results that are returned. In the Cohesity Dashboard, similar functionality is provided in Advanced Diagnostics.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.StatisticsApi()
schema_names = ['schema_names_example'] # list[str] | Specifies the list of schema names to filter by such as 'kIceboxJobVaultStats' which corresponds to 'External Target Job Stats' in Advanced Diagnostics of the Cohesity Dashboard. (optional)
metric_names = ['metric_names_example'] # list[str] | Specifies the list of metric names to filter by such as 'kRandomIos' which corresponds to 'Random IOs' in Advanced Diagnostics of the Cohesity Dashboard. (optional)

try: 
    # List the entity schemas filtered by the specified parameters.
    api_response = api_instance.get_entities_schema(schema_names=schema_names, metric_names=metric_names)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling StatisticsApi->get_entities_schema: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_names** | [**list[str]**](str.md)| Specifies the list of schema names to filter by such as &#39;kIceboxJobVaultStats&#39; which corresponds to &#39;External Target Job Stats&#39; in Advanced Diagnostics of the Cohesity Dashboard. | [optional] 
 **metric_names** | [**list[str]**](str.md)| Specifies the list of metric names to filter by such as &#39;kRandomIos&#39; which corresponds to &#39;Random IOs&#39; in Advanced Diagnostics of the Cohesity Dashboard. | [optional] 

### Return type

[**list[EntitySchemaProto]**](EntitySchemaProto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_schema_by_name**
> list[EntitySchemaProto] get_entity_schema_by_name(schema_name)

Get the entity schema for the specified schema.

An entity schema specifies the meta-data associated with entity such as the list of attributes and a time series of data. For example for a Disk entity, the entity schema specifies the Node that is using this Disk, the type of the Disk, and Metrics about the Disk such as Space Usage, Read IOs and Write IOs. Metrics define data points (time series data) to track over a period of time for a specific interval. In the Cohesity Dashboard, similar functionality is provided in Advanced Diagnostics.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.StatisticsApi()
schema_name = 'schema_name_example' # str | Name of the Schema

try: 
    # Get the entity schema for the specified schema.
    api_response = api_instance.get_entity_schema_by_name(schema_name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling StatisticsApi->get_entity_schema_by_name: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_name** | **str**| Name of the Schema | 

### Return type

[**list[EntitySchemaProto]**](EntitySchemaProto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_series_stats**
> MetricDataBlock get_time_series_stats(schema_name, entity_id, metric_name, start_time_msecs, rollup_function=rollup_function, rollup_interval_secs=rollup_interval_secs, end_time_msecs=end_time_msecs)

List a series of data points for an entity of a metric in a schema, during the specified time period.

A Metric specifies a data point (such as CPU usage and IOPS) to track over a period of time. For example for a disk in the Cluster, you can report on the 'Disk Health' (kDiskAwaitTimeMsecs) Metric of the 'Disk Health Metrics' (kSentryDiskStats) Schema for the last week. You must specify the 'k' names as input and not the descriptive names. You must also specify the id of the entity that you are reporting on such as a Cluster, disk drive, job, etc. Get the entityId by running the GET /public/statistics/entities operation. In the Cohesity Dashboard, similar functionality is provided in Advanced Diagnostics.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.StatisticsApi()
schema_name = 'schema_name_example' # str | Specifies the name of entity schema such as 'kIceboxJobVaultStats'.
entity_id = 'entity_id_example' # str | Specifies the id of the entity represented as a string. Get the entityId by running the GET public/statistics/entities operation.
metric_name = 'metric_name_example' # str | Specifies the name of the metric such as the 'kDiskAwaitTimeMsecs' which is displayed as 'Disk Health' in Advanced Diagnostics of the Cohesity Dashboard.
start_time_msecs = 789 # int | Specifies the start time for the series of metric data. Specify the start time as a Unix epoch Timestamp (in milliseconds).
rollup_function = 'rollup_function_example' # str | Specifies the rollup function to apply to the data points for the time interval specified by rollupInternalSecs. The following rollup functions are available: sum, average, count, max, min, median, percentile95, latest, and rate. For more information about the functions, see the Advanced Diagnostics in the Cohesity online help. If not specified, raw data is returned. (optional)
rollup_interval_secs = 56 # int | Specifies the time interval granularity (in seconds) for the specified rollup function. Only specify a value if Rollup function is also specified. (optional)
end_time_msecs = 789 # int | Specifies the end time for the series of metric data. Specify the end time as a Unix epoch Timestamp (in milliseconds). If not specified, the data points up to the current time are returned. (optional)

try: 
    # List a series of data points for an entity of a metric in a schema, during the specified time period.
    api_response = api_instance.get_time_series_stats(schema_name, entity_id, metric_name, start_time_msecs, rollup_function=rollup_function, rollup_interval_secs=rollup_interval_secs, end_time_msecs=end_time_msecs)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling StatisticsApi->get_time_series_stats: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_name** | **str**| Specifies the name of entity schema such as &#39;kIceboxJobVaultStats&#39;. | 
 **entity_id** | **str**| Specifies the id of the entity represented as a string. Get the entityId by running the GET public/statistics/entities operation. | 
 **metric_name** | **str**| Specifies the name of the metric such as the &#39;kDiskAwaitTimeMsecs&#39; which is displayed as &#39;Disk Health&#39; in Advanced Diagnostics of the Cohesity Dashboard. | 
 **start_time_msecs** | **int**| Specifies the start time for the series of metric data. Specify the start time as a Unix epoch Timestamp (in milliseconds). | 
 **rollup_function** | **str**| Specifies the rollup function to apply to the data points for the time interval specified by rollupInternalSecs. The following rollup functions are available: sum, average, count, max, min, median, percentile95, latest, and rate. For more information about the functions, see the Advanced Diagnostics in the Cohesity online help. If not specified, raw data is returned. | [optional] 
 **rollup_interval_secs** | **int**| Specifies the time interval granularity (in seconds) for the specified rollup function. Only specify a value if Rollup function is also specified. | [optional] 
 **end_time_msecs** | **int**| Specifies the end time for the series of metric data. Specify the end time as a Unix epoch Timestamp (in milliseconds). If not specified, the data points up to the current time are returned. | [optional] 

### Return type

[**MetricDataBlock**](MetricDataBlock.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

