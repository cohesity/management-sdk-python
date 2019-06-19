# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.


class FileLockStatusParams(object):

    """Implementation of the 'FileLockStatusParams' model.

    Specifies the parameters to get file lock status.

    Attributes:
        path (string): Specifies the file path that needs to be locked.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "path":'path'
    }

    def __init__(self,
                 path=None):
        """Constructor for the FileLockStatusParams class"""

        # Initialize members of the class
        self.path = path


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
        path = dictionary.get('path')

        # Return an object of this model
        return cls(path)


