# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.trending_data


class ProtectionTrend(object):

    """Implementation of the 'ProtectionTrend' model.

    Specifies details of a protected object with it's protection trends.


    Attributes:

        cancelled (long|int): Specifies number of cancelled runs across trends.
        environment (EnvironmentProtectionTrendEnum): Specifies environment.
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
        failed (long|int): Specifies number of failed runs across trends.
        id (long|int): Specifies protected object's Id.
        name (string): Specifies protected object's name.
        parent_source_id (long|int): Specifies protected object's parent id.
        parent_source_name (string): Specifies protected object's parent name.
        running (long|int): Specifies number of in-progress runs across trends.
        successful (long|int): Specifies number of successful runs across
            trends.
        total (long|int): Specifies total number of runs across trends.
        trends (list of TrendingData): Aggregated protection runs information
            by days/weeks.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "cancelled":'cancelled',
        "environment":'environment',
        "failed":'failed',
        "id":'id',
        "name":'name',
        "parent_source_id":'parentSourceId',
        "parent_source_name":'parentSourceName',
        "running":'running',
        "successful":'successful',
        "total":'total',
        "trends":'trends',
    }
    def __init__(self,
                 cancelled=None,
                 environment=None,
                 failed=None,
                 id=None,
                 name=None,
                 parent_source_id=None,
                 parent_source_name=None,
                 running=None,
                 successful=None,
                 total=None,
                 trends=None,
            ):

        """Constructor for the ProtectionTrend class"""

        # Initialize members of the class
        self.cancelled = cancelled
        self.environment = environment
        self.failed = failed
        self.id = id
        self.name = name
        self.parent_source_id = parent_source_id
        self.parent_source_name = parent_source_name
        self.running = running
        self.successful = successful
        self.total = total
        self.trends = trends

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
        cancelled = dictionary.get('cancelled')
        environment = dictionary.get('environment')
        failed = dictionary.get('failed')
        id = dictionary.get('id')
        name = dictionary.get('name')
        parent_source_id = dictionary.get('parentSourceId')
        parent_source_name = dictionary.get('parentSourceName')
        running = dictionary.get('running')
        successful = dictionary.get('successful')
        total = dictionary.get('total')
        trends = None
        if dictionary.get('trends') != None:
            trends = list()
            for structure in dictionary.get('trends'):
                trends.append(cohesity_management_sdk.models.trending_data.TrendingData.from_dictionary(structure))

        # Return an object of this model
        return cls(
            cancelled,
            environment,
            failed,
            id,
            name,
            parent_source_id,
            parent_source_name,
            running,
            successful,
            total,
            trends
)