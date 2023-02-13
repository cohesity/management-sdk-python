# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class PreferredDomainController(object):

    """Implementation of the 'PreferredDomainController' model.

    Specifies Preferred domain controllers (DCs) for an Active Directory
    domain.

    Attributes:
        domain_controllers (list of string): List of Domain controllers DCs in
            FQDN format that are mapped to an Active Directory Domain name.
        domain_name (string): Specifies the Domain name or the trusted domain
            of an Active Directory.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "domain_controllers":'domainControllers',
        "domain_name":'domainName'
    }

    def __init__(self,
                 domain_controllers=None,
                 domain_name=None):
        """Constructor for the PreferredDomainController class"""

        # Initialize members of the class
        self.domain_controllers = domain_controllers
        self.domain_name = domain_name


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
        domain_controllers = dictionary.get('domainControllers')
        domain_name = dictionary.get('domainName')

        # Return an object of this model
        return cls(domain_controllers,
                   domain_name)


