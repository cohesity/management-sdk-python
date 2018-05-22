# FilesystemVolume

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disks** | [**list[Disk]**](Disk.md) | Specifies information about all the disks and partitions needed to mount this logical volume. | [optional] 
**display_name** | **str** | Specifies a description about the filesystem. | [optional] 
**filesystem_type** | **str** | Specifies type of the filesystem on this volume. | [optional] 
**filesystem_uuid** | **str** | Specifies the uuid of the filesystem. | [optional] 
**is_supported** | **bool** | If true, this is a supported filesystem volume type. | [optional] 
**logical_volume** | [**FilesystemVolumeLogicalVolume**](FilesystemVolumeLogicalVolume.md) |  | [optional] 
**logical_volume_type** | **str** | Specifies the type of logical volume such as kSimpleVolume, kLVM or kLDM. &#39;kSimpleVolume&#39; indicates a simple volume. Data can be used by just mounting the only one partition present on the disk. &#39;kLVM&#39; indicates a logical volume on Linux managed by a Logical Volume Manager. In order to access the data, deviceTree must be created based on the specification in logicalVolume.deviceTree. &#39;kLDM&#39; indicates a logical volume on Windows managed by Logical Disk Manager. | [optional] 
**name** | **str** | Specifies the name of the volume such as /C. | [optional] 
**volume_guid** | **str** | VolumeGuid is the Volume guid. This is populated for kPhysical environments. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


