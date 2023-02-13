# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class UpdateTrustedDomainEnableParams(object):

    """Implementation of the 'UpdateTrustedDomainEnableParams' model.

    Specifies the params to update trusted domain enable flag.

    Attributes:
        trusted_domains_enabled (bool): Request to update enable trusted
            domains state of an Active Directory.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "trusted_domains_enabled":'trustedDomainsEnabled'
    }

    def __init__(self,
                 trusted_domains_enabled=None):
        """Constructor for the UpdateTrustedDomainEnableParams class"""

        # Initialize members of the class
        self.trusted_domains_enabled = trusted_domains_enabled


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
        trusted_domains_enabled = dictionary.get('trustedDomainsEnabled')

        # Return an object of this model
        return cls(trusted_domains_enabled)


