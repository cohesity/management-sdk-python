# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class TenantEntityUpdate(object):

    """Implementation of the 'TenantEntityUpdate' model.

    Specifies entity update details response about a tenant.

    Attributes:
        entity_ids (list of long|int): Specifies the EntityIds for respective
            tenant.
        tenant_id (string): Specifies the unique id of the tenant.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "entity_ids":'entityIds',
        "tenant_id":'tenantId'
    }

    def __init__(self,
                 entity_ids=None,
                 tenant_id=None):
        """Constructor for the TenantEntityUpdate class"""

        # Initialize members of the class
        self.entity_ids = entity_ids
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
        entity_ids = dictionary.get('entityIds')
        tenant_id = dictionary.get('tenantId')

        # Return an object of this model
        return cls(entity_ids,
                   tenant_id)


