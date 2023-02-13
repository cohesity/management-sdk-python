# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.network_pool

class IsilonAccessZone(object):

    """Implementation of the 'IsilonAccessZone' model.

    Specifies information about access zone in an Isilon Cluster.

    Attributes:
        groupnet (string): Specifies the groupnet name of the Isilon Access
            Zone.
        id (long|int): Specifies the id of the access zone.
        name (string): Specifies the name of the access zone.
        network_pools (list of NetworkPool): Specifies the network pools
            associated with the Isilon Access Zone.
        path (string): Specifies the path of the access zone in ifs. This
            should include the leading "/ifs/".

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "groupnet":'groupnet',
        "id":'id',
        "name":'name',
        "network_pools":'networkPools',
        "path":'path'
    }

    def __init__(self,
                 groupnet=None,
                 id=None,
                 name=None,
                 network_pools=None,
                 path=None):
        """Constructor for the IsilonAccessZone class"""

        # Initialize members of the class
        self.groupnet = groupnet
        self.id = id
        self.name = name
        self.network_pools = network_pools
        self.path = path


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
        groupnet = dictionary.get('groupnet')
        id = dictionary.get('id')
        name = dictionary.get('name')
        network_pools = None
        if dictionary.get('networkPools') != None:
            network_pools = list()
            for structure in dictionary.get('networkPools'):
                network_pools.append(cohesity_management_sdk.models.network_pool.NetworkPool.from_dictionary(structure))
        path = dictionary.get('path')

        # Return an object of this model
        return cls(groupnet,
                   id,
                   name,
                   network_pools,
                   path)


