# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class ExportParameters(object):

    """Implementation of the 'ExportParameters' model.

    ExportParameters specifies path required to export configuration.


    Attributes:

        path (string): Specifies the directory path where to create a
            configuration files.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "path":'path',
    }
    def __init__(self,
                 path=None,
            ):

        """Constructor for the ExportParameters class"""

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
        return cls(
            path
)