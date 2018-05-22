# UpdateClusterParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bonding_mode** | **str** | Specifies the bonding mode to use when bonding NICs to this Cluster. &#39;KActiveBackup&#39; indicates an Active-backup policy bonding mode. &#39;K802_3ad&#39; indicates an EEE 802.3ad Dynamic link aggregation bonding mode. &#39;KBalanceAlb&#39; indicates a Adaptive load balancing bonding mode. | [optional] 
**cluster_audit_log_config** | [**ClusterAuditLogConfiguration**](ClusterAuditLogConfiguration.md) | Cluster Audit Log Configuration. | [optional] 
**dns_server_ips** | **list[str]** | Specifies the IP addresses of the DNS Servers used by the Cohesity Cluster. | [optional] 
**domain_names** | **list[str]** | The first domain name specified in the array is the fully qualified domain name assigned to the Cohesity Cluster. Any additional domain names specified are used for the domain search list for hostname look-up. | [optional] 
**enable_active_monitoring** | **bool** | Specifies if Cohesity can receive monitoring information from the Cohesity Cluster. If &#39;true&#39;, remote monitoring of the Cohesity Cluster is allowed. | [optional] 
**enable_upgrade_pkg_polling** | **bool** | If &#39;true&#39;, Cohesity&#39;s upgrade server is polled for new releases. | [optional] 
**encryption_key_rotation_period_secs** | **int** | Specifies the period of time (in seconds) when encryption keys are rotated. By default, the encryption keys are rotated every 77760000 seconds (30 days). | [optional] 
**filer_audit_log_config** | [**FilerAuditLogConfiguration**](FilerAuditLogConfiguration.md) | Filer Audit Log Configuration. | [optional] 
**gateway** | **str** | Specifies the gateway IP address. | [optional] 
**is_documentation_local** | **bool** | Specifies what version of the documentation is used. If &#39;true&#39;, the version of documentation stored locally on the Cohesity Cluster is used. If &#39;false&#39;, the documentation stored on a Cohesity Web Server is used. The default is &#39;false&#39;. Cohesity recommends accessing the Help from the Cohesity Web site which provides the newest and most complete version of Help. | [optional] 
**language_locale** | **str** | Specifies the language and locale for this Cohesity Cluster. | [optional] 
**mtu** | **int** | Specifies the Maxium Transmission Unit (MTU) in bytes of the network. | [optional] 
**name** | **str** | Specifies the name of the Cohesity Cluster. | [optional] 
**ntp_settings** | [**NtpSettingsConfig**](NtpSettingsConfig.md) | Specifies if the ntp/master slave scheme should be disabled for this cluster. | [optional] 
**reverse_tunnel_enabled** | **bool** | If &#39;true&#39;, Cohesity&#39;s Remote Tunnel is enabled. Cohesity can access the Cluster and provide remote assistance via a Remote Tunnel. | [optional] 
**smb_ad_disabled** | **bool** | Specifies if Active Directory should be disabled for authentication of SMB shares. If &#39;true&#39;, Active Directory is disabled. | [optional] 
**syslog_servers** | [**list[SyslogServer]**](SyslogServer.md) | Specifies a list of Syslog servers to send audit logs to. | [optional] 
**timezone** | **str** | Specifies the timezone to use for showing time in emails, reports, filer audit logs, etc. | [optional] 
**turbo_mode** | **bool** | Specifies if the cluster is in Turbo mode. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


