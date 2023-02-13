# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class DeleteRouteParam(object):

    """Implementation of the 'DeleteRouteParam' model.

    Specifies the delete param of a Static Route.

    Attributes:
        dest_network (string): Destination network.  Specifies the destination
            network of the Static Route. overrideDescription: true
        if_name (string): Specifies the network interfaces name to use for
            communicating with the destination network.
        iface_group_name (string): Specifies the network interfaces group or
            vlan interface group to use for communicating with the destination
            network.
        node_group_name (string): Specifies the network node group to represent
            a group of nodes.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "dest_network":'destNetwork',
        "if_name":'ifName',
        "iface_group_name":'ifaceGroupName',
        "node_group_name":'nodeGroupName'
    }

    def __init__(self,
                 dest_network=None,
                 if_name=None,
                 iface_group_name=None,
                 node_group_name=None):
        """Constructor for the DeleteRouteParam class"""

        # Initialize members of the class
        self.dest_network = dest_network
        self.if_name = if_name
        self.iface_group_name = iface_group_name
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
        dest_network = dictionary.get('destNetwork')
        if_name = dictionary.get('ifName')
        iface_group_name = dictionary.get('ifaceGroupName')
        node_group_name = dictionary.get('nodeGroupName')

        # Return an object of this model
        return cls(dest_network,
                   if_name,
                   iface_group_name,
                   node_group_name)


