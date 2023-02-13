# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class UpdateLdapProviderParams(object):

    """Implementation of the 'UpdateLdapProviderParams' model.

    Specifies the params to update the LDAP provider info.

    Attributes:
        ldap_provider_id (long|int): Specifies the LDAP provider id which is
            mapped to an Active Directory

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ldap_provider_id":'ldapProviderId'
    }

    def __init__(self,
                 ldap_provider_id=None):
        """Constructor for the UpdateLdapProviderParams class"""

        # Initialize members of the class
        self.ldap_provider_id = ldap_provider_id


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
        ldap_provider_id = dictionary.get('ldapProviderId')

        # Return an object of this model
        return cls(ldap_provider_id)


