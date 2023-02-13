
# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class OutputSpec(object):

    """Implementation of the 'OutputSpec' model.

    Output specification for the mapreduce.

    Attributes:
        num_reduce_shards (int): Number of reduce shards.
        output_dir (string): Name of output directory.
        partition_id (long|int): Partition id where output will go.
        reduce_output_prefix (string): Prefix of the reduce output files. File
            names will be: ${reduce_output_prefix}-00000-of-00100 if
            num_reduce_shards=100 This name can contain some path components.
            e.g. "awb_results/run1" is a valid value. output_dir is
            deprecated.
        view_box_id (long|int): Viewbox id where the output will go.
        view_name (string): Name of the view where output will go. This will
            be filled up by yoda.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "num_reduce_shards":'numReduceShards',
        "output_dir":'outputDir',
        "partition_id":'partitionId',
        "reduce_output_prefix":'reduceOutputPrefix',
        "view_box_id":'viewBoxId',
        "view_name":'viewName'
    }

    def __init__(self,
                 num_reduce_shards=None,
                 output_dir=None,
                 partition_id=None,
                 reduce_output_prefix=None,
                 view_box_id=None,
                 view_name=None):
        """Constructor for the OutputSpec class"""

        # Initialize members of the class
        self.num_reduce_shards = num_reduce_shards
        self.output_dir = output_dir
        self.partition_id = partition_id
        self.reduce_output_prefix = reduce_output_prefix
        self.view_box_id = view_box_id
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
        num_reduce_shards = dictionary.get('numReduceShards')
        output_dir = dictionary.get('outputDir')
        partition_id = dictionary.get('partitionId')
        reduce_output_prefix = dictionary.get('reduceOutputPrefix')
        view_box_id = dictionary.get('viewBoxId')
        view_name = dictionary.get('viewName')

        # Return an object of this model
        return cls(num_reduce_shards,
                   output_dir,
                   partition_id,
                   reduce_output_prefix,
                   view_box_id,
                   view_name)


