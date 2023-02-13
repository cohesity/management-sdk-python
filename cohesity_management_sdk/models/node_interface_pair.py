# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class NodeInterfacePair(object):

    """Implementation of the 'NodeInterfacePair' model.

    Specifies a node ID and interface tuple.

    Attributes:
        iface_name (string): Specifies the name of the interface.
        node_id (long|int): Specifies list of node IDs.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "iface_name":'ifaceName',
        "node_id":'nodeId'
    }

    def __init__(self,
                 iface_name=None,
                 node_id=None):
        """Constructor for the NodeInterfacePair class"""

        # Initialize members of the class
        self.iface_name = iface_name
        self.node_id = node_id


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
        iface_name = dictionary.get('ifaceName')
        node_id = dictionary.get('nodeId')

        # Return an object of this model
        return cls(iface_name,
                   node_id)
