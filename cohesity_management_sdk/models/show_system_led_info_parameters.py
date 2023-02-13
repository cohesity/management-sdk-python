# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ShowSystemLedInfoParameters(object):

    """Implementation of the 'ShowSystemLedInfoParameters' model.

    Specifies the local or remote node for which system LED details
    are requested.

    Attributes:
        node_ip (string): Optional field. If Node IP is not specified, LED
            info for the current node is displayed.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "node_ip":'nodeIp'
    }

    def __init__(self,
                 node_ip=None):
        """Constructor for the ShowSystemLedInfoParameters class"""

        # Initialize members of the class
        self.node_ip = node_ip


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
        node_ip = dictionary.get('nodeIp')

        # Return an object of this model
        return cls(node_ip)


