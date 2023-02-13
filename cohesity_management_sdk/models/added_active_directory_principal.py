# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class AddedActiveDirectoryPrincipal(object):

    """Implementation of the 'AddedActiveDirectoryPrincipal' model.

    Specifies a group or user added to the Cohesity Cluster for an Active
    Directory principal.

    Attributes:
        created_time_msecs (long|int): Specifies the epoch time in
            milliseconds when the group or user was added to the Cohesity
            Cluster.
        description (string): Specifies a description about the user or
            group.
        domain (string): Specifies the domain of the Active Directory where
            the referenced principal is stored.
        last_updated_time_msecs (long|int): Specifies the epoch time in
            milliseconds when the group or user was last modified on the
            Cohesity Cluster.
        object_class (ObjectClassAddedActiveDirectoryPrincipalEnum): Specifies
            the type of the referenced Active Directory principal. If
            'kGroup', the referenced Active Directory principal is a group. If
            'kUser', the referenced Active Directory principal is a user.
            'kUser' specifies a user object class. 'kGroup' specifies a group
            object class. 'kComputer' specifies a computer object class.
            'kWellKnownPrincipal' specifies a well known principal.
            'kServiceAccount' specifies a service account object class.
        principal_name (string): Specifies the name of the Active Directory
            principal, that will be referenced by the group or user. The name
            of the Active Directory principal is used for naming the new group
            or user on the Cohesity Cluster.
        restricted (bool): Whether the principal is a restricted principal. A
            restricted principal can only view the objects he has permissions
            to.
        roles (list of string): Array of Roles.  Specifies the Cohesity roles
            to associate with this user or group such as 'Admin', 'Ops' or
            'View'. The Cohesity roles determine privileges on the Cohesity
            Cluster for this group or user. For example if the 'joe' user is
            added for the Active Directory 'joe' user principal and is
            associated with the Cohesity 'View' role, 'joe' can log in to the
            Cohesity Dashboard and has a read-only view of the data on the
            Cohesity Cluster.
        sid (string): Specifies the unique Security ID (SID) of the Active
            Directory principal associated with this group or user.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "created_time_msecs":'createdTimeMsecs',
        "description":'description',
        "domain":'domain',
        "last_updated_time_msecs":'lastUpdatedTimeMsecs',
        "object_class":'objectClass',
        "principal_name":'principalName',
        "restricted":'restricted',
        "roles":'roles',
        "sid":'sid'
    }

    def __init__(self,
                 created_time_msecs=None,
                 description=None,
                 domain=None,
                 last_updated_time_msecs=None,
                 object_class=None,
                 principal_name=None,
                 restricted=None,
                 roles=None,
                 sid=None):
        """Constructor for the AddedActiveDirectoryPrincipal class"""

        # Initialize members of the class
        self.created_time_msecs = created_time_msecs
        self.description = description
        self.domain = domain
        self.last_updated_time_msecs = last_updated_time_msecs
        self.object_class = object_class
        self.principal_name = principal_name
        self.restricted = restricted
        self.roles = roles
        self.sid = sid


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
        object_class = dictionary.get('objectClass')
        principal_name = dictionary.get('principalName')
        restricted = dictionary.get('restricted')
        roles = dictionary.get('roles')
        sid = dictionary.get('sid')

        # Return an object of this model
        return cls(created_time_msecs,
                   description,
                   domain,
                   last_updated_time_msecs,
                   object_class,
                   principal_name,
                   restricted,
                   roles,
                   sid)


