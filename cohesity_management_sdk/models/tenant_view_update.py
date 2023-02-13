# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class TenantViewUpdate(object):

    """Implementation of the 'TenantViewUpdate' model.

    Specifies view update details response about a tenant.

    Attributes:
        tenant_id (string): Specifies the unique id of the tenant.
        view_names (list of string): Specifies the PolicyIds for respective
            tenant.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "tenant_id":'tenantId',
        "view_names":'viewNames'
    }

    def __init__(self,
                 tenant_id=None,
                 view_names=None):
        """Constructor for the TenantViewUpdate class"""

        # Initialize members of the class
        self.tenant_id = tenant_id
        self.view_names = view_names


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
        view_names = dictionary.get('viewNames')

        # Return an object of this model
        return cls(tenant_id,
                   view_names)


