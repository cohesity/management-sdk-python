# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class Principal(object):

    """Implementation of the 'Principal' model.

    Specifies information about a single Principal.

    Attributes:
        domain (string): Specifies the domain name of the where the principal'
            account is maintained.
        full_name (string): Specifies the full name (first and last names) of
            the principal.
        object_class (ObjectClassEnum): Specifies the object class of the
            principal (either 'kGroup' or 'kUser'). 'kUser' specifies a user
            object class. 'kGroup' specifies a group object class. 'kComputer'
            specifies a computer object class. 'kWellKnownPrincipal' specifies
            a well known principal. 'kServiceAccount' specifies a service
            account object class.
        principal_name (string): Specifies the name of the principal.
        sid (string): Specifies the unique Security id (SID) of the
            principal.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "domain":'domain',
        "full_name":'fullName',
        "object_class":'objectClass',
        "principal_name":'principalName',
        "sid":'sid'
    }

    def __init__(self,
                 domain=None,
                 full_name=None,
                 object_class=None,
                 principal_name=None,
                 sid=None):
        """Constructor for the Principal class"""

        # Initialize members of the class
        self.domain = domain
        self.full_name = full_name
        self.object_class = object_class
        self.principal_name = principal_name
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
        domain = dictionary.get('domain')
        full_name = dictionary.get('fullName')
        object_class = dictionary.get('objectClass')
        principal_name = dictionary.get('principalName')
        sid = dictionary.get('sid')

        # Return an object of this model
        return cls(domain,
                   full_name,
                   object_class,
                   principal_name,
                   sid)


