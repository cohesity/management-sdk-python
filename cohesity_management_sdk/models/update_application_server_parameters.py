# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class UpdateApplicationServerParameters(object):

    """Implementation of the 'UpdateApplicationServerParameters' model.

    Specifies the parameters required to modify the parameters of previously
    registered Application Servers in a Protection Source.


    Attributes:

        applications (list of ApplicationsEnum): Specifies the types of
            applications such as 'kSQL', 'kExchange', 'kAD' running on the
            Protection Source. overrideDescription: true Supported environment
            types such as 'kView', 'kSQL', 'kVMware', etc. NOTE: 'kPuppeteer'
            refers to Cohesity's Remote Adapter. 'kVMware' indicates the VMware
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
        encryption_key (string): If set, user has encrypted the credential with
            'user_ecryption_key'. It is assumed that credentials are first
            encrypted using internal magento key and then encrypted using user
            encryption key.
        has_persistent_agent (bool): Set this to true if a persistent agent is
            running on the host. If this is specified, then credentials would
            not be used to log into the host environment. This mechanism may be
            used in environments such as VMware to get around UAC permission
            issues by running the agent as a service with the right
            credentials. If this field is not specified, credentials must be
            specified.
        is_internal_encrypted (bool): Set to true if credentials are encrypted
            by internal magneto key.
        password (string): Specifies password of the username to access the
            target source.
        protection_source_id (long|int): Specifies the Id of the Protection
            Source that contains one or more Application Servers running on it.
        username (string): Specifies username to access the target source.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "applications":'applications',
        "encryption_key":'encryptionKey',
        "has_persistent_agent":'hasPersistentAgent',
        "is_internal_encrypted":'isInternalEncrypted',
        "password":'password',
        "protection_source_id":'protectionSourceId',
        "username":'username',
    }
    def __init__(self,
                 applications=None,
                 encryption_key=None,
                 has_persistent_agent=None,
                 is_internal_encrypted=None,
                 password=None,
                 protection_source_id=None,
                 username=None,
            ):

        """Constructor for the UpdateApplicationServerParameters class"""

        # Initialize members of the class
        self.applications = applications
        self.encryption_key = encryption_key
        self.has_persistent_agent = has_persistent_agent
        self.is_internal_encrypted = is_internal_encrypted
        self.password = password
        self.protection_source_id = protection_source_id
        self.username = username

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
        applications = dictionary.get("applications")
        encryption_key = dictionary.get('encryptionKey')
        has_persistent_agent = dictionary.get('hasPersistentAgent')
        is_internal_encrypted = dictionary.get('isInternalEncrypted')
        password = dictionary.get('password')
        protection_source_id = dictionary.get('protectionSourceId')
        username = dictionary.get('username')

        # Return an object of this model
        return cls(
            applications,
            encryption_key,
            has_persistent_agent,
            is_internal_encrypted,
            password,
            protection_source_id,
            username
)