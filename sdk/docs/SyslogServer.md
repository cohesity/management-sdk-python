# SyslogServer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Specifies the IP address or hostname of the syslog server. | 
**is_cluster_auditing_enabled** | **bool** | Specifies if Cluster audit logs should be sent to this syslog server. If &#39;true&#39;, Cluster audit logs are sent to the syslog server. (default) If &#39;false&#39;, Cluster audit logs are not sent to the syslog server. Either cluster audit logs or filer audit logs should be enabled. | [optional] 
**is_filer_auditing_enabled** | **bool** | Specifies if filer audit logs should be sent to this syslog server. If &#39;true&#39;, filer audit logs are sent to the syslog server. (default) If &#39;false&#39;, filer audit logs are not sent to the syslog server. Either cluster audit logs or filer audit logs should be enabled. | [optional] 
**name** | **str** | Specifies a unique name for the syslog server on the Cluster. | [optional] 
**port** | **int** | Specifies the port where the syslog server listens. | 
**protocol** | **str** | Specifies the protocol used to send the logs. Specifies the protocol used to communicate to a server. e.g., kUDP, kTCP.  &#39;kUDP&#39; indicates UDP protocol. &#39;kTCP&#39; indicates TCP protocol. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


