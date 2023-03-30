# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.application_restore_object
import cohesity_management_sdk.models.protection_source_and_application_restore_objects
import cohesity_management_sdk.models.restore_object_details


class ApplicationRestoreParameters(object):

    """Implementation of the 'ApplicationRestoreParameters' model.

    Specifies the information regarding the application restore parameters.


    Attributes:

        application_environment (ApplicationEnvironmentEnum): Specifies the
            Environment of the Application server to restore like
            'kSQL','kAD',or 'kExchange'. Supported environment types such as
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
        application_restore_objects (list of ApplicationRestoreObject):
            Specifies the Application Server objects whose data should be
            restored.
        hosting_protection_source (RestoreObjectDetails): Specifies the restore
            information for the Protection Source object that registered and
            hosts the Application Servers. This provides the snapshot details
            from which the application should be restored.
        protection_source_and_application_objects (list of
            ProtectionSourceAndApplicationRestoreObjects): Specifies the list
            of hosting protection source and Application restore objects tuple.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "application_environment":'applicationEnvironment',
        "application_restore_objects":'applicationRestoreObjects',
        "hosting_protection_source":'hostingProtectionSource',
        "protection_source_and_application_objects":'protectionSourceAndApplicationObjects',
    }
    def __init__(self,
                 application_environment=None,
                 application_restore_objects=None,
                 hosting_protection_source=None,
                 protection_source_and_application_objects=None,
            ):

        """Constructor for the ApplicationRestoreParameters class"""

        # Initialize members of the class
        self.application_environment = application_environment
        self.application_restore_objects = application_restore_objects
        self.hosting_protection_source = hosting_protection_source
        self.protection_source_and_application_objects = protection_source_and_application_objects

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
        application_environment = dictionary.get('applicationEnvironment')
        application_restore_objects = None
        if dictionary.get('applicationRestoreObjects') != None:
            application_restore_objects = list()
            for structure in dictionary.get('applicationRestoreObjects'):
                application_restore_objects.append(cohesity_management_sdk.models.application_restore_object.ApplicationRestoreObject.from_dictionary(structure))
        hosting_protection_source = cohesity_management_sdk.models.restore_object_details.RestoreObjectDetails.from_dictionary(dictionary.get('hostingProtectionSource')) if dictionary.get('hostingProtectionSource') else None
        protection_source_and_application_objects = None
        if dictionary.get('protectionSourceAndApplicationObjects') != None:
            protection_source_and_application_objects = list()
            for structure in dictionary.get('protectionSourceAndApplicationObjects'):
                protection_source_and_application_objects.append(cohesity_management_sdk.models.protection_source_and_application_restore_objects.ProtectionSourceAndApplicationRestoreObjects.from_dictionary(structure))

        # Return an object of this model
        return cls(
            application_environment,
            application_restore_objects,
            hosting_protection_source,
            protection_source_and_application_objects
)