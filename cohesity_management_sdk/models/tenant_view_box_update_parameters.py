# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class TenantViewBoxUpdateParameters(object):

    """Implementation of the 'TenantViewBoxUpdateParameters' model.

    Specifies view box update details about a tenant.

    Attributes:
        tenant_id (string): Specifies the unique id of the tenant.
        view_box_ids (list of long|int): Specifies the ViewBoxIds for
            respective tenant.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "tenant_id":'tenantId',
        "view_box_ids":'viewBoxIds'
    }

    def __init__(self,
                 tenant_id=None,
                 view_box_ids=None):
        """Constructor for the TenantViewBoxUpdateParameters class"""

        # Initialize members of the class
        self.tenant_id = tenant_id
        self.view_box_ids = view_box_ids


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
        view_box_ids = dictionary.get('viewBoxIds')

        # Return an object of this model
        return cls(tenant_id,
                   view_box_ids)


