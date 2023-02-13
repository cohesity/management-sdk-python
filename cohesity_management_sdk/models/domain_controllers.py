# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class DomainControllers(object):

    """Implementation of the 'DomainControllers' model.

    Domain Controllers for a domain of an Active Directory domain.

    Attributes:
        domain_controllers (list of string): Domain Controllers of a domain of
            an Active Directory domain.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "domain_controllers":'domainControllers'
    }

    def __init__(self,
                 domain_controllers=None):
        """Constructor for the DomainControllers class"""

        # Initialize members of the class
        self.domain_controllers = domain_controllers


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

        # Return an object of this model
        return cls(domain_controllers)


