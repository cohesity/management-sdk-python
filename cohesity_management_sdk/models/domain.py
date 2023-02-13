# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.links

class Domain(object):

    """Implementation of the 'Domain' model.

    Keystone domain proto.

    Attributes:
        description (string): TODO: Type description here.
        enabled (bool): TODO: Type description here.
        id (string): TODO: Type description here.
        links (Links): Links to the domain resource.
        name (string): TODO: Type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "description":'description',
        "enabled":'enabled',
        "id":'id',
        "links":'links',
        "name":'name'
    }

    def __init__(self,
                 description=None,
                 enabled=None,
                 id=None,
                 links=None,
                 name=None):
        """Constructor for the Domain class"""

        # Initialize members of the class
        self.description = description
        self.enabled = enabled
        self.id = id
        self.links = links
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
        description = dictionary.get('description')
        enabled = dictionary.get('enabled')
        id = dictionary.get('id')
        name = dictionary.get('name')
        links = cohesity_management_sdk.models.links.Links.from_dictionary(dictionary.get('links')) if dictionary.get('links') else None

        # Return an object of this model
        return cls(description,
                   enabled,
                   id,
                   links,
                   name)


