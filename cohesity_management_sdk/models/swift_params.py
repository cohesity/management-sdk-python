# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class SwiftParams(object):

    """Implementation of the 'SwiftParams' model.

    Specifies the parameters of Swift configuration.

    Attributes:
        keystone_id (int|long): Specifies the associated Keystone
            configuration id.
        operator_roles (list of string): Specifies a list of operator roles.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "keystone_id": 'keystoneId',
        "operator_roles": 'operatorRoles'
    }

    def __init__(self,
                 keystone_id=None,
                 operator_roles=None):
        """Constructor for the SwiftParams class"""

        # Initialize members of the class
        self.keystone_id = keystone_id
        self.operator_roles = operator_roles


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
        keystone_id = dictionary.get('keystoneId', None)
        operator_roles = dictionary.get('operatorRoles', None)

        # Return an object of this model
        return cls(keystone_id,
                   operator_roles)


