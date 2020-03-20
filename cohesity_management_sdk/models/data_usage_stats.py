# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class DataUsageStats(object):

    """Implementation of the 'DataUsageStats' model.

    Specifies the data usage metric of the data stored on the Cohesity
    Cluster or Storage Domains (View Boxes).

    Attributes:
        data_in_bytes (long|int): Specifies the data brought into the cluster.
            This is the usage before data reduction.
        data_in_bytes_after_dedup (long|int): Specifies the the the size of
            the data has been reduced by change-block tracking and
            deduplication but before compression or data is replicated to
            other nodes as per RF or Erasure Coding policy.
        data_written_bytes (long|int): Specifies the total data written on
            local and cloud tiers, as computed by the Cohesity Cluster, after
            the size of the data has been reduced by change-block tracking,
            deduplication and compression. This does not include resiliency
            impact.
        local_data_written_bytes (long|int): Specifies the total data written
            on local tiers, as computed by the Cohesity Cluster, after the
            size of the data has been reduced by change-block tracking,
            deduplication and compression. This does not include resiliency
            impact.
        local_tier_resiliency_impact_bytes (long|int): Specifies the size of
            the data has been replicated to other nodes as per RF or Erasure
            Coding policy.
        storage_consumed_bytes (long|int): Specifies the total capacity, as
            computed by the Cohesity Cluster, after the size of the data has
            been reduced by change-block tracking, compression and
            deduplication. This includes resiliency impact.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "data_in_bytes":'dataInBytes',
        "data_in_bytes_after_dedup":'dataInBytesAfterDedup',
        "data_written_bytes":'dataWrittenBytes',
        "local_data_written_bytes":'localDataWrittenBytes',
        "local_tier_resiliency_impact_bytes":'localTierResiliencyImpactBytes',
        "storage_consumed_bytes":'storageConsumedBytes'
    }

    def __init__(self,
                 data_in_bytes=None,
                 data_in_bytes_after_dedup=None,
                 data_written_bytes=None,
                 local_data_written_bytes=None,
                 local_tier_resiliency_impact_bytes=None,
                 storage_consumed_bytes=None):
        """Constructor for the DataUsageStats class"""

        # Initialize members of the class
        self.data_in_bytes = data_in_bytes
        self.data_in_bytes_after_dedup = data_in_bytes_after_dedup
        self.data_written_bytes = data_written_bytes
        self.local_data_written_bytes = local_data_written_bytes
        self.local_tier_resiliency_impact_bytes = local_tier_resiliency_impact_bytes
        self.storage_consumed_bytes = storage_consumed_bytes


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
        data_in_bytes = dictionary.get('dataInBytes')
        data_in_bytes_after_dedup = dictionary.get('dataInBytesAfterDedup')
        data_written_bytes = dictionary.get('dataWrittenBytes')
        local_data_written_bytes = dictionary.get('localDataWrittenBytes')
        local_tier_resiliency_impact_bytes = dictionary.get('localTierResiliencyImpactBytes')
        storage_consumed_bytes = dictionary.get('storageConsumedBytes')

        # Return an object of this model
        return cls(data_in_bytes,
                   data_in_bytes_after_dedup,
                   data_written_bytes,
                   local_data_written_bytes,
                   local_tier_resiliency_impact_bytes,
                   storage_consumed_bytes)


