# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.subnet
import cohesity_management_sdk.models.quota_policy
import cohesity_management_sdk.models.view_box_stats
import cohesity_management_sdk.models.storage_policy

class ViewBox(object):

    """Implementation of the 'ViewBox' model.

    Provides details about a Storage Domain (View Box).

    Attributes:
        ad_domain_name (string): Specifies an active directory domain that
            this view box is mapped to.
        client_subnet_white_list (list of Subnet): Array of Subnets.
            Specifies the Subnets from which this Storage Domain (View Box)
            accepts requests.
        cloud_down_waterfall_threshold_pct (int): Specifies the cloud down
            water-fall threshold percentage. This indicates how full should a
            viewbox at least be before we down water-fall its data to cloud
            tier. If this field is set, the physical quota limit must be set
            also and will be used as viewbox capacity.
        cloud_down_waterfall_threshold_secs (int): Specifies the cloud down
            water-fall threshold seconds. This indicates what's the time
            threshold on water-falling data to cloud tier.
        cluster_partition_id (long|int): Specifies the Cluster Partition id
            where the Storage Domain (View Box) is located.
        cluster_partition_name (string): Specifies the Cohesity Cluster name
            where the Storage Domain (View Box) is located.
        default_user_quota_policy (QuotaPolicy): Specifies an optional quota
            policy/limits that are inherited by all users within the views in
            this viewbox.
        default_view_quota_policy (QuotaPolicy): Specifies an optional default
            logical quota limit (in bytes) for the Views in this Storage
            Domain (View Box). (Logical data is when the data is fully
            hydrated and expanded.) However, this inherited quota can be
            overwritten at the View level. A new write is not allowed if the
            Storage Domain (View Box) will exceed the specified quota.
            However, it takes time for the Cohesity Cluster to calculate the
            usage across Nodes, so the limit may be exceeded by a small
            amount. In addition, if the limit is increased or data is removed,
            there may be delay before the Cohesity Cluster allows more data to
            be written to the Storage Domain (View Box), as the Cluster is
            calculating the usage across Nodes.
        id (long|int): Specifies the Id of the Storage Domain (View Box).
        ldap_provider_id (long|int): When set, the following provides the LDAP
            provider the view box is mapped to. For any view from this view
            box, when accessed via NFS the following LDAP provider is looked
            up for getting Unix IDs of the corresponding user. Similarly, when
            a view is accessed via SMB and if the AD user's domain matches
            with the view box's AD, the following LDAP provider will be used
            to lookup Unix IDs for the corresponding AD user. Additionally
            there is also a mapping between LDAP provider and AD domain that
            is stored in AD provider config. It will be used if AD is not set
            on the view box.
        name (string): Specifies the name of the Storage Domain (View Box).
        physical_quota (QuotaPolicy): Specifies an optional quota limit (in
            bytes) for the physical usage of this Storage Domain (View Box).
            This quota limit defines a physical limit for size of the data
            that can be physically stored on the Storage Domain (View Box),
            after the data has been reduced by change block tracking,
            compression and deduplication. The physical usage is the aggregate
            sum of the data stored for this Storage Domain (View Box) on all
            disks in the Cluster. (The usage includes Cloud Tier data and user
            data.) A new write is not allowed if the Storage Domain (View Box)
            will exceed the specified quota. However, it takes time for the
            Cohesity Cluster to calculate the usage across Nodes, so the limit
            may be exceeded by a small amount. In addition, if the limit is
            increased or data is removed, there may be a delay before the
            Cohesity Cluster allows more data to be written to the Storage
            Domain (View Box), as the Cluster is calculating the usage across
            Nodes.
        removal_state (RemovalStateViewBoxEnum): Specifies the current removal
            state of the Storage Domain (View Box). 'kDontRemove' means the
            state of object is functional and it is not being removed.
            'kMarkedForRemoval' means the object is being removed.
            'kOkToRemove' means the object has been removed on the Cohesity
            Cluster and if the object is physical, it can be removed from the
            Cohesity Cluster.
        s_3_buckets_allowed (bool): Specifies whether creation of a S3 bucket
            is allowed in this Storage Domain (View Box). When a new S3 bucket
            creation request arrives, we'll look at all the View Boxes and the
            first Storage Domain (View Box) that allows creating S3 buckets in
            it will be the one where the bucket will be placed.
        stats (ViewBoxStats): Provides statistics about the Storage Domain
            (View Box).
        storage_policy (StoragePolicy): Specifies the storage options applied
            to a Storage Domain (View Box).
        tenant_id_vec (list of string): Optional ids for the tenants that this
            view box belongs. This must be checked before granting access to
            users. Unless the cluster enables view box sharing between tenants
            is allowed, there shall be at most one item in this list. Note
            that if all tenant may be deleted - such viewboxes must be garbage
            collected. This is currently done by a background thread in iris.
        treat_file_sync_as_data_sync (bool): If 'true', when the Cohesity
            Cluster is writing to a file, the file modification time is not
            persisted synchronously during the file write, so the modification
            time may not be accurate. (Typically the file modification time is
            off by 30 seconds but it can be longer.) Only set to 'false' if
            your environment requires a very accurate modification time. The
            default value is 'true' which provides the best Cohesity Cluster
            performance.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cluster_partition_id":'clusterPartitionId',
        "name":'name',
        "ad_domain_name":'adDomainName',
        "client_subnet_white_list":'clientSubnetWhiteList',
        "cloud_down_waterfall_threshold_pct":'cloudDownWaterfallThresholdPct',
        "cloud_down_waterfall_threshold_secs":'cloudDownWaterfallThresholdSecs',
        "cluster_partition_name":'clusterPartitionName',
        "default_user_quota_policy":'defaultUserQuotaPolicy',
        "default_view_quota_policy":'defaultViewQuotaPolicy',
        "id":'id',
        "ldap_provider_id":'ldapProviderId',
        "physical_quota":'physicalQuota',
        "removal_state":'removalState',
        "s_3_buckets_allowed":'s3BucketsAllowed',
        "stats":'stats',
        "storage_policy":'storagePolicy',
        "tenant_id_vec":'tenantIdVec',
        "treat_file_sync_as_data_sync":'treatFileSyncAsDataSync'
    }

    def __init__(self,
                 cluster_partition_id=None,
                 name=None,
                 ad_domain_name=None,
                 client_subnet_white_list=None,
                 cloud_down_waterfall_threshold_pct=None,
                 cloud_down_waterfall_threshold_secs=None,
                 cluster_partition_name=None,
                 default_user_quota_policy=None,
                 default_view_quota_policy=None,
                 id=None,
                 ldap_provider_id=None,
                 physical_quota=None,
                 removal_state=None,
                 s_3_buckets_allowed=None,
                 stats=None,
                 storage_policy=None,
                 tenant_id_vec=None,
                 treat_file_sync_as_data_sync=None):
        """Constructor for the ViewBox class"""

        # Initialize members of the class
        self.ad_domain_name = ad_domain_name
        self.client_subnet_white_list = client_subnet_white_list
        self.cloud_down_waterfall_threshold_pct = cloud_down_waterfall_threshold_pct
        self.cloud_down_waterfall_threshold_secs = cloud_down_waterfall_threshold_secs
        self.cluster_partition_id = cluster_partition_id
        self.cluster_partition_name = cluster_partition_name
        self.default_user_quota_policy = default_user_quota_policy
        self.default_view_quota_policy = default_view_quota_policy
        self.id = id
        self.ldap_provider_id = ldap_provider_id
        self.name = name
        self.physical_quota = physical_quota
        self.removal_state = removal_state
        self.s_3_buckets_allowed = s_3_buckets_allowed
        self.stats = stats
        self.storage_policy = storage_policy
        self.tenant_id_vec = tenant_id_vec
        self.treat_file_sync_as_data_sync = treat_file_sync_as_data_sync


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
        cluster_partition_id = dictionary.get('clusterPartitionId')
        name = dictionary.get('name')
        ad_domain_name = dictionary.get('adDomainName')
        client_subnet_white_list = None
        if dictionary.get('clientSubnetWhiteList') != None:
            client_subnet_white_list = list()
            for structure in dictionary.get('clientSubnetWhiteList'):
                client_subnet_white_list.append(cohesity_management_sdk.models.subnet.Subnet.from_dictionary(structure))
        cloud_down_waterfall_threshold_pct = dictionary.get('cloudDownWaterfallThresholdPct')
        cloud_down_waterfall_threshold_secs = dictionary.get('cloudDownWaterfallThresholdSecs')
        cluster_partition_name = dictionary.get('clusterPartitionName')
        default_user_quota_policy = cohesity_management_sdk.models.quota_policy.QuotaPolicy.from_dictionary(dictionary.get('defaultUserQuotaPolicy')) if dictionary.get('defaultUserQuotaPolicy') else None
        default_view_quota_policy = cohesity_management_sdk.models.quota_policy.QuotaPolicy.from_dictionary(dictionary.get('defaultViewQuotaPolicy')) if dictionary.get('defaultViewQuotaPolicy') else None
        id = dictionary.get('id')
        ldap_provider_id = dictionary.get('ldapProviderId')
        physical_quota = cohesity_management_sdk.models.quota_policy.QuotaPolicy.from_dictionary(dictionary.get('physicalQuota')) if dictionary.get('physicalQuota') else None
        removal_state = dictionary.get('removalState')
        s_3_buckets_allowed = dictionary.get('s3BucketsAllowed')
        stats = cohesity_management_sdk.models.view_box_stats.ViewBoxStats.from_dictionary(dictionary.get('stats')) if dictionary.get('stats') else None
        storage_policy = cohesity_management_sdk.models.storage_policy.StoragePolicy.from_dictionary(dictionary.get('storagePolicy')) if dictionary.get('storagePolicy') else None
        tenant_id_vec = dictionary.get('tenantIdVec')
        treat_file_sync_as_data_sync = dictionary.get('treatFileSyncAsDataSync')

        # Return an object of this model
        return cls(cluster_partition_id,
                   name,
                   ad_domain_name,
                   client_subnet_white_list,
                   cloud_down_waterfall_threshold_pct,
                   cloud_down_waterfall_threshold_secs,
                   cluster_partition_name,
                   default_user_quota_policy,
                   default_view_quota_policy,
                   id,
                   ldap_provider_id,
                   physical_quota,
                   removal_state,
                   s_3_buckets_allowed,
                   stats,
                   storage_policy,
                   tenant_id_vec,
                   treat_file_sync_as_data_sync)


