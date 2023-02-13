# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.sample

class StorageEfficiencyTile(object):

    """Implementation of the 'StorageEfficiencyTile' model.

    StorageEfficiencyTile gives tile information for the storage saved
    because of compression and dedupe done on the cluster.

    Attributes:
        data_in_bytes (long|int): Specifies the size of data brought into the
            cluster. This is the usage before data reduction if we ignore the
            zeroes and effects of cloning.
        data_in_bytes_samples (list of Sample): Specifies the samples taken
            for Data brought into the cluster in bytes in ascending order of
            time.
        data_in_deduped_bytes (long|int): Specifies the size of data after
            compression and or dedupe operations just before the data is
            replicated to other nodes as per RF or Erasure Coding policy.
        data_in_deduped_bytes_samples (list of Sample): Specifies the samples
            taken for morphed data in bytes in ascending order of time.
        dedupe_ratio (float): Specifies the current dedupe ratio on the
            cluster. It is the ratio of DataInBytes to DataInDedupedBytes.
        dedupe_ratio_samples (list of Sample): Specifies the samples for data
            reduction ratio in ascending order of time.
        duration_days (int): Specifies the duration in days in which the
            samples were taken. For this tile, it is 7 days.
        interval_seconds (int): Specifies the interval between the samples in
            seconds. For this tile, it is 1 day which is 86400 seconds.
        logical_used_bytes (long|int): Specifies the size of logical data
            currently represented on the cluster.
        logical_used_bytes_samples (list of Sample): Specifies the samples
            taken for logical data represented in bytes in ascending order of
            time.
        physical_used_bytes (long|int): Specifies the size of physical data
            currently consumed on the cluster.
        physical_used_bytes_samples (list of Sample): Specifies the samples
            taken for physical data consumed in bytes in ascending order of
            time.
        storage_reduction_ratio (float): Specifies the current storage
            reduction ratio on the cluster. It is the ratio of
            LogicalUsedBytes to PhysicalUsedBytes.
        storage_reduction_samples (list of Sample): Specifies the samples for
            storage reduction ratio in ascending order of time.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "data_in_bytes":'dataInBytes',
        "data_in_bytes_samples":'dataInBytesSamples',
        "data_in_deduped_bytes":'dataInDedupedBytes',
        "data_in_deduped_bytes_samples":'dataInDedupedBytesSamples',
        "dedupe_ratio":'dedupeRatio',
        "dedupe_ratio_samples":'dedupeRatioSamples',
        "duration_days":'durationDays',
        "interval_seconds":'intervalSeconds',
        "logical_used_bytes":'logicalUsedBytes',
        "logical_used_bytes_samples":'logicalUsedBytesSamples',
        "physical_used_bytes":'physicalUsedBytes',
        "physical_used_bytes_samples":'physicalUsedBytesSamples',
        "storage_reduction_ratio":'storageReductionRatio',
        "storage_reduction_samples":'storageReductionSamples'
    }

    def __init__(self,
                 data_in_bytes=None,
                 data_in_bytes_samples=None,
                 data_in_deduped_bytes=None,
                 data_in_deduped_bytes_samples=None,
                 dedupe_ratio=None,
                 dedupe_ratio_samples=None,
                 duration_days=None,
                 interval_seconds=None,
                 logical_used_bytes=None,
                 logical_used_bytes_samples=None,
                 physical_used_bytes=None,
                 physical_used_bytes_samples=None,
                 storage_reduction_ratio=None,
                 storage_reduction_samples=None):
        """Constructor for the StorageEfficiencyTile class"""

        # Initialize members of the class
        self.data_in_bytes = data_in_bytes
        self.data_in_bytes_samples = data_in_bytes_samples
        self.data_in_deduped_bytes = data_in_deduped_bytes
        self.data_in_deduped_bytes_samples = data_in_deduped_bytes_samples
        self.dedupe_ratio = dedupe_ratio
        self.dedupe_ratio_samples = dedupe_ratio_samples
        self.duration_days = duration_days
        self.interval_seconds = interval_seconds
        self.logical_used_bytes = logical_used_bytes
        self.logical_used_bytes_samples = logical_used_bytes_samples
        self.physical_used_bytes = physical_used_bytes
        self.physical_used_bytes_samples = physical_used_bytes_samples
        self.storage_reduction_ratio = storage_reduction_ratio
        self.storage_reduction_samples = storage_reduction_samples


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
        data_in_bytes_samples = None
        if dictionary.get('dataInBytesSamples') != None:
            data_in_bytes_samples = list()
            for structure in dictionary.get('dataInBytesSamples'):
                data_in_bytes_samples.append(cohesity_management_sdk.models.sample.Sample.from_dictionary(structure))
        data_in_deduped_bytes = dictionary.get('dataInDedupedBytes')
        data_in_deduped_bytes_samples = None
        if dictionary.get('dataInDedupedBytesSamples') != None:
            data_in_deduped_bytes_samples = list()
            for structure in dictionary.get('dataInDedupedBytesSamples'):
                data_in_deduped_bytes_samples.append(cohesity_management_sdk.models.sample.Sample.from_dictionary(structure))
        dedupe_ratio = dictionary.get('dedupeRatio')
        dedupe_ratio_samples = None
        if dictionary.get('dedupeRatioSamples') != None:
            dedupe_ratio_samples = list()
            for structure in dictionary.get('dedupeRatioSamples'):
                dedupe_ratio_samples.append(cohesity_management_sdk.models.sample.Sample.from_dictionary(structure))
        duration_days = dictionary.get('durationDays')
        interval_seconds = dictionary.get('intervalSeconds')
        logical_used_bytes = dictionary.get('logicalUsedBytes')
        logical_used_bytes_samples = None
        if dictionary.get('logicalUsedBytesSamples') != None:
            logical_used_bytes_samples = list()
            for structure in dictionary.get('logicalUsedBytesSamples'):
                logical_used_bytes_samples.append(cohesity_management_sdk.models.sample.Sample.from_dictionary(structure))
        physical_used_bytes = dictionary.get('physicalUsedBytes')
        physical_used_bytes_samples = None
        if dictionary.get('physicalUsedBytesSamples') != None:
            physical_used_bytes_samples = list()
            for structure in dictionary.get('physicalUsedBytesSamples'):
                physical_used_bytes_samples.append(cohesity_management_sdk.models.sample.Sample.from_dictionary(structure))
        storage_reduction_ratio = dictionary.get('storageReductionRatio')
        storage_reduction_samples = None
        if dictionary.get('storageReductionSamples') != None:
            storage_reduction_samples = list()
            for structure in dictionary.get('storageReductionSamples'):
                storage_reduction_samples.append(cohesity_management_sdk.models.sample.Sample.from_dictionary(structure))

        # Return an object of this model
        return cls(data_in_bytes,
                   data_in_bytes_samples,
                   data_in_deduped_bytes,
                   data_in_deduped_bytes_samples,
                   dedupe_ratio,
                   dedupe_ratio_samples,
                   duration_days,
                   interval_seconds,
                   logical_used_bytes,
                   logical_used_bytes_samples,
                   physical_used_bytes,
                   physical_used_bytes_samples,
                   storage_reduction_ratio,
                   storage_reduction_samples)


