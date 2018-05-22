# RestoreTask

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acropolis_parameters** | [**AcropolisRestoreParameters**](AcropolisRestoreParameters.md) | Specifies parameters for &#39;kAcropolis&#39; restore task. | [optional] 
**archive_task_uid** | [**RestoreTaskArchiveTaskUid**](RestoreTaskArchiveTaskUid.md) |  | [optional] 
**clone_view_parameters** | [**RestoreTaskCloneViewParameters**](RestoreTaskCloneViewParameters.md) |  | [optional] 
**continue_on_error** | **bool** | Specifies if the Restore Task should continue when some operations on some objects fail. If true, the Cohesity Cluster ignores intermittent errors and restores as many objects as possible. | [optional] 
**datastore_id** | **int** | Specifies the datastore where the object&#39;s files are recovered to. This field is populated when objects are recovered to a different resource pool or to a different parent source. This field is not populated when objects are recovered to their original datastore locations in the original parent source. | [optional] 
**end_time_usecs** | **int** | Specifies the end time of the Restore Task as a Unix epoch Timestamp (in microseconds). This field is only populated if the Restore Task completes. | [optional] 
**error** | [**RestoreTaskError**](RestoreTaskError.md) |  | [optional] 
**full_view_name** | **str** | Specifies the full name of a View. | [optional] 
**hyperv_parameters** | [**HypervRestoreParameters**](HypervRestoreParameters.md) | Specifies additional parameters for &#39;kHyperV&#39; restore objects. | [optional] 
**id** | **int** | Specifies the id of the Restore Task assigned by Cohesity Cluster. | [optional] 
**mount_volumes_state** | [**MountVolumesState**](MountVolumesState.md) | Specifies the states of mounting all the volumes onto a mount target for a &#39;kRecoverVMs&#39; Restore Task. | [optional] 
**name** | **str** | Specifies the name of the Restore Task. This field must be set and must be a unique name. | 
**new_parent_id** | **int** | Specify a new registered parent Protection Source. If specified the selected objects are cloned or recovered to this new Protection Source. If not specified, objects are cloned or recovered to the original Protection Source that was managing them. | [optional] 
**objects** | [**list[RestoreObject]**](RestoreObject.md) | Specifies a list of Protection Source objects or Protection Job objects (with specified Protection Source objects). | [optional] 
**restore_object_state** | [**list[RestoreObjectState]**](RestoreObjectState.md) | Specifies the states of all the objects for the &#39;kRecoverVMs&#39; and &#39;kCloneVMs&#39; Restore Tasks. | [optional] 
**start_time_usecs** | **int** | Specifies the start time for the Restore Task as a Unix epoch Timestamp (in microseconds). | [optional] 
**status** | **str** | Specifies the overall status of the Restore Task. &#39;kReadyToSchedule&#39; indicates the Restore Task is waiting to be scheduled. &#39;kProgressMonitorCreated&#39; indicates the progress monitor for the Restore Task has been created. &#39;kRetrievedFromArchive&#39; indicates that the objects to restore have been retrieved from the specified archive. A Task will only ever transition to this state if a retrieval is necessary. &#39;kAdmitted&#39; indicates the task has been admitted. After a task has been admitted, its status does not move back to &#39;kReadyToSchedule&#39; state even if it is rescheduled. &#39;kInProgress&#39; indicates that the Restore Task is in progress. &#39;kFinishingProgressMonitor&#39; indicates that the Restore Task is finishing its progress monitoring. &#39;kFinished&#39; indicates that the Restore Task has finished. The status indicating success or failure is found in the error code that is stored with the Restore Task. | [optional] 
**target_view_created** | **bool** | Is true if a new View was created by a &#39;kCloneVMs&#39; Restore Task. This field is only set for a &#39;kCloneVMs&#39; Restore Task. | [optional] 
**type** | **str** | Specifies the type of Restore Task.  &#39;kRecoverVMs&#39; specifies a Restore Task that recovers VMs. &#39;kCloneVMs&#39; specifies a Restore Task that clones VMs. &#39;kCloneView&#39; specifies a Restore Task that clones a View. &#39;kMountVolumes&#39; specifies a Restore Task that mounts volumes. &#39;kRestoreFiles&#39; specifies a Restore Task that recovers files and folders. | [optional] 
**username** | **str** | Specifies the Cohesity user who requested this Restore Task. | [optional] 
**view_box_id** | **int** | Specifies the id of the Domain (View Box) where the View is stored. | [optional] 
**vlan_parameters** | [**VlanParameters**](VlanParameters.md) | Specifies VLAN parameters for the restore operation. | [optional] 
**vmware_parameters** | [**VmwareRestoreParameters**](VmwareRestoreParameters.md) | Specifies additional parameters for &#39;kVmware&#39; restore objects. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


