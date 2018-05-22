# CreateViewBoxParamsPhysicalQuota

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_limit** | **str** | AlertLimitBytes converted to GiB format for report purposes. | [optional] 
**hard_limit** | **str** | HardLimitBytes converted to GiB format for report purposes. | [optional] 
**alert_limit_bytes** | **int** | Specifies if an alert should be triggered when the usage of this resource exceeds this quota limit. This limit is optional and is specified in bytes. If no value is specified, there is no limit. | [optional] 
**alert_threshold_percentage** | **int** | Supported only for user quota policy. Specifies when the uage goes above an alert threshold percentage which is: HardLimitBytes * AlertThresholdPercentage, eg: 80% of HardLimitBytes Can only be set if HardLimitBytes is set. Cannot be set if AlertLimitBytes is already set. | [optional] 
**hard_limit_bytes** | **int** | Specifies an optional quota limit on the usage allowed for this resource. This limit is specified in bytes. If no value is specified, there is no limit. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


