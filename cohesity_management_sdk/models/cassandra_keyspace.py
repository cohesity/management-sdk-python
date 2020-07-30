# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class CassandraKeyspace(object):

    """Implementation of the 'CassandraKeyspace' model.

    Specifies an Object containing information about a Cassandra Keyspace.

    Attributes:
    children_count (int): Number of documents in this bucket.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "children_count":'childrenCount'
    }

    def __init__(self,
                 children_count=None):
        """Constructor for the CassandraKeyspace class"""

        # Initialize members of the class
        self.children_count = children_count


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

        # Return an object of this model
        return cls(children_count)


