# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.gcp_fleet_network_params


class GcpFleetParams(object):

    """Implementation of the 'GcpFleetParams' model.

    Specifies various resources when deploying a Fleet instance on GCP.


    Attributes:

        fleet_network_tags (list of string): Specifies the network tag
            information for the fleet.
        gcp_fleet_network_params_list (list of GcpFleetNetworkParams):
            Specifies the priority list of network params for the fleet.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "fleet_network_tags":'fleetNetworkTags',
        "gcp_fleet_network_params_list":'gcpFleetNetworkParamsList',
    }
    def __init__(self,
                 fleet_network_tags=None,
                 gcp_fleet_network_params_list=None,
            ):

        """Constructor for the GcpFleetParams class"""

        # Initialize members of the class
        self.fleet_network_tags = fleet_network_tags
        self.gcp_fleet_network_params_list = gcp_fleet_network_params_list

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
        fleet_network_tags = dictionary.get("fleetNetworkTags")
        gcp_fleet_network_params_list = None
        if dictionary.get('gcpFleetNetworkParamsList') != None:
            gcp_fleet_network_params_list = list()
            for structure in dictionary.get('gcpFleetNetworkParamsList'):
                gcp_fleet_network_params_list.append(cohesity_management_sdk.models.gcp_fleet_network_params.GcpFleetNetworkParams.from_dictionary(structure))

        # Return an object of this model
        return cls(
            fleet_network_tags,
            gcp_fleet_network_params_list
)