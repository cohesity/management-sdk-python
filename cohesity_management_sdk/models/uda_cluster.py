# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class UdaCluster(object):

    """Implementation of the 'UdaCluster' model.

    Specifies an Object containing information about a Universal Data Adapter
    cluster.

    Attributes:
        hosts (list of string): Hosts of this Universal Data Adapter Cluster.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "hosts":'hosts'
    }

    def __init__(self,
                 hosts=None):
        """Constructor for the UdaCluster class"""

        # Initialize members of the class
        self.hosts = hosts


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
        hosts = dictionary.get('hosts')

        # Return an object of this model
        return cls(hosts)


