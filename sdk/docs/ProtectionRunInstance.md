# ProtectionRunInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_run** | [**BackupRun**](BackupRun.md) | Specifies details about the Backup task. A Backup task captures the original backup snapshots. | [optional] 
**copy_run** | [**list[CopyRun]**](CopyRun.md) | Specifies details about the Copy tasks of this Job Run. A Copy task copies the captured snapshots to an external target or a Remote Cohesity Cluster. | [optional] 
**job_id** | **int** | Specifies the id of the Protection Job that was run. | [optional] 
**job_name** | **str** | Specifies the name of the Protection Job name that was run. | [optional] 
**job_uid** | [**ProtectionRunInstanceJobUid**](ProtectionRunInstanceJobUid.md) |  | [optional] 
**view_box_id** | **int** | Specifies the Storage Domain (View Box) to store the backed up data. Specify the id of the Storage Domain (View Box). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


