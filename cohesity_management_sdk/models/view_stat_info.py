# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ViewStatInfo(object):

    """Implementation of the 'ViewStatInfo' model.

    Specifies the View stats per view.

    Attributes:
        cluster_id (long|int): Specifies the cluster Id.
        cluster_incarnation_id (long|int): Specifies the cluster Incarnation
            Id.
        data_read_bytes (long|int): Specifies the data read in bytes.
        data_written_bytes (long|int): Specifies the data written in bytes.
        logical_used_bytes (long|int): Specifies the logical size used in
            bytes.
        peak_read_throughput (long|int): Specifies the peak data read in bytes
            per second in the last day.
        peak_write_throughput (long|int): Specifies the peak data written in
            bytes per second in the last day.
        physical_used_bytes (long|int): Specifies the physical size used in
            bytes.
        protocols (list of ProtocolViewStatInfoEnum): Specifies the protocols
            of this view.
        storage_reduction_ratio (float): Specifies the storage reduction
            ratio.
        view_id (long|int): Specifies the view Id.
        view_name (string): Specifies the view name.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cluster_id":'clusterId',
        "cluster_incarnation_id":'clusterIncarnationId',
        "data_read_bytes":'dataReadBytes',
        "data_written_bytes":'dataWrittenBytes',
        "logical_used_bytes":'logicalUsedBytes',
        "peak_read_throughput":'peakReadThroughput',
        "peak_write_throughput":'peakWriteThroughput',
        "physical_used_bytes":'physicalUsedBytes',
        "protocols":'protocols',
        "storage_reduction_ratio":'storageReductionRatio',
        "view_id":'viewId',
        "view_name":'viewName'
    }

    def __init__(self,
                 cluster_id=None,
                 cluster_incarnation_id=None,
                 data_read_bytes=None,
                 data_written_bytes=None,
                 logical_used_bytes=None,
                 peak_read_throughput=None,
                 peak_write_throughput=None,
                 physical_used_bytes=None,
                 protocols=None,
                 storage_reduction_ratio=None,
                 view_id=None,
                 view_name=None):
        """Constructor for the ViewStatInfo class"""

        # Initialize members of the class
        self.cluster_id = cluster_id
        self.cluster_incarnation_id = cluster_incarnation_id
        self.data_read_bytes = data_read_bytes
        self.data_written_bytes = data_written_bytes
        self.logical_used_bytes = logical_used_bytes
        self.peak_read_throughput = peak_read_throughput
        self.peak_write_throughput = peak_write_throughput
        self.physical_used_bytes = physical_used_bytes
        self.protocols = protocols
        self.storage_reduction_ratio = storage_reduction_ratio
        self.view_id = view_id
        self.view_name = view_name


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
        cluster_id = dictionary.get('clusterId')
        cluster_incarnation_id = dictionary.get('clusterIncarnationId')
        data_read_bytes = dictionary.get('dataReadBytes')
        data_written_bytes = dictionary.get('dataWrittenBytes')
        logical_used_bytes = dictionary.get('logicalUsedBytes')
        peak_read_throughput = dictionary.get('peakReadThroughput')
        peak_write_throughput = dictionary.get('peakWriteThroughput')
        physical_used_bytes = dictionary.get('physicalUsedBytes')
        protocols = dictionary.get('protocols')
        storage_reduction_ratio = dictionary.get('storageReductionRatio')
        view_id = dictionary.get('viewId')
        view_name = dictionary.get('viewName')

        # Return an object of this model
        return cls(cluster_id,
                   cluster_incarnation_id,
                   data_read_bytes,
                   data_written_bytes,
                   logical_used_bytes,
                   peak_read_throughput,
                   peak_write_throughput,
                   physical_used_bytes,
                   protocols,
                   storage_reduction_ratio,
                   view_id,
                   view_name)


