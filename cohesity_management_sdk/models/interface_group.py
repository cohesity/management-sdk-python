# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.product_model_interface_tuple
import cohesity_management_sdk.models.network_params
import cohesity_management_sdk.models.node_interface_pair

class InterfaceGroup(object):

    """Implementation of the 'InterfaceGroup' model.

    Specifies the settings of an interface group.

    Attributes:
        group_type (int): Specifies node group type.
        id (int): Interface group Id.  Specifies the id of the interface
            group.
        model_interface_lists (list of ProductModelInterfaceTuple): Specifies
            the product model and interface lists.
        name (string): Specifies the name of the interface group.
        network_params (NetworkParams): TODO: type description here.
        node_interface_pairs (list of NodeInterfacePair): Specifies the node
            IDs and interface lists.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "group_type":'groupType',
        "id":'id',
        "model_interface_lists":'modelInterfaceLists',
        "name":'name',
        "network_params":'networkParams',
        "node_interface_pairs":'nodeInterfacePairs'

    }

    def __init__(self,
                 group_type=None,
                 id=None,
                 model_interface_lists=None,
                 name=None,
                 network_params=None,
                 node_interface_pairs=None):
        """Constructor for the InterfaceGroup class"""

        # Initialize members of the class
        self.group_type = group_type
        self.id = id
        self.model_interface_lists = model_interface_lists
        self.name = name
        self.network_params = network_params
        self.node_interface_pairs = node_interface_pairs


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
        group_type = dictionary.get('groupType')
        id = dictionary.get('id')
        model_interface_lists = None
        if dictionary.get('modelInterfaceLists') != None:
            model_interface_lists = list()
            for structure in dictionary.get('modelInterfaceLists'):
                model_interface_lists.append(cohesity_management_sdk.models.product_model_interface_tuple.ProductModelInterfaceTuple.from_dictionary(structure))
        name = dictionary.get('name')
        network_params = cohesity_management_sdk.models.network_params.NetworkParams.from_dictionary(dictionary.get('networkParams')) if dictionary.get('networkParams') else None
        node_interface_pairs = None
        if dictionary.get('nodeInterfacePairs') != None:
            node_interface_pairs = list()
            for structure in dictionary.get('nodeInterfacePairs'):
                node_interface_pairs.append(cohesity_management_sdk.models.node_interface_pair.NodeInterfacePair.from_dictionary(structure))

        # Return an object of this model
        return cls(group_type,
                   id,
                   model_interface_lists,
                   name,
                   network_params,
                   node_interface_pairs)


