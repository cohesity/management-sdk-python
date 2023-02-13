# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class CouchbaseCluster(object):

    """Implementation of the 'CouchbaseCluster' model.

    Specifies an Object containing information about a couchbase cluster.

    Attributes:
    seeds (list of string): Seeds of this Couchbase Cluster.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "seeds":'seeds'
    }

    def __init__(self,
                 seeds=None):
        """Constructor for the CouchbaseCluster class"""

        # Initialize members of the class
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
        seeds = dictionary.get('seeds')

        # Return an object of this model
        return cls(seeds)


