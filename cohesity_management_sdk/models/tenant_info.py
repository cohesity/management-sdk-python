# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class TenantInfo(object):

    """Implementation of the 'TenantInfo' model.

    Specifies struct with basic tenant details.

    Attributes:
        bifrost_enabled (bool): Specifies if this tenant is bifrost enabled or
            not.
        name (string): Specifies name of the tenant.
        tenant_id (string): Specifies the unique id of the tenant.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bifrost_enabled":'bifrostEnabled',
        "name":'name',
        "tenant_id":'tenantId'
    }

    def __init__(self,
                 bifrost_enabled=None,
                 name=None,
                 tenant_id=None):
        """Constructor for the TenantInfo class"""

        # Initialize members of the class
        self.bifrost_enabled = bifrost_enabled
        self.name = name
        self.tenant_id = tenant_id


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
        bifrost_enabled = dictionary.get('bifrostEnabled')
        name = dictionary.get('name')
        tenant_id = dictionary.get('tenantId')

        # Return an object of this model
        return cls(bifrost_enabled,
                   name,
                   tenant_id)


