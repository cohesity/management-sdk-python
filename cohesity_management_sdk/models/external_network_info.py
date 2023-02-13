# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ExternalNetworkInfo(object):

    """Implementation of the 'ExternalNetworkInfo' model.

    This is used to display the list of external networks, from which one can
    potentially be selected for an app instance.

    Attributes:
        axon_network_name (string): Name of axon network corresponding to this
            external network. Used for internal purposes only.
        vlan_id (int): VLAN id of the network.
        vlan_network_name (string): Display name for the UI to select the
            external network.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "axon_network_name":'axonNetworkName',
        "vlan_id":'vlanId',
        "vlan_network_name":'vlanNetworkName'
    }

    def __init__(self,
                 axon_network_name=None,
                 vlan_id=None,
                 vlan_network_name=None):
        """Constructor for the ExternalNetworkInfo class"""

        # Initialize members of the class
        self.axon_network_name = axon_network_name
        self.vlan_id = vlan_id
        self.vlan_network_name = vlan_network_name


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
        axon_network_name = dictionary.get('axonNetworkName')
        vlan_id = dictionary.get('vlanId')
        vlan_network_name = dictionary.get('vlanNetworkName')

        # Return an object of this model
        return cls(axon_network_name,
                   vlan_id,
                   vlan_network_name)


