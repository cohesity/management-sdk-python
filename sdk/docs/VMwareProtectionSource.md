# VMwareProtectionSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **int** | Specifies the id of the persistent agent. | [optional] 
**agents** | [**list[AgentInformation]**](AgentInformation.md) | This is set only if the Virtual Machine has persistent agent. | [optional] 
**connection_state** | **str** | Specifies the connection state of the Object and are only valid for ESXi hosts (&#39;kHostSystem&#39;) or Virtual Machines (&#39;kVirtualMachine&#39;). These enums are equivalent to the connection states documented in VMware&#39;s reference documentation. Examples of Cohesity connection states include &#39;kConnected&#39;, &#39;kDisconnected&#39;, &#39;kInacccessible&#39;, etc. | [optional] 
**datastore_info** | [**DatastoreInfo**](DatastoreInfo.md) | Specifies additional information of entities of type &#39;kDatastore&#39;. | [optional] 
**folder_type** | **str** | Specifies the folder type for the &#39;kFolder&#39; Object. &#39;kVMFolder&#39; indicates folder can hold VMs or vApps. &#39;kHostFolder&#39; indicates folder can hold hosts and compute resources. &#39;kDatastoreFolder&#39; indicates folder can hold datastores and storage pods. &#39;kNetworkFolder&#39; indicates folder can hold networks and switches. &#39;kRootFolder&#39; indicates folder can hold datacenters. | [optional] 
**has_persistent_agent** | **bool** | Set to true if a persistent agent is running on the Virtual Machine. This is populated for entities of type &#39;kVirtualMachine&#39;. | [optional] 
**host_type** | **str** | Specifies the host type for the &#39;kVirtualMachine&#39; Object. &#39;kLinux&#39; indicates the Linux operating system. &#39;kWindows&#39; indicates the Microsoft Windows operating system. | [optional] 
**id** | [**VMwareObjectId**](VMwareObjectId.md) | Specifies the UUID of the VMware Protection Source. | [optional] 
**name** | **str** | Specifies a human readable name of the Protection Source. | [optional] 
**tag_attributes** | [**list[TagAttribute]**](TagAttribute.md) | Specifies the optional list of VM Tag attributes associated with this Object. | [optional] 
**tools_running_status** | **str** | Specifies the status of VMware Tools for the guest OS on the VM. This is only valid for the &#39;kVirtualMachine&#39; type. &#39;kGuestToolsRunning&#39; means the VMware tools are running on the guest OS. &#39;kGuestToolsNotRunning&#39; means the VMware tools are not running on the guest OS. &#39;kUnknown&#39; means the state of the VMware tools on the guest OS is not known. &#39;kGuestToolsExecutingScripts&#39; means the guest OS is currently executing scripts using VMware tools. | [optional] 
**type** | **str** | Specifies the type of managed Object in a VMware Protection Source. Examples of VMware Objects include &#39;kVCenter&#39;, &#39;kFolder&#39;, &#39;kDatacenter&#39;, &#39;kResourcePool&#39;, &#39;kDatastore&#39;, &#39;kVirtualMachine&#39;, etc. | [optional] 
**virtual_disks** | [**list[VirtualDiskInfo]**](VirtualDiskInfo.md) | This is populated for entities of type &#39;kVirtualMachine&#39;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


