# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.data_usage_stats
import cohesity_management_sdk.models.stats_group
import cohesity_management_sdk.models.usage_schema_info


class ConsumerStats(object):

    """Implementation of the 'ConsumerStats' model.

    ConsumerStats is the stats of a single consumer. A consumer is a entity
    which consumes the storage space of a storage domain. A consumer can be a
    View, Protection Job or a Replication Job.


    Attributes:

        consumer_type (ConsumerTypeEnum): Specifies the type of the consumer.
            Type of the consumer can be one of the following three,  'kViews',
            indicates the stats info of Views used per organization (tenant)
            per view box (storage domain). 'kProtectionRuns', indicates the
            stats info of Protection Runs used per organization (tenant) per
            view box (storage domain). 'kReplicationRuns', indicates the stats
            info of Replication In used per organization (tenant) per view box
            (storage domain). 'kViewProtectionRuns', indicates the stats info
            of View Protection Runs used per organization (tenant) per view box
            (storage domain).
        group_list (list of StatsGroup): Specifies a list of groups associated
            to this consumer.
        id (long|int): Specifies the id of the consumer.
        name (string): Specifies the name of the consumer.
        protection_environment (ProtectionEnvironmentEnum): Specifies the
            source environment of the protection job. Supported environment
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
        protection_policy_name (string): Specifies the name of the protection
            policy for 'kProtectionRuns' and 'kReplicationRuns' consumer.
        quota_hard_limit_bytes (long|int): Specifies the hard limit of logical
            quota of the consumer. This field will be returned only if consumer
            type is view.
        schema_info_list (list of UsageSchemaInfo): Specifies a list of
            schemaInfos of the consumer.
        stats (DataUsageStats): Specifies details of statistics of the
            consumer.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "consumer_type":'consumerType',
        "group_list":'groupList',
        "id":'id',
        "name":'name',
        "protection_environment":'protectionEnvironment',
        "protection_policy_name":'protectionPolicyName',
        "quota_hard_limit_bytes":'quotaHardLimitBytes',
        "schema_info_list":'schemaInfoList',
        "stats":'stats',
    }
    def __init__(self,
                 consumer_type=None,
                 group_list=None,
                 id=None,
                 name=None,
                 protection_environment=None,
                 protection_policy_name=None,
                 quota_hard_limit_bytes=None,
                 schema_info_list=None,
                 stats=None,
            ):

        """Constructor for the ConsumerStats class"""

        # Initialize members of the class
        self.consumer_type = consumer_type
        self.group_list = group_list
        self.id = id
        self.name = name
        self.protection_environment = protection_environment
        self.protection_policy_name = protection_policy_name
        self.quota_hard_limit_bytes = quota_hard_limit_bytes
        self.schema_info_list = schema_info_list
        self.stats = stats

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
        consumer_type = dictionary.get('consumerType')
        group_list = None
        if dictionary.get('groupList') != None:
            group_list = list()
            for structure in dictionary.get('groupList'):
                group_list.append(cohesity_management_sdk.models.stats_group.StatsGroup.from_dictionary(structure))
        id = dictionary.get('id')
        name = dictionary.get('name')
        protection_environment = dictionary.get('protectionEnvironment')
        protection_policy_name = dictionary.get('protectionPolicyName')
        quota_hard_limit_bytes = dictionary.get('quotaHardLimitBytes')
        schema_info_list = None
        if dictionary.get('schemaInfoList') != None:
            schema_info_list = list()
            for structure in dictionary.get('schemaInfoList'):
                schema_info_list.append(cohesity_management_sdk.models.usage_schema_info.UsageSchemaInfo.from_dictionary(structure))
        stats = cohesity_management_sdk.models.data_usage_stats.DataUsageStats.from_dictionary(dictionary.get('stats')) if dictionary.get('stats') else None

        # Return an object of this model
        return cls(
            consumer_type,
            group_list,
            id,
            name,
            protection_environment,
            protection_policy_name,
            quota_hard_limit_bytes,
            schema_info_list,
            stats
)