# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.subnet

class ExternalClientSubnets(object):

    """Implementation of the 'ExternalClientSubnets' model.

    TODO: type model description here.

    Attributes:
        client_subnets (list of Subnet): Specifies the Client Subnets for the
            cluster.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "client_subnets":'clientSubnets'
    }

    def __init__(self,
                 client_subnets=None):
        """Constructor for the ExternalClientSubnets class"""

        # Initialize members of the class
        self.client_subnets = client_subnets


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
        client_subnets = None
        if dictionary.get('clientSubnets') != None:
            client_subnets = list()
            for structure in dictionary.get('clientSubnets'):
                client_subnets.append(cohesity_management_sdk.models.subnet.Subnet.from_dictionary(structure))

        # Return an object of this model
        return cls(client_subnets)


