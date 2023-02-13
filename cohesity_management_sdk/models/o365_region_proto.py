# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class O365RegionProto(object):

    """Implementation of the 'O365RegionProto' model.

    O365Region proto will store the information about the region from where
    o365 connector apis calls are made.

    Attributes:
        country (int): The country where the o365 connector apis were called
        from.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "country":'country'
    }

    def __init__(self,
                 country=None):
        """Constructor for the O365RegionProto class"""

        # Initialize members of the class
        self.country = country


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
        country = dictionary.get('country')

        # Return an object of this model
        return cls(country)


