# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class TenantConfig(object):

    """Implementation of the 'TenantConfig' model.

    Specifies struct with basic tenant specific configuration.

    Attributes:
        name (string): Specifies name of the tenant.
        restricted (bool): Whether the user is a restricted user. A restricted
            user can only view the objects he has permissions to.
        roles (list of string): Array of Roles.  Specifies the Cohesity roles
            to associate with the user such as such as 'Admin', 'Ops' or
            'View'. The Cohesity roles determine privileges on the Cohesity
            Cluster for this user.
        tenant_id (string): Specifies the unique id of the tenant.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "restricted":'restricted',
        "roles":'roles',
        "tenant_id":'tenantId'
    }

    def __init__(self,
                 name=None,
                 restricted=None,
                 roles=None,
                 tenant_id=None):
        """Constructor for the TenantConfig class"""

        # Initialize members of the class
        self.name = name
        self.restricted = restricted
        self.roles = roles
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
        name = dictionary.get('name')
        restricted = dictionary.get('restricted')
        roles = dictionary.get('roles')
        tenant_id = dictionary.get('tenantId')

        # Return an object of this model
        return cls(name,
                   restricted,
                   roles,
                   tenant_id)


