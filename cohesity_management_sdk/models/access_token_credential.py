# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class AccessTokenCredential(object):

    """Implementation of the 'AccessTokenCredential' model.

    Specifies the Cohesity credentials required for generating an access
    token.

    Attributes:
        domain (string): Specifies the domain the user is logging in to. For a
            Local user model, the domain is always LOCAL. For LDAP/AD user
            models, the domain will map to an LDAP connection string. A user
            is uniquely identified by a combination of username and domain. If
            this is not set, LOCAL is assumed.
        password (string): Specifies the password of the Cohesity user
            account.
        username (string): Specifies the login name of the Cohesity user.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "password":'password',
        "username":'username',
        "domain":'domain'
    }

    def __init__(self,
                 password=None,
                 username=None,
                 domain=None):
        """Constructor for the AccessTokenCredential class"""

        # Initialize members of the class
        self.domain = domain
        self.password = password
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
        password = dictionary.get('password')
        username = dictionary.get('username')
        domain = dictionary.get('domain')

        # Return an object of this model
        return cls(password,
                   username,
                   domain)


