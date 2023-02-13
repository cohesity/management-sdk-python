# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class LdapProviderStatus(object):

    """Implementation of the 'LdapProviderStatus' model.

    LDAP provider status struct.

    Attributes:
        status_message (string): Specifies the connection status message of an
            LDAP provider.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "status_message":'statusMessage'
    }

    def __init__(self,
                 status_message=None):
        """Constructor for the LdapProviderStatus class"""

        # Initialize members of the class
        self.status_message = status_message


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
        status_message = dictionary.get('statusMessage')

        # Return an object of this model
        return cls(status_message)


