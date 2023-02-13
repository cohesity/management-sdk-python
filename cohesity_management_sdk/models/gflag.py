# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class Gflag(object):

    """Implementation of the 'Gflag' model.

    Specifies the attributes of a service gflag.

    Attributes:
        name (string): Specifies name of the gflag.
        product_model (string): Specifies product model this gflag set on.
        reason (string): Specifies reason for setting the gflag.
        timestamp (long|int): Specifies timestamp when gflag was set.
        value (string): Specifies value of the gflag.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "product_model":'productModel',
        "reason":'reason',
        "timestamp":'timestamp',
        "value":'value'
    }

    def __init__(self,
                 name=None,
                 product_model=None,
                 reason=None,
                 timestamp=None,
                 value=None):
        """Constructor for the Gflag class"""

        # Initialize members of the class
        self.name = name
        self.product_model = product_model
        self.reason = reason
        self.timestamp = timestamp
        self.value = value


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
        product_model = dictionary.get('productModel')
        reason = dictionary.get('reason')
        timestamp = dictionary.get('timestamp')
        value = dictionary.get('value')

        # Return an object of this model
        return cls(name,
                   product_model,
                   reason,
                   timestamp,
                   value)


