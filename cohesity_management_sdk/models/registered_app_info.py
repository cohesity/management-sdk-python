# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.host_settings_check_result


class RegisteredAppInfo(object):

    """Implementation of the 'RegisteredAppInfo' model.

    TODO: type description here.


    Attributes:

        authentication_error_message (string): Specifies an authentication
            error message. This indicates the given credentials are rejected
            and the registration of the application is not successful.
        authentication_status (AuthenticationStatusEnum): Specifies the status
            of authenticating to the Protection Source when registering this
            application with Cohesity Cluster. If the status is 'kFinished' and
            there is no error, registration is successful. Specifies the status
            of the authentication during the registration of a Protection
            Source. 'kPending' indicates the authentication is in progress.
            'kScheduled' indicates the authentication is scheduled. 'kFinished'
            indicates the authentication is completed. 'kRefreshInProgress'
            indicates the refresh is in progress.
        environment (EnvironmentRegisteredAppInfoEnum): Specifies the
            application environment. Supported environment types such as
            'kView', 'kSQL', 'kVMware', etc. NOTE: 'kPuppeteer' refers to
            Cohesity's Remote Adapter. 'kVMware' indicates the VMware
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
        host_settings_check_results (list of HostSettingsCheckResult):
            Specifies the list of check results internally performed to verify
            status of various services such as 'AgnetRunning',
            'SQLWriterRunning' etc.
        refresh_error_message (string): Specifies a message if there was any
            error encountered during the last rebuild of the application tree.
            If there was no error during the last rebuild, this field is reset.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "authentication_error_message":'authenticationErrorMessage',
        "authentication_status":'authenticationStatus',
        "environment":'environment',
        "host_settings_check_results":'hostSettingsCheckResults',
        "refresh_error_message":'refreshErrorMessage',
    }
    def __init__(self,
                 authentication_error_message=None,
                 authentication_status=None,
                 environment=None,
                 host_settings_check_results=None,
                 refresh_error_message=None,
            ):

        """Constructor for the RegisteredAppInfo class"""

        # Initialize members of the class
        self.authentication_error_message = authentication_error_message
        self.authentication_status = authentication_status
        self.environment = environment
        self.host_settings_check_results = host_settings_check_results
        self.refresh_error_message = refresh_error_message

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
        authentication_error_message = dictionary.get('authenticationErrorMessage')
        authentication_status = dictionary.get('authenticationStatus')
        environment = dictionary.get('environment')
        host_settings_check_results = None
        if dictionary.get('hostSettingsCheckResults') != None:
            host_settings_check_results = list()
            for structure in dictionary.get('hostSettingsCheckResults'):
                host_settings_check_results.append(cohesity_management_sdk.models.host_settings_check_result.HostSettingsCheckResult.from_dictionary(structure))
        refresh_error_message = dictionary.get('refreshErrorMessage')

        # Return an object of this model
        return cls(
            authentication_error_message,
            authentication_status,
            environment,
            host_settings_check_results,
            refresh_error_message
)