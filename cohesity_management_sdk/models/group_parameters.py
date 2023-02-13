# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.smb_principal

class GroupParameters(object):

    """Implementation of the 'GroupParameters' model.

    Specifies the settings used to add/create a new group or modify an
    existing
    group.

    Attributes:
        description (string): Specifies a description of the group.
        domain (string): Specifies the domain of the group.
        name (string): Specifies the name of the group.
        restricted (bool): Whether the group is a restricted group. Users
            belonging to a restricted group can only view objects they have
            permissions to.
        roles (list of string): Array of Roles.  Specifies the Cohesity roles
            to associate with the group such as 'Admin', 'Ops' or 'View'. The
            Cohesity roles determine privileges on the Cohesity Cluster for
            all the users in this group.
        smb_principals (list of SmbPrincipal): Specifies the SMB principals.
            Principals will be added to this group only if IsSmbPrincipalOnly
            set to true.
        tenant_ids (list of string): Specifies the tenants to which the group
            belongs to. If not specified, session user's tenant id is
            assumed.
        users (list of string): Specifies the SID of users who are members of
            the group. This field is used only for local groups.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "description":'description',
        "domain":'domain',
        "name":'name',
        "restricted":'restricted',
        "roles":'roles',
        "smb_principals":'smbPrincipals',
        "tenant_ids":'tenantIds',
        "users":'users'
    }

    def __init__(self,
                 description=None,
                 domain=None,
                 name=None,
                 restricted=None,
                 roles=None,
                 smb_principals=None,
                 tenant_ids=None,
                 users=None):
        """Constructor for the GroupParameters class"""

        # Initialize members of the class
        self.description = description
        self.domain = domain
        self.name = name
        self.restricted = restricted
        self.roles = roles
        self.smb_principals = smb_principals
        self.tenant_ids = tenant_ids
        self.users = users


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
        description = dictionary.get('description')
        domain = dictionary.get('domain')
        name = dictionary.get('name')
        restricted = dictionary.get('restricted')
        roles = dictionary.get('roles')
        smb_principals = None
        if dictionary.get('smbPrincipals') != None:
            smb_principals = list()
            for structure in dictionary.get('smbPrincipals'):
                smb_principals.append(cohesity_management_sdk.models.smb_principal.SmbPrincipal.from_dictionary(structure))
        tenant_ids = dictionary.get('tenantIds')
        users = dictionary.get('users')

        # Return an object of this model
        return cls(description,
                   domain,
                   name,
                   restricted,
                   roles,
                   smb_principals,
                   tenant_ids,
                   users)


