# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.amqp_target_config
import cohesity_management_sdk.models.cluster_audit_log_configuration
import cohesity_management_sdk.models.cluster_hardware_info
import cohesity_management_sdk.models.cluster_stats
import cohesity_management_sdk.models.count_by_tier
import cohesity_management_sdk.models.eula_config
import cohesity_management_sdk.models.filer_audit_log_configuration
import cohesity_management_sdk.models.license_state
import cohesity_management_sdk.models.ntp_settings_config
import cohesity_management_sdk.models.old_syslog_server
import cohesity_management_sdk.models.schema_info
import cohesity_management_sdk.models.subnet
import cohesity_management_sdk.models.supported_config
import cohesity_management_sdk.models.tiering_audit_log_configuration


class Cluster(object):

    """Implementation of the 'Cluster' model.

    Specifies information about the Cohesity Cluster.


    Attributes:

        amqp_target_config (AMQPTargetConfig): Specifies the AMQP target
            config.
        apps_subnet (Subnet): The subnet for Athena apps.
        assigned_racks_count (int): Specifies the number of racks in cluster
            with at least one rack assigned.
        available_metadata_space (long|int): Information about storage
            available for metadata
        banner_enabled (bool): Specifies whether UI banner is enabled on the
            cluster or not. When banner is enabled, UI will make an additional
            API call to fetch the banner and show at the login page.
        chassis_count (int): Specifies the number of chassis in cluster.
        cluster_audit_log_config (ClusterAuditLogConfiguration): Cluster Audit
            Log Configuration.
        cluster_size (ClusterSizeEnum): Specifies the size of Cloud Edition(CE)
            Cluster such as kSmall, kNextGen. Specifies the clustersize of the
            cloud edition(CE) clusters. 'kSmall' indicates small cluster size
            of CE. 'kMedium' indicates medium cluster size of CE. 'kLarge'
            indicates large cluster size of CE. 'kXLarge' indicates extra large
            cluster size of CE. 'kNextGen' indicates next gen CE.
        cluster_software_version (string): Specifies the current release of the
            Cohesity software running on this Cohesity Cluster.
        cluster_type (ClusterTypeEnum): Specifies the type of Cluster such as
            kPhysical. 'kPhysical' indicates the Cohesity Cluster is hosted
            directly on hardware. 'kVirtualRobo' indicates the Cohesity Cluster
            is hosted in a VM on a ESXi Host of a VMware vCenter Server using
            Cohesity's Virtual Edition. 'kMicrosoftCloud' indicates the
            Cohesity Cluster is hosted in a VM on Microsoft Azure using
            Cohesity's Cloud Edition. 'kAmazonCloud' indicates the Cohesity
            Cluster is hosted in a VM on Amazon S3 using Cohesity's Cloud
            Edition. 'kGoogleCloud' indicates the Cohesity Cluster is hosted in
            a VM on Google Cloud Platform using Cohesity's Cloud Edition.
        created_time_msecs (long|int): Specifies the time when the Cohesity
            Cluster was created. This value is specified as a Unix epoch
            Timestamp (in microseconds).
        current_op_scheduled_time_secs (long|int): Specifies the time scheduled
            by the Cohesity Cluster to start the current running operation.
        current_operation (CurrentOperationEnum): Specifies the current
            Cluster-level operation in progress. 'kUpgrade' indicates the
            Cohesity Cluster is upgrading to a new release. 'kRemoveNode'
            indicates the Cohesity Cluster is removing a Node from the Cluster.
            'kNone' indicates no action is occurring on the Cohesity Cluster.
            'kDestroy' indicates the Cohesity Cluster is getting destoryed.
            'kClean' indicates the Cohesity Cluster is getting cleaned.
            'kRestartServices' indicates the Cohesity Cluster is restarting the
            services. 'kRestartSystemServices' indicates the Cohesity Cluster
            is restarting the system services.
        current_time_msecs (long|int): Specifies the current system time on the
            Cohesity Cluster. This value is specified as a Unix epoch Timestamp
            (in microseconds).
        disk_count_by_tier (list of CountByTier): Specifies the number of disks
            on the cluster by Storage Tier.
        dns_server_ips (list of string): Array of IP Addresses of DNS Servers. 
            Specifies the IP addresses of the DNS Servers used by the Cohesity
            Cluster.
        domain_names (list of string): Array of Domain Names.  The first domain
            name specified in the array is the fully qualified domain name
            assigned to the Cohesity Cluster. Any additional domain names
            specified are used for the domain search list for hostname look-up.
        enable_active_monitoring (bool): Specifies if Cohesity can receive
            monitoring information from the Cohesity Cluster. If 'true', remote
            monitoring of the Cohesity Cluster is allowed.
        enable_patches_download (bool): Specifies whether to enable downloading
            patches from Cohesity download site.
        enable_upgrade_pkg_polling (bool): If 'true', Cohesity's upgrade server
            is polled for new releases.
        encryption_enabled (bool): If 'true', the entire Cohesity Cluster is
            encrypted including all View Boxes.
        encryption_key_rotation_period_secs (long|int): Specifies the period of
            time (in seconds) when encryption keys are rotated. By default, the
            encryption keys are rotated every 77760000 seconds (30 days).
        eula_config (EulaConfig): Specifies the End User License Agreement
            (EULA) acceptance information.
        fault_tolerance_level (FaultToleranceLevelEnum): Specifies the level
            which 'MetadataFaultToleranceFactor' applies to. 'kNode' indicates
            'MetadataFaultToleranceFactor' applies to Node level. 'kChassis'
            indicates 'MetadataFaultToleranceFactor' applies to Chassis level.
            'kRack' indicates 'MetadataFaultToleranceFactor' applies to Rack
            level.
        filer_audit_log_config (FilerAuditLogConfiguration): Filer Audit Log
            Configuration.
        fips_mode_enabled (bool): Specifies if the Cohesity Cluster should
            operate in the FIPS mode, which is compliant with the Federal
            Information Processing Standard 140-2 certification.
        gateway (string): Specifies the gateway IP address.
        google_analytics_enabled (bool): Specifies whether Google Analytics is
            enabled.
        hardware_encryption_enabled (bool): Specifies if hardware
            encryption(SED) is enabled.
        hardware_info (ClusterHardwareInfo): Specifies a hardware type for
            motherboard of the nodes that make up this Cohesity Cluster such as
            S2600WB for Ivy Bridge or S2600TP for Haswell.
        id (long|int): Specifies the unique id of Cohesity Cluster.
        incarnation_id (long|int): Specifies the unique incarnation id of the
            Cohesity Cluster.
        ip_preference (int): IP preference
        is_athena_subnet_clash (bool): Specifies whether or not athena subnet
            is clashing with some other internal subnet
        is_cluster_mfa_enabled (bool): Specifies if MFA is enabled on cluster.
        is_documentation_local (bool): Specifies what version of the
            documentation is used. If 'true', the version of documentation
            stored locally on the Cohesity Cluster is used. If 'false', the
            documentation stored on a Cohesity Web Server is used. The default
            is 'false'. Cohesity recommends accessing the Help from the
            Cohesity Web site which provides the newest and most complete
            version of Help.
        kms_server_id (long|int): Specifies the KMS Server Id. This can only be
            set when the encryption is enabled on cluster.
        language_locale (string): Specifies the language and locale for this
            Cohesity Cluster.
        license_state (LicenseState): Specifies the Licensing State
            information.
        local_auth_domain_name (string): Domain name for SMB local
            authentication.
        local_groups_enabled (bool): Specifies whether to enable local groups
            on cluster. Once it is enabled, it cannot be disabled.
        metadata_fault_tolerance_factor (int): Specifies metadata fault
            tolerance setting for the cluster. This denotes the number of
            simultaneous failures[node] supported by metadata services like
            gandalf and scribe.
        minimum_failure_domains_needed (int): Specifies minimum failure domains
            needed in the cluster.
        multi_tenancy_enabled (bool): Specifies if multi tenancy is enabled in
            the cluster. Authentication & Authorization will always use
            tenant_id, however, some UI elements may be disabled when multi
            tenancy is disabled.
        name (string): Specifies the name of the Cohesity Cluster.
        node_count (long|int): Specifies the number of Nodes in the Cohesity
            Cluster.
        node_ips (string): IP addresses of nodes in the cluster
        ntp_settings (NtpSettingsConfig): Specifies if the ntp/primary
            secondary scheme should be disabled for this cluster.
        patch_version (string): Specifies the patch version applied to cluster.
        pcie_ssd_tier_rebalance_delay_secs (int): Specifies the rebalance delay
            in seconds for cluster PcieSSD storage tier.
        proto_rpc_encryption_enabled (bool): Specifies if protorpc encryption
            is enabled or not.
        proxy_vm_subnet (string): The subnet reserved for ProxyVM
        reverse_tunnel_enabled (bool): If 'true', Cohesity's Remote Tunnel is
            enabled. Cohesity can access the Cluster and provide remote
            assistance via a Remote Tunnel.
        reverse_tunnel_end_time_msecs (long|int): ReverseTunnelEndTimeMsecs
            specifies the end time in milliseconds since epoch until when the
            reverse tunnel will stay enabled.
        schema_info_list (list of SchemaInfo): Specifies the time series schema
            info of the cluster.
        security_mode_dod (bool): Specifies if Security Mode DOD is enabled or
            not.
        smb_ad_disabled (bool): Specifies if Active Directory should be
            disabled for authentication of SMB shares. If 'true', Active
            Directory is disabled.
        smb_multichannel_enabled (bool): Specifies whether SMB multichannel is
            enabled on the cluster. When this is set to true, then any SMB3
            multichannel enabled client can establish multiple TCP connection
            per session to the Server.
        stats (ClusterStats): Specifies statistics about this Cohesity Cluster.
        stig_mode (bool): TODO(mitch) StigMode is deprecated. Should it still
            be in this list??
        supported_config (SupportedConfig): Information about supported
            configuration. For example, it contains minimum number of nodes
            supported for the cluster.
        syslog_servers (list of OldSyslogServer): Syslog servers.
        target_software_version (string): Specifies the Cohesity release that
            this Cluster is being upgraded to if an upgrade operation is in
            progress.
        tenant_viewbox_sharing_enabled (bool): In case multi tenancy is
            enabled, this flag controls whether multiple tenants can be placed
            on the same viewbox. Once set to true, this flag should never
            become false.
        tiering_audit_log_config (TieringAuditLogConfiguration): Tiering Audit
            Log Configuration.
        timezone (string): Specifies the timezone to use for showing time in
            emails, reports, filer audit logs, etc.
        trust_domain (string): Trust Domain.
        turbo_mode (bool): Specifies if the cluster is in Turbo mode.
        use_heimdall (bool): Specifies whether to enable Heimdall which tells
            whether services should use temporary fleet instances to mount
            disks by talking to Heimdall.
        used_metadata_space_pct (float): UsedMetadataSpacePct measures the
            percentage about storage used for metadata over the total storage
            available for metadata
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "amqp_target_config":'amqpTargetConfig',
        "apps_subnet":'appsSubnet',
        "assigned_racks_count":'assignedRacksCount',
        "available_metadata_space":'availableMetadataSpace',
        "banner_enabled":'bannerEnabled',
        "chassis_count":'chassisCount',
        "cluster_audit_log_config":'clusterAuditLogConfig',
        "cluster_size":'clusterSize',
        "cluster_software_version":'clusterSoftwareVersion',
        "cluster_type":'clusterType',
        "created_time_msecs":'createdTimeMsecs',
        "current_op_scheduled_time_secs":'currentOpScheduledTimeSecs',
        "current_operation":'currentOperation',
        "current_time_msecs":'currentTimeMsecs',
        "disk_count_by_tier":'diskCountByTier',
        "dns_server_ips":'dnsServerIps',
        "domain_names":'domainNames',
        "enable_active_monitoring":'enableActiveMonitoring',
        "enable_patches_download":'enablePatchesDownload',
        "enable_upgrade_pkg_polling":'enableUpgradePkgPolling',
        "encryption_enabled":'encryptionEnabled',
        "encryption_key_rotation_period_secs":'encryptionKeyRotationPeriodSecs',
        "eula_config":'eulaConfig',
        "fault_tolerance_level":'faultToleranceLevel',
        "filer_audit_log_config":'filerAuditLogConfig',
        "fips_mode_enabled":'fipsModeEnabled',
        "gateway":'gateway',
        "google_analytics_enabled":'googleAnalyticsEnabled',
        "hardware_encryption_enabled":'hardwareEncryptionEnabled',
        "hardware_info":'hardwareInfo',
        "id":'id',
        "incarnation_id":'incarnationId',
        "ip_preference":'ipPreference',
        "is_athena_subnet_clash":'isAthenaSubnetClash',
        "is_cluster_mfa_enabled":'isClusterMfaEnabled',
        "is_documentation_local":'isDocumentationLocal',
        "kms_server_id":'kmsServerId',
        "language_locale":'languageLocale',
        "license_state":'licenseState',
        "local_auth_domain_name":'localAuthDomainName',
        "local_groups_enabled":'localGroupsEnabled',
        "metadata_fault_tolerance_factor":'metadataFaultToleranceFactor',
        "minimum_failure_domains_needed":'minimumFailureDomainsNeeded',
        "multi_tenancy_enabled":'multiTenancyEnabled',
        "name":'name',
        "node_count":'nodeCount',
        "node_ips":'nodeIps',
        "ntp_settings":'ntpSettings',
        "patch_version":'patchVersion',
        "pcie_ssd_tier_rebalance_delay_secs":'pcieSsdTierRebalanceDelaySecs',
        "proto_rpc_encryption_enabled":'protoRpcEncryptionEnabled',
        "proxy_vm_subnet":'proxyVMSubnet',
        "reverse_tunnel_enabled":'reverseTunnelEnabled',
        "reverse_tunnel_end_time_msecs":'reverseTunnelEndTimeMsecs',
        "schema_info_list":'schemaInfoList',
        "security_mode_dod":'securityModeDod',
        "smb_ad_disabled":'smbAdDisabled',
        "smb_multichannel_enabled":'smbMultichannelEnabled',
        "stats":'stats',
        "stig_mode":'stigMode',
        "supported_config":'supportedConfig',
        "syslog_servers":'syslogServers',
        "target_software_version":'targetSoftwareVersion',
        "tenant_viewbox_sharing_enabled":'tenantViewboxSharingEnabled',
        "tiering_audit_log_config":'tieringAuditLogConfig',
        "timezone":'timezone',
        "trust_domain":'trustDomain',
        "turbo_mode":'turboMode',
        "use_heimdall":'useHeimdall',
        "used_metadata_space_pct":'usedMetadataSpacePct',
    }
    def __init__(self,
                 amqp_target_config=None,
                 apps_subnet=None,
                 assigned_racks_count=None,
                 available_metadata_space=None,
                 banner_enabled=None,
                 chassis_count=None,
                 cluster_audit_log_config=None,
                 cluster_size=None,
                 cluster_software_version=None,
                 cluster_type=None,
                 created_time_msecs=None,
                 current_op_scheduled_time_secs=None,
                 current_operation=None,
                 current_time_msecs=None,
                 disk_count_by_tier=None,
                 dns_server_ips=None,
                 domain_names=None,
                 enable_active_monitoring=None,
                 enable_patches_download=None,
                 enable_upgrade_pkg_polling=None,
                 encryption_enabled=None,
                 encryption_key_rotation_period_secs=None,
                 eula_config=None,
                 fault_tolerance_level=None,
                 filer_audit_log_config=None,
                 fips_mode_enabled=None,
                 gateway=None,
                 google_analytics_enabled=None,
                 hardware_encryption_enabled=None,
                 hardware_info=None,
                 id=None,
                 incarnation_id=None,
                 ip_preference=None,
                 is_athena_subnet_clash=None,
                 is_cluster_mfa_enabled=None,
                 is_documentation_local=None,
                 kms_server_id=None,
                 language_locale=None,
                 license_state=None,
                 local_auth_domain_name=None,
                 local_groups_enabled=None,
                 metadata_fault_tolerance_factor=None,
                 minimum_failure_domains_needed=None,
                 multi_tenancy_enabled=None,
                 name=None,
                 node_count=None,
                 node_ips=None,
                 ntp_settings=None,
                 patch_version=None,
                 pcie_ssd_tier_rebalance_delay_secs=None,
                 proto_rpc_encryption_enabled=None,
                 proxy_vm_subnet=None,
                 reverse_tunnel_enabled=None,
                 reverse_tunnel_end_time_msecs=None,
                 schema_info_list=None,
                 security_mode_dod=None,
                 smb_ad_disabled=None,
                 smb_multichannel_enabled=None,
                 stats=None,
                 stig_mode=None,
                 supported_config=None,
                 syslog_servers=None,
                 target_software_version=None,
                 tenant_viewbox_sharing_enabled=None,
                 tiering_audit_log_config=None,
                 timezone=None,
                 trust_domain=None,
                 turbo_mode=None,
                 use_heimdall=None,
                 used_metadata_space_pct=None,
            ):

        """Constructor for the Cluster class"""

        # Initialize members of the class
        self.amqp_target_config = amqp_target_config
        self.apps_subnet = apps_subnet
        self.assigned_racks_count = assigned_racks_count
        self.available_metadata_space = available_metadata_space
        self.banner_enabled = banner_enabled
        self.chassis_count = chassis_count
        self.cluster_audit_log_config = cluster_audit_log_config
        self.cluster_size = cluster_size
        self.cluster_software_version = cluster_software_version
        self.cluster_type = cluster_type
        self.created_time_msecs = created_time_msecs
        self.current_op_scheduled_time_secs = current_op_scheduled_time_secs
        self.current_operation = current_operation
        self.current_time_msecs = current_time_msecs
        self.disk_count_by_tier = disk_count_by_tier
        self.dns_server_ips = dns_server_ips
        self.domain_names = domain_names
        self.enable_active_monitoring = enable_active_monitoring
        self.enable_patches_download = enable_patches_download
        self.enable_upgrade_pkg_polling = enable_upgrade_pkg_polling
        self.encryption_enabled = encryption_enabled
        self.encryption_key_rotation_period_secs = encryption_key_rotation_period_secs
        self.eula_config = eula_config
        self.fault_tolerance_level = fault_tolerance_level
        self.filer_audit_log_config = filer_audit_log_config
        self.fips_mode_enabled = fips_mode_enabled
        self.gateway = gateway
        self.google_analytics_enabled = google_analytics_enabled
        self.hardware_encryption_enabled = hardware_encryption_enabled
        self.hardware_info = hardware_info
        self.id = id
        self.incarnation_id = incarnation_id
        self.ip_preference = ip_preference
        self.is_athena_subnet_clash = is_athena_subnet_clash
        self.is_cluster_mfa_enabled = is_cluster_mfa_enabled
        self.is_documentation_local = is_documentation_local
        self.kms_server_id = kms_server_id
        self.language_locale = language_locale
        self.license_state = license_state
        self.local_auth_domain_name = local_auth_domain_name
        self.local_groups_enabled = local_groups_enabled
        self.metadata_fault_tolerance_factor = metadata_fault_tolerance_factor
        self.minimum_failure_domains_needed = minimum_failure_domains_needed
        self.multi_tenancy_enabled = multi_tenancy_enabled
        self.name = name
        self.node_count = node_count
        self.node_ips = node_ips
        self.ntp_settings = ntp_settings
        self.patch_version = patch_version
        self.pcie_ssd_tier_rebalance_delay_secs = pcie_ssd_tier_rebalance_delay_secs
        self.proto_rpc_encryption_enabled = proto_rpc_encryption_enabled
        self.proxy_vm_subnet = proxy_vm_subnet
        self.reverse_tunnel_enabled = reverse_tunnel_enabled
        self.reverse_tunnel_end_time_msecs = reverse_tunnel_end_time_msecs
        self.schema_info_list = schema_info_list
        self.security_mode_dod = security_mode_dod
        self.smb_ad_disabled = smb_ad_disabled
        self.smb_multichannel_enabled = smb_multichannel_enabled
        self.stats = stats
        self.stig_mode = stig_mode
        self.supported_config = supported_config
        self.syslog_servers = syslog_servers
        self.target_software_version = target_software_version
        self.tenant_viewbox_sharing_enabled = tenant_viewbox_sharing_enabled
        self.tiering_audit_log_config = tiering_audit_log_config
        self.timezone = timezone
        self.trust_domain = trust_domain
        self.turbo_mode = turbo_mode
        self.use_heimdall = use_heimdall
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
        amqp_target_config = cohesity_management_sdk.models.amqp_target_config.AMQPTargetConfig.from_dictionary(dictionary.get('amqpTargetConfig')) if dictionary.get('amqpTargetConfig') else None
        apps_subnet = cohesity_management_sdk.models.subnet.Subnet.from_dictionary(dictionary.get('appsSubnet')) if dictionary.get('appsSubnet') else None
        assigned_racks_count = dictionary.get('assignedRacksCount')
        available_metadata_space = dictionary.get('availableMetadataSpace')
        banner_enabled = dictionary.get('bannerEnabled')
        chassis_count = dictionary.get('chassisCount')
        cluster_audit_log_config = cohesity_management_sdk.models.cluster_audit_log_configuration.ClusterAuditLogConfiguration.from_dictionary(dictionary.get('clusterAuditLogConfig')) if dictionary.get('clusterAuditLogConfig') else None
        cluster_size = dictionary.get('clusterSize')
        cluster_software_version = dictionary.get('clusterSoftwareVersion')
        cluster_type = dictionary.get('clusterType')
        created_time_msecs = dictionary.get('createdTimeMsecs')
        current_op_scheduled_time_secs = dictionary.get('currentOpScheduledTimeSecs')
        current_operation = dictionary.get('currentOperation')
        current_time_msecs = dictionary.get('currentTimeMsecs')
        disk_count_by_tier = None
        if dictionary.get('diskCountByTier') != None:
            disk_count_by_tier = list()
            for structure in dictionary.get('diskCountByTier'):
                disk_count_by_tier.append(cohesity_management_sdk.models.count_by_tier.CountByTier.from_dictionary(structure))
        dns_server_ips = dictionary.get("dnsServerIps")
        domain_names = dictionary.get("domainNames")
        enable_active_monitoring = dictionary.get('enableActiveMonitoring')
        enable_patches_download = dictionary.get('enablePatchesDownload')
        enable_upgrade_pkg_polling = dictionary.get('enableUpgradePkgPolling')
        encryption_enabled = dictionary.get('encryptionEnabled')
        encryption_key_rotation_period_secs = dictionary.get('encryptionKeyRotationPeriodSecs')
        eula_config = cohesity_management_sdk.models.eula_config.EulaConfig.from_dictionary(dictionary.get('eulaConfig')) if dictionary.get('eulaConfig') else None
        fault_tolerance_level = dictionary.get('faultToleranceLevel')
        filer_audit_log_config = cohesity_management_sdk.models.filer_audit_log_configuration.FilerAuditLogConfiguration.from_dictionary(dictionary.get('filerAuditLogConfig')) if dictionary.get('filerAuditLogConfig') else None
        fips_mode_enabled = dictionary.get('fipsModeEnabled')
        gateway = dictionary.get('gateway')
        google_analytics_enabled = dictionary.get('googleAnalyticsEnabled')
        hardware_encryption_enabled = dictionary.get('hardwareEncryptionEnabled')
        hardware_info = cohesity_management_sdk.models.cluster_hardware_info.ClusterHardwareInfo.from_dictionary(dictionary.get('hardwareInfo')) if dictionary.get('hardwareInfo') else None
        id = dictionary.get('id')
        incarnation_id = dictionary.get('incarnationId')
        ip_preference = dictionary.get('ipPreference')
        is_athena_subnet_clash = dictionary.get('isAthenaSubnetClash')
        is_cluster_mfa_enabled = dictionary.get('isClusterMfaEnabled')
        is_documentation_local = dictionary.get('isDocumentationLocal')
        kms_server_id = dictionary.get('kmsServerId')
        language_locale = dictionary.get('languageLocale')
        license_state = cohesity_management_sdk.models.license_state.LicenseState.from_dictionary(dictionary.get('licenseState')) if dictionary.get('licenseState') else None
        local_auth_domain_name = dictionary.get('localAuthDomainName')
        local_groups_enabled = dictionary.get('localGroupsEnabled')
        metadata_fault_tolerance_factor = dictionary.get('metadataFaultToleranceFactor')
        minimum_failure_domains_needed = dictionary.get('minimumFailureDomainsNeeded')
        multi_tenancy_enabled = dictionary.get('multiTenancyEnabled')
        name = dictionary.get('name')
        node_count = dictionary.get('nodeCount')
        node_ips = dictionary.get('nodeIps')
        ntp_settings = cohesity_management_sdk.models.ntp_settings_config.NtpSettingsConfig.from_dictionary(dictionary.get('ntpSettings')) if dictionary.get('ntpSettings') else None
        patch_version = dictionary.get('patchVersion')
        pcie_ssd_tier_rebalance_delay_secs = dictionary.get('pcieSsdTierRebalanceDelaySecs')
        proto_rpc_encryption_enabled = dictionary.get('protoRpcEncryptionEnabled')
        proxy_vm_subnet = dictionary.get('proxyVMSubnet')
        reverse_tunnel_enabled = dictionary.get('reverseTunnelEnabled')
        reverse_tunnel_end_time_msecs = dictionary.get('reverseTunnelEndTimeMsecs')
        schema_info_list = None
        if dictionary.get('schemaInfoList') != None:
            schema_info_list = list()
            for structure in dictionary.get('schemaInfoList'):
                schema_info_list.append(cohesity_management_sdk.models.schema_info.SchemaInfo.from_dictionary(structure))
        security_mode_dod = dictionary.get('securityModeDod')
        smb_ad_disabled = dictionary.get('smbAdDisabled')
        smb_multichannel_enabled = dictionary.get('smbMultichannelEnabled')
        stats = cohesity_management_sdk.models.cluster_stats.ClusterStats.from_dictionary(dictionary.get('stats')) if dictionary.get('stats') else None
        stig_mode = dictionary.get('stigMode')
        supported_config = cohesity_management_sdk.models.supported_config.SupportedConfig.from_dictionary(dictionary.get('supportedConfig')) if dictionary.get('supportedConfig') else None
        syslog_servers = None
        if dictionary.get('syslogServers') != None:
            syslog_servers = list()
            for structure in dictionary.get('syslogServers'):
                syslog_servers.append(cohesity_management_sdk.models.old_syslog_server.OldSyslogServer.from_dictionary(structure))
        target_software_version = dictionary.get('targetSoftwareVersion')
        tenant_viewbox_sharing_enabled = dictionary.get('tenantViewboxSharingEnabled')
        tiering_audit_log_config = cohesity_management_sdk.models.tiering_audit_log_configuration.TieringAuditLogConfiguration.from_dictionary(dictionary.get('tieringAuditLogConfig')) if dictionary.get('tieringAuditLogConfig') else None
        timezone = dictionary.get('timezone')
        trust_domain = dictionary.get('trustDomain')
        turbo_mode = dictionary.get('turboMode')
        use_heimdall = dictionary.get('useHeimdall')
        used_metadata_space_pct = dictionary.get('usedMetadataSpacePct')

        # Return an object of this model
        return cls(
            amqp_target_config,
            apps_subnet,
            assigned_racks_count,
            available_metadata_space,
            banner_enabled,
            chassis_count,
            cluster_audit_log_config,
            cluster_size,
            cluster_software_version,
            cluster_type,
            created_time_msecs,
            current_op_scheduled_time_secs,
            current_operation,
            current_time_msecs,
            disk_count_by_tier,
            dns_server_ips,
            domain_names,
            enable_active_monitoring,
            enable_patches_download,
            enable_upgrade_pkg_polling,
            encryption_enabled,
            encryption_key_rotation_period_secs,
            eula_config,
            fault_tolerance_level,
            filer_audit_log_config,
            fips_mode_enabled,
            gateway,
            google_analytics_enabled,
            hardware_encryption_enabled,
            hardware_info,
            id,
            incarnation_id,
            ip_preference,
            is_athena_subnet_clash,
            is_cluster_mfa_enabled,
            is_documentation_local,
            kms_server_id,
            language_locale,
            license_state,
            local_auth_domain_name,
            local_groups_enabled,
            metadata_fault_tolerance_factor,
            minimum_failure_domains_needed,
            multi_tenancy_enabled,
            name,
            node_count,
            node_ips,
            ntp_settings,
            patch_version,
            pcie_ssd_tier_rebalance_delay_secs,
            proto_rpc_encryption_enabled,
            proxy_vm_subnet,
            reverse_tunnel_enabled,
            reverse_tunnel_end_time_msecs,
            schema_info_list,
            security_mode_dod,
            smb_ad_disabled,
            smb_multichannel_enabled,
            stats,
            stig_mode,
            supported_config,
            syslog_servers,
            target_software_version,
            tenant_viewbox_sharing_enabled,
            tiering_audit_log_config,
            timezone,
            trust_domain,
            turbo_mode,
            use_heimdall,
            used_metadata_space_pct
)