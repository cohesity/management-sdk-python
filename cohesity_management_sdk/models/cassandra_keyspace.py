# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class CassandraKeyspace(object):

    """Implementation of the 'CassandraKeyspace' model.

    Specifies an Object containing information about a Cassandra Keyspace.

    Attributes:
    children_count (int): Number of documents in this bucket.
    dc_list (list of string): If the replication strategy is set as kNetwork,
        then dc_list will have a list of data centers to which the keyspace is
        being replicated to.
    replication_strategy (ReplicationStrategyEnum): Replication stragegy for
        the keyspace. Specifies the type of an Cassandra source entity.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "children_count":'childrenCount',
        "dc_list":'dcList',
        "replication_strategy":'replicationStrategy'
    }

    def __init__(self,
                 children_count=None,
                 dc_list=None,
                 replication_strategy=None):
        """Constructor for the CassandraKeyspace class"""

        # Initialize members of the class
        self.children_count = children_count
        self.dc_list = dc_list
        self.replication_strategy = replication_strategy


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
        children_count = dictionary.get('childrenCount')
        dc_list = dictionary.get('dcList')
        replication_strategy = dictionary.get('replicationStrategy')

        # Return an object of this model
        return cls(children_count,
                   dc_list,
                   replication_strategy)


