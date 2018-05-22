# cohesity.RestoreTasksApi

All URIs are relative to *https://localhost/irisservices/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_restore_task**](RestoreTasksApi.md#cancel_restore_task) | **PUT** /public/restore/tasks/cancel/{id} | Cancel a recover or clone task with specified id.
[**create_applications_clone_task**](RestoreTasksApi.md#create_applications_clone_task) | **POST** /public/restore/applicationsClone | Create a Restore Task for cloning Applications like SQL Databases.
[**create_applications_recover_task**](RestoreTasksApi.md#create_applications_recover_task) | **POST** /public/restore/applicationsRecover | Create a Restore Task for recovering Applications like SQL Databases.
[**create_clone_task**](RestoreTasksApi.md#create_clone_task) | **POST** /public/restore/clone | Create a Restore Task for cloning VMs or a View.
[**create_recover_task**](RestoreTasksApi.md#create_recover_task) | **POST** /public/restore/recover | Create a Restore Task for recovering VMs or instantly mounting volumes.
[**create_restore_files_task**](RestoreTasksApi.md#create_restore_files_task) | **POST** /public/restore/files | Create a Restore Task for recovering files and folders.
[**get_file_snapshots_information**](RestoreTasksApi.md#get_file_snapshots_information) | **GET** /public/restore/files/snapshotsInformation | Get the information about snapshots that contain the specified file or folder. In addition, information about the file or folder is provided.
[**get_restore_task_by_id**](RestoreTasksApi.md#get_restore_task_by_id) | **GET** /public/restore/tasks/{id} | List details about a single Restore Task.
[**get_restore_tasks**](RestoreTasksApi.md#get_restore_tasks) | **GET** /public/restore/tasks | List the Restore Tasks filtered by the specified parameters.
[**get_vm_volumes_information**](RestoreTasksApi.md#get_vm_volumes_information) | **GET** /public/restore/vms/volumesInformation | Get information about the logical volumes found in a VM.
[**search_objects**](RestoreTasksApi.md#search_objects) | **GET** /public/restore/objects | Find backup objects that match the specified search and filter criteria on the Cohesity Cluster.
[**search_restored_files**](RestoreTasksApi.md#search_restored_files) | **GET** /public/restore/files | Search for files and folders to recover that match the specified search and filter criteria on the Cohesity Cluster.


# **cancel_restore_task**
> cancel_restore_task(id)

Cancel a recover or clone task with specified id.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.RestoreTasksApi()
id = 789 # int | Specifies a unique id for the Restore Task.

try: 
    # Cancel a recover or clone task with specified id.
    api_instance.cancel_restore_task(id)
except ApiException as e:
    print "Exception when calling RestoreTasksApi->cancel_restore_task: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a unique id for the Restore Task. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_applications_clone_task**
> RestoreTask create_applications_clone_task(body)

Create a Restore Task for cloning Applications like SQL Databases.

Returns the created Restore Task.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.RestoreTasksApi()
body = cohesity.ApplicationsRestoreTaskRequest() # ApplicationsRestoreTaskRequest | Request to create a Restore Task for cloning Applications like SQL DB.

try: 
    # Create a Restore Task for cloning Applications like SQL Databases.
    api_response = api_instance.create_applications_clone_task(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RestoreTasksApi->create_applications_clone_task: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApplicationsRestoreTaskRequest**](ApplicationsRestoreTaskRequest.md)| Request to create a Restore Task for cloning Applications like SQL DB. | 

### Return type

[**RestoreTask**](RestoreTask.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_applications_recover_task**
> RestoreTask create_applications_recover_task(body)

Create a Restore Task for recovering Applications like SQL Databases.

Returns the created Restore Task.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.RestoreTasksApi()
body = cohesity.ApplicationsRestoreTaskRequest() # ApplicationsRestoreTaskRequest | Request to create a Restore Task for recovering Applications like SQL DB. volumes to mount points.

try: 
    # Create a Restore Task for recovering Applications like SQL Databases.
    api_response = api_instance.create_applications_recover_task(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RestoreTasksApi->create_applications_recover_task: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApplicationsRestoreTaskRequest**](ApplicationsRestoreTaskRequest.md)| Request to create a Restore Task for recovering Applications like SQL DB. volumes to mount points. | 

### Return type

[**RestoreTask**](RestoreTask.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_clone_task**
> RestoreTask create_clone_task(body)

Create a Restore Task for cloning VMs or a View.

Returns the created Restore Task that clones VMs or a View.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.RestoreTasksApi()
body = cohesity.CloneTaskRequest() # CloneTaskRequest | Request to create a Restore Task for cloning VMs or a View.

try: 
    # Create a Restore Task for cloning VMs or a View.
    api_response = api_instance.create_clone_task(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RestoreTasksApi->create_clone_task: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloneTaskRequest**](CloneTaskRequest.md)| Request to create a Restore Task for cloning VMs or a View. | 

### Return type

[**RestoreTask**](RestoreTask.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_recover_task**
> RestoreTask create_recover_task(body)

Create a Restore Task for recovering VMs or instantly mounting volumes.

Returns the created Restore Task. This operation returns the following types of Restore Tasks: 1) A Restore Task that recovers VMs back to the original location or a new location. 2) A Restore Task that mounts the volumes of a Server (such as a VM or Physical Server) onto the specified target system. The Snapshots of the Server that contains the volumes that are mounted is determined by Array of Objects. The content of the Server is available from the mount point for the Granular Level Recovery (GLR) of application data. For example recovering Microsoft Exchange data using Kroll Ontrack® PowerControls™.  NOTE: Volumes are mounted \"instantly\" if the Snapshot is stored locally on the Cohesity Cluster. If the Snapshot is archival target, it will take longer because it must be retrieved.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.RestoreTasksApi()
body = cohesity.RecoverTaskRequest() # RecoverTaskRequest | Request to create a Restore Task for recovering VMs or mounting volumes to mount points.

try: 
    # Create a Restore Task for recovering VMs or instantly mounting volumes.
    api_response = api_instance.create_recover_task(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RestoreTasksApi->create_recover_task: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecoverTaskRequest**](RecoverTaskRequest.md)| Request to create a Restore Task for recovering VMs or mounting volumes to mount points. | 

### Return type

[**RestoreTask**](RestoreTask.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_restore_files_task**
> RestoreTask create_restore_files_task(body)

Create a Restore Task for recovering files and folders.

Returns the created Restore Task that recovers files and folders.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.RestoreTasksApi()
body = cohesity.RestoreFilesTaskRequest() # RestoreFilesTaskRequest | Request to create a Restore Task for recovering files or folders.

try: 
    # Create a Restore Task for recovering files and folders.
    api_response = api_instance.create_restore_files_task(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RestoreTasksApi->create_restore_files_task: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RestoreFilesTaskRequest**](RestoreFilesTaskRequest.md)| Request to create a Restore Task for recovering files or folders. | 

### Return type

[**RestoreTask**](RestoreTask.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_snapshots_information**
> list[FileSnapshotInformation] get_file_snapshots_information(cluster_incarnation_id, source_id, filename, job_id, cluster_id)

Get the information about snapshots that contain the specified file or folder. In addition, information about the file or folder is provided.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.RestoreTasksApi()
cluster_incarnation_id = 789 # int | Specifies the incarnation id of the Cohesity Cluster where the Job was created. An incarnation id is generated when a Cohesity Cluster is initially created. This field is required.
source_id = 789 # int | Specifies the id of the Protection Source object (such as a VM) to search. When a Job Run executes, snapshots of the specified Protection Source object are captured. This operation searches the snapshots of the object for the file or folder. This field is required.
filename = 'filename_example' # str | Specifies the name of the file or folder to find in the snapshots. This field is required.
job_id = 789 # int | Specifies the id of the Job that captured the snapshots. These snapshots are searched for the specified files or folders. This field is required.
cluster_id = 789 # int | Specifies the Cohesity Cluster id where the Job was created. This field is required.

try: 
    # Get the information about snapshots that contain the specified file or folder. In addition, information about the file or folder is provided.
    api_response = api_instance.get_file_snapshots_information(cluster_incarnation_id, source_id, filename, job_id, cluster_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RestoreTasksApi->get_file_snapshots_information: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_incarnation_id** | **int**| Specifies the incarnation id of the Cohesity Cluster where the Job was created. An incarnation id is generated when a Cohesity Cluster is initially created. This field is required. | 
 **source_id** | **int**| Specifies the id of the Protection Source object (such as a VM) to search. When a Job Run executes, snapshots of the specified Protection Source object are captured. This operation searches the snapshots of the object for the file or folder. This field is required. | 
 **filename** | **str**| Specifies the name of the file or folder to find in the snapshots. This field is required. | 
 **job_id** | **int**| Specifies the id of the Job that captured the snapshots. These snapshots are searched for the specified files or folders. This field is required. | 
 **cluster_id** | **int**| Specifies the Cohesity Cluster id where the Job was created. This field is required. | 

### Return type

[**list[FileSnapshotInformation]**](FileSnapshotInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_restore_task_by_id**
> RestoreTask get_restore_task_by_id(id)

List details about a single Restore Task.

Returns the Restore Task corresponding to the specified Restore Task id.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.RestoreTasksApi()
id = 789 # int | Specifies a unique id for the Restore Task.

try: 
    # List details about a single Restore Task.
    api_response = api_instance.get_restore_task_by_id(id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RestoreTasksApi->get_restore_task_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Specifies a unique id for the Restore Task. | 

### Return type

[**RestoreTask**](RestoreTask.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_restore_tasks**
> list[RestoreTask] get_restore_tasks(end_time_usecs=end_time_usecs, page_count=page_count, task_types=task_types, task_ids=task_ids, start_time_usecs=start_time_usecs)

List the Restore Tasks filtered by the specified parameters.

If no parameters are specified, all Restore Tasks found on the Cohesity Cluster are returned. Both running and completed Restore Tasks are reported. Specifying parameters filters the results that are returned.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.RestoreTasksApi()
end_time_usecs = 789 # int | Filter by an end time specified as a Unix epoch Timestamp (in microseconds). All Restore Tasks (both completed and running) on the Cohesity Cluster that started after the specified start time but before the specified end time are returned. If not set, the end time is the current time. (optional)
page_count = 789 # int | Specifies the number of completed Restore Tasks to return in the response for pagination purposes. Running Restore Tasks are always returned. The newest completed Restore Tasks are returned. (optional)
task_types = ['task_types_example'] # list[str] | Filter by the types of Restore Tasks such as 'kRecoverVMs', 'kCloneVMs', 'kCloneView' or 'kMountVolumes'. (optional)
task_ids = [56] # list[int] | Filter by a list of Restore Task ids. (optional)
start_time_usecs = 789 # int | Filter by a start time specified as a Unix epoch Timestamp (in microseconds). All Restore Tasks (both completed and running) on the Cohesity Cluster that started after the specified start time but before the specified end time are returned. If not set, the start time is creation time of the Cohesity Cluster. (optional)

try: 
    # List the Restore Tasks filtered by the specified parameters.
    api_response = api_instance.get_restore_tasks(end_time_usecs=end_time_usecs, page_count=page_count, task_types=task_types, task_ids=task_ids, start_time_usecs=start_time_usecs)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RestoreTasksApi->get_restore_tasks: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_time_usecs** | **int**| Filter by an end time specified as a Unix epoch Timestamp (in microseconds). All Restore Tasks (both completed and running) on the Cohesity Cluster that started after the specified start time but before the specified end time are returned. If not set, the end time is the current time. | [optional] 
 **page_count** | **int**| Specifies the number of completed Restore Tasks to return in the response for pagination purposes. Running Restore Tasks are always returned. The newest completed Restore Tasks are returned. | [optional] 
 **task_types** | [**list[str]**](str.md)| Filter by the types of Restore Tasks such as &#39;kRecoverVMs&#39;, &#39;kCloneVMs&#39;, &#39;kCloneView&#39; or &#39;kMountVolumes&#39;. | [optional] 
 **task_ids** | [**list[int]**](int.md)| Filter by a list of Restore Task ids. | [optional] 
 **start_time_usecs** | **int**| Filter by a start time specified as a Unix epoch Timestamp (in microseconds). All Restore Tasks (both completed and running) on the Cohesity Cluster that started after the specified start time but before the specified end time are returned. If not set, the start time is creation time of the Cohesity Cluster. | [optional] 

### Return type

[**list[RestoreTask]**](RestoreTask.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vm_volumes_information**
> list[VmVolumesInformation] get_vm_volumes_information(original_job_id=original_job_id, supported_volumes_only=supported_volumes_only, job_id=job_id, cluster_id=cluster_id, cluster_incarnation_id=cluster_incarnation_id, job_run_id=job_run_id, started_time_usecs=started_time_usecs, attempt_number=attempt_number, source_id=source_id)

Get information about the logical volumes found in a VM.

All fields must be specified for this operation. To get values for these fields, invoke the GET /public/restore/objects operation. A specific Job Run is defined by the jobRunId, startedTimeUsecs, and attemptNumber fields.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.RestoreTasksApi()
original_job_id = 789 # int | Specifies the id for the Protection Job that originally captured the snapshots of the original object. If the object was backed up on a Primary Cluster replicated to this Cohesity Cluster, and a new Inactive Job is created, this field still contains the id of the original Job and NOT the id of the new Inactive Job. This field is used in combination with the clusterId and clusterIncarnationId to uniquely identify a Job. (optional)
supported_volumes_only = true # bool | Specifies to return only supported volumes information. Unsupported volumes are not returned if this flag is set to true. Default is false. (optional)
job_id = 789 # int | Specifies the Job id for the Protection Job that is currently associated with the object. If the object was backed up on current Cohesity Cluster, this field contains the id for the Job that captured this backup object. If the object was backed up on a Primary Cluster and replicated to this Cohesity Cluster, a new Inactive Job is created, the object is now associated with new Inactive Job, and this field contains the id of the new Inactive Job. (optional)
cluster_id = 789 # int | Specifies the Cohesity Cluster id where the Job was created. (optional)
cluster_incarnation_id = 789 # int | Specifies the incarnation id of the Cohesity Cluster where the Job was created. An incarnation id is generated when a Cohesity Cluster is initially created. (optional)
job_run_id = 789 # int | Specifies the id of the Job Run that captured the snapshot. (optional)
started_time_usecs = 789 # int | Specifies the time when the Job Run starts capturing a snapshot. Specified as a Unix epoch Timestamp (in microseconds). (optional)
attempt_number = 789 # int | Specifies the number of the attempts made by the Job Run to capture a snapshot of the object. For example, if an snapshot is successfully captured after three attempts, this field equals 3. (optional)
source_id = 789 # int | Specifies the id of the VM object to search for volumes. (optional)

try: 
    # Get information about the logical volumes found in a VM.
    api_response = api_instance.get_vm_volumes_information(original_job_id=original_job_id, supported_volumes_only=supported_volumes_only, job_id=job_id, cluster_id=cluster_id, cluster_incarnation_id=cluster_incarnation_id, job_run_id=job_run_id, started_time_usecs=started_time_usecs, attempt_number=attempt_number, source_id=source_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RestoreTasksApi->get_vm_volumes_information: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **original_job_id** | **int**| Specifies the id for the Protection Job that originally captured the snapshots of the original object. If the object was backed up on a Primary Cluster replicated to this Cohesity Cluster, and a new Inactive Job is created, this field still contains the id of the original Job and NOT the id of the new Inactive Job. This field is used in combination with the clusterId and clusterIncarnationId to uniquely identify a Job. | [optional] 
 **supported_volumes_only** | **bool**| Specifies to return only supported volumes information. Unsupported volumes are not returned if this flag is set to true. Default is false. | [optional] 
 **job_id** | **int**| Specifies the Job id for the Protection Job that is currently associated with the object. If the object was backed up on current Cohesity Cluster, this field contains the id for the Job that captured this backup object. If the object was backed up on a Primary Cluster and replicated to this Cohesity Cluster, a new Inactive Job is created, the object is now associated with new Inactive Job, and this field contains the id of the new Inactive Job. | [optional] 
 **cluster_id** | **int**| Specifies the Cohesity Cluster id where the Job was created. | [optional] 
 **cluster_incarnation_id** | **int**| Specifies the incarnation id of the Cohesity Cluster where the Job was created. An incarnation id is generated when a Cohesity Cluster is initially created. | [optional] 
 **job_run_id** | **int**| Specifies the id of the Job Run that captured the snapshot. | [optional] 
 **started_time_usecs** | **int**| Specifies the time when the Job Run starts capturing a snapshot. Specified as a Unix epoch Timestamp (in microseconds). | [optional] 
 **attempt_number** | **int**| Specifies the number of the attempts made by the Job Run to capture a snapshot of the object. For example, if an snapshot is successfully captured after three attempts, this field equals 3. | [optional] 
 **source_id** | **int**| Specifies the id of the VM object to search for volumes. | [optional] 

### Return type

[**list[VmVolumesInformation]**](VmVolumesInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_objects**
> ObjectSearchResults search_objects(operating_systems=operating_systems, owner_entity_id=owner_entity_id, job_ids=job_ids, environments=environments, end_time_usecs=end_time_usecs, page_count=page_count, start_index=start_index, application=application, search=search, registered_source_ids=registered_source_ids, view_box_ids=view_box_ids, start_time_usecs=start_time_usecs)

Find backup objects that match the specified search and filter criteria on the Cohesity Cluster.

If no search pattern or filter parameters are specified, all backup objects currently found on the Cohesity Cluster are returned. Only leaf objects that have been protected by a Job are returned such as VMs, Views and databases. Specify a search pattern or parameters to filter the results that are returned.  The term \"items\" below refers to leaf backup objects such as VMs, Views and databases.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.RestoreTasksApi()
operating_systems = ['operating_systems_example'] # list[str] | Filter by the Operating Systems running on VMs and Physical Servers. This filter is applicable only to VMs and physical servers. (optional)
owner_entity_id = 789 # int | Filter objects by the Entity id of the owner VM. For example, if a ownerEntityId is provided while searching for SQL databases, only SQL databases belonging to the VM with the specified id are returned. ownerEntityId is only significant if application is set to SQL. (optional)
job_ids = [56] # list[int] | Filter by a list of Protection Job ids. Only items backed up by the specified Jobs are listed. (optional)
environments = ['environments_example'] # list[str] | Filter by environment types such as 'kVMware', 'kView', 'kSQL', 'kPuppeteer', 'kPhysical', 'kPure' 'kNetapp' 'kGenericNas', 'kHyperV', 'kAcropolis', or 'kAzure'. Only items from the specified environment types are returned. NOTE: 'kPuppeteer' refers to Cohesity's Remote Adapter. (optional)
end_time_usecs = 789 # int | Filter by backup completion time by specify a backup completion start and end times. Specified as a Unix epoch Timestamp (in microseconds). Only items created by backups that completed between the specified start and end times are returned. (optional)
page_count = 789 # int | Limit the number of items to return in the response for pagination purposes. (optional)
start_index = 789 # int | Specifies an index number that can be used to return subsets of items in multiple requests. Break up the items to return into multiple requests by setting pageCount and using startIndex to return a subsets of items. For example, set startIndex to 0 to get the first set of items for the first request. Increment startIndex by pageCount to get the next set of items for a next request. Continue until all items are returned and therefore the total number of returned items is equal to totalCount. (optional)
application = 'application_example' # str | Filter by application when the environment type is kSQL. For example, if SQL is specified the SQL databases are returned. (optional)
search = 'search_example' # str | Filter by searching for sub-strings in the item name. The specified string can match any part of the item name. For example: \"vm\" or \"123\" both match the item name of \"vm-123\". (optional)
registered_source_ids = [56] # list[int] | Filter by a list of Registered Sources ids. Only items from the listed Registered Sources are returned. (optional)
view_box_ids = [56] # list[int] | Filter by a list of Domains (View Boxes) ids. Only items stored in the listed Domains (View Boxes) are returned. (optional)
start_time_usecs = 789 # int | Filter by backup completion time by specifying a backup completion start and end times. Specified as a Unix epoch Timestamp (in microseconds). Only items created by backups that completed between the specified start and end times are returned. (optional)

try: 
    # Find backup objects that match the specified search and filter criteria on the Cohesity Cluster.
    api_response = api_instance.search_objects(operating_systems=operating_systems, owner_entity_id=owner_entity_id, job_ids=job_ids, environments=environments, end_time_usecs=end_time_usecs, page_count=page_count, start_index=start_index, application=application, search=search, registered_source_ids=registered_source_ids, view_box_ids=view_box_ids, start_time_usecs=start_time_usecs)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RestoreTasksApi->search_objects: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operating_systems** | [**list[str]**](str.md)| Filter by the Operating Systems running on VMs and Physical Servers. This filter is applicable only to VMs and physical servers. | [optional] 
 **owner_entity_id** | **int**| Filter objects by the Entity id of the owner VM. For example, if a ownerEntityId is provided while searching for SQL databases, only SQL databases belonging to the VM with the specified id are returned. ownerEntityId is only significant if application is set to SQL. | [optional] 
 **job_ids** | [**list[int]**](int.md)| Filter by a list of Protection Job ids. Only items backed up by the specified Jobs are listed. | [optional] 
 **environments** | [**list[str]**](str.md)| Filter by environment types such as &#39;kVMware&#39;, &#39;kView&#39;, &#39;kSQL&#39;, &#39;kPuppeteer&#39;, &#39;kPhysical&#39;, &#39;kPure&#39; &#39;kNetapp&#39; &#39;kGenericNas&#39;, &#39;kHyperV&#39;, &#39;kAcropolis&#39;, or &#39;kAzure&#39;. Only items from the specified environment types are returned. NOTE: &#39;kPuppeteer&#39; refers to Cohesity&#39;s Remote Adapter. | [optional] 
 **end_time_usecs** | **int**| Filter by backup completion time by specify a backup completion start and end times. Specified as a Unix epoch Timestamp (in microseconds). Only items created by backups that completed between the specified start and end times are returned. | [optional] 
 **page_count** | **int**| Limit the number of items to return in the response for pagination purposes. | [optional] 
 **start_index** | **int**| Specifies an index number that can be used to return subsets of items in multiple requests. Break up the items to return into multiple requests by setting pageCount and using startIndex to return a subsets of items. For example, set startIndex to 0 to get the first set of items for the first request. Increment startIndex by pageCount to get the next set of items for a next request. Continue until all items are returned and therefore the total number of returned items is equal to totalCount. | [optional] 
 **application** | **str**| Filter by application when the environment type is kSQL. For example, if SQL is specified the SQL databases are returned. | [optional] 
 **search** | **str**| Filter by searching for sub-strings in the item name. The specified string can match any part of the item name. For example: \&quot;vm\&quot; or \&quot;123\&quot; both match the item name of \&quot;vm-123\&quot;. | [optional] 
 **registered_source_ids** | [**list[int]**](int.md)| Filter by a list of Registered Sources ids. Only items from the listed Registered Sources are returned. | [optional] 
 **view_box_ids** | [**list[int]**](int.md)| Filter by a list of Domains (View Boxes) ids. Only items stored in the listed Domains (View Boxes) are returned. | [optional] 
 **start_time_usecs** | **int**| Filter by backup completion time by specifying a backup completion start and end times. Specified as a Unix epoch Timestamp (in microseconds). Only items created by backups that completed between the specified start and end times are returned. | [optional] 

### Return type

[**ObjectSearchResults**](ObjectSearchResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_restored_files**
> FileSearchResults search_restored_files(environments=environments, start_index=start_index, page_count=page_count, job_ids=job_ids, registered_source_ids=registered_source_ids, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, source_ids=source_ids, folder_only=folder_only, search=search, view_box_ids=view_box_ids)

Search for files and folders to recover that match the specified search and filter criteria on the Cohesity Cluster.

Use the files and folders returned by this operation to populate the list of files and folders to recover in the POST /public/restore/files operation. If no search pattern or filter parameters are specified, all files and folders currently found on the Cohesity Cluster are returned. Specify a search pattern or parameters to filter the results that are returned.  The term \"items\" below refers to files and folders that are found in the source objects (such as VMs).

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.RestoreTasksApi()
environments = ['environments_example'] # list[str] | Filter by environment types such as 'kVMware', 'kView', 'kSQL', 'kPuppeteer', 'kPhysical', 'kPure' 'kNetapp' or 'kGenericNas'. Only items from the specified environment types are returned. NOTE: 'kPuppeteer' refers to Cohesity's Remote Adapter. (optional)
start_index = 789 # int | Specifies an index number that can be used to return subsets of items in multiple requests. Break up the items to return into multiple requests by setting pageCount and using startIndex to return a subsets of items. For example, set startIndex to 0 to get the first set of items for the first request. Increment startIndex by pageCount to get the next set of items for a next request. Continue until all items are returned and therefore the total number of returned items is equal to totalCount. (optional)
page_count = 789 # int | Limit the number of items to return in the response for pagination purposes. (optional)
job_ids = [56] # list[int] | Filter by a list of Protection Job ids. Only items backed up by the specified Jobs are listed. (optional)
registered_source_ids = [56] # list[int] | Filter by a list of Registered Sources ids. Only items from the listed Registered Sources are returned. (optional)
start_time_usecs = 789 # int | Filter by backup completion time by specifying a backup completion start and end times. Specified as a Unix epoch Timestamp (in microseconds). Only items created by backups that completed between the specified start and end times are returned. (optional)
end_time_usecs = 789 # int | Filter by backup completion time by specify a backup completion start and end times. Specified as a Unix epoch Timestamp (in microseconds). Only items created by backups that completed between the specified start and end times are returned. (optional)
source_ids = [56] # list[int] | Filter by source ids. Only files and folders found in the listed sources (such as VMs) are returned. (optional)
folder_only = true # bool | Filter by folders or files. If true, only folders are returned. If false, only files are returned. If not specified, both files and folders are returned. (optional)
search = 'search_example' # str | Filter by searching for sub-strings in the item name. The specified string can match any part of the item name. For example: \"vm\" or \"123\" both match the item name of \"vm-123\". (optional)
view_box_ids = [56] # list[int] | Filter by a list of Domains (View Boxes) ids. Only items stored in the listed Domains (View Boxes) are returned. (optional)

try: 
    # Search for files and folders to recover that match the specified search and filter criteria on the Cohesity Cluster.
    api_response = api_instance.search_restored_files(environments=environments, start_index=start_index, page_count=page_count, job_ids=job_ids, registered_source_ids=registered_source_ids, start_time_usecs=start_time_usecs, end_time_usecs=end_time_usecs, source_ids=source_ids, folder_only=folder_only, search=search, view_box_ids=view_box_ids)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RestoreTasksApi->search_restored_files: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environments** | [**list[str]**](str.md)| Filter by environment types such as &#39;kVMware&#39;, &#39;kView&#39;, &#39;kSQL&#39;, &#39;kPuppeteer&#39;, &#39;kPhysical&#39;, &#39;kPure&#39; &#39;kNetapp&#39; or &#39;kGenericNas&#39;. Only items from the specified environment types are returned. NOTE: &#39;kPuppeteer&#39; refers to Cohesity&#39;s Remote Adapter. | [optional] 
 **start_index** | **int**| Specifies an index number that can be used to return subsets of items in multiple requests. Break up the items to return into multiple requests by setting pageCount and using startIndex to return a subsets of items. For example, set startIndex to 0 to get the first set of items for the first request. Increment startIndex by pageCount to get the next set of items for a next request. Continue until all items are returned and therefore the total number of returned items is equal to totalCount. | [optional] 
 **page_count** | **int**| Limit the number of items to return in the response for pagination purposes. | [optional] 
 **job_ids** | [**list[int]**](int.md)| Filter by a list of Protection Job ids. Only items backed up by the specified Jobs are listed. | [optional] 
 **registered_source_ids** | [**list[int]**](int.md)| Filter by a list of Registered Sources ids. Only items from the listed Registered Sources are returned. | [optional] 
 **start_time_usecs** | **int**| Filter by backup completion time by specifying a backup completion start and end times. Specified as a Unix epoch Timestamp (in microseconds). Only items created by backups that completed between the specified start and end times are returned. | [optional] 
 **end_time_usecs** | **int**| Filter by backup completion time by specify a backup completion start and end times. Specified as a Unix epoch Timestamp (in microseconds). Only items created by backups that completed between the specified start and end times are returned. | [optional] 
 **source_ids** | [**list[int]**](int.md)| Filter by source ids. Only files and folders found in the listed sources (such as VMs) are returned. | [optional] 
 **folder_only** | **bool**| Filter by folders or files. If true, only folders are returned. If false, only files are returned. If not specified, both files and folders are returned. | [optional] 
 **search** | **str**| Filter by searching for sub-strings in the item name. The specified string can match any part of the item name. For example: \&quot;vm\&quot; or \&quot;123\&quot; both match the item name of \&quot;vm-123\&quot;. | [optional] 
 **view_box_ids** | [**list[int]**](int.md)| Filter by a list of Domains (View Boxes) ids. Only items stored in the listed Domains (View Boxes) are returned. | [optional] 

### Return type

[**FileSearchResults**](FileSearchResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

