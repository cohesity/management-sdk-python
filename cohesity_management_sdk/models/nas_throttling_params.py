# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class NasThrottlingParams(object):

    """Implementation of the 'NasThrottlingParams' model.

    Message to capture throttling params for a NAS source.

    Attributes:
        max_parallelIo_full_percentage (int): This parameter indicates the
            maximum number of parallel read and write operations per volume
            for full backup as a percentage of gflag
            magneto_slave_nas_max_active_pack_tasks.
        max_parallel_io_incremental_percentage (int): This parameter
            indicates the maximum number of parallel read and write operations
            per volume for incremental backup as a percentage of gflag
          magneto_slave_nas_max_active_pack_tasks.
        max_parallel_metadata_fetch_full_percentage (int): This parameter
            indicates the maximum number of concurrent prefetch in diff
            streamer per volume for full backup as a percentage of gflag
            magneto_posix_diff_streamer_max_prefetch.
        max_parallel_metadata_fetch_incremental_percentage (int): This
            parameter indicates the maximum number of concurrent prefetch in
            diff streamer per volume for incremental backup as a percentage of
            gflag magneto_posix_diff_streamer_max_prefetch.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "max_parallelIo_full_percentage":'maxParallelIoFullPercentage',
        "max_parallel_io_incremental_percentage":'maxParallelIoIncrementalPercentage',
        "max_parallel_metadata_fetch_full_percentage":'maxParallelMetadataFetchFullPercentage',
        "max_parallel_metadata_fetch_incremental_percentage":'maxParallelMetadataFetchIncrementalPercentage'
    }

    def __init__(self,
                 max_parallelIo_full_percentage=None,
                 max_parallel_io_incremental_percentage=None,
                 max_parallel_metadata_fetch_full_percentage=None,
                 max_parallel_metadata_fetch_incremental_percentage=None):
        """Constructor for the NasThrottlingParams class"""

        # Initialize members of the class
        self.max_parallelIo_full_percentage = max_parallelIo_full_percentage
        self.max_parallel_io_incremental_percentage = max_parallel_io_incremental_percentage
        self.max_parallel_metadata_fetch_full_percentage = max_parallel_metadata_fetch_full_percentage
        self.max_parallel_metadata_fetch_incremental_percentage = max_parallel_metadata_fetch_incremental_percentage


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
        max_parallelIo_full_percentage = dictionary.get('maxParallelIoFullPercentage')
        max_parallel_io_incremental_percentage = dictionary.get('maxParallelIoIncrementalPercentage')
        max_parallel_metadata_fetch_full_percentage = dictionary.get('maxParallelMetadataFetchFullPercentage')
        max_parallel_metadata_fetch_incremental_percentage = dictionary.get('maxParallelMetadataFetchIncrementalPercentage')

        # Return an object of this model
        return cls(max_parallelIo_full_percentage,
                   max_parallel_io_incremental_percentage,
                   max_parallel_metadata_fetch_full_percentage,
                   max_parallel_metadata_fetch_incremental_percentage)


