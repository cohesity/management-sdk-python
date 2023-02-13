# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class CouchbaseConnectParams(object):

    """Implementation of the 'CouchbaseConnectParams' model.

    Specifies an Object containing information about a registered couchbase
    source.

    Attributes:
    carrier_direct_port (int): Specifies the Carrier direct/sll port.
    http_direct_port (int): Specifies the HTTP direct/sll port.
    requires_ssl (bool): Specifies whether this cluster allows connection
        through SSL only.
    seeds (list of string): Specifies the Seeds of this Couchbase Cluster.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "carrier_direct_port": 'carrierDirectPort',
        "http_direct_port": 'httpDirectPort',
        "requires_ssl": 'requiresSsl',
        "seeds":'seeds'
    }

    def __init__(self,
                 carrier_direct_port=None,
                 http_direct_port=None,
                 requires_ssl=None,
                 seeds=None):
        """Constructor for the CouchbaseConnectParams class"""

        # Initialize members of the class
        self.carrier_direct_port = carrier_direct_port
        self.http_direct_port = http_direct_port
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
        carrier_direct_port = dictionary.get('carrierDirectPort')
        http_direct_port = dictionary.get('httpDirectPort')
        requires_ssl = dictionary.get('requiresSsl')
        seeds = dictionary.get('seeds')

        # Return an object of this model
        return cls(carrier_direct_port,
                   http_direct_port,
                   requires_ssl,
                   seeds)


