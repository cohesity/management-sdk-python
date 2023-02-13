# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.domain

class Project(object):

    """Implementation of the 'Project' model.

    Keystone project proto.

    Attributes:
        domain (Domain): Domain to which the project is scoped.
        domain_id (string): Specifies the IPMI Password.
        id (string): The ID of the project.
        name (string): The name of the project.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "domain":'domain',
        "domain_id":'domainId',
        "id":'id',
        "name":'name'
    }

    def __init__(self,
                 domain=None,
                 domain_id=None,
                 id=None,
                 name=None):
        """Constructor for the Project class"""

        # Initialize members of the class
        self.domain = domain
        self.domain_id = domain_id
        self.id = id
        self.name = name


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
        domain = cohesity_management_sdk.models.domain.Domain.from_dictionary(dictionary.get('domain')) if dictionary.get('domain') else None
        domain_id = dictionary.get('domainId')
        id = dictionary.get('id')
        name = dictionary.get('name')

        # Return an object of this model
        return cls(domain,
                   domain_id,
                   id,
                   name)


