# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class BannerUpdateParameters(object):

    """Implementation of the 'BannerUpdateParameters' model.

    Specifies the settings used to update a new banner.

    Attributes:
        content (string): Specifies the content of the banner.
        description (string): description field is deprecated.
            Specifies the description of this banner.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "content": 'content',
        "description": 'description'
    }

    def __init__(self,
                 content=None,
                 description=None):
        """Constructor for the BannerUpdateParameters class"""

        # Initialize members of the class
        self.content = content
        self.description = description


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
        content = dictionary.get('content')
        description = dictionary.get('description')

        # Return an object of this model
        return cls(content,
                   description)


