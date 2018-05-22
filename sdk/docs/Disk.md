# Disk

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_blocks** | [**list[DiskBlock]**](DiskBlock.md) | Specifies a set of disk blocks by defining the location and offset of disk blocks in a disk. | [optional] 
**disk_format** | **str** | Specifies the format of the virtual disk. &#39;kVMDK&#39; indicates VMware&#39;s Virtual Disk format. &#39;kVHD&#39; indicates Microsoft&#39;s Virtual Hard Drive format. &#39;kVHDx&#39; indicates Microsoft&#39;s Hyper-V Virtual Hard Drive format. | [optional] 
**disk_partitions** | [**list[DiskPartition]**](DiskPartition.md) | Specifies information about all the partitions in this disk. | [optional] 
**partition_table_format** | **str** | Specifies partition table format on a disk. &#39;kNoPartition&#39; indicates missing partition table. &#39;kMBRPartition&#39; indicates partition table is in Master Boot Record format. &#39;kGPTPartition&#39; indicates partition table is in Guid Partition Table format. &#39;kSGIPartition&#39; indicates partition table uses SGI scheme. &#39;kSUNPartition&#39; indicates partition table uses SUN scheme. | [optional] 
**sector_size_bytes** | **int** | Specifies the sector size of hard disk. It is used for mapping the disk blocks of the disk file into a linear list of sectors. | [optional] 
**uuid** | **str** | Specifies the disk uuid. | [optional] 
**vmdk_file_name** | **str** | Specifies the disk file name. This is the VMDK name and not the flat file name. | [optional] 
**vmdk_size_bytes** | **int** | Specifies the disk size in bytes. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


