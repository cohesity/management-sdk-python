# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.org_vdc_network

class ListOrgVdcNetworksResponse(object):

    """Implementation of the 'ListOrgVdcNetworksResponse' model.

    Specifies the response returned when fetching a list of Org VDC Networks.

    Attributes:
        org_vdc_networks (list of OrgVdcNetwork): Specifies a list of Org VDC Networks.
            user.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "org_vdc_networks":'orgVdcNetworks'
    }

    def __init__(self,
                 org_vdc_networks=None):
        """Constructor for the ListOrgVdcNetworksResponse class"""

        # Initialize members of the class
        self.org_vdc_networks = org_vdc_networks


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
        org_vdc_networks = None
        if dictionary.get('orgVdcNetworks') != None:
            org_vdc_networks = list()
            for structure in dictionary.get('orgVdcNetworks'):
                org_vdc_networks.append(cohesity_management_sdk.models.org_vdc_network.OrgVdcNetwork.from_dictionary(structure))

        # Return an object of this model
        return cls(org_vdc_networks)


