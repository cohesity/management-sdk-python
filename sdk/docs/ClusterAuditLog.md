# ClusterAuditLog

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Specifies the action that caused the log to be generated. | [optional] 
**details** | **str** | Specifies more information about the action. | [optional] 
**domain** | **str** | Specifies the domain of the user who caused the action that generated the log. | [optional] 
**entity_id** | **str** | Specifies the id of the entity (object) that the action is invoked on. | [optional] 
**entity_name** | **str** | Specifies the entity (object) name that the action is invoked on. For example, if a Job called BackupEng is paused, this field returns BackupEng. | [optional] 
**entity_type** | **str** | Specifies the type of the entity (object) that the action is invoked on. For example, if a Job called BackupEng is paused, this field returns &#39;Protection Job&#39;. | [optional] 
**human_timestamp** | **str** | Specifies the time when the log was generated. The time is specified using a human readable timestamp. | [optional] 
**new_record** | **str** | Specifies the record after the action is invoked. | [optional] 
**previous_record** | **str** | Specifies the record before the action is invoked. | [optional] 
**timestamp_usecs** | **int** | Specifies the time when the log was generated. The time is specified using a Unix epoch Timestamp (in microseconds). | [optional] 
**user_name** | **str** | Specifies the user who caused the action that generated the log. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


