# cohesity.NotificationsApi

All URIs are relative to *https://localhost/irisservices/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_notifications**](NotificationsApi.md#get_notifications) | **GET** /public/sessionUser/notifications | List the notification of the session user.
[**update_notifications**](NotificationsApi.md#update_notifications) | **PUT** /public/sessionUser/notifications | Perform operations on the notification of the session user.


# **get_notifications**
> list[TaskNotification] get_notifications()

List the notification of the session user.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.NotificationsApi()

try: 
    # List the notification of the session user.
    api_response = api_instance.get_notifications()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling NotificationsApi->get_notifications: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TaskNotification]**](TaskNotification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_notifications**
> update_notifications()

Perform operations on the notification of the session user.

Returns success or failure.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.NotificationsApi()

try: 
    # Perform operations on the notification of the session user.
    api_instance.update_notifications()
except ApiException as e:
    print "Exception when calling NotificationsApi->update_notifications: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

