# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class UpdateIgnoredTrustedDomainsParams(object):

    """Implementation of the 'UpdateIgnoredTrustedDomainsParams' model.

    Specifies the params to update the list of ignored trusted domains.

    Attributes:
        ignored_trusted_domains (list of string): Specifies the list of
            trusted domains that were set by the user to be ignored during
            trusted domain discovery.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ignored_trusted_domains":'ignoredTrustedDomains'
    }

    def __init__(self,
                 ignored_trusted_domains=None):
        """Constructor for the UpdateIgnoredTrustedDomainsParams class"""

        # Initialize members of the class
        self.ignored_trusted_domains = ignored_trusted_domains


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
        ignored_trusted_domains = dictionary.get('ignoredTrustedDomains')

        # Return an object of this model
        return cls(ignored_trusted_domains)


