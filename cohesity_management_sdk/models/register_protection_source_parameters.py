# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.aws_credentials
import cohesity_management_sdk.models.azure_credentials
import cohesity_management_sdk.models.gcp_credentials
import cohesity_management_sdk.models.nas_mount_credential_params
import cohesity_management_sdk.models.office_365_credentials
import cohesity_management_sdk.models.ssl_verification
import cohesity_management_sdk.models.throttling_policy_parameters
import cohesity_management_sdk.models.throttling_policy_override

class RegisterProtectionSourceParameters(object):

    """Implementation of the 'RegisterProtectionSourceParameters' model.

    Specifies the parameters required to register a Protection Source.

    Attributes:
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
            Protection Source environment. 'kAzure' indicates the Microsoft's
            Azure Protection Source environment. 'kNetapp' indicates the
            Netapp Protection Source environment. 'kAgent' indicates the Agent
            Protection Source environment. 'kGenericNas' indicates the
            Genreric Network Attached Storage Protection Source environment.
            'kAcropolis' indicates the Acropolis Protection Source
            environment. 'kPhsicalFiles' indicates the Physical Files
            Protection Source environment. 'kIsilon' indicates the Dell EMC's
            Isilon Protection Source environment. 'kKVM' indicates the KVM
            Protection Source environment. 'kAWS' indicates the AWS Protection
            Source environment. 'kExchange' indicates the Exchange Protection
            Source environment. 'kHyperVVSS' indicates the HyperV VSS
            Protection Source environment. 'kOracle' indicates the Oracle
            Protection Source environment. 'kGCP' indicates the Google Cloud
            Platform Protection Source environment. 'kFlashBlade' indicates
            the Flash Blade Protection Source environment. 'kAWSNative'
            indicates the AWS Native Protection Source environment. 'kVCD'
            indicates the VMware's Virtual cloud Director Protection Source
            environment. 'kO365' indicates the Office 365 Protection Source
            environment. 'kO365Outlook' indicates Office 365 outlook
            Protection Source environment. 'kHyperFlex' indicates the Hyper
            Flex Protection Source environment. 'kGCPNative' indicates the GCP
            Native Protection Source environment. 'kAzureNative' indicates the
            Azure Native Protection Source environment.
        force_register (bool): TODO: type description here.
        gcp_credentials (GcpCredentials): Specifies the credentials to
            authenticate with Google Cloud Platform.
        host_type (HostTypeRegisterProtectionSourceParametersEnum): Specifies
            the optional OS type of the Protection Source (such as kWindows or
            kLinux). overrideDescription: true 'kLinux' indicates the Linux
            operating system. 'kWindows' indicates the Microsoft Windows
            operating system. 'kAix' indicates the IBM AIX operating system.
            'kSolaris' indicates the Oracle Solaris operating system.
        nas_mount_credentials (NasMountCredentialParams): Specifies the server
            credentials to connect to a NetApp server. This field is required
            for mounting SMB volumes on NetApp servers.
        netapp_type (NetappTypeEnum): Specifies the entity type such as
            'kCluster,' if the environment is kNetapp. 'kCluster' indicates a
            Netapp cluster as a protection source. 'kVserver' indicates a
            Netapp vserver in a cluster as a protection source. 'kVolume'
            indicates  a volume in Netapp vserver as a protection source.
        office_365_credentials (Office365Credentials): Specifies the
            credentials to authenticate with Office365 account.
        office_365_type (int): Specifies the entity type such as 'kDomain',
            'kOutlook', 'kMailbox', if the environment is kO365.
        password (string): Specifies password of the username to access the
            target source.
        physical_type (PhysicalTypeEnum): Specifies the entity type such as
            'kPhysicalHost' if the environment is kPhysical.
            overrideDescription: true 'kHost' indicates a single physical
            server. 'kWindowsCluster' indicates a Microsoft Windows cluster.
        pure_type (PureTypeEnum): Specifies the entity type such as
            'kStorageArray' if the environment is kPure. overrideDescription:
            true Examples of Pure Objects include 'kStorageArray' and
            'kVolume'. 'kStorageArray' indicates that entire pure storage
            array is being protected. 'kVolume' indicates that volume within
            the array is being protected.
        source_side_dedup_enabled (bool): This controls whether to use source
            side dedup on the source or not. This is only applicable to
            Protection Sources which support source side dedup (e.g., Linux
            physical servers).
        ssl_verification (SslVerification): Specifies information about SSL
            verification when registering certain sources.
        throttling_policy (ThrottlingPolicyParameters): Specifies the
            throttling policy that should be applied to this Source.
        throttling_policy_overrides (list of ThrottlingPolicyOverride): Array
            of Throttling Policy Overrides for Datastores.  Specifies a list
            of Throttling Policy for datastores that override the common
            throttling policy specified for the registered Protection Source.
            For datastores not in this list, common policy will still apply.
        username (string): Specifies username to access the target source.
        vmware_type (VmwareTypeEnum): Specifies the entity type such as
            'kVCenter' if the environment is kKMware. overrideDescription:
            true Examples of VMware Objects include 'kVCenter', 'kFolder',
            'kDatacenter', 'kResourcePool', 'kDatastore', 'kVirtualMachine',
            etc. 'kVCenter' indicates the vCenter entity in a VMware
            protection source type. 'kFolder indicates the folder entity (of
            any kind) in a VMware protection source type. 'kDatacenter'
            indicates the datacenter entity in a VMware protection source
            type. 'kComputeResource' indicates the physical compute resource
            entity in a VMware protection source type. 'kResourcePool'
            indicates the set of physical resourses within a compute resource
            or cloudcompute resource. 'kDataStore' indicates the datastore
            entity in a VMware protection source type. 'kHostSystem' indicates
            the ESXi host entity in a VMware protection source type.
            'kVirtualMachine' indicates the virtual machine entity in a VMware
            protection source type. 'kVirtualApp' indicates the virtual app
            entity in a VMware protection source type. 'kStandaloneHost'
            indicates the standalone ESXi host entity (not managed by vCenter)
            in a VMware protection source type. 'kStoragePod' indicates the
            storage pod entity in a VMware protection source type. 'kNetwork'
            indicates the standard vSwitch in a VMware protection source type.
            'kDistributedVirtualPortgroup' indicates a distributed vSwitch
            port group in a VMware protection source type. 'kTagCategory'
            indicates a tag category entity in a VMware protection source
            type. 'kTag' indocates a tag entity in a VMware protection source
            type. 'kOpaqueNetwork' indicates a opaque network which is created
            and managed by an entity outside of vSphere. 'kVCloudDirector'
            indicates a vCloud director entity in a VMware protection source
            type. 'kOrganization' indicates an Organization under a vCD in a
            VMware protection source type. 'kVirtualDatacenter' indicates a
            virtual datacenter entity in a VMware protection source type.
            'kCatalog' indocates a VCD catalog entity in a VMware protection
            source type. 'kOrgMetadata' indicates an VCD organization metadata
            in a VMware protection source type. 'kStoragePolicy' indicates a
            storage policy associated with the vApp in a VMware protection
            source type.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "aws_credentials":'awsCredentials',
        "azure_credentials":'azureCredentials',
        "endpoint":'endpoint',
        "environment":'environment',
        "force_register":'forceRegister',
        "gcp_credentials":'gcpCredentials',
        "host_type":'hostType',
        "nas_mount_credentials":'nasMountCredentials',
        "netapp_type":'netappType',
        "office_365_credentials":'office365Credentials',
        "office_365_type":'office365Type',
        "password":'password',
        "physical_type":'physicalType',
        "pure_type":'pureType',
        "source_side_dedup_enabled":'sourceSideDedupEnabled',
        "ssl_verification":'sslVerification',
        "throttling_policy":'throttlingPolicy',
        "throttling_policy_overrides":'throttlingPolicyOverrides',
        "username":'username',
        "vmware_type":'vmwareType'
    }

    def __init__(self,
                 aws_credentials=None,
                 azure_credentials=None,
                 endpoint=None,
                 environment=None,
                 force_register=None,
                 gcp_credentials=None,
                 host_type=None,
                 nas_mount_credentials=None,
                 netapp_type=None,
                 office_365_credentials=None,
                 office_365_type=None,
                 password=None,
                 physical_type=None,
                 pure_type=None,
                 source_side_dedup_enabled=None,
                 ssl_verification=None,
                 throttling_policy=None,
                 throttling_policy_overrides=None,
                 username=None,
                 vmware_type=None):
        """Constructor for the RegisterProtectionSourceParameters class"""

        # Initialize members of the class
        self.aws_credentials = aws_credentials
        self.azure_credentials = azure_credentials
        self.endpoint = endpoint
        self.environment = environment
        self.force_register = force_register
        self.gcp_credentials = gcp_credentials
        self.host_type = host_type
        self.nas_mount_credentials = nas_mount_credentials
        self.netapp_type = netapp_type
        self.office_365_credentials = office_365_credentials
        self.office_365_type = office_365_type
        self.password = password
        self.physical_type = physical_type
        self.pure_type = pure_type
        self.source_side_dedup_enabled = source_side_dedup_enabled
        self.ssl_verification = ssl_verification
        self.throttling_policy = throttling_policy
        self.throttling_policy_overrides = throttling_policy_overrides
        self.username = username
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
        aws_credentials = cohesity_management_sdk.models.aws_credentials.AwsCredentials.from_dictionary(dictionary.get('awsCredentials')) if dictionary.get('awsCredentials') else None
        azure_credentials = cohesity_management_sdk.models.azure_credentials.AzureCredentials.from_dictionary(dictionary.get('azureCredentials')) if dictionary.get('azureCredentials') else None
        endpoint = dictionary.get('endpoint')
        environment = dictionary.get('environment')
        force_register = dictionary.get('forceRegister')
        gcp_credentials = cohesity_management_sdk.models.gcp_credentials.GcpCredentials.from_dictionary(dictionary.get('gcpCredentials')) if dictionary.get('gcpCredentials') else None
        host_type = dictionary.get('hostType')
        nas_mount_credentials = cohesity_management_sdk.models.nas_mount_credential_params.NasMountCredentialParams.from_dictionary(dictionary.get('nasMountCredentials')) if dictionary.get('nasMountCredentials') else None
        netapp_type = dictionary.get('netappType')
        office_365_credentials = cohesity_management_sdk.models.office_365_credentials.Office365Credentials.from_dictionary(dictionary.get('office365Credentials')) if dictionary.get('office365Credentials') else None
        office_365_type = dictionary.get('office365Type')
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
        username = dictionary.get('username')
        vmware_type = dictionary.get('vmwareType')

        # Return an object of this model
        return cls(aws_credentials,
                   azure_credentials,
                   endpoint,
                   environment,
                   force_register,
                   gcp_credentials,
                   host_type,
                   nas_mount_credentials,
                   netapp_type,
                   office_365_credentials,
                   office_365_type,
                   password,
                   physical_type,
                   pure_type,
                   source_side_dedup_enabled,
                   ssl_verification,
                   throttling_policy,
                   throttling_policy_overrides,
                   username,
                   vmware_type)


