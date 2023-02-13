# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.cluster_identifier
import cohesity_management_sdk.models.mcm_user_profile

class UserParameters(object):

    """Implementation of the 'UserParameters' model.

    Specifies the settings used to create/add a new user or modify an
    existing user.

    Attributes:
        additional_group_names (list of string): Array of Additional Groups.
            Specifies the names of additional groups this User may belong to.
        cluster_identifiers (list of ClusterIdentifier): Specifies the list of
            clusters this user has access to. If this is not specified, access
            will be granted to all clusters.
        description (string): Specifies a description about the user.
        domain (string): Specifies the fully qualified domain name (FQDN) of
            an Active Directory or LOCAL for the default LOCAL domain on the
            Cohesity Cluster. A user is uniquely identified by combination of
            the username and the domain.
        effective_time_msecs (long|int): Specifies the epoch time in
            milliseconds when the user becomes effective. Until that time, the
            user cannot log in.
        email_address (string): Specifies the email address of the user.
        expired_time_msecs (long|int): Specifies the epoch time in
            milliseconds when the user becomes expired. After that, the user
            cannot log in.
        password (string): Specifies the password of this user.
        primary_group_name (string): Specifies the name of the primary group
            of this User.
        privilege_ids (list of PrivilegeIdUserParametersEnum): Array of
            Privileges.  Specifies the Cohesity privileges from the roles.
            This will be populated based on the union of all privileges in
            roles. Type for unique privilege Id values. All below enum values
            specify a value for all uniquely defined privileges in Cohesity.
        profiles (list of McmUserProfile): Specifies the user profiles.
            NOTE: Currently used for Helios.
        restricted (bool): Whether the user is a restricted user. A restricted
            user can only view the objects he has permissions to.
        roles (list of string): Array of Roles.  Specifies the Cohesity roles
            to associate with the user such as such as 'Admin', 'Ops' or
            'View'. The Cohesity roles determine privileges on the Cohesity
            Cluster for this user.
        username (string): Specifies the login name of the user.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "additional_group_names":'additionalGroupNames',
        "cluster_identifiers":'clusterIdentifiers',
        "description":'description',
        "domain":'domain',
        "effective_time_msecs":'effectiveTimeMsecs',
        "email_address":'emailAddress',
        "expired_time_msecs":'expiredTimeMsecs',
        "password":'password',
        "primary_group_name":'primaryGroupName',
        "privilege_ids":'privilegeIds',
        "profiles":'profiles',
        "restricted":'restricted',
        "roles":'roles',
        "username":'username'
    }

    def __init__(self,
                 additional_group_names=None,
                 cluster_identifiers=None,
                 description=None,
                 domain=None,
                 effective_time_msecs=None,
                 email_address=None,
                 expired_time_msecs=None,
                 password=None,
                 primary_group_name=None,
                 privilege_ids=None,
                 profiles=None,
                 restricted=None,
                 roles=None,
                 username=None):
        """Constructor for the UserParameters class"""

        # Initialize members of the class
        self.additional_group_names = additional_group_names
        self.cluster_identifiers = cluster_identifiers
        self.description = description
        self.domain = domain
        self.effective_time_msecs = effective_time_msecs
        self.email_address = email_address
        self.expired_time_msecs = expired_time_msecs
        self.password = password
        self.primary_group_name = primary_group_name
        self.privilege_ids = privilege_ids
        self.profiles = profiles
        self.restricted = restricted
        self.roles = roles
        self.username = username


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
        additional_group_names = dictionary.get('additionalGroupNames')
        cluster_identifiers = None
        if dictionary.get('clusterIdentifiers') != None:
            cluster_identifiers = list()
            for structure in dictionary.get('clusterIdentifiers'):
                cluster_identifiers.append(cohesity_management_sdk.models.cluster_identifier.ClusterIdentifier.from_dictionary(structure))
        description = dictionary.get('description')
        domain = dictionary.get('domain')
        effective_time_msecs = dictionary.get('effectiveTimeMsecs')
        email_address = dictionary.get('emailAddress')
        expired_time_msecs = dictionary.get('expiredTimeMsecs')
        password = dictionary.get('password')
        primary_group_name = dictionary.get('primaryGroupName')
        privilege_ids = dictionary.get('privilegeIds')
        profiles = None
        if dictionary.get('profiles') != None:
            profiles = list()
            for structure in dictionary.get('profiles'):
                profiles.append(cohesity_management_sdk.models.mcm_user_profile.McmUserProfile.from_dictionary(structure))
        restricted = dictionary.get('restricted')
        roles = dictionary.get('roles')
        username = dictionary.get('username')

        # Return an object of this model
        return cls(additional_group_names,
                   cluster_identifiers,
                   description,
                   domain,
                   effective_time_msecs,
                   email_address,
                   expired_time_msecs,
                   password,
                   primary_group_name,
                   privilege_ids,
                   profiles,
                   restricted,
                   roles,
                   username)


