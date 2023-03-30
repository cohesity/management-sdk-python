# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.protection_source_node


class ApplicationInfo(object):

    """Implementation of the 'ApplicationInfo' model.

    Specifies the application registered on the Cohesity Cluster.


    Attributes:

        application_tree_info (list of ProtectionSourceNode): Application
            Server and the subtrees below them.  Specifies the application
            subtree used to store additional application level Objects.
            Different environments use the subtree to store application level
            information. For example for SQL Server, this subtree stores the
            SQL Server instances running on a VM or a Physical Server.
            overrideDescription: true
        environment (EnvironmentApplicationInfoEnum): Specifies the environment
            type of the application such as 'kSQL', 'kExchange' registered on
            the Protection Source. overrideDescription: true Supported
            environment types such as 'kView', 'kSQL', 'kVMware', etc. NOTE:
            'kPuppeteer' refers to Cohesity's Remote Adapter. 'kVMware'
            indicates the VMware Protection Source environment. 'kHyperV'
            indicates the HyperV Protection Source environment. 'kSQL'
            indicates the SQL Protection Source environment. 'kView' indicates
            the View Protection Source environment. 'kPuppeteer' indicates the
            Cohesity's Remote Adapter. 'kPhysical' indicates the physical
            Protection Source environment. 'kPure' indicates the Pure Storage
            Protection Source environment. 'kNimble' indicates the Nimble
            Storage Protection Source environment. 'kAzure' indicates the
            Microsoft's Azure Protection Source environment. 'kNetapp'
            indicates the Netapp Protection Source environment. 'kAgent'
            indicates the Agent Protection Source environment. 'kGenericNas'
            indicates the Generic Network Attached Storage Protection Source
            environment. 'kAcropolis' indicates the Acropolis Protection Source
            environment. 'kPhysicalFiles' indicates the Physical Files
            Protection Source environment. 'kIsilon' indicates the Dell EMC's
            Isilon Protection Source environment. 'kGPFS' indicates IBM's GPFS
            Protection Source environment. 'kKVM' indicates the KVM Protection
            Source environment. 'kAWS' indicates the AWS Protection Source
            environment. 'kExchange' indicates the Exchange Protection Source
            environment. 'kHyperVVSS' indicates the HyperV VSS Protection
            Source environment. 'kOracle' indicates the Oracle Protection
            Source environment. 'kGCP' indicates the Google Cloud Platform
            Protection Source environment. 'kFlashBlade' indicates the Flash
            Blade Protection Source environment. 'kAWSNative' indicates the AWS
            Native Protection Source environment. 'kO365' indicates the Office
            365 Protection Source environment. 'kO365Outlook' indicates Office
            365 outlook Protection Source environment. 'kHyperFlex' indicates
            the Hyper Flex Protection Source environment. 'kGCPNative'
            indicates the GCP Native Protection Source environment.
            'kAzureNative' indicates the Azure Native Protection Source
            environment. 'kKubernetes' indicates a Kubernetes Protection Source
            environment. 'kElastifile' indicates Elastifile Protection Source
            environment. 'kAD' indicates Active Directory Protection Source
            environment. 'kRDSSnapshotManager' indicates AWS RDS Protection
            Source environment. 'kCassandra' indicates Cassandra Protection
            Source environment. 'kMongoDB' indicates MongoDB Protection Source
            environment. 'kCouchbase' indicates Couchbase Protection Source
            environment. 'kHdfs' indicates Hdfs Protection Source environment.
            'kHive' indicates Hive Protection Source environment. 'kHBase'
            indicates HBase Protection Source environment. 'kUDA' indicates
            Universal Data Adapter Protection Source environment. 'kO365Teams'
            indicates the Office365 Teams Protection Source environment.
            'kO365Group' indicates the Office365 Groups Protection Source
            environment. 'kO365Exchange' indicates the Office365 Mailbox
            Protection Source environment. 'kO365OneDrive' indicates the
            Office365 OneDrive Protection Source environment. 'kO365Sharepoint'
            indicates the Office365 SharePoint Protection Source environment.
            'kO365PublicFolders' indicates the Office365 PublicFolders
            Protection Source environment.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "application_tree_info":'applicationTreeInfo',
        "environment":'environment',
    }
    def __init__(self,
                 application_tree_info=None,
                 environment=None,
            ):

        """Constructor for the ApplicationInfo class"""

        # Initialize members of the class
        self.application_tree_info = application_tree_info
        self.environment = environment

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
        application_tree_info = None
        if dictionary.get('applicationTreeInfo') != None:
            application_tree_info = list()
            for structure in dictionary.get('applicationTreeInfo'):
                application_tree_info.append(cohesity_management_sdk.models.protection_source_node.ProtectionSourceNode.from_dictionary(structure))
        environment = dictionary.get('environment')

        # Return an object of this model
        return cls(
            application_tree_info,
            environment
)