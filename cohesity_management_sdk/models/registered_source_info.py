# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.connector_parameters
import cohesity_management_sdk.models.nas_mount_credential_params
import cohesity_management_sdk.models.throttling_policy_parameters
import cohesity_management_sdk.models.throttling_policy_override

class RegisteredSourceInfo(object):

    """Implementation of the 'RegisteredSourceInfo' model.

    Specifies information about a registered Source.

    Attributes:
        access_info (ConnectorParameters): Specifies the parameters required
            to establish a connection with a particular environment.
        authentication_error_message (string): Specifies an authentication
            error message. This indicates the given credentials are rejected
            and the registration of the source is not successful.
        authentication_status (AuthenticationStatusEnum): Specifies the status
            of the authenticating to the Protection Source when registering it
            with Cohesity Cluster. If the status is 'kFinished' and there is
            no error, registration is successful. Specifies the status of the
            authentication during the registration of a Protection Source.
            'kPending' indicates the authentication is in progress.
            'kScheduled' indicates the authentication is scheduled.
            'kFinished' indicates the authentication is completed.
            'kRefreshInProgress' indicates the refresh is in progres.
        environments (list of EnvironmentRegisteredSourceInfoEnum): Specifies
            a list of applications environment that are registered with this
            Protection Source such as 'kSQL'. Supported environment types such
            as 'kView', 'kSQL', 'kVMware', etc. NOTE: 'kPuppeteer' refers to
            Cohesity's Remote Adapter. 'kVMware' indicates the VMware
            Protection Source environment. 'kHyperV' indicates the HyperV
            Protection Source environment. 'kSQL' indicates the SQL Protection
            Source environment. 'kView' indicates the View Protection Source
            environment. 'kPuppeteer' indicates the Cohesity's Remote Adapter.
            'kPhysical' indicates the physical Protection Source environment.
            'kPure' indicates the Pure Storage Protection Source environment.
            'kAzure' indicates the Microsoft's Azure Protection Source
            environment. 'kNetapp' indicates the Netapp Protection Source
            environment. 'kAgent' indicates the Agent Protection Source
            environment. 'kGenericNas' indicates the Genreric Network Attached
            Storage Protection Source environment. 'kAcropolis' indicates the
            Acropolis Protection Source environment. 'kPhsicalFiles' indicates
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
            environment. 'kVCD' indicates the VMware's Virtual cloud Director
            Protection Source environment. 'kO365' indicates the Office 365
            Protection Source environment. 'kO365Outlook' indicates Office 365
            outlook Protection Source environment. 'kHyperFlex' indicates the
            Hyper Flex Protection Source environment. 'kGCPNative' indicates
            the GCP Native Protection Source environment. 'kAzureNative'
            indicates the Azure Native Protection Source environment.
            'kKubernetes' indicates a Kubernetes Protection Source
            environment.
        is_db_authenticated (bool): Specifies if application entity
            dbAuthenticated or not. ex: oracle database.
        minimum_free_space_gb (long|int): Specifies the minimum free space in
            GiB of the space expected to be available on the datastore where
            the virtual disks of the VM being backed up. If the amount of free
            space(in GiB) is lower than the value given by this field, backup
            will be aborted. Note that this field is applicable only to
            'kVMware' type of environments.
        nas_mount_credentials (NasMountCredentialParams): Specifies the
            credentials required to mount directories on the NetApp server if
            given.
        password (string): Specifies password of the username to access the
            target source.
        refresh_error_message (string): Specifies a message if there was any
            error encountered during the last rebuild of the Protection Source
            tree. If there was no error during the last rebuild, this field is
            reset.
        refresh_time_usecs (long|int): Specifies the Unix epoch time (in
            microseconds) when the Protection Source tree was most recently
            fetched and built.
        registration_time_usecs (long|int): Specifies the Unix epoch time (in
            microseconds) when the Protection Source was registered.
        throttling_policy (ThrottlingPolicyParameters): Specifies the
            throttling policy for a registered Protection Source.
        throttling_policy_overrides (list of ThrottlingPolicyOverride): Array
            of Throttling Policy Overrides for Datastores.  Specifies a list
            of Throttling Policy for datastores that override the common
            throttling policy specified for the registered Protection Source.
            For datastores not in this list, common policy will still apply.
        use_vm_bios_uuid (bool): Specifies if registered vCenter is using BIOS
            UUID to track virtual machines.
        username (string): Specifies username to access the target source.
        warning_messages (list of string): Specifies a list of warnings
            encountered during registration. Though the registration may
            succeed, warning messages imply the host environment requires some
            cleanup or fixing.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "access_info":'accessInfo',
        "authentication_error_message":'authenticationErrorMessage',
        "authentication_status":'authenticationStatus',
        "environments":'environments',
        "is_db_authenticated":'isDbAuthenticated',
        "minimum_free_space_gb":'minimumFreeSpaceGB',
        "nas_mount_credentials":'nasMountCredentials',
        "password":'password',
        "refresh_error_message":'refreshErrorMessage',
        "refresh_time_usecs":'refreshTimeUsecs',
        "registration_time_usecs":'registrationTimeUsecs',
        "throttling_policy":'throttlingPolicy',
        "throttling_policy_overrides":'throttlingPolicyOverrides',
        "use_vm_bios_uuid":'useVmBiosUuid',
        "username":'username',
        "warning_messages":'warningMessages'
    }

    def __init__(self,
                 access_info=None,
                 authentication_error_message=None,
                 authentication_status=None,
                 environments=None,
                 is_db_authenticated=None,
                 minimum_free_space_gb=None,
                 nas_mount_credentials=None,
                 password=None,
                 refresh_error_message=None,
                 refresh_time_usecs=None,
                 registration_time_usecs=None,
                 throttling_policy=None,
                 throttling_policy_overrides=None,
                 use_vm_bios_uuid=None,
                 username=None,
                 warning_messages=None):
        """Constructor for the RegisteredSourceInfo class"""

        # Initialize members of the class
        self.access_info = access_info
        self.authentication_error_message = authentication_error_message
        self.authentication_status = authentication_status
        self.environments = environments
        self.is_db_authenticated = is_db_authenticated
        self.minimum_free_space_gb = minimum_free_space_gb
        self.nas_mount_credentials = nas_mount_credentials
        self.password = password
        self.refresh_error_message = refresh_error_message
        self.refresh_time_usecs = refresh_time_usecs
        self.registration_time_usecs = registration_time_usecs
        self.throttling_policy = throttling_policy
        self.throttling_policy_overrides = throttling_policy_overrides
        self.use_vm_bios_uuid = use_vm_bios_uuid
        self.username = username
        self.warning_messages = warning_messages


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
        access_info = cohesity_management_sdk.models.connector_parameters.ConnectorParameters.from_dictionary(dictionary.get('accessInfo')) if dictionary.get('accessInfo') else None
        authentication_error_message = dictionary.get('authenticationErrorMessage')
        authentication_status = dictionary.get('authenticationStatus')
        environments = dictionary.get('environments')
        is_db_authenticated = dictionary.get('isDbAuthenticated')
        minimum_free_space_gb = dictionary.get('minimumFreeSpaceGB')
        nas_mount_credentials = cohesity_management_sdk.models.nas_mount_credential_params.NasMountCredentialParams.from_dictionary(dictionary.get('nasMountCredentials')) if dictionary.get('nasMountCredentials') else None
        password = dictionary.get('password')
        refresh_error_message = dictionary.get('refreshErrorMessage')
        refresh_time_usecs = dictionary.get('refreshTimeUsecs')
        registration_time_usecs = dictionary.get('registrationTimeUsecs')
        throttling_policy = cohesity_management_sdk.models.throttling_policy_parameters.ThrottlingPolicyParameters.from_dictionary(dictionary.get('throttlingPolicy')) if dictionary.get('throttlingPolicy') else None
        throttling_policy_overrides = None
        if dictionary.get('throttlingPolicyOverrides') != None:
            throttling_policy_overrides = list()
            for structure in dictionary.get('throttlingPolicyOverrides'):
                throttling_policy_overrides.append(cohesity_management_sdk.models.throttling_policy_override.ThrottlingPolicyOverride.from_dictionary(structure))
        use_vm_bios_uuid = dictionary.get('useVmBiosUuid')
        username = dictionary.get('username')
        warning_messages = dictionary.get('warningMessages')

        # Return an object of this model
        return cls(access_info,
                   authentication_error_message,
                   authentication_status,
                   environments,
                   is_db_authenticated,
                   minimum_free_space_gb,
                   nas_mount_credentials,
                   password,
                   refresh_error_message,
                   refresh_time_usecs,
                   registration_time_usecs,
                   throttling_policy,
                   throttling_policy_overrides,
                   use_vm_bios_uuid,
                   username,
                   warning_messages)


