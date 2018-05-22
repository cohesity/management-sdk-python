# cohesity.CertificatesApi

All URIs are relative to *https://localhost/irisservices/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_web_server_certificate**](CertificatesApi.md#delete_web_server_certificate) | **DELETE** /public/certificates/webServer | Delete the SSL Certificate in the Cluster.
[**get_web_server_certificate**](CertificatesApi.md#get_web_server_certificate) | **GET** /public/certificates/webServer | Get the Server Certificate configured on the Cluster.
[**update_web_server_certificate**](CertificatesApi.md#update_web_server_certificate) | **PUT** /public/certificates/webServer | Update the Web Server Certificate on the Cluster.


# **delete_web_server_certificate**
> delete_web_server_certificate()

Delete the SSL Certificate in the Cluster.

Returns delete status upon completion.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.CertificatesApi()

try: 
    # Delete the SSL Certificate in the Cluster.
    api_instance.delete_web_server_certificate()
except ApiException as e:
    print "Exception when calling CertificatesApi->delete_web_server_certificate: %s\n" % e
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

# **get_web_server_certificate**
> SslCertificateConfig get_web_server_certificate()

Get the Server Certificate configured on the Cluster.

Returns the Server Certificate configured on the cluster.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.CertificatesApi()

try: 
    # Get the Server Certificate configured on the Cluster.
    api_response = api_instance.get_web_server_certificate()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CertificatesApi->get_web_server_certificate: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SslCertificateConfig**](SslCertificateConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_web_server_certificate**
> SslCertificateConfig update_web_server_certificate(body=body)

Update the Web Server Certificate on the Cluster.

Returns the updated Web Server Certificate on the cluster.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.CertificatesApi()
body = cohesity.SslCertificateConfig() # SslCertificateConfig |  (optional)

try: 
    # Update the Web Server Certificate on the Cluster.
    api_response = api_instance.update_web_server_certificate(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CertificatesApi->update_web_server_certificate: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SslCertificateConfig**](SslCertificateConfig.md)|  | [optional] 

### Return type

[**SslCertificateConfig**](SslCertificateConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

