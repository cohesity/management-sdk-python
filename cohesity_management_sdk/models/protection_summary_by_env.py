# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class ProtectionSummaryByEnv(object):

    """Implementation of the 'ProtectionSummaryByEnv' model.

    ProtectionSummaryByEnv specifies the number of protected and unprotected
    objects that is break down by environment.


    Attributes:

        environment (EnvironmentProtectionSummaryByEnvEnum): Specifies the type
            of environment of the source object like kSQL etc. Supported
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
        protected_count (long|int): Specifies the number of objects that are
            protected under the given entity.
        protected_size (long|int): Specifies the total size of the protected
            objects under the given entity.
        unprotected_count (long|int): Specifies the number of objects that are
            not protected under the given entity.
        unprotected_size (long|int): Specifies the total size of the
            unprotected objects under the given entity.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "environment":'environment',
        "protected_count":'protectedCount',
        "protected_size":'protectedSize',
        "unprotected_count":'unprotectedCount',
        "unprotected_size":'unprotectedSize',
    }
    def __init__(self,
                 environment=None,
                 protected_count=None,
                 protected_size=None,
                 unprotected_count=None,
                 unprotected_size=None,
            ):

        """Constructor for the ProtectionSummaryByEnv class"""

        # Initialize members of the class
        self.environment = environment
        self.protected_count = protected_count
        self.protected_size = protected_size
        self.unprotected_count = unprotected_count
        self.unprotected_size = unprotected_size

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
        environment = dictionary.get('environment')
        protected_count = dictionary.get('protectedCount')
        protected_size = dictionary.get('protectedSize')
        unprotected_count = dictionary.get('unprotectedCount')
        unprotected_size = dictionary.get('unprotectedSize')

        # Return an object of this model
        return cls(
            environment,
            protected_count,
            protected_size,
            unprotected_count,
            unprotected_size
)