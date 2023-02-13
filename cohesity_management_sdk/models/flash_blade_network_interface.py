# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class FlashBladeNetworkInterface(object):

    """Implementation of the 'FlashBladeNetworkInterface' model.

    Specifies network interface detail of a Flash Blade Storage Array.

    Attributes:
        ip_address (string): Specifies the IP address of the Pure Storage
            FlashBlade Array.
        name (string): Specifies the name of the network interface.
        vlan (int): Specifies the id of the VLAN network of the Pure Storage
            FlashBlade Array.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ip_address":'ipAddress',
        "name":'name',
        "vlan":'vlan'
    }

    def __init__(self,
                 ip_address=None,
                 name=None,
                 vlan=None):
        """Constructor for the FlashBladeNetworkInterface class"""

        # Initialize members of the class
        self.ip_address = ip_address
        self.name = name
        self.vlan = vlan


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
        ip_address = dictionary.get('ipAddress')
        name = dictionary.get('name')
        vlan = dictionary.get('vlan')

        # Return an object of this model
        return cls(ip_address,
                   name,
                   vlan)


