# StaticRoute

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Specifies a description of the Static Route. | [optional] 
**is_update** | **bool** | Specifies if the route is currently being updated on the Cohesity Cluster. | [optional] 
**network_interface_group** | **str** | Specifies the group name of the network interfaces to use for communicating with the destination subnet. | [optional] 
**network_interface_ids** | **list[int]** | Specifies the ids of the network interfaces to use for communicating with the destination subnet. | [optional] 
**subnet** | [**StaticRouteSubnet**](StaticRouteSubnet.md) |  | [optional] 
**vlan_id** | **int** | Specifies the ID of the VLAN to use for communication with the destination subnet. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


