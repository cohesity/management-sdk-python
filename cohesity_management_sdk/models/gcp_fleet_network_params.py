# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.fleet_network_params


class GcpFleetNetworkParams(object):

    """Implementation of the 'GcpFleetNetworkParams' model.

    TODO: type description here.


    Attributes:

        fleet_subnet_priority (GcpFleetSubnetPriorityEnum): Specifies the
            priority of the subnet type. Specifies the priority of the fleet
            subnet type for GCP. 'kPrimary' implies first priority to subnet
            type. 'kSecondary' implies second priority to subnet type.
            'kTertiary' implies third priority to subnet type.
        fleet_subnet_type (GcpFleetSubnetTypeEnum): Specifies the subnet type
            of the fleet. Specifies the type of the fleet subnet for GCP.
            'kCluster' implies same subnet as of Cluster (for CE and NGCE
            cluster). 'kSourceVM' implies same subnet as of source vm.
            'kCustom' implies the custome subnet.
        network_params_list (list of FleetNetworkParams): Specifies the list of
            network params for the fleet.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "fleet_subnet_priority":'fleetSubnetPriority',
        "fleet_subnet_type":'fleetSubnetType',
        "network_params_list":'networkParamsList',
    }
    def __init__(self,
                 fleet_subnet_priority=None,
                 fleet_subnet_type=None,
                 network_params_list=None,
            ):

        """Constructor for the GcpFleetNetworkParams class"""

        # Initialize members of the class
        self.fleet_subnet_priority = fleet_subnet_priority
        self.fleet_subnet_type = fleet_subnet_type
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
        fleet_subnet_priority = dictionary.get('fleetSubnetPriority')
        fleet_subnet_type = dictionary.get('fleetSubnetType')
        network_params_list = None
        if dictionary.get('networkParamsList') != None:
            network_params_list = list()
            for structure in dictionary.get('networkParamsList'):
                network_params_list.append(cohesity_management_sdk.models.fleet_network_params.FleetNetworkParams.from_dictionary(structure))

        # Return an object of this model
        return cls(
            fleet_subnet_priority,
            fleet_subnet_type,
            network_params_list
)