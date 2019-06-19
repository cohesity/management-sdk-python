# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.subnet

class StaticRoute(object):

    """Implementation of the 'StaticRoute' model.

    Specifies the settings of a Static Route.

    Attributes:
        description (string): Specifies a description of the Static Route.
        is_update (bool): Specifies if the route is currently being updated on
            the Cohesity Cluster.
        network_interface_group (string): Specifies the group name of the
            network interfaces to use for communicating with the destination
            subnet.
        network_interface_ids (list of long|int): Array of Network Interface
            Ids.  Specifies the ids of the network interfaces to use for
            communicating with the destination subnet.
        subnet (Subnet): Specifies the destination subnet of the Static Route.
            The netmask can be specified by setting netmaskBits or netmaskIp4.
            The netmask can only be set using netmaskIp4 if the IP address is
            an IPv4 address.
        vlan_id (int): Specifies the ID of the VLAN to use for communication
            with the destination subnet.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "description":'description',
        "is_update":'isUpdate',
        "network_interface_group":'networkInterfaceGroup',
        "network_interface_ids":'networkInterfaceIds',
        "subnet":'subnet',
        "vlan_id":'vlanId'
    }

    def __init__(self,
                 description=None,
                 is_update=None,
                 network_interface_group=None,
                 network_interface_ids=None,
                 subnet=None,
                 vlan_id=None):
        """Constructor for the StaticRoute class"""

        # Initialize members of the class
        self.description = description
        self.is_update = is_update
        self.network_interface_group = network_interface_group
        self.network_interface_ids = network_interface_ids
        self.subnet = subnet
        self.vlan_id = vlan_id


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
        description = dictionary.get('description')
        is_update = dictionary.get('isUpdate')
        network_interface_group = dictionary.get('networkInterfaceGroup')
        network_interface_ids = dictionary.get('networkInterfaceIds')
        subnet = cohesity_management_sdk.models.subnet.Subnet.from_dictionary(dictionary.get('subnet')) if dictionary.get('subnet') else None
        vlan_id = dictionary.get('vlanId')

        # Return an object of this model
        return cls(description,
                   is_update,
                   network_interface_group,
                   network_interface_ids,
                   subnet,
                   vlan_id)


