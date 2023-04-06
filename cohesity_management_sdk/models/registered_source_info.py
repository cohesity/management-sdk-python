# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.cassandra_connect_params
import cohesity_management_sdk.models.connector_parameters
import cohesity_management_sdk.models.couchbase_connect_params
import cohesity_management_sdk.models.credentials
import cohesity_management_sdk.models.hbase_connect_params
import cohesity_management_sdk.models.hdfs_connect_params
import cohesity_management_sdk.models.hive_connect_params
import cohesity_management_sdk.models.mongo_db_connect_params
import cohesity_management_sdk.models.nas_mount_credential_params
import cohesity_management_sdk.models.o_365_connect_params
import cohesity_management_sdk.models.office_365_credentials
import cohesity_management_sdk.models.physical_params
import cohesity_management_sdk.models.registered_app_info
import cohesity_management_sdk.models.registered_protection_source_isilon_params
import cohesity_management_sdk.models.sfdc_params
import cohesity_management_sdk.models.subnet
import cohesity_management_sdk.models.throttling_policy_override
import cohesity_management_sdk.models.throttling_policy_parameters
import cohesity_management_sdk.models.uda_connect_params
import cohesity_management_sdk.models.vlan_parameters


class RegisteredSourceInfo(object):

    """Implementation of the 'RegisteredSourceInfo' model.

    Specifies information about a registered Source.


    Attributes:

        access_info (ConnectorParameters): Specifies the parameters required to
            establish a connection with a particular environment.
        allowed_ip_addresses (list of string): Specifies the list of IP
            Addresses on the registered source to be exclusively allowed for
            doing any type of IO operations.
        authentication_error_message (string): Specifies an authentication
            error message. This indicates the given credentials are rejected
            and the registration of the source is not successful.
        authentication_status (AuthenticationStatusEnum): Specifies the status
            of the authenticating to the Protection Source when registering it
            with Cohesity Cluster. If the status is 'kFinished' and there is no
            error, registration is successful. Specifies the status of the
            authentication during the registration of a Protection Source.
            'kPending' indicates the authentication is in progress.
            'kScheduled' indicates the authentication is scheduled. 'kFinished'
            indicates the authentication is completed. 'kRefreshInProgress'
            indicates the refresh is in progress.
        blacklisted_ip_addresses (list of string): This field is deprecated.
            Use DeniedIpAddresses instead. deprecated: true
        cassandra_params (CassandraConnectParams): Contains all the additional
            params specified by the user while registering the Cassandra
            source.
        couchbase_params (CouchbaseConnectParams): Contains all the additional
            params specified by the user while registering the Couchbase
            source.
        denied_ip_addresses (list of string): Specifies the list of IP
            Addresses on the registered source to be denied for doing any type
            of IO operations.
        environments (list of EnvironmentsEnum): Specifies a list of
            applications environment that are registered with this Protection
            Source such as 'kSQL'. Supported environment types such as 'kView',
            'kSQL', 'kVMware', etc. NOTE: 'kPuppeteer' refers to Cohesity's
            Remote Adapter. 'kVMware' indicates the VMware Protection Source
            environment. 'kHyperV' indicates the HyperV Protection Source
            environment. 'kSQL' indicates the SQL Protection Source
            environment. 'kView' indicates the View Protection Source
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
        hbase_params (HBaseConnectParams): Contains all the additional params
            specified by the user while registering the HBase source.
        hdfs_params (HdfsConnectParams): Contains all the additional params
            specified by the user while registering the Hdfs source.
        hive_params (HiveConnectParams): Contains all the additional params
            specified by the user while registering the Hive source.
        is_db_authenticated (bool): Specifies if application entity
            dbAuthenticated or not. ex: oracle database.
        is_storage_array_snapshot_enabled (bool): Specifies if this source
            entity has enabled storage array snapshot or not.
        isilon_params (RegisteredProtectionSourceIsilonParams): Contains all
            the registered source params specified by the user while
            configuring the Isilon source.
        link_vms_across_vcenter (bool): Specifies if the VM linking feature is
            enabled for this VCenter This means that VMs present in this
            VCenter which earlier belonged to some other VCenter(also registerd
            on same cluster) and were migrated, will be linked during EH
            refresh. This will enable preserving snapshot chains for migrated
            VMs.
        minimum_free_space_gb (long|int): Specifies the minimum free space in
            GiB of the space expected to be available on the datastore where
            the virtual disks of the VM being backed up. If the amount of free
            space(in GiB) is lower than the value given by this field, backup
            will be aborted. Note that this field is applicable only to
            'kVMware' type of environments.
        minimum_free_space_percent (long|int): Specifies the minimum free space
            in percentage of the space expected to be available on the
            datastore where the virtual disks of the VM being backed up. If the
            amount of free space(in percentage) is lower than the value given
            by this field, backup will be aborted. Note that this field is
            applicable only to 'kVMware' type of environments.
        mongodb_params (MongoDBConnectParams): Contains all the additional
            params specified by the user while registering the MongoDB source.
        nas_mount_credentials (NasMountCredentialParams): Specifies the
            credentials required to mount directories on the NetApp server if
            given.
        o_365_params (O365ConnectParams): Contains all the additional params
            specified by the user while registering the Office 365 source.
        office_365_credentials_list (list of Office365Credentials): Office365
            Source Credentials.  Specifies credentials needed to authenticate &
            authorize user for Office365.
        office_365_region (string): Specifies the region for Office365. Inorder
            to truly categorize M365 region, clients should not depend upon the
            endpoint, instead look at this attribute for the same.
        office_365_service_account_credentials_list (list of Credentials):
            Office365 Service Account Credentials.  Specifies credentials for
            improving mailbox backup performance for O365.
        password (string): Specifies password of the username to access the
            target source.
        physical_params (PhysicalParams): Contains all the additional params
            specified by the user for source throttling configuration.
        progress_monitor_path (string): Captures the current progress and pulse
            details w.r.t to either the registration or refresh.
        refresh_error_message (string): Specifies a message if there was any
            error encountered during the last rebuild of the Protection Source
            tree. If there was no error during the last rebuild, this field is
            reset.
        refresh_time_usecs (long|int): Specifies the Unix epoch time (in
            microseconds) when the Protection Source tree was most recently
            fetched and built.
        registered_apps_info (list of RegisteredAppInfo): Specifies information
            of the applications registered on this protection source.
        registration_time_usecs (long|int): Specifies the Unix epoch time (in
            microseconds) when the Protection Source was registered.
        sfdc_params (SfdcParams): Contains all the additional params specified
            by the user while registering the Salesforce source.
        subnets (list of Subnet): Specifies the list of subnets added during
            creation or updation of vmare source. Currently, this field will
            only be populated in case of VMware registration.
        throttling_policy (ThrottlingPolicyParameters): Specifies the
            throttling policy that should be applied to all datastores under
            this registered Protection Source.
        throttling_policy_overrides (list of ThrottlingPolicyOverride): Array
            of Throttling Policy Overrides for Datastores.  Specifies a list of
            Throttling Policy for datastores that override the common
            throttling policy specified for the registered Protection Source.
            For datastores not in this list, common policy will still apply.
        uda_params (UdaConnectParams): Contains all the additional params
            specified by the user while registering the Universal Data Adapter
            source.
        use_o_auth_for_exchange_online (bool): Specifies whether OAuth should
            be used for authentication in case of Exchange Online.
        use_vm_bios_uuid (bool): Specifies if registered vCenter is using BIOS
            UUID to track virtual machines.
        user_messages (list of string): Specifies the additional details
            encountered during registration. Though the registration may
            succeed, user messages imply the host environment requires some
            cleanup or fixing.
        username (string): Specifies username to access the target source.
        vlan_params (VlanParameters): Specifies the VLAN parameters to be used
            for performing the backup/restore of this entity.
        warning_messages (list of string): Specifies a list of warnings
            encountered during registration. Though the registration may
            succeed, warning messages imply the host environment requires some
            cleanup or fixing.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "access_info":'accessInfo',
        "allowed_ip_addresses":'allowedIpAddresses',
        "authentication_error_message":'authenticationErrorMessage',
        "authentication_status":'authenticationStatus',
        "blacklisted_ip_addresses":'blacklistedIpAddresses',
        "cassandra_params":'cassandraParams',
        "couchbase_params":'couchbaseParams',
        "denied_ip_addresses":'deniedIpAddresses',
        "environments":'environments',
        "hbase_params":'hbaseParams',
        "hdfs_params":'hdfsParams',
        "hive_params":'hiveParams',
        "is_db_authenticated":'isDbAuthenticated',
        "is_storage_array_snapshot_enabled":'isStorageArraySnapshotEnabled',
        "isilon_params":'isilonParams',
        "link_vms_across_vcenter":'linkVmsAcrossVcenter',
        "minimum_free_space_gb":'minimumFreeSpaceGB',
        "minimum_free_space_percent":'minimumFreeSpacePercent',
        "mongodb_params":'mongodbParams',
        "nas_mount_credentials":'nasMountCredentials',
        "o_365_params":'o365Params',
        "office_365_credentials_list":'office365CredentialsList',
        "office_365_region":'office365Region',
        "office_365_service_account_credentials_list":'office365ServiceAccountCredentialsList',
        "password":'password',
        "physical_params":'physicalParams',
        "progress_monitor_path":'progressMonitorPath',
        "refresh_error_message":'refreshErrorMessage',
        "refresh_time_usecs":'refreshTimeUsecs',
        "registered_apps_info":'registeredAppsInfo',
        "registration_time_usecs":'registrationTimeUsecs',
        "sfdc_params":'sfdcParams',
        "subnets":'subnets',
        "throttling_policy":'throttlingPolicy',
        "throttling_policy_overrides":'throttlingPolicyOverrides',
        "uda_params":'udaParams',
        "use_o_auth_for_exchange_online":'useOAuthForExchangeOnline',
        "use_vm_bios_uuid":'useVmBiosUuid',
        "user_messages":'userMessages',
        "username":'username',
        "vlan_params":'vlanParams',
        "warning_messages":'warningMessages',
    }
    def __init__(self,
                 access_info=None,
                 allowed_ip_addresses=None,
                 authentication_error_message=None,
                 authentication_status=None,
                 blacklisted_ip_addresses=None,
                 cassandra_params=None,
                 couchbase_params=None,
                 denied_ip_addresses=None,
                 environments=None,
                 hbase_params=None,
                 hdfs_params=None,
                 hive_params=None,
                 is_db_authenticated=None,
                 is_storage_array_snapshot_enabled=None,
                 isilon_params=None,
                 link_vms_across_vcenter=None,
                 minimum_free_space_gb=None,
                 minimum_free_space_percent=None,
                 mongodb_params=None,
                 nas_mount_credentials=None,
                 o_365_params=None,
                 office_365_credentials_list=None,
                 office_365_region=None,
                 office_365_service_account_credentials_list=None,
                 password=None,
                 physical_params=None,
                 progress_monitor_path=None,
                 refresh_error_message=None,
                 refresh_time_usecs=None,
                 registered_apps_info=None,
                 registration_time_usecs=None,
                 sfdc_params=None,
                 subnets=None,
                 throttling_policy=None,
                 throttling_policy_overrides=None,
                 uda_params=None,
                 use_o_auth_for_exchange_online=None,
                 use_vm_bios_uuid=None,
                 user_messages=None,
                 username=None,
                 vlan_params=None,
                 warning_messages=None,
            ):

        """Constructor for the RegisteredSourceInfo class"""

        # Initialize members of the class
        self.access_info = access_info
        self.allowed_ip_addresses = allowed_ip_addresses
        self.authentication_error_message = authentication_error_message
        self.authentication_status = authentication_status
        self.blacklisted_ip_addresses = blacklisted_ip_addresses
        self.cassandra_params = cassandra_params
        self.couchbase_params = couchbase_params
        self.denied_ip_addresses = denied_ip_addresses
        self.environments = environments
        self.hbase_params = hbase_params
        self.hdfs_params = hdfs_params
        self.hive_params = hive_params
        self.is_db_authenticated = is_db_authenticated
        self.is_storage_array_snapshot_enabled = is_storage_array_snapshot_enabled
        self.isilon_params = isilon_params
        self.link_vms_across_vcenter = link_vms_across_vcenter
        self.minimum_free_space_gb = minimum_free_space_gb
        self.minimum_free_space_percent = minimum_free_space_percent
        self.mongodb_params = mongodb_params
        self.nas_mount_credentials = nas_mount_credentials
        self.o_365_params = o_365_params
        self.office_365_credentials_list = office_365_credentials_list
        self.office_365_region = office_365_region
        self.office_365_service_account_credentials_list = office_365_service_account_credentials_list
        self.password = password
        self.physical_params = physical_params
        self.progress_monitor_path = progress_monitor_path
        self.refresh_error_message = refresh_error_message
        self.refresh_time_usecs = refresh_time_usecs
        self.registered_apps_info = registered_apps_info
        self.registration_time_usecs = registration_time_usecs
        self.sfdc_params = sfdc_params
        self.subnets = subnets
        self.throttling_policy = throttling_policy
        self.throttling_policy_overrides = throttling_policy_overrides
        self.uda_params = uda_params
        self.use_o_auth_for_exchange_online = use_o_auth_for_exchange_online
        self.use_vm_bios_uuid = use_vm_bios_uuid
        self.user_messages = user_messages
        self.username = username
        self.vlan_params = vlan_params
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
        allowed_ip_addresses = dictionary.get("allowedIpAddresses")
        authentication_error_message = dictionary.get('authenticationErrorMessage')
        authentication_status = dictionary.get('authenticationStatus')
        blacklisted_ip_addresses = dictionary.get("blacklistedIpAddresses")
        cassandra_params = cohesity_management_sdk.models.cassandra_connect_params.CassandraConnectParams.from_dictionary(dictionary.get('cassandraParams')) if dictionary.get('cassandraParams') else None
        couchbase_params = cohesity_management_sdk.models.couchbase_connect_params.CouchbaseConnectParams.from_dictionary(dictionary.get('couchbaseParams')) if dictionary.get('couchbaseParams') else None
        denied_ip_addresses = dictionary.get("deniedIpAddresses")
        environments = dictionary.get("environments")
        hbase_params = cohesity_management_sdk.models.hbase_connect_params.HBaseConnectParams.from_dictionary(dictionary.get('hbaseParams')) if dictionary.get('hbaseParams') else None
        hdfs_params = cohesity_management_sdk.models.hdfs_connect_params.HdfsConnectParams.from_dictionary(dictionary.get('hdfsParams')) if dictionary.get('hdfsParams') else None
        hive_params = cohesity_management_sdk.models.hive_connect_params.HiveConnectParams.from_dictionary(dictionary.get('hiveParams')) if dictionary.get('hiveParams') else None
        is_db_authenticated = dictionary.get('isDbAuthenticated')
        is_storage_array_snapshot_enabled = dictionary.get('isStorageArraySnapshotEnabled')
        isilon_params = cohesity_management_sdk.models.registered_protection_source_isilon_params.RegisteredProtectionSourceIsilonParams.from_dictionary(dictionary.get('isilonParams')) if dictionary.get('isilonParams') else None
        link_vms_across_vcenter = dictionary.get('linkVmsAcrossVcenter')
        minimum_free_space_gb = dictionary.get('minimumFreeSpaceGB')
        minimum_free_space_percent = dictionary.get('minimumFreeSpacePercent')
        mongodb_params = cohesity_management_sdk.models.mongo_db_connect_params.MongoDBConnectParams.from_dictionary(dictionary.get('mongodbParams')) if dictionary.get('mongodbParams') else None
        nas_mount_credentials = cohesity_management_sdk.models.nas_mount_credential_params.NasMountCredentialParams.from_dictionary(dictionary.get('nasMountCredentials')) if dictionary.get('nasMountCredentials') else None
        o_365_params = cohesity_management_sdk.models.o_365_connect_params.O365ConnectParams.from_dictionary(dictionary.get('o365Params')) if dictionary.get('o365Params') else None
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
        physical_params = cohesity_management_sdk.models.physical_params.PhysicalParams.from_dictionary(dictionary.get('physicalParams')) if dictionary.get('physicalParams') else None
        progress_monitor_path = dictionary.get('progressMonitorPath')
        refresh_error_message = dictionary.get('refreshErrorMessage')
        refresh_time_usecs = dictionary.get('refreshTimeUsecs')
        registered_apps_info = None
        if dictionary.get('registeredAppsInfo') != None:
            registered_apps_info = list()
            for structure in dictionary.get('registeredAppsInfo'):
                registered_apps_info.append(cohesity_management_sdk.models.registered_app_info.RegisteredAppInfo.from_dictionary(structure))
        registration_time_usecs = dictionary.get('registrationTimeUsecs')
        sfdc_params = cohesity_management_sdk.models.sfdc_params.SfdcParams.from_dictionary(dictionary.get('sfdcParams')) if dictionary.get('sfdcParams') else None
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
        uda_params = cohesity_management_sdk.models.uda_connect_params.UdaConnectParams.from_dictionary(dictionary.get('udaParams')) if dictionary.get('udaParams') else None
        use_o_auth_for_exchange_online = dictionary.get('useOAuthForExchangeOnline')
        use_vm_bios_uuid = dictionary.get('useVmBiosUuid')
        user_messages = dictionary.get("userMessages")
        username = dictionary.get('username')
        vlan_params = cohesity_management_sdk.models.vlan_parameters.VlanParameters.from_dictionary(dictionary.get('vlanParams')) if dictionary.get('vlanParams') else None
        warning_messages = dictionary.get("warningMessages")

        # Return an object of this model
        return cls(
            access_info,
            allowed_ip_addresses,
            authentication_error_message,
            authentication_status,
            blacklisted_ip_addresses,
            cassandra_params,
            couchbase_params,
            denied_ip_addresses,
            environments,
            hbase_params,
            hdfs_params,
            hive_params,
            is_db_authenticated,
            is_storage_array_snapshot_enabled,
            isilon_params,
            link_vms_across_vcenter,
            minimum_free_space_gb,
            minimum_free_space_percent,
            mongodb_params,
            nas_mount_credentials,
            o_365_params,
            office_365_credentials_list,
            office_365_region,
            office_365_service_account_credentials_list,
            password,
            physical_params,
            progress_monitor_path,
            refresh_error_message,
            refresh_time_usecs,
            registered_apps_info,
            registration_time_usecs,
            sfdc_params,
            subnets,
            throttling_policy,
            throttling_policy_overrides,
            uda_params,
            use_o_auth_for_exchange_online,
            use_vm_bios_uuid,
            user_messages,
            username,
            vlan_params,
            warning_messages
)