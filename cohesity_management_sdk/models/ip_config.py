# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class IpConfig(object):

    """Implementation of the 'IpConfig' model.

    Specifies the configuration of an IP.

    Attributes:
        interface_name (string): The interface name. Specifies which interface
            to assign IP to.
        ip_family (int): IpFamily of this config.
        ips (list of string): The interface ips.
        node_ids (list of int): Node ids.
        role (string): The interface role.
        subnet_gateway (string): The interface gateway.
        subnet_mask_bits (int): The interface subnet mask bits.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "interface_name": 'interfaceName',
        "ip_family": 'ipFamily',
        "ips": 'ips',
        "node_ids": 'nodeIds',
        "role":'role',
        "subnet_gateway":'subnetGateway',
        "subnet_mask_bits":'subnetMaskBits'
    }

    def __init__(self,
                 interface_name=None,
                 ip_family=None,
                 ips=None,
                 node_ids=None,
                 role=None,
                 subnet_gateway=None,
                 subnet_mask_bits=None):
        """Constructor for the IpConfig class"""

        # Initialize members of the class
        self.interface_name = interface_name
        self.ip_family = ip_family
        self.ips = ips
        self.node_ids = node_ids
        self.role = role
        self.subnet_gateway = subnet_gateway
        self.subnet_mask_bits = subnet_mask_bits

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
        interface_name = dictionary.get('interfaceName')
        ip_family = dictionary.get('ipFamily')
        ips = dictionary.get('ips')
        node_ids = dictionary.get('nodeIds')
        role = dictionary.get('role')
        subnet_gateway = dictionary.get('subnetGateway')
        subnet_mask_bits = dictionary.get('subnetMaskBits')

        # Return an object of this model
        return cls(interface_name,
                   ip_family,
                   ips,
                   node_ids,
                   role,
                   subnet_gateway,
                   subnet_mask_bits)


