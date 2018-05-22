# cohesity.PreferencesApi

All URIs are relative to *https://localhost/irisservices/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_preferences**](PreferencesApi.md#get_user_preferences) | **GET** /public/sessionUser/preferences | List the preferences of the session user.
[**update_user_preferences**](PreferencesApi.md#update_user_preferences) | **PUT** /public/sessionUser/preferences | Update the preferences of the session user


# **get_user_preferences**
> list[UserPreferencesProtoUserPreferencesPreference] get_user_preferences()

List the preferences of the session user.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.PreferencesApi()

try: 
    # List the preferences of the session user.
    api_response = api_instance.get_user_preferences()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PreferencesApi->get_user_preferences: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[UserPreferencesProtoUserPreferencesPreference]**](UserPreferencesProtoUserPreferencesPreference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_preferences**
> list[UserPreferencesProtoUserPreferencesPreference] update_user_preferences(body=body)

Update the preferences of the session user

Returns the updated user preferences.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.PreferencesApi()
body = [cohesity.UserPreferencesProtoUserPreferencesPreference()] # list[UserPreferencesProtoUserPreferencesPreference] | Request to create or update User Preferences (optional)

try: 
    # Update the preferences of the session user
    api_response = api_instance.update_user_preferences(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PreferencesApi->update_user_preferences: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[UserPreferencesProtoUserPreferencesPreference]**](UserPreferencesProtoUserPreferencesPreference.md)| Request to create or update User Preferences | [optional] 

### Return type

[**list[UserPreferencesProtoUserPreferencesPreference]**](UserPreferencesProtoUserPreferencesPreference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

