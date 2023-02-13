# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class CassandraCluster(object):

    """Implementation of the 'CassandraCluster' model.

    Specifies an Object containing information about a Cassandra cluster.

    Attributes:
    primary_host (string): Primary host from this Cassandra cluster.
    seeds (list of string): Seeds of this Cassandra Cluster.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "primary_host":'primaryHost',
        "seeds":'seeds'
    }

    def __init__(self,
                 primary_host=None,
                 seeds=None):
        """Constructor for the CassandraCluster class"""

        # Initialize members of the class
        self.primary_host = primary_host
        self.seeds = seeds


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
        primary_host = dictionary.get('primaryHost')
        seeds = dictionary.get('seeds')

        # Return an object of this model
        return cls(primary_host,
                   seeds)


