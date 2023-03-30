# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class IpUnconfig(object):

    """Implementation of the 'IpUnconfig' model.

    Specifies the unconfiguration of an IP.


    Attributes:

        interface_name (string): The interface name.
        ip_family (int): IpFamily of this config.
        node_ids (list of long|int): Node ids.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "interface_name":'interfaceName',
        "ip_family":'ipFamily',
        "node_ids":'nodeIds',
    }
    def __init__(self,
                 interface_name=None,
                 ip_family=None,
                 node_ids=None,
            ):

        """Constructor for the IpUnconfig class"""

        # Initialize members of the class
        self.interface_name = interface_name
        self.ip_family = ip_family
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
        interface_name = dictionary.get('interfaceName')
        ip_family = dictionary.get('ipFamily')
        node_ids = dictionary.get("nodeIds")

        # Return an object of this model
        return cls(
            interface_name,
            ip_family,
            node_ids
)