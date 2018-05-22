# VmwareEnvJobParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**excluded_disks** | [**list[DiskUnit]**](DiskUnit.md) | Specifies the list of Disks to be excluded from backing up. These disks are excluded from all Protection Sources in the Protection Job. | [optional] 
**fallback_to_crash_consistent** | **bool** | If true, takes a crash-consistent snapshot when app-consistent snapshot fails. Otherwise, the snapshot attempt is marked failed. | [optional] 
**skip_physical_rdm_disks** | **bool** | If true, skip physical RDM disks when backing up VMs. Otherwise, backup of VMs having physical RDM will fail. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


