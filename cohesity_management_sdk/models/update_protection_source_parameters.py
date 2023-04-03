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
import cohesity_management_sdk.models.registered_protection_source_isilon_params
import cohesity_management_sdk.models.ssl_verification
import cohesity_management_sdk.models.subnet
import cohesity_management_sdk.models.throttling_policy_override
import cohesity_management_sdk.models.throttling_policy_parameters
import cohesity_management_sdk.models.vlan_parameters


class UpdateProtectionSourceParameters(object):

    """Implementation of the 'UpdateProtectionSourceParameters' model.

    UpdateProtectionSourceParameters defines a public data definition for
    updating protection source.


    Attributes:

        is_storage_array_snapshot_enabled (bool): Specifies if this source
            entity has enabled storage array snapshot or not.
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
        endpoint (string): Specifies the network endpoint of the Protection
            Source where it is reachable. It could be an URL or hostname or an
            IP address of the Protection Source.
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
        is_proxy_host (bool): Specifies if the physical host has to be
            registered as a proxy host.
        isilon_params (RegisteredProtectionSourceIsilonParams): Specifies the
            registered protection source params for Isilon Source
        kubernetes_credentials (KubernetesCredentials): Specifies the
            credentials needed to authenticate a Kubernetes cluster.
        kubernetes_params (KubernetesParams): Extra parameters needed for
            updating a K8s resource.
        minimum_free_space_gb (long|int): Specifies the minimum space in GB
            after which backup jobs will be canceled due to low space.
        nas_mount_credentials (NasMountCredentialParams): Specifies the server
            credentials to connect to a NetApp server. This field is required
            for mounting SMB volumes on NetApp servers.
        office_365_credentials_list (list of Office365Credentials): Office365
            Source Credentials.  Specifies credentials needed to authenticate &
            authorize user for Office365 using MS Graph APIs.
        office_365_region (string): Specifies the region for Office365.
        office_365_service_account_credentials_list (list of Credentials):
            Office365 Service Account Credentials.  Specifies credentials for
            improving mailbox backup performance for O365.
        password (string): Specifies password of the username to access the
            target source.
        proxy_host_source_id_list (list of long|int): Specifies the list of the
            protection source id of the windows physical host which will be
            used during the protection and recovery of the sites that belong to
            a office365 domain.
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
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "is_storage_array_snapshot_enabled":'IsStorageArraySnapshotEnabled',
        "agent_endpoint":'agentEndpoint',
        "allowed_ip_addresses":'allowedIpAddresses',
        "aws_credentials":'awsCredentials',
        "aws_fleet_params":'awsFleetParams',
        "azure_credentials":'azureCredentials',
        "blacklisted_ip_addresses":'blacklistedIpAddresses',
        "cluster_network_info":'clusterNetworkInfo',
        "denied_ip_addresses":'deniedIpAddresses',
        "endpoint":'endpoint',
        "exchange_dag_protection_preference":'exchangeDagProtectionPreference',
        "force_register":'forceRegister',
        "gcp_credentials":'gcpCredentials',
        "host_type":'hostType',
        "is_proxy_host":'isProxyHost',
        "isilon_params":'isilonParams',
        "kubernetes_credentials":'kubernetesCredentials',
        "kubernetes_params":'kubernetesParams',
        "minimum_free_space_gb":'minimumFreeSpaceGB',
        "nas_mount_credentials":'nasMountCredentials',
        "office_365_credentials_list":'office365CredentialsList',
        "office_365_region":'office365Region',
        "office_365_service_account_credentials_list":'office365ServiceAccountCredentialsList',
        "password":'password',
        "proxy_host_source_id_list":'proxyHostSourceIdList',
        "source_side_dedup_enabled":'sourceSideDedupEnabled',
        "ssl_verification":'sslVerification',
        "subnets":'subnets',
        "throttling_policy":'throttlingPolicy',
        "throttling_policy_overrides":'throttlingPolicyOverrides',
        "use_existing_credentials":'useExistingCredentials',
        "use_o_auth_for_exchange_online":'useOAuthForExchangeOnline',
        "username":'username',
        "vlan_params":'vlanParams',
    }
    def __init__(self,
                 is_storage_array_snapshot_enabled=None,
                 agent_endpoint=None,
                 allowed_ip_addresses=None,
                 aws_credentials=None,
                 aws_fleet_params=None,
                 azure_credentials=None,
                 blacklisted_ip_addresses=None,
                 cluster_network_info=None,
                 denied_ip_addresses=None,
                 endpoint=None,
                 exchange_dag_protection_preference=None,
                 force_register=None,
                 gcp_credentials=None,
                 host_type=None,
                 is_proxy_host=None,
                 isilon_params=None,
                 kubernetes_credentials=None,
                 kubernetes_params=None,
                 minimum_free_space_gb=None,
                 nas_mount_credentials=None,
                 office_365_credentials_list=None,
                 office_365_region=None,
                 office_365_service_account_credentials_list=None,
                 password=None,
                 proxy_host_source_id_list=None,
                 source_side_dedup_enabled=None,
                 ssl_verification=None,
                 subnets=None,
                 throttling_policy=None,
                 throttling_policy_overrides=None,
                 use_existing_credentials=None,
                 use_o_auth_for_exchange_online=None,
                 username=None,
                 vlan_params=None,
            ):

        """Constructor for the UpdateProtectionSourceParameters class"""

        # Initialize members of the class
        self.is_storage_array_snapshot_enabled = is_storage_array_snapshot_enabled
        self.agent_endpoint = agent_endpoint
        self.allowed_ip_addresses = allowed_ip_addresses
        self.aws_credentials = aws_credentials
        self.aws_fleet_params = aws_fleet_params
        self.azure_credentials = azure_credentials
        self.blacklisted_ip_addresses = blacklisted_ip_addresses
        self.cluster_network_info = cluster_network_info
        self.denied_ip_addresses = denied_ip_addresses
        self.endpoint = endpoint
        self.exchange_dag_protection_preference = exchange_dag_protection_preference
        self.force_register = force_register
        self.gcp_credentials = gcp_credentials
        self.host_type = host_type
        self.is_proxy_host = is_proxy_host
        self.isilon_params = isilon_params
        self.kubernetes_credentials = kubernetes_credentials
        self.kubernetes_params = kubernetes_params
        self.minimum_free_space_gb = minimum_free_space_gb
        self.nas_mount_credentials = nas_mount_credentials
        self.office_365_credentials_list = office_365_credentials_list
        self.office_365_region = office_365_region
        self.office_365_service_account_credentials_list = office_365_service_account_credentials_list
        self.password = password
        self.proxy_host_source_id_list = proxy_host_source_id_list
        self.source_side_dedup_enabled = source_side_dedup_enabled
        self.ssl_verification = ssl_verification
        self.subnets = subnets
        self.throttling_policy = throttling_policy
        self.throttling_policy_overrides = throttling_policy_overrides
        self.use_existing_credentials = use_existing_credentials
        self.use_o_auth_for_exchange_online = use_o_auth_for_exchange_online
        self.username = username
        self.vlan_params = vlan_params

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
        agent_endpoint = dictionary.get('agentEndpoint')
        allowed_ip_addresses = dictionary.get("allowedIpAddresses")
        aws_credentials = cohesity_management_sdk.models.aws_credentials.AwsCredentials.from_dictionary(dictionary.get('awsCredentials')) if dictionary.get('awsCredentials') else None
        aws_fleet_params = cohesity_management_sdk.models.aws_fleet_params.AwsFleetParams.from_dictionary(dictionary.get('awsFleetParams')) if dictionary.get('awsFleetParams') else None
        azure_credentials = cohesity_management_sdk.models.azure_credentials.AzureCredentials.from_dictionary(dictionary.get('azureCredentials')) if dictionary.get('azureCredentials') else None
        blacklisted_ip_addresses = dictionary.get("blacklistedIpAddresses")
        cluster_network_info = cohesity_management_sdk.models.fleet_network_params.FleetNetworkParams.from_dictionary(dictionary.get('clusterNetworkInfo')) if dictionary.get('clusterNetworkInfo') else None
        denied_ip_addresses = dictionary.get("deniedIpAddresses")
        endpoint = dictionary.get('endpoint')
        exchange_dag_protection_preference = cohesity_management_sdk.models.exchange_dag_protection_preference.ExchangeDAGProtectionPreference.from_dictionary(dictionary.get('exchangeDagProtectionPreference')) if dictionary.get('exchangeDagProtectionPreference') else None
        force_register = dictionary.get('forceRegister')
        gcp_credentials = cohesity_management_sdk.models.gcp_credentials.GcpCredentials.from_dictionary(dictionary.get('gcpCredentials')) if dictionary.get('gcpCredentials') else None
        host_type = dictionary.get('hostType')
        is_proxy_host = dictionary.get('isProxyHost')
        isilon_params = cohesity_management_sdk.models.registered_protection_source_isilon_params.RegisteredProtectionSourceIsilonParams.from_dictionary(dictionary.get('isilonParams')) if dictionary.get('isilonParams') else None
        kubernetes_credentials = cohesity_management_sdk.models.kubernetes_credentials.KubernetesCredentials.from_dictionary(dictionary.get('kubernetesCredentials')) if dictionary.get('kubernetesCredentials') else None
        kubernetes_params = cohesity_management_sdk.models.kubernetes_params.KubernetesParams.from_dictionary(dictionary.get('kubernetesParams')) if dictionary.get('kubernetesParams') else None
        minimum_free_space_gb = dictionary.get('minimumFreeSpaceGB')
        nas_mount_credentials = cohesity_management_sdk.models.nas_mount_credential_params.NasMountCredentialParams.from_dictionary(dictionary.get('nasMountCredentials')) if dictionary.get('nasMountCredentials') else None
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
        password = dictionary.get('password')
        proxy_host_source_id_list = dictionary.get("proxyHostSourceIdList")
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

        # Return an object of this model
        return cls(
            is_storage_array_snapshot_enabled,
            agent_endpoint,
            allowed_ip_addresses,
            aws_credentials,
            aws_fleet_params,
            azure_credentials,
            blacklisted_ip_addresses,
            cluster_network_info,
            denied_ip_addresses,
            endpoint,
            exchange_dag_protection_preference,
            force_register,
            gcp_credentials,
            host_type,
            is_proxy_host,
            isilon_params,
            kubernetes_credentials,
            kubernetes_params,
            minimum_free_space_gb,
            nas_mount_credentials,
            office_365_credentials_list,
            office_365_region,
            office_365_service_account_credentials_list,
            password,
            proxy_host_source_id_list,
            source_side_dedup_enabled,
            ssl_verification,
            subnets,
            throttling_policy,
            throttling_policy_overrides,
            use_existing_credentials,
            use_o_auth_for_exchange_online,
            username,
            vlan_params
)