# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class GpfsCluster(object):

    """Implementation of the 'GpfsCluster' model.

    Specifies information about a GPFS Cluster.

    Attributes:
        ces_addresses (list of string): Specifies a list of CES(Cluster Export
            Services) IP addresses of a GPFS Cluster.
        id (int): Specifies a globally unique id of a GPFS Cluster.
        primary_server (string): Specifies a primary server of a GPFS
            Cluster.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ces_addresses":'cesAddresses',
        "id":'id',
        "primary_server":'primaryServer'
    }

    def __init__(self,
                 ces_addresses=None,
                 id=None,
                 primary_server=None):
        """Constructor for the GpfsCluster class"""

        # Initialize members of the class
        self.ces_addresses = ces_addresses
        self.id = id
        self.primary_server = primary_server


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
        ces_addresses = dictionary.get('cesAddresses')
        id = dictionary.get('id')
        primary_server = dictionary.get('primaryServer')

        # Return an object of this model
        return cls(ces_addresses,
                   id,
                   primary_server)


