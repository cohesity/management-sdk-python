# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.aws_credentials
import cohesity_management_sdk.models.azure_credentials
import cohesity_management_sdk.models.exchange_dag_protection_preference
import cohesity_management_sdk.models.gcp_credentials
import cohesity_management_sdk.models.kubernetes_credentials
import cohesity_management_sdk.models.nas_mount_credential_params
import cohesity_management_sdk.models.office_365_credentials
import cohesity_management_sdk.models.ssl_verification
import cohesity_management_sdk.models.throttling_policy_parameters
import cohesity_management_sdk.models.throttling_policy_override
import cohesity_management_sdk.models.vlan_parameters

class RegisterProtectionSourceParameters(object):

    """Implementation of the 'RegisterProtectionSourceParameters' model.

    Specifies the parameters required to register a Protection Source.

    Attributes:
        acropolis_type (AcropolisTypeEnum): Specifies the entity type if the
            environment is kAcropolis. overrideDescription: true
        agent_endpoint (string): Specifies the agent endpoint if it is
            different from the source endpoint.
        aws_credentials (AwsCredentials): Specifies the credentials to
            authenticate with AWS Cloud Platform.
        azure_credentials (AzureCredentials): Specifies the credentials to
            authenticate with Azure Cloud Platform.
        endpoint (string): Specifies the network endpoint of the Protection
            Source where it is reachable. It could be an URL or hostname or an
            IP address of the Protection Source.
        environment (EnvironmentRegisterProtectionSourceParametersEnum):
            Specifies the environment such as 'kPhysical' or 'kVMware' of the
            Protection Source. overrideDescription: true Supported environment
            types such as 'kView', 'kSQL', 'kVMware', etc. NOTE: 'kPuppeteer'
            refers to Cohesity's Remote Adapter. 'kVMware' indicates the
            VMware Protection Source environment. 'kHyperV' indicates the
            HyperV Protection Source environment. 'kSQL' indicates the SQL
            Protection Source environment. 'kView' indicates the View
            Protection Source environment. 'kPuppeteer' indicates the
            Cohesity's Remote Adapter. 'kPhysical' indicates the physical
            Protection Source environment. 'kPure' indicates the Pure Storage
            Protection Source environment. 'Nimble' indicates the Nimble
            Storage Protection Source environment. 'kAzure' indicates the
            Microsoft's Azure Protection Source environment. 'kNetapp'
            indicates the Netapp Protection Source environment. 'kAgent'
            indicates the Agent Protection Source environment. 'kGenericNas'
            indicates the Generic Network Attached Storage Protection Source
            environment. 'kAcropolis' indicates the Acropolis Protection
            Source environment. 'kPhsicalFiles' indicates the Physical Files
            Protection Source environment. 'kIsilon' indicates the Dell EMC's
            Isilon Protection Source environment. 'kGPFS' indicates IBM's GPFS
            Protection Source environment. 'kKVM' indicates the KVM Protection
            Source environment. 'kAWS' indicates the AWS Protection Source
            environment. 'kExchange' indicates the Exchange Protection Source
            environment. 'kHyperVVSS' indicates the HyperV VSS Protection
            Source environment. 'kOracle' indicates the Oracle Protection
            Source environment. 'kGCP' indicates the Google Cloud Platform
            Protection Source environment. 'kFlashBlade' indicates the Flash
            Blade Protection Source environment. 'kAWSNative' indicates the
            AWS Native Protection Source environment. 'kO365' indicates the
            Office 365 Protection Source environment. 'kO365Outlook'
            indicates Office 365 outlook Protection Source environment.
            'kHyperFlex' indicates the Hyper Flex Protection Source
            environment. 'kGCPNative' indicates the GCP Native Protection
            Source environment. 'kAzureNative' indicates the Azure Native
            Protection Source environment. 'kKubernetes' indicates a
            Kubernetes Protection Source environment. 'kElastifile'
            indicates Elastifile Protection Source environment. 'kAD'
            indicates Active Directory Protection Source environment.
            'kRDSSnapshotManager' indicates AWS RDS Protection Source
            environment.
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
        gcp_credentials (GcpCredentials): Specifies the credentials to
            authenticate with Google Cloud Platform.
        host_type (HostTypeRegisterProtectionSourceParametersEnum): Specifies
            the optional OS type of the Protection Source (such as kWindows or
            kLinux). overrideDescription: true 'kLinux' indicates the Linux
            operating system. 'kWindows' indicates the Microsoft Windows
            operating system. 'kAix' indicates the IBM AIX operating system.
            'kSolaris' indicates the Oracle Solaris operating system.
            'kSapHana' indicates the Sap Hana database system developed by SAP
            SE. 'kOther' indicates the other types of operating system.
        hyperv_type (HypervTypeEnum): Specifies the entity type if the
            environment is kHyperV. overrideDescription: true
        kubernetes_credentials (KubernetesCredentials): Specifies the
            credentials to authenticate with a Kubernetes Cluster.
        kubernetes_type (KubernetesTypeEnum): Specifies the entity type if the
            environment is kKubernetes. overrideDescription: true
        kvm_type (KvmTypeEnum): Specifies the entity type if the environment
            is kKVM. overrideDescription: true
        nas_mount_credentials (NasMountCredentialParams): Specifies the server
            credentials to connect to a NetApp server. This field is required
            for mounting SMB volumes on NetApp servers.
        netapp_type (NetappTypeEnum): Specifies the entity type such as
            'kCluster,' if the environment is kNetapp.
        nimble_type (NimbleTypeEnum): Specifies the entity type such as
            'kStorageArray' if the environment is kNimble.
        office365_credentials_list (list of Office365Credentials): Office365 Source
            Credentials.

            Specifies credentials needed to authenticate & authorize user for
            Office365 using MS Graph APIs.
        office_365_type (Office365TypeEnum): Specifies the entity type such as
            'kDomain', 'kOutlook', 'kMailbox', if the environment is kO365.
        password (string): Specifies password of the username to access the
            target source.
        physical_type (PhysicalTypeEnum): Specifies the entity type such as
            'kPhysicalHost' if the environment is kPhysical.
            overrideDescription: true
        pure_type (PureTypeEnum): Specifies the entity type such as
            'kStorageArray' if the environment is kPure.
        source_side_dedup_enabled (bool): This controls whether to use source
            side dedup on the source or not. This is only applicable to
            sources which support source side dedup (e.g., Linux physical
            servers).
        ssl_verification (SslVerification): SSL verification parameter is
            applicable to VMware environment. It can be populated with the
            server's CA certificate or certificate chain and vCenter's
            certificate will be validated against this.
        throttling_policy (ThrottlingPolicyParameters): Specifies the
            throttling policy that should be applied to this Source.
        throttling_policy_overrides (list of ThrottlingPolicyOverride): Array
            of Throttling Policy Overrides for Datastores.  Specifies a list
            of Throttling Policy for datastores that override the common
            throttling policy specified for the registered Protection Source.
            For datastores not in this list, common policy will still apply.
        use_o_auth_for_exchange_online (bool): Specifies whether OAuth should
            be used for authentication in case of Exchange Online.
        username (string): Specifies username to access the target source.
        vlan_params (VlanParameters): Specifies the VLAN parameters to be used
            while taking the backup of this entity and is the preferred
            selection for restoring the same. For restores, the VLAN
            parameters specifed here can be overridden. Currently, this is
            only applicable for Physical hosts running Oracle.
        vmware_type (VmwareTypeEnum): Specifies the entity type such as
            'kVCenter' if the environment is kVMware.
            overrideDescription: true

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "acropolis_type":'acropolisType',
        "agent_endpoint":'agentEndpoint',
        "aws_credentials":'awsCredentials',
        "azure_credentials":'azureCredentials',
        "endpoint":'endpoint',
        "environment":'environment',
        "exchange_dag_protection_preference":'exchangeDAGProtectionPreference',
        "force_register":'forceRegister',
        "gcp_credentials":'gcpCredentials',
        "host_type":'hostType',
        "hyperv_type":'hyperVType',
        "kubernetes_credentials":'kubernetesCredentials',
        "kubernetes_type":'kubernetesType',
        "kvm_type":'kvmType',
        "nas_mount_credentials":'nasMountCredentials',
        "netapp_type":'netappType',
        "nimble_type":'nimbleType',
        "office365_credentials_list":"office365CredentialsList",
        "office_365_type":'office365Type',
        "password":'password',
        "physical_type":'physicalType',
        "pure_type":'pureType',
        "source_side_dedup_enabled":'sourceSideDedupEnabled',
        "ssl_verification":'sslVerification',
        "throttling_policy":'throttlingPolicy',
        "throttling_policy_overrides":'throttlingPolicyOverrides',
        "use_o_auth_for_exchange_online":'useOAuthForExchangeOnline',
        "username":'username',
        "vlan_params":"vlanParams",
        "vmware_type":'vmwareType'
    }

    def __init__(self,
                 acropolis_type=None,
                 agent_endpoint=None,
                 aws_credentials=None,
                 azure_credentials=None,
                 endpoint=None,
                 environment=None,
                 exchange_dag_protection_preference=None,
                 force_register=None,
                 gcp_credentials=None,
                 host_type=None,
                 hyperv_type=None,
                 kubernetes_credentials=None,
                 kubernetes_type=None,
                 kvm_type=None,
                 nas_mount_credentials=None,
                 netapp_type=None,
                 nimble_type=None,
                 office365_credentials_list=None,
                 office_365_type=None,
                 password=None,
                 physical_type=None,
                 pure_type=None,
                 source_side_dedup_enabled=None,
                 ssl_verification=None,
                 throttling_policy=None,
                 throttling_policy_overrides=None,
                 use_o_auth_for_exchange_online=None,
                 username=None,
                 vlan_params=None,
                 vmware_type=None):
        """Constructor for the RegisterProtectionSourceParameters class"""

        # Initialize members of the class
        self.acropolis_type = acropolis_type
        self.agent_endpoint = agent_endpoint
        self.aws_credentials = aws_credentials
        self.azure_credentials = azure_credentials
        self.endpoint = endpoint
        self.environment = environment
        self.force_register = force_register
        self.exchange_dag_protection_preference = exchange_dag_protection_preference
        self.gcp_credentials = gcp_credentials
        self.host_type = host_type
        self.hyperv_type = hyperv_type
        self.kubernetes_credentials = kubernetes_credentials
        self.kubernetes_type = kubernetes_type
        self.kvm_type = kvm_type
        self.nas_mount_credentials = nas_mount_credentials
        self.netapp_type = netapp_type
        self.nimble_type = nimble_type
        self.office365_credentials_list = office365_credentials_list
        self.office_365_type = office_365_type
        self.password = password
        self.physical_type = physical_type
        self.pure_type = pure_type
        self.source_side_dedup_enabled = source_side_dedup_enabled
        self.ssl_verification = ssl_verification
        self.throttling_policy = throttling_policy
        self.throttling_policy_overrides = throttling_policy_overrides
        self.use_o_auth_for_exchange_online = use_o_auth_for_exchange_online
        self.username = username
        self.vlan_params = vlan_params
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
        acropolis_type = dictionary.get('acropolisType')
        agent_endpoint = dictionary.get('agentEndpoint')
        aws_credentials = cohesity_management_sdk.models.aws_credentials.AwsCredentials.from_dictionary(dictionary.get('awsCredentials')) if dictionary.get('awsCredentials') else None
        azure_credentials = cohesity_management_sdk.models.azure_credentials.AzureCredentials.from_dictionary(dictionary.get('azureCredentials')) if dictionary.get('azureCredentials') else None
        endpoint = dictionary.get('endpoint')
        environment = dictionary.get('environment')
        exchange_dag_protection_preference = cohesity_management_sdk.models.exchange_dag_protection_preference.ExchangeDAGProtectionPreference.from_dictionary(dictionary.get('exchangeDAGProtectionPreference')) if dictionary.get('exchangeDAGProtectionPreference') else None
        force_register = dictionary.get('forceRegister')
        gcp_credentials = cohesity_management_sdk.models.gcp_credentials.GcpCredentials.from_dictionary(dictionary.get('gcpCredentials')) if dictionary.get('gcpCredentials') else None
        host_type = dictionary.get('hostType')
        hyperv_type = dictionary.get('hyperVType')
        kubernetes_credentials = cohesity_management_sdk.models.kubernetes_credentials.KubernetesCredentials.from_dictionary(dictionary.get('kubernetesCredentials')) if dictionary.get('kubernetesCredentials') else None
        kubernetes_type = dictionary.get('kubernetesType')
        kvm_type = dictionary.get('kvmType')
        nas_mount_credentials = cohesity_management_sdk.models.nas_mount_credential_params.NasMountCredentialParams.from_dictionary(dictionary.get('nasMountCredentials')) if dictionary.get('nasMountCredentials') else None
        netapp_type = dictionary.get('netappType')
        nimble_type = dictionary.get('nimbleType')
        office_365_type = dictionary.get('office365Type')
        office365_credentials_list = None
        if dictionary.get('office365CredentialsList') != None:
            office365_credentials_list = list()
            for structure in dictionary.get('office365CredentialsList'):
                office365_credentials_list.append(cohesity_management_sdk.office_365_credentials.Office365Credentials.from_dictionary(structure))
        password = dictionary.get('password')
        physical_type = dictionary.get('physicalType')
        pure_type = dictionary.get('pureType')
        source_side_dedup_enabled = dictionary.get('sourceSideDedupEnabled')
        ssl_verification = cohesity_management_sdk.models.ssl_verification.SslVerification.from_dictionary(dictionary.get('sslVerification')) if dictionary.get('sslVerification') else None
        throttling_policy = cohesity_management_sdk.models.throttling_policy_parameters.ThrottlingPolicyParameters.from_dictionary(dictionary.get('throttlingPolicy')) if dictionary.get('throttlingPolicy') else None
        throttling_policy_overrides = None
        if dictionary.get('throttlingPolicyOverrides') != None:
            throttling_policy_overrides = list()
            for structure in dictionary.get('throttlingPolicyOverrides'):
                throttling_policy_overrides.append(cohesity_management_sdk.models.throttling_policy_override.ThrottlingPolicyOverride.from_dictionary(structure))
        use_o_auth_for_exchange_online = dictionary.get('useOAuthForExchangeOnline')
        username = dictionary.get('username')
        vlan_params = cohesity_management_sdk.models.vlan_parameters.VlanParameters.from_dictionary(dictionary.get('vlanParams')) if dictionary.get('vlanParams') else None
        vmware_type = dictionary.get('vmwareType')

        # Return an object of this model
        return cls(acropolis_type,
                   agent_endpoint,
                   aws_credentials,
                   azure_credentials,
                   endpoint,
                   environment,
                   exchange_dag_protection_preference,
                   force_register,
                   gcp_credentials,
                   host_type,
                   hyperv_type,
                   kubernetes_credentials,
                   kubernetes_type,
                   kvm_type,
                   nas_mount_credentials,
                   netapp_type,
                   nimble_type,
                   office365_credentials_list,
                   office_365_type,
                   password,
                   physical_type,
                   pure_type,
                   source_side_dedup_enabled,
                   ssl_verification,
                   throttling_policy,
                   throttling_policy_overrides,
                   use_o_auth_for_exchange_online,
                   username,
                   vlan_params,
                   vmware_type)


