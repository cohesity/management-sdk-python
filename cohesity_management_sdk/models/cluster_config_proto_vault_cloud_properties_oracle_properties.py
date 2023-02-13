# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ClusterConfigProto_Vault_CloudProperties_OracleProperties(object):

    """Implementation of the 'ClusterConfigProto_Vault_CloudProperties_OracleProperties' model.

    Attributes:
        tenant (string): Tenant part of the REST endpoints for Oracle S3 compatible vaults.
        tier_type (int): TODO: Type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "tenant": 'tenant',
        "tier_type": 'tierType'
    }

    def __init__(self,
                 tenant=None,
                 tier_type=None):
        """Constructor for the ClusterConfigProto_Vault_CloudProperties_OracleProperties class"""

        # Initialize members of the class
        self.tenant = tenant
        self.tier_type = tier_type


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
        tenant = dictionary.get('tenant', None)
        tier_type = dictionary.get('tierType', None)

        # Return an object of this model
        return cls(tenant,
                   tier_type)


