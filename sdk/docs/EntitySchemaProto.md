# EntitySchemaProto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes_descriptor** | [**EntitySchemaProtoAttributesDescriptor**](EntitySchemaProtoAttributesDescriptor.md) |  | [optional] 
**is_internal_schema** | **bool** | Specifies if this schema should be displayed in Advanced Diagnostics of the Cohesity Dashboard. If false, the schema is displayed. | [optional] 
**name** | **str** | Specifies a name that uniquely identifies an entity schema such as &#39;kBridgeClusterStats&#39;. | [optional] 
**schema_descriptive_name** | **str** | Specifies the name of the Schema as displayed in Advanced Diagnostics of the Cohesity Dashboard. For example for the &#39;kBridgeClusterStats&#39; Schema, the descriptive name is &#39;Cluster Physical Stats&#39;. | [optional] 
**schema_help_text** | **str** | Specifies an optional informational description about the schema. | [optional] 
**time_series_descriptor_vec** | [**list[EntitySchemaProtoTimeSeriesDescriptor]**](EntitySchemaProtoTimeSeriesDescriptor.md) | List of time series of data (set of data points) for metrics. | [optional] 
**version** | **int** | Specifies the version of the entity schema. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


