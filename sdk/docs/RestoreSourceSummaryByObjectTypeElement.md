# RestoreSourceSummaryByObjectTypeElement

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore_id** | **int** | Specifies the datastore where the object&#39;s files are recovered to. This field is populated when objects are recovered to a different resource pool or to a different parent source. This field is not populated when objects are recovered to their original datastore locations in the original parent source. | [optional] 
**file_restore_info** | [**list[FileRestoreInfo]**](FileRestoreInfo.md) |  | [optional] 
**name** | **str** | Specifies the name of the Restore Task. This field must be set and must be a unique name. | 
**objects** | [**list[RestoreObject]**](RestoreObject.md) | Specifies a list of Protection Source objects or Protection Job objects (with specified Protection Source objects). | [optional] 
**protection_source_name** | **str** | The protection source name. | [optional] 
**start_time_usecs** | **int** | Specifies the start time of the Restore Task as a Unix epoch Timestamp (in microseconds). | [optional] 
**type** | **str** | Specify the object type to filter with. Specifies the type of Restore Task.  &#39;kRecoverVMs&#39; specifies a Restore Task that recovers VMs. &#39;kCloneVMs&#39; specifies a Restore Task that clones VMs. &#39;kCloneView&#39; specifies a Restore Task that clones a View. &#39;kMountVolumes&#39; specifies a Restore Task that mounts volumes. &#39;kRestoreFiles&#39; specifies a Restore Task that recovers files and folders. | [optional] 
**username** | **str** | Specifies the Cohesity user who requested this Restore Task. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


