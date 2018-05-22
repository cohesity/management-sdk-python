# VmwareCloneParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore_folder_id** | **int** | Specifies the folder where the restore datastore should be created. This is applicable only when the VMs are being cloned. | [optional] 
**disable_network** | **bool** | Specifies whether the network should be left in disabled state. Attached network is enabled by default. Set this flag to true to disable it. | [optional] 
**network_id** | **int** | Specifies a network configuration to be attached to the cloned or recovered object. For kCloneVMs and kRecoverVMs tasks, original network configuration is detached if the cloned or recovered object is kept under a different parent Protection Source or a different Resource Pool. By default, for kRecoverVMs task, original network configuration is preserved if the recovered object is kept under the same parent Protection Source and the same Resource Pool. Specify this field to override the preserved network configuration or to attach a new network configuration to the cloned or recovered objects. You can get the networkId of the kNetwork object by setting includeNetworks to &#39;true&#39; in the GET /public/protectionSources operation. In the response, get the id of the desired kNetwork object, the resource pool, and the registered parent Protection Source. | [optional] 
**powered_on** | **bool** | Specifies the power state of the cloned or recovered objects. By default, the cloned or recovered objects are powered off. | [optional] 
**prefix** | **str** | Specifies a prefix to prepended to the source object name to derive a new name for the recovered or cloned object. By default, cloned or recovered objects retain their original name. Length of this field is limited to 8 characters. | [optional] 
**resource_pool_id** | **int** | Specifies the resource pool where the cloned or recovered objects are attached. This field is mandatory for kCloneVMs Restore Tasks always. For kRecoverVMs Restore Tasks, this field is mandatory only if newParentId field is specified. If this field is not specified, recovered objects are attached to the original resource pool under the original parent. | [optional] 
**suffix** | **str** | Specifies a suffix to appended to the original source object name to derive a new name for the recovered or cloned object. By default, cloned or recovered objects retain their original name. Length of this field is limited to 8 characters. | [optional] 
**vm_folder_id** | **int** | Specifies a folder where the VMs should be restored. This is applicable only when the VMs are being restored to an alternate location or if clone is being performed. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


