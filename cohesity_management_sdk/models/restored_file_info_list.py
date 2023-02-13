# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class RestoredFileInfoList(object):

    """Implementation of the 'RestoredFileInfoList' model.

    TODO: type model description here.

    Attributes:
        is_directory (bool): Specifies whether the path points to directory.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "is_directory":'isDirectory'
    }

    def __init__(self,
                 is_directory=None):
        """Constructor for the RestoredFileInfoList class"""

        # Initialize members of the class
        self.is_directory = is_directory


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
        is_directory = dictionary.get('isDirectory')

        # Return an object of this model
        return cls(is_directory)


