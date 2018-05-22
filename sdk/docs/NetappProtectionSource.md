# NetappProtectionSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_info** | [**NetappClusterInfo**](NetappClusterInfo.md) | Specifies information about a NetApp cluster and is only valid for a NetApp Object of type kCluster. | [optional] 
**is_top_level** | **bool** | Specifies if this Object is a top level Object. Because a top level Object can either be a NetApp cluster or a Vserver, this cannot be determined only by type. | [optional] 
**name** | **str** | Specifies the name of the NetApp Object. | [optional] 
**type** | **str** | Specifies the type of managed NetApp Object in a NetApp Protection Source such as &#39;kCluster&#39;, &#39;kVserver&#39; or &#39;kVolume&#39;. | [optional] 
**uuid** | **str** | Specifies the globally unique ID of this Object assigned by the NetApp server. | [optional] 
**volume_info** | [**NetappVolumeInfo**](NetappVolumeInfo.md) | Specifies information about a NetApp volume and is only valid for a NetApp Object of type kVolume. | [optional] 
**vserver_info** | [**NetappVserverInfo**](NetappVserverInfo.md) | Specifies information about a NetApp Vserver and is only valid for a NetApp Object of type kVserver. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


