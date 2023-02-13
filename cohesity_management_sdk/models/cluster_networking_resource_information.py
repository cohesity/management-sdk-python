# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.cluster_networking_endpoint

class ClusterNetworkingResourceInformation(object):

    """Implementation of the 'ClusterNetworkingResourceInformation' model.

    Specifies a resource with IP address.

    Attributes:
        endpoints (list of ClusterNetworkingEndpoint): The endpoints by which
            the resource is accessible.
        mtype (string): The type of the resource.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "endpoints":'endpoints',
        "mtype":'type'
    }

    def __init__(self,
                 endpoints=None,
                 mtype=None):
        """Constructor for the ClusterNetworkingResourceInformation class"""

        # Initialize members of the class
        self.endpoints = endpoints
        self.mtype = mtype


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
        endpoints = None
        if dictionary.get('endpoints') != None:
            endpoints = list()
            for structure in dictionary.get('endpoints'):
                endpoints.append(cohesity_management_sdk.models.cluster_networking_endpoint.ClusterNetworkingEndpoint.from_dictionary(structure))
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(endpoints,
                   mtype)


