# Cluster

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bonding_mode** | **str** | Specifies the bonding mode to use when bonding NICs to this Cluster. &#39;KActiveBackup&#39; indicates an Active-backup policy bonding mode. &#39;K802_3ad&#39; indicates an EEE 802.3ad Dynamic link aggregation bonding mode. &#39;KBalanceAlb&#39; indicates a Adaptive load balancing bonding mode. | [optional] 
**cluster_audit_log_config** | [**ClusterAuditLogConfiguration**](ClusterAuditLogConfiguration.md) | Cluster Audit Log Configuration. | [optional] 
**cluster_software_version** | **str** | Specifies the current release of the Cohesity software running on this Cohesity Cluster. | [optional] 
**cluster_type** | **str** | Specifies the type of Cluster such as kPhysical. &#39;kPhysical&#39; indicates the Cohesity Cluster is hosted directly on hardware. &#39;kVirtualRobo&#39; indicates the Cohesity Cluster is hosted in a VM on a ESXi Host of a VMware vCenter Server using Cohesity&#39;s Virtual Edition. &#39;kMicrosoftCloud&#39; indicates the Cohesity Cluster is hosed in a VM on Microsoft Azure using Cohesity&#39;s Cloud Edition. &#39;kAmazonCloud&#39; indicates the Cohesity Cluster is hosed in a VM on Amazon S3 using Cohesity&#39;s Cloud Edition. &#39;kGoogleCloud&#39; indicates the Cohesity Cluster is hosed in a VM on Google Cloud Platform using Cohesity&#39;s Cloud Edition. | [optional] 
**created_time_msecs** | **int** | Specifies the time when the Cohesity Cluster was created. This value is specified as a Unix epoch Timestamp (in microseconds). | [optional] 
**current_op_scheduled_time_secs** | **int** | Specifies the time scheduled by the Cohesity Cluster to start the current running operation. | [optional] 
**current_operation** | **str** | Specifies the current Cluster-level operation in progress. &#39;kUpgrade&#39; indicates the Cohesity Cluster is upgrading to a new release. &#39;kRemoveNode&#39; indicates the Cohesity Cluster is removing a Node from the Cluster. &#39;kNone&#39; indicates no action is occurring on the Cohesity Cluster. | [optional] 
**current_time_msecs** | **int** | Specifies the current system time on the Cohesity Cluster. This value is specified as a Unix epoch Timestamp (in microseconds). | [optional] 
**dns_server_ips** | **list[str]** | Specifies the IP addresses of the DNS Servers used by the Cohesity Cluster. | [optional] 
**domain_names** | **list[str]** | The first domain name specified in the array is the fully qualified domain name assigned to the Cohesity Cluster. Any additional domain names specified are used for the domain search list for hostname look-up. | [optional] 
**enable_active_monitoring** | **bool** | Specifies if Cohesity can receive monitoring information from the Cohesity Cluster. If &#39;true&#39;, remote monitoring of the Cohesity Cluster is allowed. | [optional] 
**enable_upgrade_pkg_polling** | **bool** | If &#39;true&#39;, Cohesity&#39;s upgrade server is polled for new releases. | [optional] 
**encryption_enabled** | **bool** | If &#39;true&#39;, the entire Cohesity Cluster is encrypted including all View Boxes. | [optional] 
**encryption_key_rotation_period_secs** | **int** | Specifies the period of time (in seconds) when encryption keys are rotated. By default, the encryption keys are rotated every 77760000 seconds (30 days). | [optional] 
**eula_config** | [**ClusterEulaConfig**](ClusterEulaConfig.md) |  | [optional] 
**filer_audit_log_config** | [**FilerAuditLogConfiguration**](FilerAuditLogConfiguration.md) | Filer Audit Log Configuration. | [optional] 
**fips_mode_enabled** | **bool** | Specifies if the Cohesity Cluster should operate in the FIPS mode, which is compliant with the Federal Information Processing Standard 140-2 certification. | [optional] 
**gateway** | **str** | Specifies the gateway IP address. | [optional] 
**hardware_info** | [**ClusterHardwareInfo**](ClusterHardwareInfo.md) | Specifies a hardware type for motherboard of the nodes that make up this Cohesity Cluster such as S2600WB for Ivy Bridge or S2600TP for Haswell. | [optional] 
**id** | **int** | Specifies the unique id of Cohesity Cluster. | [optional] 
**incarnation_id** | **int** | Specifies the unique incarnation id of the Cohesity Cluster. | [optional] 
**is_documentation_local** | **bool** | Specifies what version of the documentation is used. If &#39;true&#39;, the version of documentation stored locally on the Cohesity Cluster is used. If &#39;false&#39;, the documentation stored on a Cohesity Web Server is used. The default is &#39;false&#39;. Cohesity recommends accessing the Help from the Cohesity Web site which provides the newest and most complete version of Help. | [optional] 
**language_locale** | **str** | Specifies the language and locale for this Cohesity Cluster. | [optional] 
**mtu** | **int** | Specifies the Maxium Transmission Unit (MTU) in bytes of the network. | [optional] 
**name** | **str** | Specifies the name of the Cohesity Cluster. | [optional] 
**node_count** | **int** | Specifies the number of Nodes in the Cohesity Cluster. | [optional] 
**ntp_settings** | [**NtpSettingsConfig**](NtpSettingsConfig.md) | Specifies if the ntp/master slave scheme should be disabled for this cluster. | [optional] 
**reverse_tunnel_enabled** | **bool** | If &#39;true&#39;, Cohesity&#39;s Remote Tunnel is enabled. Cohesity can access the Cluster and provide remote assistance via a Remote Tunnel. | [optional] 
**smb_ad_disabled** | **bool** | Specifies if Active Directory should be disabled for authentication of SMB shares. If &#39;true&#39;, Active Directory is disabled. | [optional] 
**stats** | [**ClusterStats**](ClusterStats.md) | Specifies statistics about this Cohesity Cluster. | [optional] 
**supported_config** | [**SupportedConfig**](SupportedConfig.md) | Information about supported configuration. For example, it contains minimum number of nodes supported for the cluster. | [optional] 
**syslog_servers** | [**list[SyslogServer]**](SyslogServer.md) | Specifies a list of Syslog servers to send audit logs to. | [optional] 
**target_software_version** | **str** | Specifies the Cohesity release that this Cluster is being upgraded to if an upgrade operation is in progress. | [optional] 
**timezone** | **str** | Specifies the timezone to use for showing time in emails, reports, filer audit logs, etc. | [optional] 
**turbo_mode** | **bool** | Specifies if the cluster is in Turbo mode. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


