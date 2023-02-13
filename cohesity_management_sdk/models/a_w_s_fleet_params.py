# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.fleet_tag
import cohesity_management_sdk.models.fleet_network_params

class AwsFleetParams(object):

    """Implementation of the 'AwsFleetParams' model.

    Specifies various resources when deploying a VM to Fleet instances.

    Attributes:
        fleet_subnet_type (FleetSubnetTypeEnum): Specifies the subnet type of
            the fleet. Specifies the type of the fleet subnet. 'kCluster'
            implies same subnet as of Cluster, valid only for Cloud Edition
            cluster. 'kSourceVM' implies same subnet as of source vm.
            'kCustom' implies the custome subnet.
        fleet_tags (list of FleetTag): Specifies the tag information for the
            fleet.
        network_params_list (list of FleetNetworkParams): Specifies the list
            of network params for the fleet.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "fleet_subnet_type":'fleetSubnetType',
        "fleet_tags":'fleetTags',
        "network_params_list":'networkParamsList'
    }

    def __init__(self,
                 fleet_subnet_type=None,
                 fleet_tags=None,
                 network_params_list=None):
        """Constructor for the AwsFleetParams class"""

        # Initialize members of the class
        self.fleet_subnet_type = fleet_subnet_type
        self.fleet_tags = fleet_tags
        self.network_params_list = network_params_list


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
        fleet_subnet_type = dictionary.get('fleetSubnetType')
        fleet_tags = None
        if dictionary.get('fleetTags') != None:
            fleet_tags = list()
            for structure in dictionary.get('fleetTags'):
                fleet_tags.append(cohesity_management_sdk.models.fleet_tag.FleetTag.from_dictionary(structure))
        network_params_list = None
        if dictionary.get('networkParamsList') != None:
            network_params_list = list()
            for structure in dictionary.get('networkParamsList'):
                network_params_list.append(cohesity_management_sdk.models.fleet_network_params.FleetNetworkParams.from_dictionary(structure))

        # Return an object of this model
        return cls(fleet_subnet_type,
                   fleet_tags,
                   network_params_list)


