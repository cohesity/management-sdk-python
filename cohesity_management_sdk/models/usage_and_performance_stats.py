# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class UsageAndPerformanceStats(object):

    """Implementation of the 'UsageAndPerformanceStats' model.

    Provides usage and performance statistics
    for entities such as a disks, Nodes or Clusters.

    Attributes:
        data_in_bytes (long|int): Specifies the data read from the protected
            objects by the Cohesity Cluster before any data reduction using
            deduplication and compression.
        data_in_bytes_after_reduction (long|int): Morphed Usage before data is
            replicated to other nodes as per RF or Erasure Coding policy.
        min_usable_physical_capacity_bytes (long|int): Specifies the minimum
            usable capacity available after erasure coding or RF. This will
            only be populated for cluster. If a cluster has multiple Domains
            (View Boxes) with different RF or erasure coding, this metric will
            be computed using the scheme that will provide least saving.
        num_bytes_read (long|int): Provides the total number of bytes read in
            the last 30 seconds.
        num_bytes_written (long|int): Provides the total number of bytes
            written in the last 30 second.
        physical_capacity_bytes (long|int): Provides the total physical
            capacity in bytes of all the storage devices, after subtracting
            space reserved for cluster services
        read_ios (long|int): Provides the number of Read IOs that occurred in
            the last 30 seconds.
        read_latency_msecs (float): Provides the Read latency in milliseconds
            for the Read IOs that occurred during the last 30 seconds.
        system_capacity_bytes (long|int): Provides the total available
            capacity as computed by the Linux 'statfs' command.
        system_usage_bytes (long|int): Provides the usage of bytes, as
            computed by the Linux 'statfs' command, after the size of the data
            is reduced by change-block tracking, compression and
            deduplication.
        total_physical_raw_usage_bytes (long|int): Provides the usage of
            bytes, as computed by the Cohesity Cluster, before the size of the
            data is reduced by change-block tracking, compression and
            deduplication.
        total_physical_usage_bytes (long|int): Provides the data stored
            locally, after the data has been reduced by deduplication and
            compression, including the space required for honoring the
            resiliency settings (EC/RF).
        write_ios (long|int): Provides the number of Write IOs that occurred
            in the last 30 seconds.
        write_latency_msecs (float): Provides the Write latency in
            milliseconds for the Write IOs that occurred during the last 30
            seconds.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "data_in_bytes":'dataInBytes',
        "data_in_bytes_after_reduction":'dataInBytesAfterReduction',
        "min_usable_physical_capacity_bytes":'minUsablePhysicalCapacityBytes',
        "num_bytes_read":'numBytesRead',
        "num_bytes_written":'numBytesWritten',
        "physical_capacity_bytes":'physicalCapacityBytes',
        "read_ios":'readIos',
        "read_latency_msecs":'readLatencyMsecs',
        "system_capacity_bytes":'systemCapacityBytes',
        "system_usage_bytes":'systemUsageBytes',
        "total_physical_raw_usage_bytes":'totalPhysicalRawUsageBytes',
        "total_physical_usage_bytes":'totalPhysicalUsageBytes',
        "write_ios":'writeIos',
        "write_latency_msecs":'writeLatencyMsecs'
    }

    def __init__(self,
                 data_in_bytes=None,
                 data_in_bytes_after_reduction=None,
                 min_usable_physical_capacity_bytes=None,
                 num_bytes_read=None,
                 num_bytes_written=None,
                 physical_capacity_bytes=None,
                 read_ios=None,
                 read_latency_msecs=None,
                 system_capacity_bytes=None,
                 system_usage_bytes=None,
                 total_physical_raw_usage_bytes=None,
                 total_physical_usage_bytes=None,
                 write_ios=None,
                 write_latency_msecs=None):
        """Constructor for the UsageAndPerformanceStats class"""

        # Initialize members of the class
        self.data_in_bytes = data_in_bytes
        self.data_in_bytes_after_reduction = data_in_bytes_after_reduction
        self.min_usable_physical_capacity_bytes = min_usable_physical_capacity_bytes
        self.num_bytes_read = num_bytes_read
        self.num_bytes_written = num_bytes_written
        self.physical_capacity_bytes = physical_capacity_bytes
        self.read_ios = read_ios
        self.read_latency_msecs = read_latency_msecs
        self.system_capacity_bytes = system_capacity_bytes
        self.system_usage_bytes = system_usage_bytes
        self.total_physical_raw_usage_bytes = total_physical_raw_usage_bytes
        self.total_physical_usage_bytes = total_physical_usage_bytes
        self.write_ios = write_ios
        self.write_latency_msecs = write_latency_msecs


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
        data_in_bytes_after_reduction = dictionary.get('dataInBytesAfterReduction')
        min_usable_physical_capacity_bytes = dictionary.get('minUsablePhysicalCapacityBytes')
        num_bytes_read = dictionary.get('numBytesRead')
        num_bytes_written = dictionary.get('numBytesWritten')
        physical_capacity_bytes = dictionary.get('physicalCapacityBytes')
        read_ios = dictionary.get('readIos')
        read_latency_msecs = dictionary.get('readLatencyMsecs')
        system_capacity_bytes = dictionary.get('systemCapacityBytes')
        system_usage_bytes = dictionary.get('systemUsageBytes')
        total_physical_raw_usage_bytes = dictionary.get('totalPhysicalRawUsageBytes')
        total_physical_usage_bytes = dictionary.get('totalPhysicalUsageBytes')
        write_ios = dictionary.get('writeIos')
        write_latency_msecs = dictionary.get('writeLatencyMsecs')

        # Return an object of this model
        return cls(data_in_bytes,
                   data_in_bytes_after_reduction,
                   min_usable_physical_capacity_bytes,
                   num_bytes_read,
                   num_bytes_written,
                   physical_capacity_bytes,
                   read_ios,
                   read_latency_msecs,
                   system_capacity_bytes,
                   system_usage_bytes,
                   total_physical_raw_usage_bytes,
                   total_physical_usage_bytes,
                   write_ios,
                   write_latency_msecs)


