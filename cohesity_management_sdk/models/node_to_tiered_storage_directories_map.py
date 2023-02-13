# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class NodeToTieredStorageDirectoriesMap(object):

    """Implementation of the 'NodeToTieredStorageDirectoriesMap' model.

    Mapping of each Cassandra node to a list of tiered storage directories.

    Attributes:
        cassandra_node_name (string): Name of the Cassandra node.
        tiered_storage_directories_vec (list of string): Array of tiered
            storage directories.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cassandra_node_name": 'cassandraNodeName',
        "tiered_storage_directories_vec": 'tieredStorageDirectoriesVec'
    }

    def __init__(self,
                 cassandra_node_name=None,
                 tiered_storage_directories_vec=None):
        """Constructor for the NodeToTieredStorageDirectoriesMap class"""

        # Initialize members of the class
        self.cassandra_node_name = cassandra_node_name
        self.tiered_storage_directories_vec = tiered_storage_directories_vec


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
        cassandra_node_name = dictionary.get('cassandraNodeName')
        tiered_storage_directories_vec = dictionary.get(
            'tieredStorageDirectoriesVec')

        # Return an object of this model
        return cls(cassandra_node_name,
                   tiered_storage_directories_vec)


