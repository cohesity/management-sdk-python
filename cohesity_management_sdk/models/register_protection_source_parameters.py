# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.aws_credentials
import cohesity_management_sdk.models.aws_fleet_params
import cohesity_management_sdk.models.azure_credentials
import cohesity_management_sdk.models.credentials
import cohesity_management_sdk.models.exchange_dag_protection_preference
import cohesity_management_sdk.models.fleet_network_params
import cohesity_management_sdk.models.gcp_credentials
import cohesity_management_sdk.models.kubernetes_credentials
import cohesity_management_sdk.models.kubernetes_params
import cohesity_management_sdk.models.nas_mount_credential_params
import cohesity_management_sdk.models.office_365_credentials
import cohesity_management_sdk.models.physical_params
import cohesity_management_sdk.models.registered_protection_source_isilon_params
import cohesity_management_sdk.models.ssl_verification
import cohesity_management_sdk.models.subnet
import cohesity_management_sdk.models.throttling_policy_override
import cohesity_management_sdk.models.throttling_policy_parameters
import cohesity_management_sdk.models.vlan_parameters
import cohesity_management_sdk.models.vmware_params


class RegisterProtectionSourceParameters(object):

    """Implementation of the 'RegisterProtectionSourceParameters' model.

    Specifies the parameters required to register a Protection Source.


    Attributes:

        is_storage_array_snapshot_enabled (bool): Specifies if this source
            entity has enabled storage array snapshot or not.
        acropolis_type (AcropolisTypeEnum): Specifies the entity type if the
            environment is kAcropolis. overrideDescription: true
        agent_endpoint (string): Specifies the agent endpoint if it is
            different from the source endpoint.
        allowed_ip_addresses (list of string): Specifies the list of IP
            Addresses on the registered source to be exclusively allowed for
            doing any type of IO operations.
        aws_credentials (AwsCredentials): Specifies credentials needed to
            authenticate with AWS Cloud Platform.
        aws_fleet_params (AwsFleetParams): Specifies information related to AWS
            fleets launched for various purposes. This will only be set for
            kIAMUser entity.
        azure_credentials (AzureCredentials): Specifies credentials needed to
            authenticate with Azure Cloud Platform.
        blacklisted_ip_addresses (list of string): This field is deprecated.
            Use DeniedIpAddresses instead. deprecated: true
        cluster_network_info (FleetNetworkParams): Specifies information
            related to cluster. This is only valid for CE clusters. This is
            only populated for kIAMUser entity.
        denied_ip_addresses (list of string): Specifies the list of IP
            Addresses on the registered source to be denied for doing any type
            of IO operations.
        encryption_key (string): If set, user has encrypted the credential with
            'user_ecryption_key'. It is assumed that credentials are first
            encrypted using internal magento key and then encrypted using user
            encryption key.
        endpoint (string): Specifies the network endpoint of the Protection
            Source where it is reachable. It could be an URL or hostname or an
            IP address of the Protection Source.
        environment (EnvironmentRegisterProtectionSourceParametersEnum):
            Specifies the environment such as 'kPhysical' or 'kVMware' of the
            Protection Source. overrideDescription: true Supported environment
            types such as 'kView', 'kSQL', 'kVMware', etc. NOTE: 'kPuppeteer'
            refers to Cohesity's Remote Adapter. 'kVMware' indicates the VMware
            Protection Source environment. 'kHyperV' indicates the HyperV
            Protection Source environment. 'kSQL' indicates the SQL Protection
            Source environment. 'kView' indicates the View Protection Source
            environment. 'kPuppeteer' indicates the Cohesity's Remote Adapter.
            'kPhysical' indicates the physical Protection Source environment.
            'kPure' indicates the Pure Storage Protection Source environment.
            'kNimble' indicates the Nimble Storage Protection Source
            environment. 'kAzure' indicates the Microsoft's Azure Protection
            Source environment. 'kNetapp' indicates the Netapp Protection
            Source environment. 'kAgent' indicates the Agent Protection Source
            environment. 'kGenericNas' indicates the Generic Network Attached
            Storage Protection Source environment. 'kAcropolis' indicates the
            Acropolis Protection Source environment. 'kPhysicalFiles' indicates
            the Physical Files Protection Source environment. 'kIsilon'
            indicates the Dell EMC's Isilon Protection Source environment.
            'kGPFS' indicates IBM's GPFS Protection Source environment. 'kKVM'
            indicates the KVM Protection Source environment. 'kAWS' indicates
            the AWS Protection Source environment. 'kExchange' indicates the
            Exchange Protection Source environment. 'kHyperVVSS' indicates the
            HyperV VSS Protection Source environment. 'kOracle' indicates the
            Oracle Protection Source environment. 'kGCP' indicates the Google
            Cloud Platform Protection Source environment. 'kFlashBlade'
            indicates the Flash Blade Protection Source environment.
            'kAWSNative' indicates the AWS Native Protection Source
            environment. 'kO365' indicates the Office 365 Protection Source
            environment. 'kO365Outlook' indicates Office 365 outlook Protection
            Source environment. 'kHyperFlex' indicates the Hyper Flex
            Protection Source environment. 'kGCPNative' indicates the GCP
            Native Protection Source environment. 'kAzureNative' indicates the
            Azure Native Protection Source environment. 'kKubernetes' indicates
            a Kubernetes Protection Source environment. 'kElastifile' indicates
            Elastifile Protection Source environment. 'kAD' indicates Active
            Directory Protection Source environment. 'kRDSSnapshotManager'
            indicates AWS RDS Protection Source environment. 'kCassandra'
            indicates Cassandra Protection Source environment. 'kMongoDB'
            indicates MongoDB Protection Source environment. 'kCouchbase'
            indicates Couchbase Protection Source environment. 'kHdfs'
            indicates Hdfs Protection Source environment. 'kHive' indicates
            Hive Protection Source environment. 'kHBase' indicates HBase
            Protection Source environment. 'kUDA' indicates Universal Data
            Adapter Protection Source environment. 'kO365Teams' indicates the
            Office365 Teams Protection Source environment. 'kO365Group'
            indicates the Office365 Groups Protection Source environment.
            'kO365Exchange' indicates the Office365 Mailbox Protection Source
            environment. 'kO365OneDrive' indicates the Office365 OneDrive
            Protection Source environment. 'kO365Sharepoint' indicates the
            Office365 SharePoint Protection Source environment.
            'kO365PublicFolders' indicates the Office365 PublicFolders
            Protection Source environment.
        exchange_dag_protection_preference (ExchangeDAGProtectionPreference):
            Specifies information about the preference order while choosing
            between which database copy of the exchange database which is part
            of DAG should be protected.
        force_register (bool): ForceRegister is applicable to Physical
            Environment. By default, the agent running on a physical host will
            fail the registration, if it is already registered as part of
            another cluster. By setting this option to true, agent can be
            forced to register with the current cluster. This is a hidden
            parameter and should not be documented externally.
        gcp_credentials (GcpCredentials): Specifies credentials needed to
            authenticate with Google Cloud Platform.
        host_type (HostTypeEnum): Specifies the optional OS type of the
            Protection Source (such as kWindows or kLinux).
            overrideDescription: true 'kLinux' indicates the Linux operating
            system. 'kWindows' indicates the Microsoft Windows operating
            system. 'kAix' indicates the IBM AIX operating system. 'kSolaris'
            indicates the Oracle Solaris operating system. 'kSapHana' indicates
            the Sap Hana database system developed by SAP SE. 'kSapOracle'
            indicates the Sap Oracle database system developed by SAP SE.
            'kCockroachDB' indicates the CockroachDB database system. 'kMySQL'
            indicates the MySQL database system. 'kOther' indicates the other
            types of operating system.
        hyperv_type (HyperVTypeEnum): Specifies the entity type if the
            environment is kHyperV. overrideDescription: true
        is_internal_encrypted (bool): Set to true if credentials are encrypted
            by internal magneto key.
        is_proxy_host (bool): Specifies if the physical host has to be
            registered as a proxy host.
        isilon_params (RegisteredProtectionSourceIsilonParams): Specifies the
            registered protection source params for Isilon Source
        kubernetes_credentials (KubernetesCredentials): Specifies the
            credentials needed to authenticate a Kubernetes cluster.
        kubernetes_params (KubernetesParams): Extra parameters needed for
            registering a K8s resource.
        kubernetes_type (KubernetesTypeEnum): Specifies the entity type if the
            environment is kKubernetes. overrideDescription: true
        kvm_type (KvmTypeEnum): Specifies the entity type if the environment is
            kKVM. overrideDescription: true
        nas_mount_credentials (NasMountCredentialParams): Specifies the server
            credentials to connect to a NetApp server. This field is required
            for mounting SMB volumes on NetApp servers.
        netapp_type (NetappTypeEnum): Specifies the entity type such as
            'kCluster,' if the environment is kNetapp.
        nimble_type (NimbleTypeEnum): Specifies the entity type such as
            'kStorageArray' if the environment is kNimble. overrideDescription:
            true
        office_365_credentials_list (list of Office365Credentials): Office365
            Source Credentials.  Specifies credentials needed to authenticate &
            authorize user for Office365 using MS Graph APIs.
        office_365_region (string): Specifies the region for Office365.
        office_365_service_account_credentials_list (list of Credentials):
            Office365 Service Account Credentials.  Specifies credentials for
            improving mailbox backup performance for O365.
        office_365_type (Office365TypeEnum): Specifies the entity type such as
            'kDomain', 'kOutlook', 'kMailbox', if the environment is kO365.
        password (string): Specifies password of the username to access the
            target source.
        physical_params (PhysicalParams): Contains all params specified by the
            user while registering a physical entity.
        physical_type (PhysicalTypeEnum): Specifies the entity type such as
            'kPhysicalHost' if the environment is kPhysical.
            overrideDescription: true
        proxy_host_source_id_list (list of long|int): Specifies the list of the
            protection source id of the windows physical host which will be
            used during the protection and recovery of the sites that belong to
            a office365 domain.
        pure_type (PureTypeEnum): Specifies the entity type such as
            'kStorageArray' if the environment is kPure. overrideDescription:
            true
        source_side_dedup_enabled (bool): This controls whether to use source
            side dedup on the source or not. This is only applicable to sources
            which support source side dedup (e.g., Linux physical servers).
        ssl_verification (SslVerification): SSL verification parameter is
            applicable to VMware environment. It can be populated with the
            server's CA certificate or certificate chain and vCenter's
            certificate will be validated against this.
        subnets (list of Subnet): Specifies the list of subnet IP addresses and
            CIDR prefix for enabeling network data transfer. Currently, only
            Subnet IP and NetbaskBits are valid input fields. All other fields
            provided as input will be ignored.
        throttling_policy (ThrottlingPolicyParameters): Specifies the
            throttling policy that should be applied to this Source.
        throttling_policy_overrides (list of ThrottlingPolicyOverride): Array
            of Throttling Policy Overrides for Datastores.  Specifies a list of
            Throttling Policy for datastores that override the common
            throttling policy specified for the registered Protection Source.
            For datastores not in this list, common policy will still apply.
        use_existing_credentials (bool): Specifies whether to use existing
            Office365 credentials like password and client secret for app id's.
        use_o_auth_for_exchange_online (bool): Specifies whether OAuth should
            be used for authentication in case of Exchange Online.
        username (string): Specifies username to access the target source.
        vlan_params (VlanParameters): Specifies the VLAN parameters to be used
            while taking the backup of this entity and is the preferred
            selection for restoring the same. For restores, the VLAN parameters
            specifed here can be overridden. Currently, this is only applicable
            for Physical hosts running Oracle.
        vmware_params (VmwareParams): Contains all params specified by the user
            while registering a Vmware entity.
        vmware_type (VMwareTypeEnum): Specifies the entity type such as
            'kVCenter' if the environment is kKMware. overrideDescription: true
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "is_storage_array_snapshot_enabled":'IsStorageArraySnapshotEnabled',
        "acropolis_type":'acropolisType',
        "agent_endpoint":'agentEndpoint',
        "allowed_ip_addresses":'allowedIpAddresses',
        "aws_credentials":'awsCredentials',
        "aws_fleet_params":'awsFleetParams',
        "azure_credentials":'azureCredentials',
        "blacklisted_ip_addresses":'blacklistedIpAddresses',
        "cluster_network_info":'clusterNetworkInfo',
        "denied_ip_addresses":'deniedIpAddresses',
        "encryption_key":'encryptionKey',
        "endpoint":'endpoint',
        "environment":'environment',
        "exchange_dag_protection_preference":'exchangeDagProtectionPreference',
        "force_register":'forceRegister',
        "gcp_credentials":'gcpCredentials',
        "host_type":'hostType',
        "hyperv_type":'hyperVType',
        "is_internal_encrypted":'isInternalEncrypted',
        "is_proxy_host":'isProxyHost',
        "isilon_params":'isilonParams',
        "kubernetes_credentials":'kubernetesCredentials',
        "kubernetes_params":'kubernetesParams',
        "kubernetes_type":'kubernetesType',
        "kvm_type":'kvmType',
        "nas_mount_credentials":'nasMountCredentials',
        "netapp_type":'netappType',
        "nimble_type":'nimbleType',
        "office_365_credentials_list":'office365CredentialsList',
        "office_365_region":'office365Region',
        "office_365_service_account_credentials_list":'office365ServiceAccountCredentialsList',
        "office_365_type":'office365Type',
        "password":'password',
        "physical_params":'physicalParams',
        "physical_type":'physicalType',
        "proxy_host_source_id_list":'proxyHostSourceIdList',
        "pure_type":'pureType',
        "source_side_dedup_enabled":'sourceSideDedupEnabled',
        "ssl_verification":'sslVerification',
        "subnets":'subnets',
        "throttling_policy":'throttlingPolicy',
        "throttling_policy_overrides":'throttlingPolicyOverrides',
        "use_existing_credentials":'useExistingCredentials',
        "use_o_auth_for_exchange_online":'useOAuthForExchangeOnline',
        "username":'username',
        "vlan_params":'vlanParams',
        "vmware_params":'vmwareParams',
        "vmware_type":'vmwareType',
    }
    def __init__(self,
                 is_storage_array_snapshot_enabled=None,
                 acropolis_type=None,
                 agent_endpoint=None,
                 allowed_ip_addresses=None,
                 aws_credentials=None,
                 aws_fleet_params=None,
                 azure_credentials=None,
                 blacklisted_ip_addresses=None,
                 cluster_network_info=None,
                 denied_ip_addresses=None,
                 encryption_key=None,
                 endpoint=None,
                 environment=None,
                 exchange_dag_protection_preference=None,
                 force_register=None,
                 gcp_credentials=None,
                 host_type=None,
                 hyperv_type=None,
                 is_internal_encrypted=None,
                 is_proxy_host=None,
                 isilon_params=None,
                 kubernetes_credentials=None,
                 kubernetes_params=None,
                 kubernetes_type=None,
                 kvm_type=None,
                 nas_mount_credentials=None,
                 netapp_type=None,
                 nimble_type=None,
                 office_365_credentials_list=None,
                 office_365_region=None,
                 office_365_service_account_credentials_list=None,
                 office_365_type=None,
                 password=None,
                 physical_params=None,
                 physical_type=None,
                 proxy_host_source_id_list=None,
                 pure_type=None,
                 source_side_dedup_enabled=None,
                 ssl_verification=None,
                 subnets=None,
                 throttling_policy=None,
                 throttling_policy_overrides=None,
                 use_existing_credentials=None,
                 use_o_auth_for_exchange_online=None,
                 username=None,
                 vlan_params=None,
                 vmware_params=None,
                 vmware_type=None,
            ):

        """Constructor for the RegisterProtectionSourceParameters class"""

        # Initialize members of the class
        self.is_storage_array_snapshot_enabled = is_storage_array_snapshot_enabled
        self.acropolis_type = acropolis_type
        self.agent_endpoint = agent_endpoint
        self.allowed_ip_addresses = allowed_ip_addresses
        self.aws_credentials = aws_credentials
        self.aws_fleet_params = aws_fleet_params
        self.azure_credentials = azure_credentials
        self.blacklisted_ip_addresses = blacklisted_ip_addresses
        self.cluster_network_info = cluster_network_info
        self.denied_ip_addresses = denied_ip_addresses
        self.encryption_key = encryption_key
        self.endpoint = endpoint
        self.environment = environment
        self.exchange_dag_protection_preference = exchange_dag_protection_preference
        self.force_register = force_register
        self.gcp_credentials = gcp_credentials
        self.host_type = host_type
        self.hyperv_type = hyperv_type
        self.is_internal_encrypted = is_internal_encrypted
        self.is_proxy_host = is_proxy_host
        self.isilon_params = isilon_params
        self.kubernetes_credentials = kubernetes_credentials
        self.kubernetes_params = kubernetes_params
        self.kubernetes_type = kubernetes_type
        self.kvm_type = kvm_type
        self.nas_mount_credentials = nas_mount_credentials
        self.netapp_type = netapp_type
        self.nimble_type = nimble_type
        self.office_365_credentials_list = office_365_credentials_list
        self.office_365_region = office_365_region
        self.office_365_service_account_credentials_list = office_365_service_account_credentials_list
        self.office_365_type = office_365_type
        self.password = password
        self.physical_params = physical_params
        self.physical_type = physical_type
        self.proxy_host_source_id_list = proxy_host_source_id_list
        self.pure_type = pure_type
        self.source_side_dedup_enabled = source_side_dedup_enabled
        self.ssl_verification = ssl_verification
        self.subnets = subnets
        self.throttling_policy = throttling_policy
        self.throttling_policy_overrides = throttling_policy_overrides
        self.use_existing_credentials = use_existing_credentials
        self.use_o_auth_for_exchange_online = use_o_auth_for_exchange_online
        self.username = username
        self.vlan_params = vlan_params
        self.vmware_params = vmware_params
        self.vmware_type = vmware_type

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
        is_storage_array_snapshot_enabled = dictionary.get('IsStorageArraySnapshotEnabled')
        acropolis_type = dictionary.get('acropolisType')
        agent_endpoint = dictionary.get('agentEndpoint')
        allowed_ip_addresses = dictionary.get("allowedIpAddresses")
        aws_credentials = cohesity_management_sdk.models.aws_credentials.AwsCredentials.from_dictionary(dictionary.get('awsCredentials')) if dictionary.get('awsCredentials') else None
        aws_fleet_params = cohesity_management_sdk.models.aws_fleet_params.AwsFleetParams.from_dictionary(dictionary.get('awsFleetParams')) if dictionary.get('awsFleetParams') else None
        azure_credentials = cohesity_management_sdk.models.azure_credentials.AzureCredentials.from_dictionary(dictionary.get('azureCredentials')) if dictionary.get('azureCredentials') else None
        blacklisted_ip_addresses = dictionary.get("blacklistedIpAddresses")
        cluster_network_info = cohesity_management_sdk.models.fleet_network_params.FleetNetworkParams.from_dictionary(dictionary.get('clusterNetworkInfo')) if dictionary.get('clusterNetworkInfo') else None
        denied_ip_addresses = dictionary.get("deniedIpAddresses")
        encryption_key = dictionary.get('encryptionKey')
        endpoint = dictionary.get('endpoint')
        environment = dictionary.get('environment')
        exchange_dag_protection_preference = cohesity_management_sdk.models.exchange_dag_protection_preference.ExchangeDAGProtectionPreference.from_dictionary(dictionary.get('exchangeDagProtectionPreference')) if dictionary.get('exchangeDagProtectionPreference') else None
        force_register = dictionary.get('forceRegister')
        gcp_credentials = cohesity_management_sdk.models.gcp_credentials.GcpCredentials.from_dictionary(dictionary.get('gcpCredentials')) if dictionary.get('gcpCredentials') else None
        host_type = dictionary.get('hostType')
        hyperv_type = dictionary.get('hyperVType')
        is_internal_encrypted = dictionary.get('isInternalEncrypted')
        is_proxy_host = dictionary.get('isProxyHost')
        isilon_params = cohesity_management_sdk.models.registered_protection_source_isilon_params.RegisteredProtectionSourceIsilonParams.from_dictionary(dictionary.get('isilonParams')) if dictionary.get('isilonParams') else None
        kubernetes_credentials = cohesity_management_sdk.models.kubernetes_credentials.KubernetesCredentials.from_dictionary(dictionary.get('kubernetesCredentials')) if dictionary.get('kubernetesCredentials') else None
        kubernetes_params = cohesity_management_sdk.models.kubernetes_params.KubernetesParams.from_dictionary(dictionary.get('kubernetesParams')) if dictionary.get('kubernetesParams') else None
        kubernetes_type = dictionary.get('kubernetesType')
        kvm_type = dictionary.get('kvmType')
        nas_mount_credentials = cohesity_management_sdk.models.nas_mount_credential_params.NasMountCredentialParams.from_dictionary(dictionary.get('nasMountCredentials')) if dictionary.get('nasMountCredentials') else None
        netapp_type = dictionary.get('netappType')
        nimble_type = dictionary.get('nimbleType')
        office_365_credentials_list = None
        if dictionary.get('office365CredentialsList') != None:
            office_365_credentials_list = list()
            for structure in dictionary.get('office365CredentialsList'):
                office_365_credentials_list.append(cohesity_management_sdk.models.office_365_credentials.Office365Credentials.from_dictionary(structure))
        office_365_region = dictionary.get('office365Region')
        office_365_service_account_credentials_list = None
        if dictionary.get('office365ServiceAccountCredentialsList') != None:
            office_365_service_account_credentials_list = list()
            for structure in dictionary.get('office365ServiceAccountCredentialsList'):
                office_365_service_account_credentials_list.append(cohesity_management_sdk.models.credentials.Credentials.from_dictionary(structure))
        office_365_type = dictionary.get('office365Type')
        password = dictionary.get('password')
        physical_params = cohesity_management_sdk.models.physical_params.PhysicalParams.from_dictionary(dictionary.get('physicalParams')) if dictionary.get('physicalParams') else None
        physical_type = dictionary.get('physicalType')
        proxy_host_source_id_list = dictionary.get("proxyHostSourceIdList")
        pure_type = dictionary.get('pureType')
        source_side_dedup_enabled = dictionary.get('sourceSideDedupEnabled')
        ssl_verification = cohesity_management_sdk.models.ssl_verification.SslVerification.from_dictionary(dictionary.get('sslVerification')) if dictionary.get('sslVerification') else None
        subnets = None
        if dictionary.get('subnets') != None:
            subnets = list()
            for structure in dictionary.get('subnets'):
                subnets.append(cohesity_management_sdk.models.subnet.Subnet.from_dictionary(structure))
        throttling_policy = cohesity_management_sdk.models.throttling_policy_parameters.ThrottlingPolicyParameters.from_dictionary(dictionary.get('throttlingPolicy')) if dictionary.get('throttlingPolicy') else None
        throttling_policy_overrides = None
        if dictionary.get('throttlingPolicyOverrides') != None:
            throttling_policy_overrides = list()
            for structure in dictionary.get('throttlingPolicyOverrides'):
                throttling_policy_overrides.append(cohesity_management_sdk.models.throttling_policy_override.ThrottlingPolicyOverride.from_dictionary(structure))
        use_existing_credentials = dictionary.get('useExistingCredentials')
        use_o_auth_for_exchange_online = dictionary.get('useOAuthForExchangeOnline')
        username = dictionary.get('username')
        vlan_params = cohesity_management_sdk.models.vlan_parameters.VlanParameters.from_dictionary(dictionary.get('vlanParams')) if dictionary.get('vlanParams') else None
        vmware_params = cohesity_management_sdk.models.vmware_params.VmwareParams.from_dictionary(dictionary.get('vmwareParams')) if dictionary.get('vmwareParams') else None
        vmware_type = dictionary.get('vmwareType')

        # Return an object of this model
        return cls(
            is_storage_array_snapshot_enabled,
            acropolis_type,
            agent_endpoint,
            allowed_ip_addresses,
            aws_credentials,
            aws_fleet_params,
            azure_credentials,
            blacklisted_ip_addresses,
            cluster_network_info,
            denied_ip_addresses,
            encryption_key,
            endpoint,
            environment,
            exchange_dag_protection_preference,
            force_register,
            gcp_credentials,
            host_type,
            hyperv_type,
            is_internal_encrypted,
            is_proxy_host,
            isilon_params,
            kubernetes_credentials,
            kubernetes_params,
            kubernetes_type,
            kvm_type,
            nas_mount_credentials,
            netapp_type,
            nimble_type,
            office_365_credentials_list,
            office_365_region,
            office_365_service_account_credentials_list,
            office_365_type,
            password,
            physical_params,
            physical_type,
            proxy_host_source_id_list,
            pure_type,
            source_side_dedup_enabled,
            ssl_verification,
            subnets,
            throttling_policy,
            throttling_policy_overrides,
            use_existing_credentials,
            use_o_auth_for_exchange_online,
            username,
            vlan_params,
            vmware_params,
            vmware_type
)