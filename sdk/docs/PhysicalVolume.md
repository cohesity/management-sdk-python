# PhysicalVolume

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_path** | **str** | Specifies the path to the device that hosts the volume locally. | [optional] 
**guid** | **str** | Specifies an id for the Physical Volume. | [optional] 
**is_extended_attributes_supported** | **bool** | Specifies whether this volume supports extended attributes (like ACLs) when performing file backups. | [optional] 
**is_protected** | **bool** | Specifies if a volume is protected by a Job. | [optional] 
**label** | **str** | Specifies a volume label that can be used for displaying additional identifying information about a volume. | [optional] 
**logical_size_bytes** | **int** | Specifies the logical size of the volume in bytes that is not reduced by change-block tracking, compression and deduplication. | [optional] 
**mount_points** | **list[str]** | Specifies the mount points where the volume is mounted, for example: &#39;C:\\&#39;, &#39;/mnt/foo&#39; etc. | [optional] 
**network_path** | **str** | Specifies the full path to connect to the network attached volume. For example, (IP or hostname):/path/to/share for NFS volumes). | [optional] 
**used_size_bytes** | **int** | Specifies the size used by the volume in bytes. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


