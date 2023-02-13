# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class Route(object):

    """Implementation of the 'Route' model.

    Specifies the settings of a Static Route.

    Attributes:
        description (string): Specifies a description of the Static Route.
        dest_network (string): Destination network.  Specifies the destination
            network of the Static Route. overrideDescription: true
        if_name (string): Specifies the network interfaces name to use for
            communicating with the destination network.
        iface_group_name (string): Specifies the network interfaces group or
            interface group with vlan id to use for communicating with the
            destination network.
        mtu (int): Specifies MTU setting per route.
        next_hop (string): Specifies the next hop to the destination network.
        node_group_name (string): Specifies the network node group to
            represent a group of nodes.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "description":'description',
        "dest_network":'destNetwork',
        "if_name":'ifName',
        "iface_group_name":'ifaceGroupName',
        "mtu":'mtu',
        "next_hop":'nextHop',
        "node_group_name":'nodeGroupName'
    }

    def __init__(self,
                 description=None,
                 dest_network=None,
                 if_name=None,
                 iface_group_name=None,
                 mtu=None,
                 next_hop=None,
                 node_group_name=None):
        """Constructor for the Route class"""

        # Initialize members of the class
        self.description = description
        self.dest_network = dest_network
        self.if_name = if_name
        self.iface_group_name = iface_group_name
        self.mtu = mtu
        self.next_hop = next_hop
        self.node_group_name = node_group_name


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
        dest_network = dictionary.get('destNetwork')
        if_name = dictionary.get('ifName')
        iface_group_name = dictionary.get('ifaceGroupName')
        mtu = dictionary.get('mtu')
        next_hop = dictionary.get('nextHop')
        node_group_name = dictionary.get('nodeGroupName')

        # Return an object of this model
        return cls(description,
                   dest_network,
                   if_name,
                   iface_group_name,
                   mtu,
                   next_hop,
                   node_group_name)


