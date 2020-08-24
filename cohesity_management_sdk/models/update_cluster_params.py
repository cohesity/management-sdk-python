# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.subnet
import cohesity_management_sdk.models.cluster_audit_log_configuration
import cohesity_management_sdk.models.filer_audit_log_configuration
import cohesity_management_sdk.models.ntp_settings_config
import cohesity_management_sdk.models.syslog_server

class UpdateClusterParams(object):

    """Implementation of the 'UpdateClusterParams' model.

    Specifies the configuration settings that can be updated on the
    Cohesity Cluster.

    Attributes:
        apps_subnet (Subnet): The subnet for Athena apps.
        banner_enabled (bool): Specifies whether UI banner is enabled on the
            cluster or not. When banner is enabled, UI will make an additional
            API call to fetch the banner and show at the login page.
        cluster_audit_log_config (ClusterAuditLogConfiguration): Specifies the
            settings of the Cluster audit log configuration.
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
        encryption_key_rotation_period_secs (long|int): Specifies the period
            of time (in seconds) when encryption keys are rotated. By default,
            the encryption keys are rotated every 77760000 seconds (30 days).
        fault_tolerance_level (UpdateClusterParamsFaultToleranceLevelEnum):
            Specifies the level which 'MetadataFaultToleranceFactor' applies
            to.
            'kNode' indicates 'MetadataFaultToleranceFactor' applies to Node
            level.
            'kChassis' indicates 'MetadataFaultToleranceFactor' applies to
            Chassis level.
            'kRack' indicates 'MetadataFaultToleranceFactor' applies to Rack
            level.
        filer_audit_log_config (FilerAuditLogConfiguration): Specifies the
            settings of the filer audit log configuration.
        gateway (string): Specifies the gateway IP address.
        google_analytics_enabled (bool): Specifies whether Google Analytics is
            enabled.
        is_documentation_local (bool): Specifies what version of the
            documentation is used. If 'true', the version of documentation
            stored locally on the Cohesity Cluster is used. If 'false', the
            documentation stored on a Cohesity Web Server is used. The default
            is 'false'. Cohesity recommends accessing the Help from the
            Cohesity Web site which provides the newest and most complete
            version of Help.
        language_locale (string): Specifies the language and locale for this
            Cohesity Cluster.
        local_auth_domain_name (string): Domain name for SMB local
            authentication.
        local_groups_enabled (bool): Specifies whether to enable local groups
            on cluster. Once it is enabled, it cannot be disabled.
        metadata_fault_tolerance_factor (int): Specifies metadata fault
            tolerance setting for the cluster. This denotes the number of
            simultaneous failures[node] supported by metadata services like
            gandalf and scribe.
        multi_tenancy_enabled (bool): Specifies if multi tenancy is enabled in
            the cluster. Authentication & Authorization will always use
            tenant_id, however, some UI elements may be disabled when multi
            tenancy is disabled.
        name (string): Specifies the name of the Cohesity Cluster.
        ntp_settings (NtpSettingsConfig): Specifies if the ntp/master slave
            scheme should be disabled for this cluster.
        pcie_ssd_tier_rebalance_delay_secs (int): Specifies the rebalance
            delay in seconds for cluster PcieSSD storage tier.
        reverse_tunnel_enabled (bool): If 'true', Cohesity's Remote Tunnel is
            enabled. Cohesity can access the Cluster and provide remote
            assistance via a Remote Tunnel.
        reverse_tunnel_end_time_msecs (long|int): ReverseTunnelEndTimeMsecs
            specifies the end time in milliseconds since epoch until when the
            reverse tunnel will stay enabled.
        smb_ad_disabled (bool): Specifies if Active Directory should be
            disabled for authentication of SMB shares. If 'true', Active
            Directory is disabled.
        smb_multichannel_enabled (bool): Specifies whether SMB multichannel is
            enabled on the cluster. When this is set to true, then any SMB3
            multichannel enabled client can establish multiple TCP connection
            per session to the Server.
        stig_mode (bool): Specifies if STIG mode is enabled or not.
        syslog_servers (list of SyslogServer): Array of Syslog Servers.
            Specifies a list of Syslog servers to send audit logs to.
        tenant_viewbox_sharing_enabled (bool): In case multi tenancy is
            enabled, this flag controls whether multiple tenants can be placed
            on the same viewbox. Once set to true, this flag should never
            become false.
        timezone (string): Specifies the timezone to use for showing time in
            emails, reports, filer audit logs, etc.
        turbo_mode (bool): Specifies if the cluster is in Turbo mode.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "apps_subnet":'appsSubnet',
        "banner_enabled":'bannerEnabled',
        "cluster_audit_log_config":'clusterAuditLogConfig',
        "dns_server_ips":'dnsServerIps',
        "domain_names":'domainNames',
        "enable_active_monitoring":'enableActiveMonitoring',
        "enable_upgrade_pkg_polling":'enableUpgradePkgPolling',
        "encryption_key_rotation_period_secs":'encryptionKeyRotationPeriodSecs',
        "fault_tolerance_level":'faultToleranceLevel',
        "filer_audit_log_config":'filerAuditLogConfig',
        "gateway":'gateway',
        "google_analytics_enabled":'googleAnalyticsEnabled',
        "is_documentation_local":'isDocumentationLocal',
        "language_locale":'languageLocale',
        "local_auth_domain_name":'localAuthDomainName',
        "local_groups_enabled":'localGroupsEnabled',
        "metadata_fault_tolerance_factor":'metadataFaultToleranceFactor',
        "multi_tenancy_enabled":'multiTenancyEnabled',
        "name":'name',
        "ntp_settings":'ntpSettings',
        "pcie_ssd_tier_rebalance_delay_secs":'pcieSsdTierRebalanceDelaySecs',
        "reverse_tunnel_enabled":'reverseTunnelEnabled',
        "reverse_tunnel_end_time_msecs":'reverseTunnelEndTimeMsecs',
        "smb_ad_disabled":'smbAdDisabled',
        "smb_multichannel_enabled":'smbMultichannelEnabled',
        "stig_mode":'stigMode',
        "syslog_servers":'syslogServers',
        "tenant_viewbox_sharing_enabled":'tenantViewboxSharingEnabled',
        "timezone":'timezone',
        "turbo_mode":'turboMode'
    }

    def __init__(self,
                 apps_subnet=None,
                 banner_enabled=None,
                 cluster_audit_log_config=None,
                 dns_server_ips=None,
                 domain_names=None,
                 enable_active_monitoring=None,
                 enable_upgrade_pkg_polling=None,
                 encryption_key_rotation_period_secs=None,
                 fault_tolerance_level=None,
                 filer_audit_log_config=None,
                 gateway=None,
                 google_analytics_enabled=None,
                 is_documentation_local=None,
                 language_locale=None,
                 local_auth_domain_name=None,
                 local_groups_enabled=None,
                 metadata_fault_tolerance_factor=None,
                 multi_tenancy_enabled=None,
                 name=None,
                 ntp_settings=None,
                 pcie_ssd_tier_rebalance_delay_secs=None,
                 reverse_tunnel_enabled=None,
                 reverse_tunnel_end_time_msecs=None,
                 smb_ad_disabled=None,
                 smb_multichannel_enabled=None,
                 stig_mode=None,
                 syslog_servers=None,
                 tenant_viewbox_sharing_enabled=None,
                 timezone=None,
                 turbo_mode=None):
        """Constructor for the UpdateClusterParams class"""

        # Initialize members of the class
        self.apps_subnet = apps_subnet
        self.banner_enabled = banner_enabled
        self.cluster_audit_log_config = cluster_audit_log_config
        self.dns_server_ips = dns_server_ips
        self.domain_names = domain_names
        self.enable_active_monitoring = enable_active_monitoring
        self.enable_upgrade_pkg_polling = enable_upgrade_pkg_polling
        self.encryption_key_rotation_period_secs = encryption_key_rotation_period_secs
        self.fault_tolerance_level = fault_tolerance_level
        self.filer_audit_log_config = filer_audit_log_config
        self.gateway = gateway
        self.google_analytics_enabled = google_analytics_enabled
        self.is_documentation_local = is_documentation_local
        self.language_locale = language_locale
        self.local_auth_domain_name = local_auth_domain_name
        self.local_groups_enabled = local_groups_enabled
        self.metadata_fault_tolerance_factor = metadata_fault_tolerance_factor
        self.multi_tenancy_enabled = multi_tenancy_enabled
        self.name = name
        self.ntp_settings = ntp_settings
        self.pcie_ssd_tier_rebalance_delay_secs = pcie_ssd_tier_rebalance_delay_secs
        self.reverse_tunnel_enabled = reverse_tunnel_enabled
        self.reverse_tunnel_end_time_msecs = reverse_tunnel_end_time_msecs
        self.smb_ad_disabled = smb_ad_disabled
        self.smb_multichannel_enabled = smb_multichannel_enabled
        self.stig_mode = stig_mode
        self.syslog_servers = syslog_servers
        self.tenant_viewbox_sharing_enabled = tenant_viewbox_sharing_enabled
        self.timezone = timezone
        self.turbo_mode = turbo_mode


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
        apps_subnet = cohesity_management_sdk.models.subnet.Subnet.from_dictionary(dictionary.get('appsSubnet')) if dictionary.get('appsSubnet') else None
        banner_enabled = dictionary.get('bannerEnabled')
        cluster_audit_log_config = cohesity_management_sdk.models.cluster_audit_log_configuration.ClusterAuditLogConfiguration.from_dictionary(dictionary.get('clusterAuditLogConfig')) if dictionary.get('clusterAuditLogConfig') else None
        dns_server_ips = dictionary.get('dnsServerIps')
        domain_names = dictionary.get('domainNames')
        enable_active_monitoring = dictionary.get('enableActiveMonitoring')
        enable_upgrade_pkg_polling = dictionary.get('enableUpgradePkgPolling')
        encryption_key_rotation_period_secs = dictionary.get('encryptionKeyRotationPeriodSecs')
        fault_tolerance_level = dictionary.get('faultToleranceLevel')
        filer_audit_log_config = cohesity_management_sdk.models.filer_audit_log_configuration.FilerAuditLogConfiguration.from_dictionary(dictionary.get('filerAuditLogConfig')) if dictionary.get('filerAuditLogConfig') else None
        gateway = dictionary.get('gateway')
        google_analytics_enabled = dictionary.get('googleAnalyticsEnabled')
        is_documentation_local = dictionary.get('isDocumentationLocal')
        language_locale = dictionary.get('languageLocale')
        local_auth_domain_name = dictionary.get('localAuthDomainName')
        local_groups_enabled = dictionary.get('localGroupsEnabled')
        metadata_fault_tolerance_factor = dictionary.get('metadataFaultToleranceFactor')
        multi_tenancy_enabled = dictionary.get('multiTenancyEnabled')
        name = dictionary.get('name')
        ntp_settings = cohesity_management_sdk.models.ntp_settings_config.NtpSettingsConfig.from_dictionary(dictionary.get('ntpSettings')) if dictionary.get('ntpSettings') else None
        pcie_ssd_tier_rebalance_delay_secs = dictionary.get('pcieSsdTierRebalanceDelaySecs')
        reverse_tunnel_enabled = dictionary.get('reverseTunnelEnabled')
        reverse_tunnel_end_time_msecs = dictionary.get('reverseTunnelEndTimeMsecs')
        smb_ad_disabled = dictionary.get('smbAdDisabled')
        smb_multichannel_enabled = dictionary.get('smbMultichannelEnabled')
        stig_mode = dictionary.get('stigMode')
        syslog_servers = None
        if dictionary.get('syslogServers') != None:
            syslog_servers = list()
            for structure in dictionary.get('syslogServers'):
                syslog_servers.append(cohesity_management_sdk.models.syslog_server.SyslogServer.from_dictionary(structure))
        tenant_viewbox_sharing_enabled = dictionary.get('tenantViewboxSharingEnabled')
        timezone = dictionary.get('timezone')
        turbo_mode = dictionary.get('turboMode')

        # Return an object of this model
        return cls(apps_subnet,
                   banner_enabled,
                   cluster_audit_log_config,
                   dns_server_ips,
                   domain_names,
                   enable_active_monitoring,
                   enable_upgrade_pkg_polling,
                   encryption_key_rotation_period_secs,
                   fault_tolerance_level,
                   filer_audit_log_config,
                   gateway,
                   google_analytics_enabled,
                   is_documentation_local,
                   language_locale,
                   local_auth_domain_name,
                   local_groups_enabled,
                   metadata_fault_tolerance_factor,
                   multi_tenancy_enabled,
                   name,
                   ntp_settings,
                   pcie_ssd_tier_rebalance_delay_secs,
                   reverse_tunnel_enabled,
                   reverse_tunnel_end_time_msecs,
                   smb_ad_disabled,
                   smb_multichannel_enabled,
                   stig_mode,
                   syslog_servers,
                   tenant_viewbox_sharing_enabled,
                   timezone,
                   turbo_mode)


