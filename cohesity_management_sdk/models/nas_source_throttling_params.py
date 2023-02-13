# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class NasSourceThrottlingParams(object):

    """Implementation of the 'NasSourceThrottlingParams' model.

    Specifies the NAS specific source throttling parameters during source
    registration or during backup of the source.

    Attributes:
        max_parallel_metadata_fetch_full_percentage (int): Specifies the
            percentage value of maximum concurrent metadata to be fetched
            during full backup of the source.
        max_parallel_metadata_fetch_incremental_percentage (int): Specifies
            the IPMI IP of the node (if physical cluster).
        max_parallel_read_write_full_percentage (int): Specifies the
            percentage value of maximum concurrent IO during full backup
        max_parallel_read_write_incremental_percentage (int): Specifies the
            percentage value of maximum concurrent IO during incremental
            backup of the source.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "max_parallel_metadata_fetch_full_percentage":'maxParallelMetadataFetchFullPercentage',
        "max_parallel_metadata_fetch_incremental_percentage":'maxParallelMetadataFetchIncrementalPercentage',
        "max_parallel_read_write_full_percentage":'maxParallelReadWriteFullPercentage',
        "max_parallel_read_write_incremental_percentage":'maxParallelReadWriteIncrementalPercentage'
    }

    def __init__(self,
                 max_parallel_metadata_fetch_full_percentage=None,
                 max_parallel_metadata_fetch_incremental_percentage=None,
                 max_parallel_read_write_full_percentage=None,
                 max_parallel_read_write_incremental_percentage=None):
        """Constructor for the NasSourceThrottlingParams class"""

        # Initialize members of the class
        self.max_parallel_metadata_fetch_full_percentage = max_parallel_metadata_fetch_full_percentage
        self.max_parallel_metadata_fetch_incremental_percentage = max_parallel_metadata_fetch_incremental_percentage
        self.max_parallel_read_write_full_percentage = max_parallel_read_write_full_percentage
        self.max_parallel_read_write_incremental_percentage = max_parallel_read_write_incremental_percentage


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
        max_parallel_metadata_fetch_full_percentage = dictionary.get('maxParallelMetadataFetchFullPercentage')
        max_parallel_metadata_fetch_incremental_percentage = dictionary.get('maxParallelMetadataFetchIncrementalPercentage')
        max_parallel_read_write_full_percentage = dictionary.get('maxParallelReadWriteFullPercentage')
        max_parallel_read_write_incremental_percentage = dictionary.get('maxParallelReadWriteIncrementalPercentage')

        # Return an object of this model
        return cls(max_parallel_metadata_fetch_full_percentage,
                   max_parallel_metadata_fetch_incremental_percentage,
                   max_parallel_read_write_full_percentage,
                   max_parallel_read_write_incremental_percentage)


