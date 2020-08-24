# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class DataUsageStats(object):

    """Implementation of the 'DataUsageStats' model.

    Specifies the data usage metric of the data stored on the Cohesity
    Cluster or Storage Domains (View Boxes).

    Attributes:
        cloud_data_written_bytes (long|int): Specifies the total data written
            on cloud tiers, as computed by the Cohesity Cluster.
        cloud_data_written_bytes_timestamp_usec (long|int): Specifies
            Timestamp of CloudDataWrittenBytes.
        cloud_total_physical_usage_bytes (long|int): Specifies the total cloud
            capacity, as computed by the Cohesity Cluster, after the size of
            the data has been reduced by change-block tracking, compression
            and deduplication.
        cloud_total_physical_usage_bytes_timestamp_usec (long|int): Specifies
            Timestamp of CloudTotalPhysicalUsageBytes.
        data_in_bytes (long|int): Specifies the data read from the protected
            objects by the Cohesity Cluster before any data reduction using
            deduplication and compression.
        data_in_bytes_after_dedup (long|int): Specifies the size of
            the data has been reduced by change-block tracking and
            deduplication but before compression or data is replicated to
            other nodes as per RF or Erasure Coding policy.
        data_in_bytes_after_dedup_timestamp_usec (long|int): Specifies
            Timestamp of DataInBytesAfterDedup.
        data_in_bytes_timestamp_usec (long|int): Specifies Timestamp of
            DataInBytes.
        data_protect_logical_usage_bytes (long|int): Specifies the logical
            data used by Data Protect on Cohesity cluster.
        data_protect_logical_usage_bytes_timestamp_usec (long|int): Specifies
            Timestamp of DataProtectLogicalUsageBytes.
        data_protect_physical_usage_bytes (long|int): Specifies the physical
            data used by Data Protect on Cohesity cluster.
        data_protect_physical_usage_bytes_timestamp_usec (long|int): Specifies
            Timestamp of DataProtectPhysicalUsageBytes.
        data_written_bytes (long|int): Specifies the data written after it has
            been reduced by deduplication and compression. This does not
            include resiliency impact.
        data_written_bytes_timestamp_usec (long|int): Specifies Timestamp of
            DataWrittenBytes.
        file_services_logical_usage_bytes (long|int): Specifies the logical
            data used by File services on Cohesity cluster.
        file_services_logical_usage_bytes_timestamp_usec (long|int): Specifies
            Timestamp of FileServicesLogicalUsageBytes.
        file_services_physical_usage_bytes (long|int): Specifies the physical
            data used by File services on Cohesity cluster.
        file_services_physical_usage_bytes_timestamp_usec (long|int):
            Specifies Timestamp of FileServicesPhysicalUsageBytes.
        local_data_written_bytes (long|int): Specifies the total data written
            on local tiers, as computed by the Cohesity Cluster, after the
            size of the data has been reduced by change-block tracking,
            deduplication and compression. This does not include resiliency
            impact.
        local_data_written_bytes_timestamp_usec (long|int): Specifies
            Timestamp of LocalDataWrittenBytes.
        local_tier_resiliency_impact_bytes (long|int): Specifies the size of
            the data has been replicated to other nodes as per RF or Erasure
            Coding policy.
        local_tier_resiliency_impact_bytes_timestamp_usec (long|int):
            Specifies Timestamp of LocalTierResiliencyImpactBytes.
        local_total_physical_usage_bytes (long|int): Specifies the total local
            capacity, as computed by the Cohesity Cluster, after the size of
            the data has been reduced by change-block tracking, compression
            and deduplication.
        local_total_physical_usage_bytes_timestamp_usec (long|int): Specifies
            Timestamp of LocalTotalPhysicalUsageBytes.
        outdated_logical_usage_bytes_timestamp_usec (long|int): Specifies
            Timestamp of OutdatedLogicalUsageBytes.
        storage_consumed_bytes (long|int): Specifies the total capacity, as
            computed by the Cohesity Cluster, after the size of the data has
            been reduced by change-block tracking, compression and
            deduplication. This includes resiliency impact.
        storage_consumed_bytes_timestamp_usec (long|int): Specifies Timestamp
            of StorageConsumedBytes.
        total_logical_usage_bytes (long|int): Provides the combined data
            residing on protected objects. The size of data before reduction
            by deduplication and compression.
        total_logical_usage_bytes_timestamp_usec (long|int): Specifies
            Timestamp of TotalLogicalUsageBytes.
        unique_physical_data_bytes (int): pecifies the unique physical data
            usage in bytes.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cloud_data_written_bytes":'cloudDataWrittenBytes',
        "cloud_data_written_bytes_timestamp_usec":'cloudDataWrittenBytesTimestampUsec',
        "cloud_total_physical_usage_bytes":'cloudTotalPhysicalUsageBytes',
        "cloud_total_physical_usage_bytes_timestamp_usec":'cloudTotalPhysicalUsageBytesTimestampUsec',
        "data_in_bytes":'dataInBytes',
        "data_in_bytes_after_dedup":'dataInBytesAfterDedup',
        "data_in_bytes_after_dedup_timestamp_usec":'dataInBytesAfterDedupTimestampUsec',
        "data_in_bytes_timestamp_usec":'dataInBytesTimestampUsec',
        "data_protect_logical_usage_bytes":'dataProtectLogicalUsageBytes',
        "data_protect_logical_usage_bytes_timestamp_usec":'dataProtectLogicalUsageBytesTimestampUsec',
        "data_protect_physical_usage_bytes":'dataProtectPhysicalUsageBytes',
        "data_protect_physical_usage_bytes_timestamp_usec":'dataProtectPhysicalUsageBytesTimestampUsec',
        "data_written_bytes":'dataWrittenBytes',
        "data_written_bytes_timestamp_usec":'dataWrittenBytesTimestampUsec',
        "file_services_logical_usage_bytes":'fileServicesLogicalUsageBytes',
        "file_services_logical_usage_bytes_timestamp_usec":'fileServicesLogicalUsageBytesTimestampUsec',
        "file_services_physical_usage_bytes":'fileServicesPhysicalUsageBytes',
        "file_services_physical_usage_bytes_timestamp_usec":'fileServicesPhysicalUsageBytesTimestampUsec',
        "local_data_written_bytes":'localDataWrittenBytes',
        "local_data_written_bytes_timestamp_usec":'localDataWrittenBytesTimestampUsec',
        "local_tier_resiliency_impact_bytes":'localTierResiliencyImpactBytes',
        "local_tier_resiliency_impact_bytes_timestamp_usec":'localTierResiliencyImpactBytesTimestampUsec',
        "local_total_physical_usage_bytes":'localTotalPhysicalUsageBytes',
        "local_total_physical_usage_bytes_timestamp_usec":'localTotalPhysicalUsageBytesTimestampUsec',
        "outdated_logical_usage_bytes_timestamp_usec":'outdatedLogicalUsageBytesTimestampUsec',
        "storage_consumed_bytes":'storageConsumedBytes',
        "storage_consumed_bytes_timestamp_usec":'storageConsumedBytesTimestampUsec',
        "total_logical_usage_bytes":'totalLogicalUsageBytes',
        "total_logical_usage_bytes_timestamp_usec":'totalLogicalUsageBytesTimestampUsec',
        "unique_physical_data_bytes":'uniquePhysicalDataBytes'
    }

    def __init__(self,
                 cloud_data_written_bytes=None,
                 cloud_data_written_bytes_timestamp_usec=None,
                 cloud_total_physical_usage_bytes=None,
                 cloud_total_physical_usage_bytes_timestamp_usec=None,
                 data_in_bytes=None,
                 data_in_bytes_after_dedup=None,
                 data_in_bytes_after_dedup_timestamp_usec=None,
                 data_in_bytes_timestamp_usec=None,
                 data_protect_logical_usage_bytes=None,
                 data_protect_logical_usage_bytes_timestamp_usec=None,
                 data_protect_physical_usage_bytes=None,
                 data_protect_physical_usage_bytes_timestamp_usec=None,
                 data_written_bytes=None,
                 data_written_bytes_timestamp_usec=None,
                 file_services_logical_usage_bytes=None,
                 file_services_logical_usage_bytes_timestamp_usec=None,
                 file_services_physical_usage_bytes=None,
                 file_services_physical_usage_bytes_timestamp_usec=None,
                 local_data_written_bytes=None,
                 local_data_written_bytes_timestamp_usec=None,
                 local_tier_resiliency_impact_bytes=None,
                 local_tier_resiliency_impact_bytes_timestamp_usec=None,
                 local_total_physical_usage_bytes=None,
                 local_total_physical_usage_bytes_timestamp_usec=None,
                 outdated_logical_usage_bytes_timestamp_usec=None,
                 storage_consumed_bytes=None,
                 storage_consumed_bytes_timestamp_usec=None,
                 total_logical_usage_bytes=None,
                 total_logical_usage_bytes_timestamp_usec=None,
                 unique_physical_data_bytes=None):
        """Constructor for the DataUsageStats class"""

        # Initialize members of the class
        self.cloud_data_written_bytes = cloud_data_written_bytes
        self.cloud_data_written_bytes_timestamp_usec = cloud_data_written_bytes_timestamp_usec
        self.cloud_total_physical_usage_bytes = cloud_total_physical_usage_bytes
        self.cloud_total_physical_usage_bytes_timestamp_usec = cloud_total_physical_usage_bytes_timestamp_usec
        self.data_in_bytes = data_in_bytes
        self.data_in_bytes_after_dedup = data_in_bytes_after_dedup
        self.data_in_bytes_after_dedup_timestamp_usec = data_in_bytes_after_dedup_timestamp_usec
        self.data_in_bytes_timestamp_usec = data_in_bytes_timestamp_usec
        self.data_protect_logical_usage_bytes = data_protect_logical_usage_bytes
        self.data_protect_logical_usage_bytes_timestamp_usec = data_protect_logical_usage_bytes_timestamp_usec
        self.data_protect_physical_usage_bytes = data_protect_physical_usage_bytes
        self.data_protect_physical_usage_bytes_timestamp_usec = data_protect_physical_usage_bytes_timestamp_usec
        self.data_written_bytes = data_written_bytes
        self.data_written_bytes_timestamp_usec = data_written_bytes_timestamp_usec
        self.file_services_logical_usage_bytes = file_services_logical_usage_bytes
        self.file_services_logical_usage_bytes_timestamp_usec = file_services_logical_usage_bytes_timestamp_usec
        self.file_services_physical_usage_bytes = file_services_physical_usage_bytes
        self.file_services_physical_usage_bytes_timestamp_usec = file_services_physical_usage_bytes_timestamp_usec
        self.local_data_written_bytes = local_data_written_bytes
        self.local_data_written_bytes_timestamp_usec = local_data_written_bytes_timestamp_usec
        self.local_tier_resiliency_impact_bytes = local_tier_resiliency_impact_bytes
        self.local_tier_resiliency_impact_bytes_timestamp_usec = local_tier_resiliency_impact_bytes_timestamp_usec
        self.local_total_physical_usage_bytes = local_total_physical_usage_bytes
        self.local_total_physical_usage_bytes_timestamp_usec = local_total_physical_usage_bytes_timestamp_usec
        self.outdated_logical_usage_bytes_timestamp_usec = outdated_logical_usage_bytes_timestamp_usec
        self.storage_consumed_bytes = storage_consumed_bytes
        self.storage_consumed_bytes_timestamp_usec = storage_consumed_bytes_timestamp_usec
        self.total_logical_usage_bytes = total_logical_usage_bytes
        self.total_logical_usage_bytes_timestamp_usec = total_logical_usage_bytes_timestamp_usec
        self.unique_physical_data_bytes = unique_physical_data_bytes


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
        cloud_data_written_bytes_timestamp_usec = dictionary.get('cloudDataWrittenBytesTimestampUsec')
        cloud_total_physical_usage_bytes = dictionary.get('cloudTotalPhysicalUsageBytes')
        cloud_total_physical_usage_bytes_timestamp_usec = dictionary.get('cloudTotalPhysicalUsageBytesTimestampUsec')
        data_in_bytes = dictionary.get('dataInBytes')
        data_in_bytes_after_dedup = dictionary.get('dataInBytesAfterDedup')
        data_in_bytes_after_dedup_timestamp_usec = dictionary.get('dataInBytesAfterDedupTimestampUsec')
        data_in_bytes_timestamp_usec = dictionary.get('dataInBytesTimestampUsec')
        data_protect_logical_usage_bytes = dictionary.get('dataProtectLogicalUsageBytes')
        data_protect_logical_usage_bytes_timestamp_usec = dictionary.get('dataProtectLogicalUsageBytesTimestampUsec')
        data_protect_physical_usage_bytes = dictionary.get('dataProtectPhysicalUsageBytes')
        data_protect_physical_usage_bytes_timestamp_usec = dictionary.get('dataProtectPhysicalUsageBytesTimestampUsec')
        data_written_bytes = dictionary.get('dataWrittenBytes')
        data_written_bytes_timestamp_usec = dictionary.get('dataWrittenBytesTimestampUsec')
        file_services_logical_usage_bytes = dictionary.get('fileServicesLogicalUsageBytes')
        file_services_logical_usage_bytes_timestamp_usec = dictionary.get('fileServicesLogicalUsageBytesTimestampUsec')
        file_services_physical_usage_bytes = dictionary.get('fileServicesPhysicalUsageBytes')
        file_services_physical_usage_bytes_timestamp_usec = dictionary.get('fileServicesPhysicalUsageBytesTimestampUsec')
        local_data_written_bytes = dictionary.get('localDataWrittenBytes')
        local_data_written_bytes_timestamp_usec = dictionary.get('localDataWrittenBytesTimestampUsec')
        local_tier_resiliency_impact_bytes = dictionary.get('localTierResiliencyImpactBytes')
        local_tier_resiliency_impact_bytes_timestamp_usec = dictionary.get('localTierResiliencyImpactBytesTimestampUsec')
        local_total_physical_usage_bytes = dictionary.get('localTotalPhysicalUsageBytes')
        local_total_physical_usage_bytes_timestamp_usec = dictionary.get('localTotalPhysicalUsageBytesTimestampUsec')
        outdated_logical_usage_bytes_timestamp_usec = dictionary.get('outdatedLogicalUsageBytesTimestampUsec')
        storage_consumed_bytes = dictionary.get('storageConsumedBytes')
        storage_consumed_bytes_timestamp_usec = dictionary.get('storageConsumedBytesTimestampUsec')
        total_logical_usage_bytes = dictionary.get('totalLogicalUsageBytes')
        total_logical_usage_bytes_timestamp_usec = dictionary.get('totalLogicalUsageBytesTimestampUsec')
        unique_physical_data_bytes = dictionary.get('uniquePhysicalDataBytes')

        # Return an object of this model
        return cls(cloud_data_written_bytes,
                   cloud_data_written_bytes_timestamp_usec,
                   cloud_total_physical_usage_bytes,
                   cloud_total_physical_usage_bytes_timestamp_usec,
                   data_in_bytes,
                   data_in_bytes_after_dedup,
                   data_in_bytes_after_dedup_timestamp_usec,
                   data_in_bytes_timestamp_usec,
                   data_protect_logical_usage_bytes,
                   data_protect_logical_usage_bytes_timestamp_usec,
                   data_protect_physical_usage_bytes,
                   data_protect_physical_usage_bytes_timestamp_usec,
                   data_written_bytes,
                   data_written_bytes_timestamp_usec,
                   file_services_logical_usage_bytes,
                   file_services_logical_usage_bytes_timestamp_usec,
                   file_services_physical_usage_bytes,
                   file_services_physical_usage_bytes_timestamp_usec,
                   local_data_written_bytes,
                   local_data_written_bytes_timestamp_usec,
                   local_tier_resiliency_impact_bytes,
                   local_tier_resiliency_impact_bytes_timestamp_usec,
                   local_total_physical_usage_bytes,
                   local_total_physical_usage_bytes_timestamp_usec,
                   outdated_logical_usage_bytes_timestamp_usec,
                   storage_consumed_bytes,
                   storage_consumed_bytes_timestamp_usec,
                   total_logical_usage_bytes,
                   total_logical_usage_bytes_timestamp_usec,
                   unique_physical_data_bytes)


