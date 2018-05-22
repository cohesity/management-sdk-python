# RegisteredApplicationServerRegisteredProtectionSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acropolis_protection_source** | [**ProtectionSourceAcropolisProtectionSource**](ProtectionSourceAcropolisProtectionSource.md) |  | [optional] 
**aws_protection_source** | [**ProtectionSourceAwsProtectionSource**](ProtectionSourceAwsProtectionSource.md) |  | [optional] 
**azure_protection_source** | [**ProtectionSourceAzureProtectionSource**](ProtectionSourceAzureProtectionSource.md) |  | [optional] 
**environment** | **str** | Specifies the environment (such as &#39;kVMware&#39; or &#39;kSQL&#39;) where the Protection Source exists. Depending on the environment, one of the following Protection Sources are initialized.  NOTE: kPuppeteer refers to Cohesity&#39;s Remote Adapter. Supported environment types include &#39;kView&#39;, &#39;kSQL&#39;, &#39;kVMware&#39;, &#39;kPuppeteer&#39;, &#39;kPhysical&#39;, &#39;kPure&#39;, &#39;kNetapp, &#39;kGenericNas, &#39;kHyperV&#39;, &#39;kAcropolis&#39;, &#39;kAzure&#39;. NOTE: &#39;kPuppeteer&#39; refers to Cohesity&#39;s Remote Adapter. | [optional] 
**hyperv_protection_source** | [**ProtectionSourceHypervProtectionSource**](ProtectionSourceHypervProtectionSource.md) |  | [optional] 
**id** | **int** | Specifies an id of the Protection Source. | [optional] 
**kvm_protection_source** | [**ProtectionSourceKvmProtectionSource**](ProtectionSourceKvmProtectionSource.md) |  | [optional] 
**name** | **str** | Specifies a name of the Protection Source. | [optional] 
**nas_protection_source** | [**ProtectionSourceNasProtectionSource**](ProtectionSourceNasProtectionSource.md) |  | [optional] 
**netapp_protection_source** | [**ProtectionSourceNetappProtectionSource**](ProtectionSourceNetappProtectionSource.md) |  | [optional] 
**parent_id** | **int** | Specifies an id of the parent of the Protection Source. | [optional] 
**physical_protection_source** | [**ProtectionSourcePhysicalProtectionSource**](ProtectionSourcePhysicalProtectionSource.md) |  | [optional] 
**pure_protection_source** | [**ProtectionSourcePureProtectionSource**](ProtectionSourcePureProtectionSource.md) |  | [optional] 
**sql_protection_source** | [**ProtectionSourceSqlProtectionSource**](ProtectionSourceSqlProtectionSource.md) |  | [optional] 
**view_protection_source** | [**ProtectionSourceViewProtectionSource**](ProtectionSourceViewProtectionSource.md) |  | [optional] 
**vm_ware_protection_source** | [**ProtectionSourceVmWareProtectionSource**](ProtectionSourceVmWareProtectionSource.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


