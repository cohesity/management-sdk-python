# Node

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity_by_tier** | [**list[CapacityByTier]**](CapacityByTier.md) |  | [optional] 
**chassis_info** | [**ChassisInfo**](ChassisInfo.md) | ChassisInfo describes the information for the chassis of the node. | [optional] 
**cluster_partition_id** | **int** | ClusterPartitionId is the Id of the cluster partition to which the Node belongs. | [optional] 
**cluster_partition_name** | **str** | ClusterPartitionName is the name of the cluster to which the Node belongs. | [optional] 
**disk_count** | **int** | DiskCount is the number of disks in a node. | [optional] 
**id** | **int** | Id is the Id of the Node. | [optional] 
**ip** | **str** | Ip is the IP address of the Node. | [optional] 
**is_marked_for_removal** | **bool** | IsMarkedForRemoval specifies whether the node has been marked for removal. | [optional] 
**max_physical_capacity_bytes** | **int** | MaxPhysicalCapacityBytes specifies the maximum physical capacity of the node in bytes. | [optional] 
**node_hardware_info** | [**NodeHardwareInfo**](NodeHardwareInfo.md) | HardwareInfo describes the hardware of the node. | [optional] 
**node_incarnation_id** | **int** | NodeIncarnationId is the incarnation id  of this node. The incarnation id is changed every time the data is wiped from the node. Various services on a node is only run if incarnation id of the node matches the incarnation id of the cluster. Whenever a mismatch is detected, Nexus will stop all services and clean the data from the node. After clean operation is completed, Nexus will set the node incarnation id to cluster incarnation id and start the services. | [optional] 
**node_software_version** | **str** | NodeSoftwareVersion is the current version of Cohesity software installed on a node. | [optional] 
**offline_mount_paths_of_disks** | **list[str]** | OfflineMountPathsOfDisks provides the corresponding mount paths for direct attached disks that are currently offline - access to these were detected to hang sometime in the past. After these disks have been fixed, their mount paths needs to be removed from the following list before these will be accessed again. | [optional] 
**removal_state** | **str** | RemovalState specifies the removal state of the node. &#39;kDontRemove&#39; means the state of object is functional and it is not being removed. &#39;kMarkedForRemoval&#39; means the object is being removed. &#39;kOkToRemove&#39; means the object has been removed on the Cohesity Cluster and if the object is physical, it can be removed from the Cohesity Cluster. | [optional] 
**stats** | [**NodeStats**](NodeStats.md) | Stats describes the node stats. | [optional] 
**system_disks** | [**list[NodeSystemDiskInfo]**](NodeSystemDiskInfo.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


