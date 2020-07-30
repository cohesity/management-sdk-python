# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class MongoDBConnectParams(object):

    """Implementation of the 'MongoDBConnectParams' model.

    Specifies an Object containing information about a registered mongodb
    source.

    Attributes:
        authenticating_database_name (string): Specifies the Authenticating
            Database for this MongoDB cluster.
        has_authentication (bool): Specifies whether authentication is
            configured on this MongoDB cluster.
        requires_ssl (bool): Specifies whether connection is allowed through
            SSL only in this cluster.
        seeds (list of string): Specifies the seeds of this MongoDB Cluster.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "authenticating_database_name":'authenticatingDatabaseName',
        "has_authentication":'hasAuthentication',
        "requires_ssl":'requiresSsl',
        "seeds":'seeds'
    }

    def __init__(self,
                 authenticating_database_name=None,
                 has_authentication=None,
                 requires_ssl=None,
                 seeds=None):
        """Constructor for the MongoDBConnectParams class"""

        # Initialize members of the class
        self.authenticating_database_name = authenticating_database_name
        self.has_authentication = has_authentication
        self.requires_ssl = requires_ssl
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
        authenticating_database_name = dictionary.get('authenticatingDatabaseName')
        has_authentication = dictionary.get('hasAuthentication')
        requires_ssl = dictionary.get('requiresSsl')
        seeds = dictionary.get('seeds')

        # Return an object of this model
        return cls(authenticating_database_name,
                   has_authentication,
                   requires_ssl,
                   seeds)


