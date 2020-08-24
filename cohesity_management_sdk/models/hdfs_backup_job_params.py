# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class HdfsBackupJobParams(object):

    """Implementation of the 'HdfsBackupJobParams' model.

    Contains any additional hdfs environment specific backup params at the
    job level.

    Attributes:
    hdfs_pattern (list of string): Any path/Glob pattern from HDFS that is to
        protected.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "hdfs_pattern":'hdfsPattern'
    }

    def __init__(self,
                 hdfs_pattern=None):
        """Constructor for the HdfsBackupJobParams class"""

        # Initialize members of the class
        self.hdfs_pattern = hdfs_pattern


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
        hdfs_pattern = dictionary.get('hdfsPattern')

        # Return an object of this model
        return cls(hdfs_pattern)


