# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.cluster_networking_resource_information

class NetworkingInformation(object):

    """Implementation of the 'NetworkingInformation' model.

    Specifies the struct containing information about network addresses
    configured on the given box. This is needed for dealing with
    Windows/Oracle
    Cluster resources that we discover and protect automatically.

    Attributes:
        resource_vec (list of ClusterNetworkingResourceInformation): The list
            of resources on the system that are accessible by an IP
            address.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "resource_vec":'resourceVec'
    }

    def __init__(self,
                 resource_vec=None):
        """Constructor for the NetworkingInformation class"""

        # Initialize members of the class
        self.resource_vec = resource_vec


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
        resource_vec = None
        if dictionary.get('resourceVec') != None:
            resource_vec = list()
            for structure in dictionary.get('resourceVec'):
                resource_vec.append(cohesity_management_sdk.models.cluster_networking_resource_information.ClusterNetworkingResourceInformation.from_dictionary(structure))

        # Return an object of this model
        return cls(resource_vec)


