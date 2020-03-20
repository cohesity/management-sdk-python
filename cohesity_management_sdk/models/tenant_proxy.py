# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class TenantProxy(object):

    """Implementation of the 'TenantProxy' model.

    Specifies the data for tenant proxy which has been deployed in tenant's
    enviroment.

    Attributes:
        ip_address (string): Specifies the ip address of the proxy.
        tenant_id (string): Specifies the unique id of the tenant.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ip_address":'ipAddress',
        "tenant_id":'tenantId'
    }

    def __init__(self,
                 ip_address=None,
                 tenant_id=None):
        """Constructor for the TenantProxy class"""

        # Initialize members of the class
        self.ip_address = ip_address
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
        ip_address = dictionary.get('ipAddress')
        tenant_id = dictionary.get('tenantId')

        # Return an object of this model
        return cls(ip_address,
                   tenant_id)


