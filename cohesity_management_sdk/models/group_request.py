# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.specifies_struct_with_smb_principal_details

class GroupRequest(object):

    """Implementation of the 'Group Request.' model.

    Specifies the settings used to add/create a new group or modify an
    existing
    group.

    Attributes:
        description (string): Specifies a description of the group.
        domain (string): Specifies the domain of the group.
        is_smb_principal_only (bool): Specify that this group can have only
            SMB principals as members if this is set to true. This Field can
            not change once group is created.
        name (string): Specifies the name of the group.
        restricted (bool): Whether the group is a restricted group. Users
            belonging to a restricted group can only view objects they have
            permissions to.
        roles (list of string): Array of Roles.  Specifies the Cohesity roles
            to associate with the group such as 'Admin', 'Ops' or 'View'. The
            Cohesity roles determine privileges on the Cohesity Cluster for
            all the users in this group.
        smb_principals (list of SpecifiesStructWithSMBPrincipalDetails):
            Specifies the SMB principals. Principals will be added to this
            group only if IsSmbPrincipalOnly set to true.
        tenant_id (string): Specifies the unique id of the tenant.
        users (list of string): Specifies the users who are members of the
            group. This field is used only for local groups.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "description":'description',
        "domain":'domain',
        "is_smb_principal_only":'isSmbPrincipalOnly',
        "name":'name',
        "restricted":'restricted',
        "roles":'roles',
        "smb_principals":'smbPrincipals',
        "tenant_id":'tenantId',
        "users":'users'
    }

    def __init__(self,
                 description=None,
                 domain=None,
                 is_smb_principal_only=None,
                 name=None,
                 restricted=None,
                 roles=None,
                 smb_principals=None,
                 tenant_id=None,
                 users=None):
        """Constructor for the GroupRequest class"""

        # Initialize members of the class
        self.description = description
        self.domain = domain
        self.is_smb_principal_only = is_smb_principal_only
        self.name = name
        self.restricted = restricted
        self.roles = roles
        self.smb_principals = smb_principals
        self.tenant_id = tenant_id
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
        is_smb_principal_only = dictionary.get('isSmbPrincipalOnly')
        name = dictionary.get('name')
        restricted = dictionary.get('restricted')
        roles = dictionary.get('roles')
        smb_principals = None
        if dictionary.get('smbPrincipals') != None:
            smb_principals = list()
            for structure in dictionary.get('smbPrincipals'):
                smb_principals.append(cohesity_management_sdk.models.specifies_struct_with_smb_principal_details.SpecifiesStructWithSMBPrincipalDetails.from_dictionary(structure))
        tenant_id = dictionary.get('tenantId')
        users = dictionary.get('users')

        # Return an object of this model
        return cls(description,
                   domain,
                   is_smb_principal_only,
                   name,
                   restricted,
                   roles,
                   smb_principals,
                   tenant_id,
                   users)


