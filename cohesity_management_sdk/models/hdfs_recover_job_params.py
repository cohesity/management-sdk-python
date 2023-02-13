# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class HdfsRecoverJobParams(object):

    """Implementation of the 'HdfsRecoverJobParams' model.

    Contains any additional hdfs environment specific params for the
    recover job.

    Attributes:
        hdfs_exclude_pattern (list of string): Any path/Glob pattern from HDFS
            that is to excluded.
        hdfs_recover_pattern (list of string): Any path/Glob pattern from HDFS
            that is to recovered.
        target_directory (string): A target directory where all the recovered
            entities are created
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "hdfs_exclude_pattern":'hdfsExcludePattern',
        "hdfs_recover_pattern":'hdfsRecoverPattern',
        "target_directory":'targetDirectory'
    }

    def __init__(self,
                 hdfs_exclude_pattern=None,
                 hdfs_recover_pattern=None,
                 target_directory=None):
        """Constructor for the HdfsRecoverJobParams class"""

        # Initialize members of the class
        self.hdfs_exclude_pattern = hdfs_exclude_pattern
        self.hdfs_recover_pattern = hdfs_recover_pattern
        self.target_directory = target_directory


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
        hdfs_exclude_pattern = dictionary.get('hdfsExcludePattern')
        hdfs_recover_pattern = dictionary.get('hdfsRecoverPattern')
        target_directory = dictionary.get('targetDirectory')

        # Return an object of this model
        return cls(hdfs_exclude_pattern,
                   hdfs_recover_pattern,
                   target_directory)


