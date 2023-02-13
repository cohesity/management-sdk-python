# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class IpUnconfig(object):

    """Implementation of the 'IpUnconfig' model.

    Specifies the unconfiguration of an IP.

    Attributes:
        ip_family (int): IpFamily of this config.
        interface_name (string): The interface name.
        node_ids (list of int): Node ids.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ip_family":'IpFamily',
        "interface_name":'interfaceName',
        "node_ids":'nodeIds'
    }

    def __init__(self,
                 ip_family=None,
                 interface_name=None,
                 node_ids=None):
        """Constructor for the IpUnconfig class"""

        # Initialize members of the class
        self.ip_family = ip_family
        self.interface_name = interface_name
        self.node_ids = node_ids


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
        ip_family = dictionary.get('IpFamily')
        interface_name = dictionary.get('interfaceName')
        node_ids = dictionary.get('nodeIds')

        # Return an object of this model
        return cls(ip_family,
                   interface_name,
                   node_ids)


