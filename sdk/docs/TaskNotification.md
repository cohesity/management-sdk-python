# TaskNotification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_time_msecs** | **int** | Timestamp at which the notification was created. | [optional] 
**description** | **str** | Description holds the actual notification text generated for the event. | [optional] 
**dismissed** | **int** | Dismissed keeps track of whether a notification has been seen or not. User may choose to dismiss individual event or all notifications at once. Nil or 0 value represents false. | [optional] 
**dismissed_time_msecs** | **int** | Timestamp at which user dismissed this notification event | [optional] 
**entity_id** | **int** | Entity fields will help clients navigate to the source page from where the notification event originated. | [optional] 
**entity_type** | **str** |  | [optional] 
**notification_id** | **str** | NotificationId identifies a user notification event uniquely. This can also be used to dismiss individual notifications. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


