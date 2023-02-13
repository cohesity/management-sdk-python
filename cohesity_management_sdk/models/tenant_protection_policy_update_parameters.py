# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class TenantProtectionPolicyUpdateParameters(object):

    """Implementation of the 'TenantProtectionPolicyUpdateParameters' model.

    Specifies protection policy update details about a tenant.

    Attributes:
        policy_ids (list of string): Specifies the PolicyIds for respective
            tenant.
        tenant_id (string): Specifies the unique id of the tenant.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "policy_ids":'policyIds',
        "tenant_id":'tenantId'
    }

    def __init__(self,
                 policy_ids=None,
                 tenant_id=None):
        """Constructor for the TenantProtectionPolicyUpdateParameters class"""

        # Initialize members of the class
        self.policy_ids = policy_ids
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
        policy_ids = dictionary.get('policyIds')
        tenant_id = dictionary.get('tenantId')

        # Return an object of this model
        return cls(policy_ids,
                   tenant_id)


