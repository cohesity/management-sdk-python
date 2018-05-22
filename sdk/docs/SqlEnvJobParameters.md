# SqlEnvJobParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aag_preference** | **str** | kPrimaryReplicaOnly implies backups should always occur on the primary replica. kSecondaryReplicaOnly implies backups should always occur on the secondary replica. kPreferSecondaryReplica implies secondary replica is preferred for backups. kAnyReplica implies no preference of about whether backups are performed on the primary replica or on a secondary replica. If no secondary replica is available, then performing backups on the primary replica is acceptable. | [optional] 
**aag_preference_from_sql_server** | **bool** | If true, AAG preferences are taken from the SQL server host. If this is set to false or not given, preferences can be overridden by aagBackupPreference. | [optional] 
**backup_system_databases** | **bool** | If true, system databases are backed up. If this is set to false, system databases are not backed up. If this field is not specified, default value is true. | [optional] 
**backup_type** | **str** | kSqlVSSVolume implies volume based VSS full backup. kSqlVSSFile implies file based VSS full backup. | [optional] 
**backup_volumes_only** | **bool** | If set to true, only the volumes associated with databases should be backed up. The user cannot select additional volumes at host level for backup.  If set to false, all the volumes on the host machine will be backed up. In this case, the user can further select the exact set of volumes using host level params.  Note that the volumes associated with selected databases will always be included in the backup. | [optional] 
**is_copy_only_full** | **bool** | If true, the backup is a full backup with the copy-only option specified. | [optional] 
**user_database_preference** | **str** | kBackupAllDatabases implies to backup all databases. kBackupAllExceptAAGDatabases implies not to backup AAG databases. kBackupOnlyAAGDatabases implies to backup only AAG databases. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


