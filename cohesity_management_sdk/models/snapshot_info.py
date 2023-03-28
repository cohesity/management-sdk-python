# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class SnapshotInfo(object):

    """Implementation of the 'SnapshotInfo' model.

    Specifies details about the snapshot task created to backup or copy one
    source object like a VM.


    Attributes:

        environment (EnvironmentSnapshotInfoEnum): Specifies the environment
            type (such as kVMware or kSQL) that contains the source to backup.
            Supported environment types such as 'kView', 'kSQL', 'kVMware',
            etc. NOTE: 'kPuppeteer' refers to Cohesity's Remote Adapter.
            'kVMware' indicates the VMware Protection Source environment.
            'kHyperV' indicates the HyperV Protection Source environment.
            'kSQL' indicates the SQL Protection Source environment. 'kView'
            indicates the View Protection Source environment. 'kPuppeteer'
            indicates the Cohesity's Remote Adapter. 'kPhysical' indicates the
            physical Protection Source environment. 'kPure' indicates the Pure
            Storage Protection Source environment. 'kNimble' indicates the
            Nimble Storage Protection Source environment. 'kAzure' indicates
            the Microsoft's Azure Protection Source environment. 'kNetapp'
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
        relative_snapshot_directory (string): Specifies the relative directory
            path from root path where the snapshot is stored.
        root_path (string): Specifies the root path where the snapshot is
            stored, using the following format: "/ViewBox/ViewName/fs".
        source_snapshot_create_time_usecs (long|int): Specifies the snapshot
            create time of the already created snapshot on the source
        source_snapshot_name (string): Specifies the name of the snapshot
            backed up in a Netapp Data-Protect Volume where we use already
            created snapshot on the source
        view_name (string): Specifies the name of the View that is cloned.
            NOTE: This field is only populated for View cloning.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "environment":'environment',
        "relative_snapshot_directory":'relativeSnapshotDirectory',
        "root_path":'rootPath',
        "source_snapshot_create_time_usecs":'sourceSnapshotCreateTimeUsecs',
        "source_snapshot_name":'sourceSnapshotName',
        "view_name":'viewName',
    }
    def __init__(self,
                 environment=None,
                 relative_snapshot_directory=None,
                 root_path=None,
                 source_snapshot_create_time_usecs=None,
                 source_snapshot_name=None,
                 view_name=None,
            ):

        """Constructor for the SnapshotInfo class"""

        # Initialize members of the class
        self.environment = environment
        self.relative_snapshot_directory = relative_snapshot_directory
        self.root_path = root_path
        self.source_snapshot_create_time_usecs = source_snapshot_create_time_usecs
        self.source_snapshot_name = source_snapshot_name
        self.view_name = view_name

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
        relative_snapshot_directory = dictionary.get('relativeSnapshotDirectory')
        root_path = dictionary.get('rootPath')
        source_snapshot_create_time_usecs = dictionary.get('sourceSnapshotCreateTimeUsecs')
        source_snapshot_name = dictionary.get('sourceSnapshotName')
        view_name = dictionary.get('viewName')

        # Return an object of this model
        return cls(
            environment,
            relative_snapshot_directory,
            root_path,
            source_snapshot_create_time_usecs,
            source_snapshot_name,
            view_name
)