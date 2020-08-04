# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.aws_credentials
import cohesity_management_sdk.models.azure_credentials
import cohesity_management_sdk.models.gcp_credentials
import cohesity_management_sdk.models.kubernetes_credentials
import cohesity_management_sdk.models.nas_mount_credential_params
import cohesity_management_sdk.models.office_365_credentials
import cohesity_management_sdk.models.ssl_verification
import cohesity_management_sdk.models.throttling_policy_parameters
import cohesity_management_sdk.models.throttling_policy_override
import cohesity_management_sdk.models.exchange_dag_protection_preference
import cohesity_management_sdk.models.vlan_parameters

class UpdateProtectionSourceParameters(object):

    """Implementation of the 'UpdateProtectionSourceParameters' model.

    UpdateProtectionSourceParameters defines a public data definition
    for updating protection source.

    Attributes:
        agent_endpoint (string): Specifies the agent endpoint if it is
            different from the source endpoint.
        aws_credentials (AwsCredentials): Specifies the credentials to
            authenticate with AWS Cloud Platform.
        azure_credentials (AzureCredentials): Specifies the credentials to
            authenticate with Azure Cloud Platform.
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
        gcp_credentials (GcpCredentials): Specifies the credentials to
            authenticate with Google Cloud Platform.
        host_type (HostTypeUpdateProtectionSourceParametersEnum): Specifies
            the optional OS type of the Protection Source (such as kWindows or
            kLinux). overrideDescription: true 'kLinux' indicates the Linux
            operating system. 'kWindows' indicates the Microsoft Windows
            operating system. 'kAix' indicates the IBM AIX operating system.
            'kSolaris' indicates the Oracle Solaris operating system.
            'kSapHana' indicates the Sap Hana database system developed by SAP
            SE. 'kOther' indicates the other types of operating system.
        kubernetes_credentials (KubernetesCredentials): Specifies the
            credentials to authenticate with a Kubernetes Cluster.
        minimum_free_space_gb (long|int): Specifies the minimum space in GB
            after which backup jobs will be canceled due to low space.
        nas_mount_credentials (NasMountCredentialParams): Specifies the server
            credentials to connect to a NetApp server. This field is required
            for mounting SMB volumes on NetApp servers.
        office_365_credentials (Office365Credentials): Specifies the
            credentials to authenticate with Office365 account.
        password (string): Specifies password of the username to access the
            target source.
        source_side_dedup_enabled (bool): This controls whether to use source
            side dedup on the source or not. This is only applicable to
            sources which support source side dedup (e.g., Linux physical
            servers).
        ssl_verification (SslVerification): Specifies information about SSL
            verification when registering certain sources.
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

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "agent_endpoint":'agentEndpoint',
        "aws_credentials":'awsCredentials',
        "azure_credentials":'azureCredentials',
        "endpoint":'endpoint',
        "exchange_dag_protection_preference":'exchangeDagProtectionPreference',
        "force_register":'forceRegister',
        "gcp_credentials":'gcpCredentials',
        "host_type":'hostType',
        "kubernetes_credentials":'kubernetesCredentials',
        "minimum_free_space_gb":'minimumFreeSpaceGB',
        "nas_mount_credentials":'nasMountCredentials',
        "office_365_credentials":'office365Credentials',
        "password":'password',
        "source_side_dedup_enabled":'sourceSideDedupEnabled',
        "ssl_verification":'sslVerification',
        "throttling_policy":'throttlingPolicy',
        "throttling_policy_overrides":'throttlingPolicyOverrides',
        "use_o_auth_for_exchange_online":'useOAuthForExchangeOnline',
        "username":'username',
        "vlan_params":'vlanParams'
    }

    def __init__(self,
                 agent_endpoint=None,
                 aws_credentials=None,
                 azure_credentials=None,
                 endpoint=None,
                 exchange_dag_protection_preference=None,
                 force_register=None,
                 gcp_credentials=None,
                 host_type=None,
                 kubernetes_credentials=None,
                 minimum_free_space_gb=None,
                 nas_mount_credentials=None,
                 office_365_credentials=None,
                 password=None,
                 source_side_dedup_enabled=None,
                 ssl_verification=None,
                 throttling_policy=None,
                 throttling_policy_overrides=None,
                 use_o_auth_for_exchange_online=None,
                 username=None,
                 vlan_params=None):
        """Constructor for the UpdateProtectionSourceParameters class"""

        # Initialize members of the class
        self.agent_endpoint = agent_endpoint
        self.aws_credentials = aws_credentials
        self.azure_credentials = azure_credentials
        self.endpoint = endpoint
        self.exchange_dag_protection_preference = exchange_dag_protection_preference
        self.force_register = force_register
        self.gcp_credentials = gcp_credentials
        self.host_type = host_type
        self.kubernetes_credentials = kubernetes_credentials
        self.minimum_free_space_gb = minimum_free_space_gb
        self.nas_mount_credentials = nas_mount_credentials
        self.office_365_credentials = office_365_credentials
        self.password = password
        self.source_side_dedup_enabled = source_side_dedup_enabled
        self.ssl_verification = ssl_verification
        self.throttling_policy = throttling_policy
        self.throttling_policy_overrides = throttling_policy_overrides
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
        agent_endpoint = dictionary.get('agentEndpoint')
        aws_credentials = cohesity_management_sdk.models.aws_credentials.AwsCredentials.from_dictionary(dictionary.get('awsCredentials')) if dictionary.get('awsCredentials') else None
        azure_credentials = cohesity_management_sdk.models.azure_credentials.AzureCredentials.from_dictionary(dictionary.get('azureCredentials')) if dictionary.get('azureCredentials') else None
        exchange_dag_protection_preference = cohesity_management_sdk.models.exchange_dag_protection_preference.ExchangeDAGProtectionPreference.from_dictionary(dictionary.get('exchangeDagProtectionPreference')) if dictionary.get('exchangeDagProtectionPreference') else None
        endpoint = dictionary.get('endpoint')
        force_register = dictionary.get('forceRegister')
        gcp_credentials = cohesity_management_sdk.models.gcp_credentials.GcpCredentials.from_dictionary(dictionary.get('gcpCredentials')) if dictionary.get('gcpCredentials') else None
        host_type = dictionary.get('hostType')
        kubernetes_credentials = cohesity_management_sdk.models.kubernetes_credentials.KubernetesCredentials.from_dictionary(dictionary.get('kubernetesCredentials')) if dictionary.get('kubernetesCredentials') else None
        minimum_free_space_gb = dictionary.get('minimumFreeSpaceGB')
        nas_mount_credentials = cohesity_management_sdk.models.nas_mount_credential_params.NasMountCredentialParams.from_dictionary(dictionary.get('nasMountCredentials')) if dictionary.get('nasMountCredentials') else None
        office_365_credentials = cohesity_management_sdk.models.office_365_credentials.Office365Credentials.from_dictionary(dictionary.get('office365Credentials')) if dictionary.get('office365Credentials') else None
        password = dictionary.get('password')
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

        # Return an object of this model
        return cls(agent_endpoint,
                   aws_credentials,
                   azure_credentials,
                   endpoint,
                   exchange_dag_protection_preference,
                   force_register,
                   gcp_credentials,
                   host_type,
                   kubernetes_credentials,
                   minimum_free_space_gb,
                   nas_mount_credentials,
                   office_365_credentials,
                   password,
                   source_side_dedup_enabled,
                   ssl_verification,
                   throttling_policy,
                   throttling_policy_overrides,
                   use_o_auth_for_exchange_online,
                   username,
                   vlan_params)


