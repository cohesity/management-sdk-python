# ViewUserQuotas

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cookie** | **str** | This cookie can be used in the succeeding call to list user quotas and usages to get the next set of user quota overrides. If set to nil, it means that there&#39;s no more results that the server could provide. | [optional] 
**quota_and_usage_in_all_views** | [**list[QuotaAndUsageInView]**](QuotaAndUsageInView.md) |  | [optional] 
**summary_for_user** | [**UserQuotaSummaryForUser**](UserQuotaSummaryForUser.md) | UserQuotaSummaryForUser is the summary for user quotas in all views for a user. | [optional] 
**summary_for_view** | [**UserQuotaSummaryForView**](UserQuotaSummaryForView.md) | UserQuotaSummaryForView is the summary for user quotas in a view. | [optional] 
**user_quota_settings** | [**UserQuotaSettings**](UserQuotaSettings.md) | The default user quota policy for this view. | [optional] 
**users_quota_and_usage** | [**list[UserQuotaAndUsage]**](UserQuotaAndUsage.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


