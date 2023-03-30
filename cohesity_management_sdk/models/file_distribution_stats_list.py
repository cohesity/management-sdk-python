# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class FileDistributionStatsList(object):

    """Implementation of the 'FileDistributionStatsList' model.

    Specifies the File distribution stats list.


    Attributes:

    """


    # Create a mapping from Model property names to API property names
    _names = {
    }
    def __init__(self,
            ):

        """Constructor for the FileDistributionStatsList class"""

        # Initialize members of the class

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

        # Return an object of this model
        return cls(

)