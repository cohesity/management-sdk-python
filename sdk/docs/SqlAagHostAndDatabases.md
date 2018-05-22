# SqlAagHostAndDatabases

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aag_databases** | [**list[AagAndDatabases]**](AagAndDatabases.md) |  | [optional] 
**application_node** | [**ProtectionSourceNode**](ProtectionSourceNode.md) | Specifies the subtree used to store application-level Objects. Different environments use the subtree to store application-level information. For example for SQL Server, this subtree stores the SQL Server instances running on a VM or Physical hosts. | [optional] 
**databases** | [**list[ProtectionSource]**](ProtectionSource.md) | Specifies all database entities found on the server. Database may or may not be in an AAG. | [optional] 
**error_message** | **str** | Specifies an error message when the host is not registered as an SQL host. | [optional] 
**unknown_host_name** | **str** | Specifies the name of the host that is not registered as an SQL server on Cohesity Cluser. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


