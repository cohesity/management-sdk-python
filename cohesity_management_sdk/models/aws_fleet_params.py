# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.aws_fleet_params_tag
import cohesity_management_sdk.models.aws_fleet_params_network_params
import cohesity_management_sdk.models.aws_fleet_params_network_params_map_entry

class AWSFleetParams(object):

    """Implementation of the 'AWSFleetParams' model.

    Params for AWS fleets deployment.

    Attributes:
        fleet_subnet_type (int): Fleet's subnet type. This field should always
            be set when specifying fleet params.
        fleet_tag_vec (list of AWSFleetParams_Tag):Optional list of tags to be
            associated with the fleets.
        network_params (AWSFleetParams_NetworkParams): Network information for
            the fleet. This will be only set when fleet_subnet_type is kCustom.
        network_params_map (list of AWSFleetParams_NetworkParamsMapEntry): Map
            for a region to network params, as network params can be defined
            per region. Only set when kCustom fleet subnet type is being used.
        network_params_vec (list of AWSFleetParams_NetworkParams): Network
            information for the fleet. This will be only set when
            fleet_subnet_type is kCustom.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "fleet_subnet_type":'fleetSubnetType',
        "fleet_tag_vec":'fleetTagVec',
        "network_params":'networkParams',
        "network_params_map":'networkParamsMap',
        "network_params_vec":'networkParamsVec'
    }

    def __init__(self,
                 fleet_subnet_type=None,
                 fleet_tag_vec=None,
                 network_params=None,
                 network_params_map=None,
                 network_params_vec=None):
        """Constructor for the AWSFleetParams class"""

        # Initialize members of the class
        self.fleet_subnet_type = fleet_subnet_type
        self.fleet_tag_vec = fleet_tag_vec
        self.network_params = network_params
        self.network_params_map = network_params_map
        self.network_params_vec = network_params_vec


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
        fleet_tag_vec = None
        if dictionary.get('fleetTagVec') != None:
            fleet_tag_vec = list()
            for structure in dictionary.get('fleetTagVec'):
                fleet_tag_vec.append(cohesity_management_sdk.models.aws_fleet_params_tag.AWSFleetParams_Tag.from_dictionary(structure))
        network_params = cohesity_management_sdk.models.aws_fleet_params_network_params.AWSFleetParams_NetworkParams.from_dictionary(dictionary.get('networkParams')) if dictionary.get('networkParams') else None
        network_params_map = None
        if dictionary.get('networkParamsMap') != None:
            network_params_map = list()
            for structure in dictionary.get('networkParamsMap'):
                network_params_map.append(cohesity_management_sdk.models.aws_fleet_params_network_params_map_entry.AWSFleetParams_NetworkParamsMapEntry.from_dictionary(structure))
        network_params_vec = None
        if dictionary.get('networkParamsVec') != None:
            network_params_vec = list()
            for structure in dictionary.get('networkParamsVec'):
                network_params_vec.append(cohesity_management_sdk.models.aws_fleet_params_network_params.AWSFleetParams_NetworkParams.from_dictionary(structure))

        # Return an object of this model
        return cls(fleet_subnet_type,
                   fleet_tag_vec,
                   network_params,
                   network_params_map,
                   network_params_vec)


