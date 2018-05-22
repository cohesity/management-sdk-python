# cohesity.ProtectionSourcesApi

All URIs are relative to *https://localhost/irisservices/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_protection_sources_object_by_id**](ProtectionSourcesApi.md#get_protection_sources_object_by_id) | **GET** /public/protectionSources/objects/{id} | Get details about a single Protection Source Object.
[**get_protection_sources_objects**](ProtectionSourcesApi.md#get_protection_sources_objects) | **GET** /public/protectionSources/objects | List details about Protection Source objects.
[**list_application_servers**](ProtectionSourcesApi.md#list_application_servers) | **GET** /public/protectionSources/applicationServers | Returns the registered Application Servers and their Object subtrees.
[**list_protected_vms**](ProtectionSourcesApi.md#list_protected_vms) | **GET** /public/protectionSources/protectedVms | Returns the list of protected VMs in a registered Protection Source tree.
[**list_protection_sources**](ProtectionSourcesApi.md#list_protection_sources) | **GET** /public/protectionSources | Returns the registered Protection Sources and their Object subtrees.
[**list_protection_sources_registration_info**](ProtectionSourcesApi.md#list_protection_sources_registration_info) | **GET** /public/protectionSources/registrationInfo | 
[**list_protection_sources_root_nodes**](ProtectionSourcesApi.md#list_protection_sources_root_nodes) | **GET** /public/protectionSources/rootNodes | Returns the top level (root) Protection Sources with registration information.
[**list_sql_aag_hosts_and_databases**](ProtectionSourcesApi.md#list_sql_aag_hosts_and_databases) | **GET** /public/protectionSources/sqlAagHostsAndDatabases | Returns the registered Protection Sources and their Object subtrees.
[**list_virtual_machines**](ProtectionSourcesApi.md#list_virtual_machines) | **GET** /public/protectionSources/virtualMachines | Returns the Virtual Machines in a vCenter Server.
[**refresh_protection_source_by_id**](ProtectionSourcesApi.md#refresh_protection_source_by_id) | **POST** /public/protectionSources/refresh/{id} | Refresh the Object hierarchy of the Protection Sources tree.
[**register_application_servers**](ProtectionSourcesApi.md#register_application_servers) | **POST** /public/protectionSources/applicationServers | Register a Protection Source as running one or more Application Servers like Microsoft SQL servers or Microsoft Exchange servers.
[**register_protection_source**](ProtectionSourcesApi.md#register_protection_source) | **POST** /public/protectionSources/register | Register a Protection Source.
[**unregister_application_servers**](ProtectionSourcesApi.md#unregister_application_servers) | **DELETE** /public/protectionSources/applicationServers/{id} | Unregister Application Servers like Microsoft SQL servers or Microsoft Exchange servers running on a Protection Source.
[**update_application_servers**](ProtectionSourcesApi.md#update_application_servers) | **PUT** /public/protectionSources/applicationServers | Modifies the registration parameters of Application Servers in a Protection Source.
[**upgrade_physical_agents**](ProtectionSourcesApi.md#upgrade_physical_agents) | **POST** /public/physicalAgents/upgrade | Initiate a request to upgrade Cohesity agents on one or more Physical Servers registered on the Cohesity Cluster.


# **get_protection_sources_object_by_id**
> ProtectionSource get_protection_sources_object_by_id(id)

Get details about a single Protection Source Object.

Returns the Protection Source object corresponding to the specified id.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ProtectionSourcesApi()
id = 789 # int | Specifies a unique id of the Protection Source to return.

try: 
    # Get details about a single Protection Source Object.
    api_response = api_instance.get_protection_sources_object_by_id(id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProtectionSourcesApi->get_protection_sources_object_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a unique id of the Protection Source to return. | 

### Return type

[**ProtectionSource**](ProtectionSource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_protection_sources_objects**
> list[ProtectionSource] get_protection_sources_objects(object_ids=object_ids)

List details about Protection Source objects.

Returns the Protection Source objects corresponding to the specified ids.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ProtectionSourcesApi()
object_ids = [56] # list[int] | Specifies the ids of the Protection Source objects to return. (optional)

try: 
    # List details about Protection Source objects.
    api_response = api_instance.get_protection_sources_objects(object_ids=object_ids)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProtectionSourcesApi->get_protection_sources_objects: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_ids** | [**list[int]**](int.md)| Specifies the ids of the Protection Source objects to return. | [optional] 

### Return type

[**list[ProtectionSource]**](ProtectionSource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_application_servers**
> list[RegisteredApplicationServer] list_application_servers(protection_sources_root_node_id=protection_sources_root_node_id, environment=environment, application=application)

Returns the registered Application Servers and their Object subtrees.

Given the root node id of a Protection Source tree, returns the list of Application Servers registered under that tree based on the filters.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ProtectionSourcesApi()
protection_sources_root_node_id = 789 # int | Specifies the Protection Source Id of the root node of a Protection Sources tree. A root node represents a registered Source on the Cohesity Cluster, such as a vCenter Server. (optional)
environment = 'environment_example' # str | Specifies the environment such as 'kPhysical' or 'kVMware' of the Protection Source tree. overrideDescription: true Supported environment types include 'kView', 'kSQL', 'kVMware', 'kPuppeteer', 'kPhysical', 'kPure', 'kNetapp, 'kGenericNas, 'kHyperV', 'kAcropolis', 'kAzure'. NOTE: 'kPuppeteer' refers to Cohesity's Remote Adapter. (optional)
application = 'application_example' # str | Specifies the application such as 'kSQL', 'kExchange' running on the Protection Source. overrideDescription: true Supported environment types include 'kView', 'kSQL', 'kVMware', 'kPuppeteer', 'kPhysical', 'kPure', 'kNetapp, 'kGenericNas, 'kHyperV', 'kAcropolis', 'kAzure'. NOTE: 'kPuppeteer' refers to Cohesity's Remote Adapter. (optional)

try: 
    # Returns the registered Application Servers and their Object subtrees.
    api_response = api_instance.list_application_servers(protection_sources_root_node_id=protection_sources_root_node_id, environment=environment, application=application)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProtectionSourcesApi->list_application_servers: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **protection_sources_root_node_id** | **int**| Specifies the Protection Source Id of the root node of a Protection Sources tree. A root node represents a registered Source on the Cohesity Cluster, such as a vCenter Server. | [optional] 
 **environment** | **str**| Specifies the environment such as &#39;kPhysical&#39; or &#39;kVMware&#39; of the Protection Source tree. overrideDescription: true Supported environment types include &#39;kView&#39;, &#39;kSQL&#39;, &#39;kVMware&#39;, &#39;kPuppeteer&#39;, &#39;kPhysical&#39;, &#39;kPure&#39;, &#39;kNetapp, &#39;kGenericNas, &#39;kHyperV&#39;, &#39;kAcropolis&#39;, &#39;kAzure&#39;. NOTE: &#39;kPuppeteer&#39; refers to Cohesity&#39;s Remote Adapter. | [optional] 
 **application** | **str**| Specifies the application such as &#39;kSQL&#39;, &#39;kExchange&#39; running on the Protection Source. overrideDescription: true Supported environment types include &#39;kView&#39;, &#39;kSQL&#39;, &#39;kVMware&#39;, &#39;kPuppeteer&#39;, &#39;kPhysical&#39;, &#39;kPure&#39;, &#39;kNetapp, &#39;kGenericNas, &#39;kHyperV&#39;, &#39;kAcropolis&#39;, &#39;kAzure&#39;. NOTE: &#39;kPuppeteer&#39; refers to Cohesity&#39;s Remote Adapter. | [optional] 

### Return type

[**list[RegisteredApplicationServer]**](RegisteredApplicationServer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_protected_vms**
> list[ProtectedVmInfo] list_protected_vms(environment, id)

Returns the list of protected VMs in a registered Protection Source tree.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ProtectionSourcesApi()
environment = 'environment_example' # str | Specifies the environment type of the registered Protection Source such as 'kVMware', 'kSQL', 'kView' 'kPhysical', 'kPuppeteer', 'kPure', 'kNetapp', 'kGenericNas', 'kHyperV', 'kAcropolis', or 'kAzure'. For example, set this parameter to 'kVMware' if the registered Protection Source is of 'kVMware' environment type. Supported environment types include 'kView', 'kSQL', 'kVMware', 'kPuppeteer', 'kPhysical', 'kPure', 'kNetapp, 'kGenericNas, 'kHyperV', 'kAcropolis', 'kAzure'. NOTE: 'kPuppeteer' refers to Cohesity's Remote Adapter.
id = 789 # int | Specifies the Id of a registered Protection Source of the type given in environment.

try: 
    # Returns the list of protected VMs in a registered Protection Source tree.
    api_response = api_instance.list_protected_vms(environment, id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProtectionSourcesApi->list_protected_vms: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| Specifies the environment type of the registered Protection Source such as &#39;kVMware&#39;, &#39;kSQL&#39;, &#39;kView&#39; &#39;kPhysical&#39;, &#39;kPuppeteer&#39;, &#39;kPure&#39;, &#39;kNetapp&#39;, &#39;kGenericNas&#39;, &#39;kHyperV&#39;, &#39;kAcropolis&#39;, or &#39;kAzure&#39;. For example, set this parameter to &#39;kVMware&#39; if the registered Protection Source is of &#39;kVMware&#39; environment type. Supported environment types include &#39;kView&#39;, &#39;kSQL&#39;, &#39;kVMware&#39;, &#39;kPuppeteer&#39;, &#39;kPhysical&#39;, &#39;kPure&#39;, &#39;kNetapp, &#39;kGenericNas, &#39;kHyperV&#39;, &#39;kAcropolis&#39;, &#39;kAzure&#39;. NOTE: &#39;kPuppeteer&#39; refers to Cohesity&#39;s Remote Adapter. | 
 **id** | **int**| Specifies the Id of a registered Protection Source of the type given in environment. | 

### Return type

[**list[ProtectedVmInfo]**](ProtectedVmInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_protection_sources**
> list[ProtectionSourceNode] list_protection_sources(id=id, exclude_types=exclude_types, include_datastores=include_datastores, include_networks=include_networks, include_vm_folders=include_vm_folders, environments=environments, environment=environment)

Returns the registered Protection Sources and their Object subtrees.

If no parameters are specified, all Protection Sources that are registered on the Cohesity Cluster are returned. In addition, an Object subtree gathered from each Source is returned. For example, the Cohesity Cluster interrogates a Source VMware vCenter Server and creates an hierarchical Object subtree that mirrors the Inventory tree on vCenter Server. The contents of the Object tree is returned as a \"nodes\" hierarchy of \"protectionSource\"s. Specifying parameters can alter the results that are returned.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ProtectionSourcesApi()
id = 789 # int | Return the Object subtree for the passed in Protection Source id. (optional)
exclude_types = ['exclude_types_example'] # list[str] | Filter out the Object types (and their subtrees) that match the passed in types such as 'kVCenter', 'kFolder', 'kDatacenter', 'kComputeResource', 'kResourcePool', 'kDatastore', 'kHostSystem', 'kVirtualMachine', etc. For example, set this parameter to 'kResourcePool' to exclude Resource Pool Objects from being returned. (optional)
include_datastores = true # bool | Set this parameter to true to also return kDatastore object types found in the Source in addition to their Object subtrees. By default, datastores are not returned. (optional)
include_networks = true # bool | Set this parameter to true to also return kNetwork object types found in the Source in addition to their Object subtrees. By default, network objects are not returned. (optional)
include_vm_folders = true # bool | Set this parameter to true to also return kVMFolder object types found in the Source in addition to their Object subtrees. By default, VM folder objects are not returned. (optional)
environments = ['environments_example'] # list[str] | Return only Protection Sources that match the passed in environment type such as 'kVMware', 'kSQL', 'kView' 'kPhysical', 'kPuppeteer', 'kPure', 'kNetapp', 'kGenericNas', 'kHyperV', 'kAcropolis', or 'kAzure'. For example, set this parameter to 'kVMware' to only return the Sources (and their Object subtrees) found in the 'kVMware' (VMware vCenter Server) environment.  NOTE: 'kPuppeteer' refers to Cohesity's Remote Adapter. (optional)
environment = 'environment_example' # str | This field is deprecated. Use environments instead. deprecated: true (optional)

try: 
    # Returns the registered Protection Sources and their Object subtrees.
    api_response = api_instance.list_protection_sources(id=id, exclude_types=exclude_types, include_datastores=include_datastores, include_networks=include_networks, include_vm_folders=include_vm_folders, environments=environments, environment=environment)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProtectionSourcesApi->list_protection_sources: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Return the Object subtree for the passed in Protection Source id. | [optional] 
 **exclude_types** | [**list[str]**](str.md)| Filter out the Object types (and their subtrees) that match the passed in types such as &#39;kVCenter&#39;, &#39;kFolder&#39;, &#39;kDatacenter&#39;, &#39;kComputeResource&#39;, &#39;kResourcePool&#39;, &#39;kDatastore&#39;, &#39;kHostSystem&#39;, &#39;kVirtualMachine&#39;, etc. For example, set this parameter to &#39;kResourcePool&#39; to exclude Resource Pool Objects from being returned. | [optional] 
 **include_datastores** | **bool**| Set this parameter to true to also return kDatastore object types found in the Source in addition to their Object subtrees. By default, datastores are not returned. | [optional] 
 **include_networks** | **bool**| Set this parameter to true to also return kNetwork object types found in the Source in addition to their Object subtrees. By default, network objects are not returned. | [optional] 
 **include_vm_folders** | **bool**| Set this parameter to true to also return kVMFolder object types found in the Source in addition to their Object subtrees. By default, VM folder objects are not returned. | [optional] 
 **environments** | [**list[str]**](str.md)| Return only Protection Sources that match the passed in environment type such as &#39;kVMware&#39;, &#39;kSQL&#39;, &#39;kView&#39; &#39;kPhysical&#39;, &#39;kPuppeteer&#39;, &#39;kPure&#39;, &#39;kNetapp&#39;, &#39;kGenericNas&#39;, &#39;kHyperV&#39;, &#39;kAcropolis&#39;, or &#39;kAzure&#39;. For example, set this parameter to &#39;kVMware&#39; to only return the Sources (and their Object subtrees) found in the &#39;kVMware&#39; (VMware vCenter Server) environment.  NOTE: &#39;kPuppeteer&#39; refers to Cohesity&#39;s Remote Adapter. | [optional] 
 **environment** | **str**| This field is deprecated. Use environments instead. deprecated: true | [optional] 

### Return type

[**list[ProtectionSourceNode]**](ProtectionSourceNode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_protection_sources_registration_info**
> GetRegistrationInfoResponse list_protection_sources_registration_info(view_names=view_names, environments=environments, ids=ids)



Returns the registration and protection information of the registered Protection Sources.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ProtectionSourcesApi()
view_names = ['view_names_example'] # list[str] | Return only the Views whose names are specified in the list. (optional)
environments = ['environments_example'] # list[str] | Return only Protection Sources that match the passed in environment type such as 'kVMware', 'kSQL', 'kView' 'kPhysical', 'kPuppeteer', 'kPure', 'kNetapp', 'kGenericNas', 'kHyperV', 'kAcropolis', or 'kAzure'. For example, set this parameter to 'kVMware' to only return the Sources (and their Object subtrees) found in the 'kVMware' (VMware vCenter Server) environment.  NOTE: 'kPuppeteer' refers to Cohesity's Remote Adapter. (optional)
ids = [56] # list[int] | Return only the registered root nodes whose Ids are given in the list. (optional)

try: 
    api_response = api_instance.list_protection_sources_registration_info(view_names=view_names, environments=environments, ids=ids)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProtectionSourcesApi->list_protection_sources_registration_info: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_names** | [**list[str]**](str.md)| Return only the Views whose names are specified in the list. | [optional] 
 **environments** | [**list[str]**](str.md)| Return only Protection Sources that match the passed in environment type such as &#39;kVMware&#39;, &#39;kSQL&#39;, &#39;kView&#39; &#39;kPhysical&#39;, &#39;kPuppeteer&#39;, &#39;kPure&#39;, &#39;kNetapp&#39;, &#39;kGenericNas&#39;, &#39;kHyperV&#39;, &#39;kAcropolis&#39;, or &#39;kAzure&#39;. For example, set this parameter to &#39;kVMware&#39; to only return the Sources (and their Object subtrees) found in the &#39;kVMware&#39; (VMware vCenter Server) environment.  NOTE: &#39;kPuppeteer&#39; refers to Cohesity&#39;s Remote Adapter. | [optional] 
 **ids** | [**list[int]**](int.md)| Return only the registered root nodes whose Ids are given in the list. | [optional] 

### Return type

[**GetRegistrationInfoResponse**](GetRegistrationInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_protection_sources_root_nodes**
> list[ProtectionSourceNode] list_protection_sources_root_nodes(id=id, environments=environments, environment=environment)

Returns the top level (root) Protection Sources with registration information.

Returns the root Protection Sources and the registration information for each of these Sources.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ProtectionSourcesApi()
id = 789 # int | Return the registration information for the Protection Source id. (optional)
environments = ['environments_example'] # list[str] | Return only the root Protection Sources that match the passed in environment type such as 'kVMware', 'kSQL', 'kView', 'kPuppeteer', 'kPhysical', 'kPure', 'kNetapp', 'kGenericNas', 'kHyperV', 'kAcropolis' 'kAzure'. For example, set this parameter to 'kVMware' to only return the root Protection Sources found in the 'kVMware' (VMware vCenter) environment. In addition, the registration information for each Source is returned.  NOTE: 'kPuppeteer' refers to Cohesity's Remote Adapter. (optional)
environment = 'environment_example' # str | This field is deprecated. Use environments instead. deprecated: true (optional)

try: 
    # Returns the top level (root) Protection Sources with registration information.
    api_response = api_instance.list_protection_sources_root_nodes(id=id, environments=environments, environment=environment)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProtectionSourcesApi->list_protection_sources_root_nodes: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Return the registration information for the Protection Source id. | [optional] 
 **environments** | [**list[str]**](str.md)| Return only the root Protection Sources that match the passed in environment type such as &#39;kVMware&#39;, &#39;kSQL&#39;, &#39;kView&#39;, &#39;kPuppeteer&#39;, &#39;kPhysical&#39;, &#39;kPure&#39;, &#39;kNetapp&#39;, &#39;kGenericNas&#39;, &#39;kHyperV&#39;, &#39;kAcropolis&#39; &#39;kAzure&#39;. For example, set this parameter to &#39;kVMware&#39; to only return the root Protection Sources found in the &#39;kVMware&#39; (VMware vCenter) environment. In addition, the registration information for each Source is returned.  NOTE: &#39;kPuppeteer&#39; refers to Cohesity&#39;s Remote Adapter. | [optional] 
 **environment** | **str**| This field is deprecated. Use environments instead. deprecated: true | [optional] 

### Return type

[**list[ProtectionSourceNode]**](ProtectionSourceNode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sql_aag_hosts_and_databases**
> list[SqlAagHostAndDatabases] list_sql_aag_hosts_and_databases(sql_protection_source_ids)

Returns the registered Protection Sources and their Object subtrees.

Given a list of Protection Source Ids registered as SQL servers, returns AAGs found and the databases in AAG(Always on Availablity Group).

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ProtectionSourcesApi()
sql_protection_source_ids = [56] # list[int] | Specifies a list of Ids of Protection Sources registered as SQL servers. These sources may have one or more SQL databases in them. Some of them may be part of AAGs(Always on Availability Group).

try: 
    # Returns the registered Protection Sources and their Object subtrees.
    api_response = api_instance.list_sql_aag_hosts_and_databases(sql_protection_source_ids)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProtectionSourcesApi->list_sql_aag_hosts_and_databases: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sql_protection_source_ids** | [**list[int]**](int.md)| Specifies a list of Ids of Protection Sources registered as SQL servers. These sources may have one or more SQL databases in them. Some of them may be part of AAGs(Always on Availability Group). | 

### Return type

[**list[SqlAagHostAndDatabases]**](SqlAagHostAndDatabases.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_virtual_machines**
> list[ProtectionSource] list_virtual_machines(v_center_id=v_center_id, names=names, uuids=uuids, protected=protected)

Returns the Virtual Machines in a vCenter Server.

Returns all Virtual Machines found in all the vCenter Servers registered on the Cohesity Cluster that match the filter criteria specified using parameters. If an id is specified, only VMs found in the specified vCenter Server are returned. Only VM Objects are returned. Other VMware Objects such as datacenters are not returned.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ProtectionSourcesApi()
v_center_id = 789 # int | Limit the VMs returned to the set of VMs found in a specific vCenter Server. Pass in the root Protection Source id for the vCenter Server to search for VMs. (optional)
names = ['names_example'] # list[str] | Limit the returned VMs to those that exactly match the passed in VM name. To match multiple VM names, specify multiple \"names\" parameters that each specify a single VM name. The string must exactly match the passed in VM name and wild cards are not supported. (optional)
uuids = ['uuids_example'] # list[str] | Limit the returned VMs to those that exactly match the passed in UUIDs. (optional)
protected = true # bool | Limit the returned VMs to those that have been protected by a Protection Job. By default, both protected and unprotected VMs are returned. (optional)

try: 
    # Returns the Virtual Machines in a vCenter Server.
    api_response = api_instance.list_virtual_machines(v_center_id=v_center_id, names=names, uuids=uuids, protected=protected)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProtectionSourcesApi->list_virtual_machines: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v_center_id** | **int**| Limit the VMs returned to the set of VMs found in a specific vCenter Server. Pass in the root Protection Source id for the vCenter Server to search for VMs. | [optional] 
 **names** | [**list[str]**](str.md)| Limit the returned VMs to those that exactly match the passed in VM name. To match multiple VM names, specify multiple \&quot;names\&quot; parameters that each specify a single VM name. The string must exactly match the passed in VM name and wild cards are not supported. | [optional] 
 **uuids** | [**list[str]**](str.md)| Limit the returned VMs to those that exactly match the passed in UUIDs. | [optional] 
 **protected** | **bool**| Limit the returned VMs to those that have been protected by a Protection Job. By default, both protected and unprotected VMs are returned. | [optional] 

### Return type

[**list[ProtectionSource]**](ProtectionSource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_protection_source_by_id**
> refresh_protection_source_by_id(id)

Refresh the Object hierarchy of the Protection Sources tree.

Force an immediate refresh between the specified Protection Source tree on the Cohesity Cluster and the Inventory tree in the associated vCenter Server.  For example if a new VM is added to the vCenter Server, after a refresh, a new Protection Source node for this VM is added to the Protection Sources tree.  Success indicates the forced refresh has been started. The amount of time to complete a refresh depends on the size of the Object hierarchies.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ProtectionSourcesApi()
id = 789 # int | Id of the root node of the Protection Sources tree to refresh.  Force a refresh of the Object hierarchy for the passed in Protection Sources Id.

try: 
    # Refresh the Object hierarchy of the Protection Sources tree.
    api_instance.refresh_protection_source_by_id(id)
except ApiException as e:
    print "Exception when calling ProtectionSourcesApi->refresh_protection_source_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of the root node of the Protection Sources tree to refresh.  Force a refresh of the Object hierarchy for the passed in Protection Sources Id. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_application_servers**
> ProtectionSource register_application_servers(body)

Register a Protection Source as running one or more Application Servers like Microsoft SQL servers or Microsoft Exchange servers.

Registering Application Servers will help Cohesity Cluster such that any application specific data can be backed up.  Returns the Protection Source registered upon success.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ProtectionSourcesApi()
body = cohesity.RegisterApplicationServersParameters() # RegisterApplicationServersParameters | Request to register Application Servers in a Protection Source.

try: 
    # Register a Protection Source as running one or more Application Servers like Microsoft SQL servers or Microsoft Exchange servers.
    api_response = api_instance.register_application_servers(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProtectionSourcesApi->register_application_servers: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RegisterApplicationServersParameters**](RegisterApplicationServersParameters.md)| Request to register Application Servers in a Protection Source. | 

### Return type

[**ProtectionSource**](ProtectionSource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_protection_source**
> ProtectionSource register_protection_source(body)

Register a Protection Source.

Register a Protection Source on the Cohesity Cluster. It could be the root node of a vCenter Server or a physcical server.  Returns the newly registered Protection Source upon success.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ProtectionSourcesApi()
body = cohesity.RegisterProtectionSourceParameters() # RegisterProtectionSourceParameters | Request to register a protection source.

try: 
    # Register a Protection Source.
    api_response = api_instance.register_protection_source(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProtectionSourcesApi->register_protection_source: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RegisterProtectionSourceParameters**](RegisterProtectionSourceParameters.md)| Request to register a protection source. | 

### Return type

[**ProtectionSource**](ProtectionSource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unregister_application_servers**
> ProtectionSource unregister_application_servers(id)

Unregister Application Servers like Microsoft SQL servers or Microsoft Exchange servers running on a Protection Source.

Unregistering Application Servers will fail if the Protection Source is currently being backed up.  Returns the Protection Source whose Application Servers are unregistered upon success.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ProtectionSourcesApi()
id = 789 # int | Specifies a unique id of the Protection Source to unregister the Application Servers. If the Protection Source is currently being backed up, unregister operation will fail.

try: 
    # Unregister Application Servers like Microsoft SQL servers or Microsoft Exchange servers running on a Protection Source.
    api_response = api_instance.unregister_application_servers(id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProtectionSourcesApi->unregister_application_servers: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a unique id of the Protection Source to unregister the Application Servers. If the Protection Source is currently being backed up, unregister operation will fail. | 

### Return type

[**ProtectionSource**](ProtectionSource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_application_servers**
> ProtectionSource update_application_servers(body)

Modifies the registration parameters of Application Servers in a Protection Source.

Returns the Protection Source whose registration parameters of its Application Servers are modified upon success.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ProtectionSourcesApi()
body = cohesity.UpdateApplicationServerParameters() # UpdateApplicationServerParameters | Request to modify the Application Servers registration of a Protection Source.

try: 
    # Modifies the registration parameters of Application Servers in a Protection Source.
    api_response = api_instance.update_application_servers(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProtectionSourcesApi->update_application_servers: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateApplicationServerParameters**](UpdateApplicationServerParameters.md)| Request to modify the Application Servers registration of a Protection Source. | 

### Return type

[**ProtectionSource**](ProtectionSource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upgrade_physical_agents**
> UpgradePhysicalAgentsMessage upgrade_physical_agents(body=body)

Initiate a request to upgrade Cohesity agents on one or more Physical Servers registered on the Cohesity Cluster.

If the request is successful, the Cohesity agents on the specified Physical Servers are upgraded to the agent release currently available from this Cohesity Cluster. For example if the Cluster is upgraded from 3.7.1 to 4.0, the agents on the specified Physical Servers can be upgraded to 4.0 using this POST operation. To get the agentIds to pass into this operation, call GET /public/protectionSources with the environment set to 'KPhysical'. In addition this GET operation returns the agentUpgradability field, that indicates if an agent can be upgraded. Use the agentUpgradability field to determine which Physical Servers to upgrade using this POST /public/physicalAgents/upgrade operation.  WARNING: Only agents at a particular Cohesity release can be upgraded using this operation. See the Cohesity online help for details.  Returns the status of the upgrade initiation.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.ProtectionSourcesApi()
body = cohesity.UpgradePhysicalServerAgents() # UpgradePhysicalServerAgents | Request to upgrade agents on Physical Servers. (optional)

try: 
    # Initiate a request to upgrade Cohesity agents on one or more Physical Servers registered on the Cohesity Cluster.
    api_response = api_instance.upgrade_physical_agents(body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProtectionSourcesApi->upgrade_physical_agents: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpgradePhysicalServerAgents**](UpgradePhysicalServerAgents.md)| Request to upgrade agents on Physical Servers. | [optional] 

### Return type

[**UpgradePhysicalAgentsMessage**](UpgradePhysicalAgentsMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

