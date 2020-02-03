# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class TenantInfo(object):

    """Implementation of the 'TenantInfo' model.

    Specifies struct with basic tenant details.

    Attributes:
        name (string): Specifies name of the tenant.
        tenant_id (string): Specifies the unique id of the tenant.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "tenant_id":'tenantId'
    }

    def __init__(self,
                 name=None,
                 tenant_id=None):
        """Constructor for the TenantInfo class"""

        # Initialize members of the class
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
        name = dictionary.get('name')
        tenant_id = dictionary.get('tenantId')

        # Return an object of this model
        return cls(name,
                   tenant_id)


