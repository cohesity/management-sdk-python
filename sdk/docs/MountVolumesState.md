# MountVolumesState

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bring_disks_online** | **bool** | Optional setting that determines if the volumes are brought online on the mount target after attaching the disks. This option is only significant for VMs. | [optional] 
**mount_volume_results** | [**list[MountVolumeResult]**](MountVolumeResult.md) | Specifies the results of mounting each specified volume. | [optional] 
**other_error** | [**MountVolumesStateOtherError**](MountVolumesStateOtherError.md) |  | [optional] 
**target_source_id** | **int** | Specifies the target Protection Source Id where the volumes will be mounted. NOTE: The source that was backed up and the mount target must be the same type, for example if the source is a VMware VM, then the mount target must also be a VMware VM. The mount target must be registered on the Cohesity Cluster. | [optional] 
**username** | **str** | Specifies the username to access the mount target. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


