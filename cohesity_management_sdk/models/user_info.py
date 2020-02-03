# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class UserInfo(object):

    """Implementation of the 'UserInfo' model.

    Specifies struct with basic user details.

    Attributes:
        domain (string): Specifies domain name of the user.
        sid (string): Specifies unique Security ID (SID) of the user.
        user_name (string): Specifies user name of the user.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "domain":'domain',
        "sid":'sid',
        "user_name":'userName'
    }

    def __init__(self,
                 domain=None,
                 sid=None,
                 user_name=None):
        """Constructor for the UserInfo class"""

        # Initialize members of the class
        self.domain = domain
        self.sid = sid
        self.user_name = user_name


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
        sid = dictionary.get('sid')
        user_name = dictionary.get('userName')

        # Return an object of this model
        return cls(domain,
                   sid,
                   user_name)


