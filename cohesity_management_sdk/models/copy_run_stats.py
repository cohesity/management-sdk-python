# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class CopyRunStats(object):

    """Implementation of the 'CopyRunStats' model.

    Stats for one copy task or aggregated stats of a Copy Run in a
    Protection Job Run.

    Attributes:
        end_time_usecs (long|int): Specifies the time when this replication
            ended. If not set, then the replication has not ended yet.
        is_incremental (bool): Specifies whether this archival is incremental
            for archival targets.
        logical_bytes_transferred (long|int): Specifies the number of logical
            bytes transferred for this replication so far. This value can
            never exceed the total logical size of the replicated view.
        logical_size_bytes (long|int): Specifies the total amount of logical
            data to be transferred for this replication.
        logical_transfer_rate_bps (long|int): Specifies average logical bytes
            transfer rate in bytes per second for archchival targets.
        physical_bytes_transferred (long|int): Specifies the number of
            physical bytes sent over the wire for replication targets.
        start_time_usecs (long|int): Specifies the time when this replication
            was started. If not set, then replication has not been started
            yet.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "end_time_usecs":'endTimeUsecs',
        "is_incremental":'isIncremental',
        "logical_bytes_transferred":'logicalBytesTransferred',
        "logical_size_bytes":'logicalSizeBytes',
        "logical_transfer_rate_bps":'logicalTransferRateBps',
        "physical_bytes_transferred":'physicalBytesTransferred',
        "start_time_usecs":'startTimeUsecs'
    }

    def __init__(self,
                 end_time_usecs=None,
                 is_incremental=None,
                 logical_bytes_transferred=None,
                 logical_size_bytes=None,
                 logical_transfer_rate_bps=None,
                 physical_bytes_transferred=None,
                 start_time_usecs=None):
        """Constructor for the CopyRunStats class"""

        # Initialize members of the class
        self.end_time_usecs = end_time_usecs
        self.is_incremental = is_incremental
        self.logical_bytes_transferred = logical_bytes_transferred
        self.logical_size_bytes = logical_size_bytes
        self.logical_transfer_rate_bps = logical_transfer_rate_bps
        self.physical_bytes_transferred = physical_bytes_transferred
        self.start_time_usecs = start_time_usecs


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
        end_time_usecs = dictionary.get('endTimeUsecs')
        is_incremental = dictionary.get('isIncremental')
        logical_bytes_transferred = dictionary.get('logicalBytesTransferred')
        logical_size_bytes = dictionary.get('logicalSizeBytes')
        logical_transfer_rate_bps = dictionary.get('logicalTransferRateBps')
        physical_bytes_transferred = dictionary.get('physicalBytesTransferred')
        start_time_usecs = dictionary.get('startTimeUsecs')

        # Return an object of this model
        return cls(end_time_usecs,
                   is_incremental,
                   logical_bytes_transferred,
                   logical_size_bytes,
                   logical_transfer_rate_bps,
                   physical_bytes_transferred,
                   start_time_usecs)


