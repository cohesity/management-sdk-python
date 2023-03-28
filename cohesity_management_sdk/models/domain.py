# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class Domain(object):

    """Implementation of the 'Domain' model.

    Specifies a domain and its trusted domains.


    Attributes:

        domain_name (string): Specifies the domain name.
        trusted_domains (list of string): Specifies a list of trusted domains
            of this domain.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "domain_name":'domainName',
        "trusted_domains":'trustedDomains',
    }
    def __init__(self,
                 domain_name=None,
                 trusted_domains=None,
            ):

        """Constructor for the Domain class"""

        # Initialize members of the class
        self.domain_name = domain_name
        self.trusted_domains = trusted_domains

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
        domain_name = dictionary.get('domainName')
        trusted_domains = dictionary.get("trustedDomains")

        # Return an object of this model
        return cls(
            domain_name,
            trusted_domains
)