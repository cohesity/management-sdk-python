# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.aws_fleet_params_tag
import cohesity_management_sdk.models.aws_fleet_params_network_params

class AWSFleetParams(object):

    """Implementation of the 'AWSFleetParams' model.

    Params for AWS fleets deployment.

    Attributes:
        fleet_subnet_type (int): Fleet's subnet type. This field should always
            be set when specifying fleet params.
        fleet_tag_vec (list of AWSFleetParams_Tag):Optional list of tags to be
            associated with the fleets.
        network_params (AWSFleetParams_NetworkParams): This will be only set
            when fleet_subnet_type is kCustom.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "fleet_subnet_type":'fleetSubnetType',
        "fleet_tag_vec":'fleetTagVec',
        "network_params":'networkParams'
    }

    def __init__(self,
                 fleet_subnet_type=None,
                 fleet_tag_vec=None,
                 network_params=None):
        """Constructor for the AWSFleetParams class"""

        # Initialize members of the class
        self.fleet_subnet_type = fleet_subnet_type
        self.fleet_tag_vec = fleet_tag_vec
        self.network_params = network_params


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

        # Return an object of this model
        return cls(fleet_subnet_type,
                   fleet_tag_vec,
                   network_params)


