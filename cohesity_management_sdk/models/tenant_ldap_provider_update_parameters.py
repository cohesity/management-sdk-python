# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class TenantLdapProviderUpdateParameters(object):

    """Implementation of the 'TenantLdapProviderUpdateParameters' model.

    Specifies Ldap Provider update details about a tenant.

    Attributes:
        ldap_provider_ids (list of long|int): Specifies the ids of ldap
            providers for respective tenant.
        tenant_id (string): Specifies the unique id of the tenant.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ldap_provider_ids":'ldapProviderIds',
        "tenant_id":'tenantId'
    }

    def __init__(self,
                 ldap_provider_ids=None,
                 tenant_id=None):
        """Constructor for the TenantLdapProviderUpdateParameters class"""

        # Initialize members of the class
        self.ldap_provider_ids = ldap_provider_ids
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
        ldap_provider_ids = dictionary.get('ldapProviderIds')
        tenant_id = dictionary.get('tenantId')

        # Return an object of this model
        return cls(ldap_provider_ids,
                   tenant_id)


