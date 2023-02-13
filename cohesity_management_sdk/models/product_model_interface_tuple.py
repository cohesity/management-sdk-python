# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ProductModelInterfaceTuple(object):

    """Implementation of the 'ProductModelInterfaceTuple' model.

    Specifies a group of product model and interface set.

    Attributes:
        iface_name (string): Specifies the name of the interface.
        product_model_name (string): Specifies the product model name.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "iface_name":'ifaceName',
        "product_model_name":'productModelName'
    }

    def __init__(self,
                 iface_name=None,
                 product_model_name=None):
        """Constructor for the ProductModelInterfaceTuple class"""

        # Initialize members of the class
        self.iface_name = iface_name
        self.product_model_name = product_model_name


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
        product_model_name = dictionary.get('productModelName')

        # Return an object of this model
        return cls(iface_name,
                   product_model_name)


