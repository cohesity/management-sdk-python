# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class TenantIdData(object):

    """Implementation of the 'TenantIdData' model.

    Specifies id of a tenant.

    Attributes:
        tenant_id (string): Specifies the unique id of the tenant.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "tenant_id":'tenantId'
    }

    def __init__(self,
                 tenant_id=None):
        """Constructor for the TenantIdData class"""

        # Initialize members of the class
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
        tenant_id = dictionary.get('tenantId')

        # Return an object of this model
        return cls(tenant_id)


