# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.apps_config
import cohesity_management_sdk.models.cluster_audit_log_configuration
import cohesity_management_sdk.models.eula_config
import cohesity_management_sdk.models.filer_audit_log_configuration
import cohesity_management_sdk.models.cluster_hardware_info
import cohesity_management_sdk.models.ntp_settings_config
import cohesity_management_sdk.models.cluster_stats
import cohesity_management_sdk.models.supported_config
import cohesity_management_sdk.models.syslog_server

class Cluster(object):

    """Implementation of the 'Cluster' model.

    Specifies information about the Cohesity Cluster.

    Attributes:
        apps_settings (AppsConfig): TODO: type description here.
        available_metadata_space (long|int): Information about storage
            available for metadata
        banner_enabled (bool): Specifies whether UI banner is enabled on the
            cluster or not. When banner is enabled, UI will make an additional
            API call to fetch the banner and show at the login page.
        bonding_mode (BondingModeEnum): Specifies the bonding mode to use when
            bonding NICs to this Cluster. 'KActiveBackup' indicates an
            Active-backup policy bonding mode. 'K802_3ad' indicates an EEE
            802.3ad Dynamic link aggregation bonding mode. 'KBalanceAlb'
            indicates a Adaptive load balancing bonding mode.
        cluster_audit_log_config (ClusterAuditLogConfiguration): Specifies the
            settings of the Cluster audit log configuration.
        cluster_software_version (string): Specifies the current release of
            the Cohesity software running on this Cohesity Cluster.
        cluster_type (ClusterTypeClusterEnum): Specifies the type of Cluster
            such as kPhysical. 'kPhysical' indicates the Cohesity Cluster is
            hosted directly on hardware. 'kVirtualRobo' indicates the Cohesity
            Cluster is hosted in a VM on a ESXi Host of a VMware vCenter
            Server using Cohesity's Virtual Edition. 'kMicrosoftCloud'
            indicates the Cohesity Cluster is hosed in a VM on Microsoft Azure
            using Cohesity's Cloud Edition. 'kAmazonCloud' indicates the
            Cohesity Cluster is hosed in a VM on Amazon S3 using Cohesity's
            Cloud Edition. 'kGoogleCloud' indicates the Cohesity Cluster is
            hosed in a VM on Google Cloud Platform using Cohesity's Cloud
            Edition.
        created_time_msecs (long|int): Specifies the time when the Cohesity
            Cluster was created. This value is specified as a Unix epoch
            Timestamp (in microseconds).
        current_op_scheduled_time_secs (long|int): Specifies the time
            scheduled by the Cohesity Cluster to start the current running
            operation.
        current_operation (CurrentOperationEnum): Specifies the current
            Cluster-level operation in progress. 'kUpgrade' indicates the
            Cohesity Cluster is upgrading to a new release. 'kRemoveNode'
            indicates the Cohesity Cluster is removing a Node from the
            Cluster. 'kNone' indicates no action is occurring on the Cohesity
            Cluster. 'kDestroy' indicates the Cohesity Cluster is getting
            destoryed. 'kClean' indicates the Cohesity Cluster is getting
            cleaned. 'kRestartServices' indicates the Cohesity Cluster is
            restarting the services.
        current_time_msecs (long|int): Specifies the current system time on
            the Cohesity Cluster. This value is specified as a Unix epoch
            Timestamp (in microseconds).
        dns_server_ips (list of string): Array of IP Addresses of DNS Servers.
            Specifies the IP addresses of the DNS Servers used by the Cohesity
            Cluster.
        domain_names (list of string): Array of Domain Names.  The first
            domain name specified in the array is the fully qualified domain
            name assigned to the Cohesity Cluster. Any additional domain names
            specified are used for the domain search list for hostname
            look-up.
        enable_active_monitoring (bool): Specifies if Cohesity can receive
            monitoring information from the Cohesity Cluster. If 'true',
            remote monitoring of the Cohesity Cluster is allowed.
        enable_upgrade_pkg_polling (bool): If 'true', Cohesity's upgrade
            server is polled for new releases.
        encryption_enabled (bool): If 'true', the entire Cohesity Cluster is
            encrypted including all View Boxes.
        encryption_key_rotation_period_secs (long|int): Specifies the period
            of time (in seconds) when encryption keys are rotated. By default,
            the encryption keys are rotated every 77760000 seconds (30 days).
        eula_config (EulaConfig): Specifies the End User License Agreement
            (EULA) acceptance information.
        filer_audit_log_config (FilerAuditLogConfiguration): Specifies the
            settings of the filer audit log configuration.
        fips_mode_enabled (bool): Specifies if the Cohesity Cluster should
            operate in the FIPS mode, which is compliant with the Federal
            Information Processing Standard 140-2 certification.
        gateway (string): Specifies the gateway IP address.
        google_analytics_enabled (bool): Specifies whether Google Analytics is
            enabled.
        hardware_info (ClusterHardwareInfo): Specifies a hardware type for
            motherboard of the Nodes that make up this Cohesity Cluster such
            as S2600WB for Ivy Bridge or S2600TP for Haswell.
        id (long|int): Specifies the unique id of Cohesity Cluster.
        incarnation_id (long|int): Specifies the unique incarnation id of the
            Cohesity Cluster.
        is_documentation_local (bool): Specifies what version of the
            documentation is used. If 'true', the version of documentation
            stored locally on the Cohesity Cluster is used. If 'false', the
            documentation stored on a Cohesity Web Server is used. The default
            is 'false'. Cohesity recommends accessing the Help from the
            Cohesity Web site which provides the newest and most complete
            version of Help.
        language_locale (string): Specifies the language and locale for this
            Cohesity Cluster.
        license_server_claimed (bool): Speifies if cluster is claimed by
            Helios or not.
        local_groups_enabled (bool): Specifies whether to enable local groups
            on cluster. Once it is enabled, it cannot be disabled.
        metadata_fault_tolerance_factor (int): Specifies metadata fault
            tolerance setting for the cluster. This denotes the number of
            simultaneous failures[node] supported by metadata services like
            gandalf and scribe.
        mtu (int): Specifies the Maxium Transmission Unit (MTU) in bytes of
            the network.
        multi_tenancy_enabled (bool): Specifies if multi tenancy is enabled in
            the cluster. Authentication & Authorization will always use
            tenant_id, however, some UI elements may be disabled when multi
            tenancy is disabled.
        name (string): Specifies the name of the Cohesity Cluster.
        node_count (long|int): Specifies the number of Nodes in the Cohesity
            Cluster.
        ntp_settings (NtpSettingsConfig): TODO: type description here.
        proxy_vm_subnet (string): The subnet reserved for ProxyVM
        reverse_tunnel_enabled (bool): If 'true', Cohesity's Remote Tunnel is
            enabled. Cohesity can access the Cluster and provide remote
            assistance via a Remote Tunnel.
        reverse_tunnel_end_time_msecs (long|int): ReverseTunnelEndTimeMsecs
            specifies the end time in milliseconds since epoch until when the
            reverse tunnel will stay enabled.
        smb_ad_disabled (bool): Specifies if Active Directory should be
            disabled for authentication of SMB shares. If 'true', Active
            Directory is disabled.
        stats (ClusterStats): Specifies statistics about this Cohesity
            Cluster.
        stig_mode (bool): Specifies if STIG mode is enabled or not.
        supported_config (SupportedConfig): Lists the supported Erasure Coding
            options for the number of Nodes in the Cohesity Cluster. In
            addition, the minimum number of Nodes supported for this Cluster
            type is defined.
        syslog_servers (list of SyslogServer): Array of Syslog Servers.
            Specifies a list of Syslog servers to send audit logs to.
        target_software_version (string): Specifies the Cohesity release that
            this Cluster is being upgraded to if an upgrade operation is in
            progress.
        tenant_viewbox_sharing_enabled (bool): In case multi tenancy is
            enabled, this flag controls whether multiple tenants can be placed
            on the same viewbox. Once set to true, this flag should never
            become false.
        timezone (string): Specifies the timezone to use for showing time in
            emails, reports, filer audit logs, etc.
        turbo_mode (bool): Specifies if the cluster is in Turbo mode.
        used_metadata_space_pct (float): UsedMetadataSpacePct measures the
            percentage about storage used for metadata over the total storage
            available for metadata

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "apps_settings":'appsSettings',
        "available_metadata_space":'availableMetadataSpace',
        "banner_enabled":'bannerEnabled',
        "bonding_mode":'bondingMode',
        "cluster_audit_log_config":'clusterAuditLogConfig',
        "cluster_software_version":'clusterSoftwareVersion',
        "cluster_type":'clusterType',
        "created_time_msecs":'createdTimeMsecs',
        "current_op_scheduled_time_secs":'currentOpScheduledTimeSecs',
        "current_operation":'currentOperation',
        "current_time_msecs":'currentTimeMsecs',
        "dns_server_ips":'dnsServerIps',
        "domain_names":'domainNames',
        "enable_active_monitoring":'enableActiveMonitoring',
        "enable_upgrade_pkg_polling":'enableUpgradePkgPolling',
        "encryption_enabled":'encryptionEnabled',
        "encryption_key_rotation_period_secs":'encryptionKeyRotationPeriodSecs',
        "eula_config":'eulaConfig',
        "filer_audit_log_config":'filerAuditLogConfig',
        "fips_mode_enabled":'fipsModeEnabled',
        "gateway":'gateway',
        "google_analytics_enabled":'googleAnalyticsEnabled',
        "hardware_info":'hardwareInfo',
        "id":'id',
        "incarnation_id":'incarnationId',
        "is_documentation_local":'isDocumentationLocal',
        "language_locale":'languageLocale',
        "license_server_claimed":'licenseServerClaimed',
        "local_groups_enabled":'localGroupsEnabled',
        "metadata_fault_tolerance_factor":'metadataFaultToleranceFactor',
        "mtu":'mtu',
        "multi_tenancy_enabled":'multiTenancyEnabled',
        "name":'name',
        "node_count":'nodeCount',
        "ntp_settings":'ntpSettings',
        "proxy_vm_subnet":'proxyVMSubnet',
        "reverse_tunnel_enabled":'reverseTunnelEnabled',
        "reverse_tunnel_end_time_msecs":'reverseTunnelEndTimeMsecs',
        "smb_ad_disabled":'smbAdDisabled',
        "stats":'stats',
        "stig_mode":'stigMode',
        "supported_config":'supportedConfig',
        "syslog_servers":'syslogServers',
        "target_software_version":'targetSoftwareVersion',
        "tenant_viewbox_sharing_enabled":'tenantViewboxSharingEnabled',
        "timezone":'timezone',
        "turbo_mode":'turboMode',
        "used_metadata_space_pct":'usedMetadataSpacePct'
    }

    def __init__(self,
                 apps_settings=None,
                 available_metadata_space=None,
                 banner_enabled=None,
                 bonding_mode=None,
                 cluster_audit_log_config=None,
                 cluster_software_version=None,
                 cluster_type=None,
                 created_time_msecs=None,
                 current_op_scheduled_time_secs=None,
                 current_operation=None,
                 current_time_msecs=None,
                 dns_server_ips=None,
                 domain_names=None,
                 enable_active_monitoring=None,
                 enable_upgrade_pkg_polling=None,
                 encryption_enabled=None,
                 encryption_key_rotation_period_secs=None,
                 eula_config=None,
                 filer_audit_log_config=None,
                 fips_mode_enabled=None,
                 gateway=None,
                 google_analytics_enabled=None,
                 hardware_info=None,
                 id=None,
                 incarnation_id=None,
                 is_documentation_local=None,
                 language_locale=None,
                 license_server_claimed=None,
                 local_groups_enabled=None,
                 metadata_fault_tolerance_factor=None,
                 mtu=None,
                 multi_tenancy_enabled=None,
                 name=None,
                 node_count=None,
                 ntp_settings=None,
                 proxy_vm_subnet=None,
                 reverse_tunnel_enabled=None,
                 reverse_tunnel_end_time_msecs=None,
                 smb_ad_disabled=None,
                 stats=None,
                 stig_mode=None,
                 supported_config=None,
                 syslog_servers=None,
                 target_software_version=None,
                 tenant_viewbox_sharing_enabled=None,
                 timezone=None,
                 turbo_mode=None,
                 used_metadata_space_pct=None):
        """Constructor for the Cluster class"""

        # Initialize members of the class
        self.apps_settings = apps_settings
        self.available_metadata_space = available_metadata_space
        self.banner_enabled = banner_enabled
        self.bonding_mode = bonding_mode
        self.cluster_audit_log_config = cluster_audit_log_config
        self.cluster_software_version = cluster_software_version
        self.cluster_type = cluster_type
        self.created_time_msecs = created_time_msecs
        self.current_op_scheduled_time_secs = current_op_scheduled_time_secs
        self.current_operation = current_operation
        self.current_time_msecs = current_time_msecs
        self.dns_server_ips = dns_server_ips
        self.domain_names = domain_names
        self.enable_active_monitoring = enable_active_monitoring
        self.enable_upgrade_pkg_polling = enable_upgrade_pkg_polling
        self.encryption_enabled = encryption_enabled
        self.encryption_key_rotation_period_secs = encryption_key_rotation_period_secs
        self.eula_config = eula_config
        self.filer_audit_log_config = filer_audit_log_config
        self.fips_mode_enabled = fips_mode_enabled
        self.gateway = gateway
        self.google_analytics_enabled = google_analytics_enabled
        self.hardware_info = hardware_info
        self.id = id
        self.incarnation_id = incarnation_id
        self.is_documentation_local = is_documentation_local
        self.language_locale = language_locale
        self.license_server_claimed = license_server_claimed
        self.local_groups_enabled = local_groups_enabled
        self.metadata_fault_tolerance_factor = metadata_fault_tolerance_factor
        self.mtu = mtu
        self.multi_tenancy_enabled = multi_tenancy_enabled
        self.name = name
        self.node_count = node_count
        self.ntp_settings = ntp_settings
        self.proxy_vm_subnet = proxy_vm_subnet
        self.reverse_tunnel_enabled = reverse_tunnel_enabled
        self.reverse_tunnel_end_time_msecs = reverse_tunnel_end_time_msecs
        self.smb_ad_disabled = smb_ad_disabled
        self.stats = stats
        self.stig_mode = stig_mode
        self.supported_config = supported_config
        self.syslog_servers = syslog_servers
        self.target_software_version = target_software_version
        self.tenant_viewbox_sharing_enabled = tenant_viewbox_sharing_enabled
        self.timezone = timezone
        self.turbo_mode = turbo_mode
        self.used_metadata_space_pct = used_metadata_space_pct


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        apps_settings = cohesity_management_sdk.models.apps_config.AppsConfig.from_dictionary(dictionary.get('appsSettings')) if dictionary.get('appsSettings') else None
        available_metadata_space = dictionary.get('availableMetadataSpace')
        banner_enabled = dictionary.get('bannerEnabled')
        bonding_mode = dictionary.get('bondingMode')
        cluster_audit_log_config = cohesity_management_sdk.models.cluster_audit_log_configuration.ClusterAuditLogConfiguration.from_dictionary(dictionary.get('clusterAuditLogConfig')) if dictionary.get('clusterAuditLogConfig') else None
        cluster_software_version = dictionary.get('clusterSoftwareVersion')
        cluster_type = dictionary.get('clusterType')
        created_time_msecs = dictionary.get('createdTimeMsecs')
        current_op_scheduled_time_secs = dictionary.get('currentOpScheduledTimeSecs')
        current_operation = dictionary.get('currentOperation')
        current_time_msecs = dictionary.get('currentTimeMsecs')
        dns_server_ips = dictionary.get('dnsServerIps')
        domain_names = dictionary.get('domainNames')
        enable_active_monitoring = dictionary.get('enableActiveMonitoring')
        enable_upgrade_pkg_polling = dictionary.get('enableUpgradePkgPolling')
        encryption_enabled = dictionary.get('encryptionEnabled')
        encryption_key_rotation_period_secs = dictionary.get('encryptionKeyRotationPeriodSecs')
        eula_config = cohesity_management_sdk.models.eula_config.EulaConfig.from_dictionary(dictionary.get('eulaConfig')) if dictionary.get('eulaConfig') else None
        filer_audit_log_config = cohesity_management_sdk.models.filer_audit_log_configuration.FilerAuditLogConfiguration.from_dictionary(dictionary.get('filerAuditLogConfig')) if dictionary.get('filerAuditLogConfig') else None
        fips_mode_enabled = dictionary.get('fipsModeEnabled')
        gateway = dictionary.get('gateway')
        google_analytics_enabled = dictionary.get('googleAnalyticsEnabled')
        hardware_info = cohesity_management_sdk.models.cluster_hardware_info.ClusterHardwareInfo.from_dictionary(dictionary.get('hardwareInfo')) if dictionary.get('hardwareInfo') else None
        id = dictionary.get('id')
        incarnation_id = dictionary.get('incarnationId')
        is_documentation_local = dictionary.get('isDocumentationLocal')
        language_locale = dictionary.get('languageLocale')
        license_server_claimed = dictionary.get('licenseServerClaimed')
        local_groups_enabled = dictionary.get('localGroupsEnabled')
        metadata_fault_tolerance_factor = dictionary.get('metadataFaultToleranceFactor')
        mtu = dictionary.get('mtu')
        multi_tenancy_enabled = dictionary.get('multiTenancyEnabled')
        name = dictionary.get('name')
        node_count = dictionary.get('nodeCount')
        ntp_settings = cohesity_management_sdk.models.ntp_settings_config.NtpSettingsConfig.from_dictionary(dictionary.get('ntpSettings')) if dictionary.get('ntpSettings') else None
        proxy_vm_subnet = dictionary.get('proxyVMSubnet')
        reverse_tunnel_enabled = dictionary.get('reverseTunnelEnabled')
        reverse_tunnel_end_time_msecs = dictionary.get('reverseTunnelEndTimeMsecs')
        smb_ad_disabled = dictionary.get('smbAdDisabled')
        stats = cohesity_management_sdk.models.cluster_stats.ClusterStats.from_dictionary(dictionary.get('stats')) if dictionary.get('stats') else None
        stig_mode = dictionary.get('stigMode')
        supported_config = cohesity_management_sdk.models.supported_config.SupportedConfig.from_dictionary(dictionary.get('supportedConfig')) if dictionary.get('supportedConfig') else None
        syslog_servers = None
        if dictionary.get('syslogServers') != None:
            syslog_servers = list()
            for structure in dictionary.get('syslogServers'):
                syslog_servers.append(cohesity_management_sdk.models.syslog_server.SyslogServer.from_dictionary(structure))
        target_software_version = dictionary.get('targetSoftwareVersion')
        tenant_viewbox_sharing_enabled = dictionary.get('tenantViewboxSharingEnabled')
        timezone = dictionary.get('timezone')
        turbo_mode = dictionary.get('turboMode')
        used_metadata_space_pct = dictionary.get('usedMetadataSpacePct')

        # Return an object of this model
        return cls(apps_settings,
                   available_metadata_space,
                   banner_enabled,
                   bonding_mode,
                   cluster_audit_log_config,
                   cluster_software_version,
                   cluster_type,
                   created_time_msecs,
                   current_op_scheduled_time_secs,
                   current_operation,
                   current_time_msecs,
                   dns_server_ips,
                   domain_names,
                   enable_active_monitoring,
                   enable_upgrade_pkg_polling,
                   encryption_enabled,
                   encryption_key_rotation_period_secs,
                   eula_config,
                   filer_audit_log_config,
                   fips_mode_enabled,
                   gateway,
                   google_analytics_enabled,
                   hardware_info,
                   id,
                   incarnation_id,
                   is_documentation_local,
                   language_locale,
                   license_server_claimed,
                   local_groups_enabled,
                   metadata_fault_tolerance_factor,
                   mtu,
                   multi_tenancy_enabled,
                   name,
                   node_count,
                   ntp_settings,
                   proxy_vm_subnet,
                   reverse_tunnel_enabled,
                   reverse_tunnel_end_time_msecs,
                   smb_ad_disabled,
                   stats,
                   stig_mode,
                   supported_config,
                   syslog_servers,
                   target_software_version,
                   tenant_viewbox_sharing_enabled,
                   timezone,
                   turbo_mode,
                   used_metadata_space_pct)


