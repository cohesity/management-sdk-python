# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class TenantProxy(object):

    """Implementation of the 'TenantProxy' model.

    Specifies the data for tenant proxy which has been deployed in tenant's
    enviroment.

    Attributes:
        constituent_id (long|int): Specifies the constituent id of the proxy.
        ip_address (string): Specifies the ip address of the proxy.
        tenant_id (string): Specifies the unique id of the tenant.
        version (string): Specifies the version of the proxy.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "constituent_id":'constituentId',
        "ip_address":'ipAddress',
        "tenant_id":'tenantId',
        "version":'version'
    }

    def __init__(self,
                 constituent_id=None,
                 ip_address=None,
                 tenant_id=None,
                 version=None):
        """Constructor for the TenantProxy class"""

        # Initialize members of the class
        self.constituent_id = constituent_id
        self.ip_address = ip_address
        self.tenant_id = tenant_id
        self.version = version


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
        constituent_id = dictionary.get('constituentId')
        ip_address = dictionary.get('ipAddress')
        tenant_id = dictionary.get('tenantId')
        version = dictionary.get('version')

        # Return an object of this model
        return cls(constituent_id,
                   ip_address,
                   tenant_id,
                   version)


