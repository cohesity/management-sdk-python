# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.


class DataUsageStats(object):

    """Implementation of the 'DataUsageStats' model.

    Specifies the data usage metric of the data stored on the Cohesity
    Cluster or Storage Domains (View Boxes).

    Attributes:
        cloud_data_written_bytes (long|int): Specifies the total data written
            on cloud tiers, as computed by the Cohesity Cluster.
        cloud_total_physical_usage_bytes (long|int): Specifies the total cloud
            capacity, as computed by the Cohesity Cluster, after the size of
            the data has been reduced by change-block tracking, compression
            and deduplication.
        data_in_bytes (long|int): Specifies the data brought into the cluster.
            This is the usage before data reduction.
        data_in_bytes_after_dedup (long|int): Specifies the the the size of
            the data has been reduced by change-block tracking and
            deduplication but before compression or data is replicated to
            other nodes as per RF or Erasure Coding policy.
        data_protect_logical_usage_bytes (long|int): Specifies the logical
            data used by Data Protect on Cohesity cluster.
        data_protect_physical_usage_bytes (long|int): Specifies the physical
            data used by Data Protect on Cohesity cluster.
        data_written_bytes (long|int): Specifies the total data written on
            local and cloud tiers, as computed by the Cohesity Cluster, after
            the size of the data has been reduced by change-block tracking,
            deduplication and compression. This does not include resiliency
            impact.
        file_services_logical_usage_bytes (long|int): Specifies the logical
            data used by File services on Cohesity cluster.
        file_services_physical_usage_bytes (long|int): Specifies the physical
            data used by File services on Cohesity cluster.
        local_data_written_bytes (long|int): Specifies the total data written
            on local tiers, as computed by the Cohesity Cluster, after the
            size of the data has been reduced by change-block tracking,
            deduplication and compression. This does not include resiliency
            impact.
        local_tier_resiliency_impact_bytes (long|int): Specifies the size of
            the data has been replicated to other nodes as per RF or Erasure
            Coding policy.
        local_total_physical_usage_bytes (long|int): Specifies the total local
            capacity, as computed by the Cohesity Cluster, after the size of
            the data has been reduced by change-block tracking, compression
            and deduplication.
        storage_consumed_bytes (long|int): Specifies the total capacity, as
            computed by the Cohesity Cluster, after the size of the data has
            been reduced by change-block tracking, compression and
            deduplication. This includes resiliency impact.
        total_logical_usage_bytes (long|int): Specifies the logical usage as
            computed by the Cohesity Cluster. The size of the data without
            reduction by change-block tracking, compression and
            deduplication.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cloud_data_written_bytes":'cloudDataWrittenBytes',
        "cloud_total_physical_usage_bytes":'cloudTotalPhysicalUsageBytes',
        "data_in_bytes":'dataInBytes',
        "data_in_bytes_after_dedup":'dataInBytesAfterDedup',
        "data_protect_logical_usage_bytes":'dataProtectLogicalUsageBytes',
        "data_protect_physical_usage_bytes":'dataProtectPhysicalUsageBytes',
        "data_written_bytes":'dataWrittenBytes',
        "file_services_logical_usage_bytes":'fileServicesLogicalUsageBytes',
        "file_services_physical_usage_bytes":'fileServicesPhysicalUsageBytes',
        "local_data_written_bytes":'localDataWrittenBytes',
        "local_tier_resiliency_impact_bytes":'localTierResiliencyImpactBytes',
        "local_total_physical_usage_bytes":'localTotalPhysicalUsageBytes',
        "storage_consumed_bytes":'storageConsumedBytes',
        "total_logical_usage_bytes":'totalLogicalUsageBytes'
    }

    def __init__(self,
                 cloud_data_written_bytes=None,
                 cloud_total_physical_usage_bytes=None,
                 data_in_bytes=None,
                 data_in_bytes_after_dedup=None,
                 data_protect_logical_usage_bytes=None,
                 data_protect_physical_usage_bytes=None,
                 data_written_bytes=None,
                 file_services_logical_usage_bytes=None,
                 file_services_physical_usage_bytes=None,
                 local_data_written_bytes=None,
                 local_tier_resiliency_impact_bytes=None,
                 local_total_physical_usage_bytes=None,
                 storage_consumed_bytes=None,
                 total_logical_usage_bytes=None):
        """Constructor for the DataUsageStats class"""

        # Initialize members of the class
        self.cloud_data_written_bytes = cloud_data_written_bytes
        self.cloud_total_physical_usage_bytes = cloud_total_physical_usage_bytes
        self.data_in_bytes = data_in_bytes
        self.data_in_bytes_after_dedup = data_in_bytes_after_dedup
        self.data_protect_logical_usage_bytes = data_protect_logical_usage_bytes
        self.data_protect_physical_usage_bytes = data_protect_physical_usage_bytes
        self.data_written_bytes = data_written_bytes
        self.file_services_logical_usage_bytes = file_services_logical_usage_bytes
        self.file_services_physical_usage_bytes = file_services_physical_usage_bytes
        self.local_data_written_bytes = local_data_written_bytes
        self.local_tier_resiliency_impact_bytes = local_tier_resiliency_impact_bytes
        self.local_total_physical_usage_bytes = local_total_physical_usage_bytes
        self.storage_consumed_bytes = storage_consumed_bytes
        self.total_logical_usage_bytes = total_logical_usage_bytes


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
        cloud_data_written_bytes = dictionary.get('cloudDataWrittenBytes')
        cloud_total_physical_usage_bytes = dictionary.get('cloudTotalPhysicalUsageBytes')
        data_in_bytes = dictionary.get('dataInBytes')
        data_in_bytes_after_dedup = dictionary.get('dataInBytesAfterDedup')
        data_protect_logical_usage_bytes = dictionary.get('dataProtectLogicalUsageBytes')
        data_protect_physical_usage_bytes = dictionary.get('dataProtectPhysicalUsageBytes')
        data_written_bytes = dictionary.get('dataWrittenBytes')
        file_services_logical_usage_bytes = dictionary.get('fileServicesLogicalUsageBytes')
        file_services_physical_usage_bytes = dictionary.get('fileServicesPhysicalUsageBytes')
        local_data_written_bytes = dictionary.get('localDataWrittenBytes')
        local_tier_resiliency_impact_bytes = dictionary.get('localTierResiliencyImpactBytes')
        local_total_physical_usage_bytes = dictionary.get('localTotalPhysicalUsageBytes')
        storage_consumed_bytes = dictionary.get('storageConsumedBytes')
        total_logical_usage_bytes = dictionary.get('totalLogicalUsageBytes')

        # Return an object of this model
        return cls(cloud_data_written_bytes,
                   cloud_total_physical_usage_bytes,
                   data_in_bytes,
                   data_in_bytes_after_dedup,
                   data_protect_logical_usage_bytes,
                   data_protect_physical_usage_bytes,
                   data_written_bytes,
                   file_services_logical_usage_bytes,
                   file_services_physical_usage_bytes,
                   local_data_written_bytes,
                   local_tier_resiliency_impact_bytes,
                   local_total_physical_usage_bytes,
                   storage_consumed_bytes,
                   total_logical_usage_bytes)


