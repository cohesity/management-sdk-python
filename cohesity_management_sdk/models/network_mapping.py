# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class NetworkMapping(object):

    """Implementation of the 'NetworkMapping' model.

    Specifies the information needed when mapping the source networks to
    target networks during restore and clone actions.

    Attributes:
        disable_network (bool): Specifies if the network should be disabled.
            On restore or clone of the VM, if the network should be kept in
            disabled state, set this flag to true. The mapped network is
            enabled by default.
        preserve_mac_address (bool): Specifies if the source mac address
            should be preserved after restore or clone. In case of collision
            of mac address on target network the job won't fail. Address
            collision should be resolved manually.
        source_network_id (long|int): Specifies the id of the source network.
        target_network_id (long|int): Specifies the id of target network.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "disable_network":'disableNetwork',
        "preserve_mac_address":'preserveMacAddress',
        "source_network_id":'sourceNetworkId',
        "target_network_id":'targetNetworkId'
    }

    def __init__(self,
                 disable_network=None,
                 preserve_mac_address=None,
                 source_network_id=None,
                 target_network_id=None):
        """Constructor for the NetworkMapping class"""

        # Initialize members of the class
        self.disable_network = disable_network
        self.preserve_mac_address = preserve_mac_address
        self.source_network_id = source_network_id
        self.target_network_id = target_network_id


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
        disable_network = dictionary.get('disableNetwork')
        preserve_mac_address = dictionary.get('preserveMacAddress')
        source_network_id = dictionary.get('sourceNetworkId')
        target_network_id = dictionary.get('targetNetworkId')

        # Return an object of this model
        return cls(disable_network,
                   preserve_mac_address,
                   source_network_id,
                   target_network_id)


