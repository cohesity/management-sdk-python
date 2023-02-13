# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class TenantGroupUpdateParameters(object):

    """Implementation of the 'TenantGroupUpdateParameters' model.

    Specifies group update details about a tenant.

    Attributes:
        sids (list of string): Specifies the array of Sid of the groups.
        tenant_id (string): Specifies the unique id of the tenant.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "sids":'sids',
        "tenant_id":'tenantId'
    }

    def __init__(self,
                 sids=None,
                 tenant_id=None):
        """Constructor for the TenantGroupUpdateParameters class"""

        # Initialize members of the class
        self.sids = sids
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
        sids = dictionary.get('sids')
        tenant_id = dictionary.get('tenantId')

        # Return an object of this model
        return cls(sids,
                   tenant_id)


