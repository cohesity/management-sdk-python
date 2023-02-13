# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.network_mapping_proto
import cohesity_management_sdk.models.entity_proto
import cohesity_management_sdk.models.org_v_d_c_network

class RestoredObjectNetworkConfigProto(object):

    """Implementation of the 'RestoredObjectNetworkConfigProto' model.

    TODO: type model description here.

    Attributes:
        detach_network (bool): If this is set to true, then the network will
            be detached from the recovered or cloned VMs. NOTE: If this is set
            to true, then all the following fields will be ignored.
        disable_network (bool): This can be set to true to indicate that the
            attached network should be left in disabled state.
        mappings (list of NetworkMappingProto): The network mappings to be
            applied to the target object.
        network_entity (EntityProto): Specifies the attributes and the latest
            statistics about an entity.
        preserve_mac_address_on_new_network (bool): If this is true and we are
            attaching to a new network entity, then the VM's MAC address will
            be preserved on the new network.
        vcd_network (OrgVDCNetwork): This will be populated for
            kVirtualDatacenter.
        vnic_entity (EntityProto): Specifies the attributes and the latest
            statistics about an entity.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "detach_network":'detachNetwork',
        "disable_network":'disableNetwork',
        "mappings":'mappings',
        "network_entity":'networkEntity',
        "preserve_mac_address_on_new_network":'preserveMacAddressOnNewNetwork',
        "vcd_network":'vcdNetwork',
        "vnic_entity":'vnicEntity'
    }

    def __init__(self,
                 detach_network=None,
                 disable_network=None,
                 mappings=None,
                 network_entity=None,
                 preserve_mac_address_on_new_network=None,
                 vcd_network=None,
                 vnic_entity=None):
        """Constructor for the RestoredObjectNetworkConfigProto class"""

        # Initialize members of the class
        self.detach_network = detach_network
        self.disable_network = disable_network
        self.mappings = mappings
        self.network_entity = network_entity
        self.preserve_mac_address_on_new_network = preserve_mac_address_on_new_network
        self.vcd_network = vcd_network
        self.vnic_entity = vnic_entity


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
        detach_network = dictionary.get('detachNetwork')
        disable_network = dictionary.get('disableNetwork')
        mappings = None
        if dictionary.get('mappings') != None:
            mappings = list()
            for structure in dictionary.get('mappings'):
                mappings.append(cohesity_management_sdk.models.network_mapping_proto.NetworkMappingProto.from_dictionary(structure))
        network_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('networkEntity')) if dictionary.get('networkEntity') else None
        preserve_mac_address_on_new_network = dictionary.get('preserveMacAddressOnNewNetwork')
        vcd_network = cohesity_management_sdk.models.org_v_d_c_network.OrgVDCNetwork.from_dictionary(dictionary.get('vcdNetwork')) if dictionary.get('vcdNetwork') else None
        vnic_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('vnicEntity')) if dictionary.get('vnicEntity') else None

        # Return an object of this model
        return cls(detach_network,
                   disable_network,
                   mappings,
                   network_entity,
                   preserve_mac_address_on_new_network,
                   vcd_network,
                   vnic_entity)


