# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.smb_principal

class Group(object):

    """Implementation of the 'Group' model.

    Specifies details about the group.

    Attributes:
        created_time_msecs (long|int): Specifies the epoch time in
            milliseconds when the group was created/added.
        description (string): Specifies a description of the group.
        domain (string): Specifies the domain of the group.
        last_updated_time_msecs (long|int): Specifies the epoch time in
            milliseconds when the group was last modified.
        name (string): Specifies the name of the group.
        restricted (bool): Whether the group is a restricted group. Users
            belonging to a restricted group can only view objects they have
            permissions to.
        roles (list of string): Array of Roles.  Specifies the Cohesity roles
            to associate with the group such as 'Admin', 'Ops' or 'View'. The
            Cohesity roles determine privileges on the Cohesity Cluster for
            all the users in this group.
        sid (string): Specifies the unique Security ID (SID) of the group.
        smb_principals (list of SmbPrincipal): Specifies the SMB principals.
            Principals will be added to this group only if IsSmbPrincipalOnly
            set to true.
        tenant_ids (list of string): Specifies the tenants to which the group
            belongs to. If not specified, session user's tenant id is
            assumed.
        usernames (list of string): Specifies the username of users who are
            members of the group. This field is used only for local groups.
        users (list of string): Specifies the SID of users who are members of
            the group. This field is used only for local groups.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "created_time_msecs":'createdTimeMsecs',
        "description":'description',
        "domain":'domain',
        "last_updated_time_msecs":'lastUpdatedTimeMsecs',
        "name":'name',
        "restricted":'restricted',
        "roles":'roles',
        "sid":'sid',
        "smb_principals":'smbPrincipals',
        "tenant_ids":'tenantIds',
        "usernames":'usernames',
        "users":'users'
    }

    def __init__(self,
                 created_time_msecs=None,
                 description=None,
                 domain=None,
                 last_updated_time_msecs=None,
                 name=None,
                 restricted=None,
                 roles=None,
                 sid=None,
                 smb_principals=None,
                 tenant_ids=None,
                 usernames=None,
                 users=None):
        """Constructor for the Group class"""

        # Initialize members of the class
        self.created_time_msecs = created_time_msecs
        self.description = description
        self.domain = domain
        self.last_updated_time_msecs = last_updated_time_msecs
        self.name = name
        self.restricted = restricted
        self.roles = roles
        self.sid = sid
        self.smb_principals = smb_principals
        self.tenant_ids = tenant_ids
        self.usernames = usernames
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
        created_time_msecs = dictionary.get('createdTimeMsecs')
        description = dictionary.get('description')
        domain = dictionary.get('domain')
        last_updated_time_msecs = dictionary.get('lastUpdatedTimeMsecs')
        name = dictionary.get('name')
        restricted = dictionary.get('restricted')
        roles = dictionary.get('roles')
        sid = dictionary.get('sid')
        smb_principals = None
        if dictionary.get('smbPrincipals') != None:
            smb_principals = list()
            for structure in dictionary.get('smbPrincipals'):
                smb_principals.append(cohesity_management_sdk.models.smb_principal.SmbPrincipal.from_dictionary(structure))
        tenant_ids = dictionary.get('tenantIds')
        usernames = dictionary.get('usernames')
        users = dictionary.get('users')

        # Return an object of this model
        return cls(created_time_msecs,
                   description,
                   domain,
                   last_updated_time_msecs,
                   name,
                   restricted,
                   roles,
                   sid,
                   smb_principals,
                   tenant_ids,
                   usernames,
                   users)


