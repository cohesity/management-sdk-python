# AmazonCloudCredentials

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key_id** | **str** | Specifies the access key for Amazon service account. See the Cohesity online help for the value to specify for this field based on the current S3 Compatible Vault (External Target) type. For example for Iron Mountain, specify the user name from Iron Mountain for this field. | [optional] 
**region** | **str** | Specifies the region to use for the Amazon service account. | [optional] 
**secret_access_key** | **str** | Specifies the secret access key for Amazon service account. See the Cohesity online help for the value to specify for this field based on the current S3-compatible Vault (External Target) type. | [optional] 
**service_url** | **str** | Specifies the URL (Endpoint) for the service such as s3like.notamazon.com. This field is only significant for S3-compatible cloud services. | [optional] 
**signature_version** | **int** | Specifies the version of the S3 Compliance. This field must be set to 2 or 4 and the default version is 2. This field is only significant for S3-compatible cloud services. See the Cohesity online help for the supported S3-compatible Vault (External Target) types and the value to specify for this field based on the current S3-compatible Vault (External Target) type. | [optional] 
**use_https** | **bool** | Specifies whether to use http or https to connect to the service. If true, a secure connection (https) is used. This field is only significant for S3-compatible cloud services. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


