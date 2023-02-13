# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.entity_proto

class NetworkMappingProto(object):

    """Implementation of the 'NetworkMappingProto' model.

    TODO: type model description here.

    Attributes:
        disable_network (bool): This can be set to true to indicate that the
            attached network should be left in disabled state. This value
            takes priority over the value in
            RestoredObjectNetworkConfigProto.
        preserve_mac_address_on_new_network (bool): VM's MAC address will be
            preserved on the new network. This value takes priority over the
            value in RestoredObjectNetworkConfigProto.
        source_network_entity (EntityProto): Specifies the attributes and the
            latest statistics about an entity.
        target_network_entity (EntityProto): Specifies the attributes and the
            latest statistics about an entity.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "disable_network":'disableNetwork',
        "preserve_mac_address_on_new_network":'preserveMacAddressOnNewNetwork',
        "source_network_entity":'sourceNetworkEntity',
        "target_network_entity":'targetNetworkEntity'
    }

    def __init__(self,
                 disable_network=None,
                 preserve_mac_address_on_new_network=None,
                 source_network_entity=None,
                 target_network_entity=None):
        """Constructor for the NetworkMappingProto class"""

        # Initialize members of the class
        self.disable_network = disable_network
        self.preserve_mac_address_on_new_network = preserve_mac_address_on_new_network
        self.source_network_entity = source_network_entity
        self.target_network_entity = target_network_entity


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
        preserve_mac_address_on_new_network = dictionary.get('preserveMacAddressOnNewNetwork')
        source_network_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('sourceNetworkEntity')) if dictionary.get('sourceNetworkEntity') else None
        target_network_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('targetNetworkEntity')) if dictionary.get('targetNetworkEntity') else None

        # Return an object of this model
        return cls(disable_network,
                   preserve_mac_address_on_new_network,
                   source_network_entity,
                   target_network_entity)


