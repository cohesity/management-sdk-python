# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.fleet_network_params
import cohesity_management_sdk.models.fleet_tag

class FleetParams(object):

    """Implementation of the 'FleetParams' model.

    Specifies various resources when deploying a VM to Fleet instances.

    Attributes:
        fleet_network_params (FleetNetworkParams): Specifies the network
            params for the fleet.
        fleet_subnet_type (FleetSubnetTypeEnum): Specifies the subnet type
            of the fleet.
            Specifies the type of the fleet subnet.
            'kCluster' implies same subnet as of Cluster, valid only for Cloud
                Edition cluster.
            'kSourceVM' implies same subnet as of source vm.
            'kCustom' implies the custome subnet.
        fleet_tags (list of FleetTag): Specifies the tag information for the
            fleet.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "fleet_network_params":'fleetNetworkParams',
        "fleet_subnet_type":'fleetSubnetType',
        "fleet_tags":'fleetTags'
    }

    def __init__(self,
                 fleet_network_params=None,
                 fleet_subnet_type=None,
                 fleet_tags=None):
        """Constructor for the FleetParams class"""

        # Initialize members of the class
        self.fleet_network_params = fleet_network_params
        self.fleet_subnet_type = fleet_subnet_type
        self.fleet_tags = fleet_tags


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
        fleet_network_params = cohesity_management_sdk.models.fleet_network_params.FleetNetworkParams.from_dictionary(dictionary.get('fleetNetworkParams')) if dictionary.get('fleetNetworkParams') else None
        fleet_subnet_type = dictionary.get('fleetSubnetType')
        fleet_tags = None
        if dictionary.get('fleetTags') != None:
            fleet_tags = list()
            for structure in dictionary.get('fleetTags'):
                fleet_tags.append(cohesity_management_sdk.models.fleet_tag.FleetTag.from_dictionary(structure))

        # Return an object of this model
        return cls(fleet_network_params,
                   fleet_subnet_type,
                   fleet_tags)


