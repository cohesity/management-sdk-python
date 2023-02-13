# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class CreateIpConfigParameters(object):

    """Implementation of the 'CreateIpConfigParameters' model.

    Specifies the parameters needed for an ipconfig request.

    Attributes:
        ips (list of string): Specifies the interface ips.
        mtu (int): Specifies the interface mtu.
        name (string): Specifies the interface name.
        role (RoleCreateIpConfigParametersEnum): Specifies the interface role.
            'kPrimary' indicates a primary role. 'kSecondary' indicates a
            secondary role.
        subnet_gateway (string): Specifies the interface gateway.
        subnet_mask (string): Specifies the interface subnet mask.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "ips":'ips',
        "mtu":'mtu',
        "role":'role',
        "subnet_gateway":'subnetGateway',
        "subnet_mask":'subnetMask'
    }

    def __init__(self,
                 name=None,
                 ips=None,
                 mtu=None,
                 role=None,
                 subnet_gateway=None,
                 subnet_mask=None):
        """Constructor for the CreateIpConfigParameters class"""

        # Initialize members of the class
        self.ips = ips
        self.mtu = mtu
        self.name = name
        self.role = role
        self.subnet_gateway = subnet_gateway
        self.subnet_mask = subnet_mask


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
        name = dictionary.get('name')
        ips = dictionary.get('ips')
        mtu = dictionary.get('mtu')
        role = dictionary.get('role')
        subnet_gateway = dictionary.get('subnetGateway')
        subnet_mask = dictionary.get('subnetMask')

        # Return an object of this model
        return cls(name,
                   ips,
                   mtu,
                   role,
                   subnet_gateway,
                   subnet_mask)


