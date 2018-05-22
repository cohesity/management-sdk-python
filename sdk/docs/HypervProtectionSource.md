# HypervProtectionSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_info** | [**AgentInformation**](AgentInformation.md) | Specifies information about the agent running on the HyperV objects. | [optional] 
**backup_type** | **str** | Specifies the type of backup supported by the VM. &#39;kRctBackup&#39;, &#39;kVssBackup&#39; Specifies the type of an HyperV datastore object. &#39;kRctBackup&#39; indicates backup is done using RCT/checkpoints. &#39;kVssBackup&#39; indicates backup is done using VSS. | [optional] 
**cluster_name** | **str** | Specifies the cluster name for &#39;kHostCluster&#39; objects. | [optional] 
**datastore_info** | [**HypervDatastore**](HypervDatastore.md) | Specifies additional information for &#39;kDatastore&#39; objects. | [optional] 
**description** | **str** | Specifies a description about the Protection Source. | [optional] 
**host_type** | **str** | Specifies host OS type for &#39;kVirtualMachine&#39; objects. &#39;kLinux&#39; indicates the Linux operating system. &#39;kWindows&#39; indicates the Microsoft Windows operating system. | [optional] 
**hyperv_uuid** | **str** | Specifies the UUID for &#39;kVirtualMachine&#39; HyperV objects. | [optional] 
**name** | **str** | Specifies the name of the HyperV Object. | [optional] 
**type** | **str** | Specifies the type of an HyperV Protection Source Object such as &#39;kSCVMMServer&#39;, &#39;kStandaloneHost&#39;, &#39;kNetwork&#39;, etc. overrideDescription: true Specifies the type of an HyperV Protection Source. &#39;kSCVMMServer&#39; indicates a collection of root folders clusters. &#39;kStandaloneHost&#39; indicates a single Nutanix cluster. &#39;kStandaloneCluster&#39; indicates a single Nutanix cluster. &#39;kHostGroup&#39; indicates a Nutanix cluster manageed by a Prism Central. &#39;kHost&#39; indicates an HyperV host. &#39;kHostCluster&#39; indicates a Nutanix cluster manageed by a Prism Central. &#39;kVirtualMachine&#39; indicates a Virtual Machine. &#39;kNetwork&#39; indicates a Virtual Machine network object. &#39;kDatastore&#39; represents a storage container object. | [optional] 
**uuid** | **str** | Specifies the UUID of the Object. This is unique within the HyperV environment. | [optional] 
**vm_info** | [**HypervVirtualMachine**](HypervVirtualMachine.md) | Specifies additional information for &#39;kVirtualMachine&#39; objects. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


