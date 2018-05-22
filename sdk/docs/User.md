# User

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_time_msecs** | **int** | Specifies the epoch time in milliseconds when the user account was created on the Cohesity Cluster. | [optional] 
**description** | **str** | Specifies a description about the user. | [optional] 
**domain** | **str** | Specifies the fully qualified domain name (FQDN) of an Active Directory or LOCAL for the default LOCAL domain on the Cohesity Cluster. A user is uniquely identified by combination of the username and the domain. | [optional] 
**effective_time_msecs** | **int** | Specifies the epoch time in milliseconds when the user becomes effective. Until that time, the user cannot log in. | [optional] 
**email_address** | **str** | Specifies the email address of the user. | [optional] 
**last_updated_time_msecs** | **int** | Specifies the epoch time in milliseconds when the user account was last modified on the Cohesity Cluster. | [optional] 
**password** | **str** | Specifies the password of this user. | [optional] 
**restricted** | **bool** | Whether the user is a restricted user. A restricted user can only view the objects he has permissions to. | [optional] 
**roles** | **list[str]** | Specifies the Cohesity roles to associate with the user such as such as &#39;Admin&#39;, &#39;Ops&#39; or &#39;View&#39;. The Cohesity roles determine privileges on the Cohesity Cluster for this user. | [optional] 
**s3_access_key_id** | **str** | Specifies the S3 Account Access Key ID. | [optional] 
**s3_account_id** | **str** | Specifies the S3 Account Canonical User ID. | [optional] 
**s3_secret_key** | **str** | Specifies the S3 Account Secret Key. | [optional] 
**sid** | **str** | Specifies the unique Security ID (SID) of the user. | [optional] 
**username** | **str** | Specifies the login name of the user. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


