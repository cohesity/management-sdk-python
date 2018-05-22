# SqlProtectionSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_available_for_vss_backup** | **bool** | Specifies whether the database is marked as available for backup according to the SQL Server VSS writer. This may be false if either the state of the databases is not online, or if the VSS writer is not online. This field is set only for type &#39;kDatabase&#39;. | [optional] 
**created_timestamp** | **str** | Specifies the time when the database was created. It is displayed in the timezone of the SQL server on which this database is running. | [optional] 
**database_name** | **str** | Specifies the database name of the SQL Protection Source, if the type is database. | [optional] 
**db_aag_entity_id** | **int** | Specifies the AAG entity id if the database is part of an AAG. This field is set only for type &#39;kDatabase&#39;. | [optional] 
**db_aag_name** | **str** | Specifies the name of the AAG if the database is part of an AAG. This field is set only for type &#39;kDatabase&#39;. | [optional] 
**db_files** | [**list[DbFileInfo]**](DbFileInfo.md) | Specifies the last known information about the set of database files on the host. This field is set only for type &#39;kDatabase&#39;. | [optional] 
**id** | [**SqlSourceId**](SqlSourceId.md) | Specifies an id that identifies an SQL Object. | [optional] 
**name** | **str** | Specifies the instance name of the SQL Protection Source | [optional] 
**owner_id** | **int** | Specifies the id of the container VM for the SQL Protection Source. | [optional] 
**recovery_model** | **str** | Specifies the Recovery Model for the database in SQL environment. Only meaningful for the &#39;kDatabase&#39; SQL Protection Source. Specifies the Recovery Model set for the Microsoft SQL Server. &#39;kSimpleRecoveryModel&#39; indicates the Simple SQL Recovery Model which does not utilize log backups. &#39;kFullRecoveryModel&#39; indicates the Full SQL Recovery Model which requires log backups and allows recovery to a single point in time. &#39;kBulkLoggedRecoveryModel&#39; indicates the Bulk Logged SQL Recovery Model which requires log backups and allows high-performance bulk copy operations. | [optional] 
**sql_server_db_state** | **int** | The state of the database as returned by SQL Server. | [optional] 
**type** | **str** | Specifies the type of the managed Object in a SQL Protection Source. Examples of SQL Objects include &#39;kInstance&#39; and &#39;kDatabase&#39;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


