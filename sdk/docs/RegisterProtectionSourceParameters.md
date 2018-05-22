# RegisterProtectionSourceParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **str** | Specifies the network endpoint of the Protection Source where it is reachable. It could be an URL or hostname or an IP address of the Protection Source. | [optional] 
**environment** | **str** | Specifies the environment such as &#39;kPhysical&#39; or &#39;kVMware&#39; of the Protection Source. overrideDescription: true Supported environment types include &#39;kView&#39;, &#39;kSQL&#39;, &#39;kVMware&#39;, &#39;kPuppeteer&#39;, &#39;kPhysical&#39;, &#39;kPure&#39;, &#39;kNetapp, &#39;kGenericNas, &#39;kHyperV&#39;, &#39;kAcropolis&#39;, &#39;kAzure&#39;. NOTE: &#39;kPuppeteer&#39; refers to Cohesity&#39;s Remote Adapter. | [optional] 
**force_register** | **bool** |  | [optional] 
**host_type** | **str** | Specifies the optional OS type of the Protection Source (such as kWindows or kLinux). overrideDescription: true &#39;kLinux&#39; indicates the Linux operating system. &#39;kWindows&#39; indicates the Microsoft Windows operating system. | [optional] 
**nas_mount_credentials** | [**RegisterProtectionSourceParametersNasMountCredentials**](RegisterProtectionSourceParametersNasMountCredentials.md) |  | [optional] 
**netapp_type** | **str** | Specifies the entity type such as &#39;kCluster,&#39; if the environment is kNetapp. | [optional] 
**password** | **str** | Specifies password of the username to access the target source. | [optional] 
**physical_type** | **str** | Specifies the entity type such as &#39;kPhysicalHost&#39; if the environment is kPhysical. overrideDescription: true &#39;kHost&#39; indicates a single physical server. &#39;kWindowsCluster&#39; indicates a Microsoft Windows cluster. | [optional] 
**pure_type** | **str** | Specifies the entity type such as &#39;kStorageArray&#39; if the environment is kPure. overrideDescription: true Examples of Pure Objects include &#39;kStorageArray&#39; and &#39;kVolume&#39;. | [optional] 
**source_side_dedup_enabled** | **bool** | This controls whether to use source side dedup on the source or not. This is only applicable to Protection Sources which support source side dedup (e.g., Linux physical servers). | [optional] 
**throttling_policy** | [**RegisterProtectionSourceParametersThrottlingPolicy**](RegisterProtectionSourceParametersThrottlingPolicy.md) |  | [optional] 
**throttling_policy_overrides** | [**list[ThrottlingPolicyOverride]**](ThrottlingPolicyOverride.md) | Specifies a list of Throttling Policy for datastores that override the common throttling policy specified for the registered Protection Source. For datastores not in this list, common policy will still apply. | [optional] 
**username** | **str** | Specifies username to access the target source. | [optional] 
**vmware_type** | **str** | Specifies the entity type such as &#39;kVCenter&#39; if the environment is kKMware. overrideDescription: true Examples of VMware Objects include &#39;kVCenter&#39;, &#39;kFolder&#39;, &#39;kDatacenter&#39;, &#39;kResourcePool&#39;, &#39;kDatastore&#39;, &#39;kVirtualMachine&#39;, etc. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


