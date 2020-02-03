# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.product_model_interface_tuple
import cohesity_management_sdk.models.network_params

class InterfaceGroup(object):

    """Implementation of the 'InterfaceGroup' model.

    Specifies the settings of an interface group.

    Attributes:
        id (int): Interface group Id.  Specifies the id of the interface
            group.
        model_interface_lists (list of ProductModelInterfaceTuple): Specifies
            the product model and interface lists.
        name (string): Specifies the name of the interface group.
        network_params (NetworkParams): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "model_interface_lists":'modelInterfaceLists',
        "name":'name',
        "network_params":'networkParams'
    }

    def __init__(self,
                 id=None,
                 model_interface_lists=None,
                 name=None,
                 network_params=None):
        """Constructor for the InterfaceGroup class"""

        # Initialize members of the class
        self.id = id
        self.model_interface_lists = model_interface_lists
        self.name = name
        self.network_params = network_params


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
        id = dictionary.get('id')
        model_interface_lists = None
        if dictionary.get('modelInterfaceLists') != None:
            model_interface_lists = list()
            for structure in dictionary.get('modelInterfaceLists'):
                model_interface_lists.append(cohesity_management_sdk.models.product_model_interface_tuple.ProductModelInterfaceTuple.from_dictionary(structure))
        name = dictionary.get('name')
        network_params = cohesity_management_sdk.models.network_params.NetworkParams.from_dictionary(dictionary.get('networkParams')) if dictionary.get('networkParams') else None

        # Return an object of this model
        return cls(id,
                   model_interface_lists,
                   name,
                   network_params)


