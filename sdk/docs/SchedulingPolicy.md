# SchedulingPolicy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continuous_schedule** | [**ProtectionPolicyFullSchedulingPolicyContinuousSchedule**](ProtectionPolicyFullSchedulingPolicyContinuousSchedule.md) |  | [optional] 
**daily_schedule** | [**ProtectionPolicyFullSchedulingPolicyDailySchedule**](ProtectionPolicyFullSchedulingPolicyDailySchedule.md) |  | [optional] 
**monthly_schedule** | [**ProtectionPolicyFullSchedulingPolicyMonthlySchedule**](ProtectionPolicyFullSchedulingPolicyMonthlySchedule.md) |  | [optional] 
**periodicity** | **str** | Specifies how often to start new Job Runs of a Protection Job. &#39;kDaily&#39; means new Job Runs start daily. &#39;kMonthly&#39; means new Job Runs start monthly. &#39;kContinuous&#39; means new Job Runs repetitively start at the beginning of the specified time interval (in hours or minutes). &#39;kOneOff&#39; means this is an additional schedule. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


