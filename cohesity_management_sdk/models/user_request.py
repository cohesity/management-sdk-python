# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.


class UserRequest(object):

    """Implementation of the 'User Request.' model.

    Specifies the settings used to create/add a new user or modify an
    existing user.

    Attributes:
        additional_group_names (list of string): Array of Additional Groups.
            Specifies the names of additional groups this User may belong to.
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
        "description":'description',
        "domain":'domain',
        "effective_time_msecs":'effectiveTimeMsecs',
        "email_address":'emailAddress',
        "expired_time_msecs":'expiredTimeMsecs',
        "password":'password',
        "primary_group_name":'primaryGroupName',
        "restricted":'restricted',
        "roles":'roles',
        "username":'username'
    }

    def __init__(self,
                 additional_group_names=None,
                 description=None,
                 domain=None,
                 effective_time_msecs=None,
                 email_address=None,
                 expired_time_msecs=None,
                 password=None,
                 primary_group_name=None,
                 restricted=None,
                 roles=None,
                 username=None):
        """Constructor for the UserRequest class"""

        # Initialize members of the class
        self.additional_group_names = additional_group_names
        self.description = description
        self.domain = domain
        self.effective_time_msecs = effective_time_msecs
        self.email_address = email_address
        self.expired_time_msecs = expired_time_msecs
        self.password = password
        self.primary_group_name = primary_group_name
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
        description = dictionary.get('description')
        domain = dictionary.get('domain')
        effective_time_msecs = dictionary.get('effectiveTimeMsecs')
        email_address = dictionary.get('emailAddress')
        expired_time_msecs = dictionary.get('expiredTimeMsecs')
        password = dictionary.get('password')
        primary_group_name = dictionary.get('primaryGroupName')
        restricted = dictionary.get('restricted')
        roles = dictionary.get('roles')
        username = dictionary.get('username')

        # Return an object of this model
        return cls(additional_group_names,
                   description,
                   domain,
                   effective_time_msecs,
                   email_address,
                   expired_time_msecs,
                   password,
                   primary_group_name,
                   restricted,
                   roles,
                   username)


