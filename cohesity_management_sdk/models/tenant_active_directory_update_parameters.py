# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class TenantActiveDirectoryUpdateParameters(object):

    """Implementation of the 'TenantActiveDirectoryUpdateParameters' model.

    Specifies Active Directory update details about a tenant.

    Attributes:
        active_directory_domains (list of string): Specifies the
            ActiveDirectoryDomain vec for respective tenant.
        tenant_id (string): Specifies the unique id of the tenant.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "active_directory_domains":'activeDirectoryDomains',
        "tenant_id":'tenantId'
    }

    def __init__(self,
                 active_directory_domains=None,
                 tenant_id=None):
        """Constructor for the TenantActiveDirectoryUpdateParameters class"""

        # Initialize members of the class
        self.active_directory_domains = active_directory_domains
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
        active_directory_domains = dictionary.get('activeDirectoryDomains')
        tenant_id = dictionary.get('tenantId')

        # Return an object of this model
        return cls(active_directory_domains,
                   tenant_id)


