# UserQuotaSummaryForView

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_user_quota_policy** | [**QuotaPolicy**](QuotaPolicy.md) | Default quota policy applied to all the users in the view who doesn&#39;t have a policy override. | [optional] 
**num_users_above_alert_threshold** | **int** | Number of users who has exceeded their specified alert limit. | [optional] 
**num_users_above_hard_limit** | **int** | Number of users who has exceeded their specified quota hard limit. | [optional] 
**total_num_users** | **int** | Total number of users who has either a user quota policy override specified or has non-zero logical usage. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


