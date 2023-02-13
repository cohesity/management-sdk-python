# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class MapReduceFileFormats(object):

    """Implementation of the 'MapReduceFileFormats' model.

    Specifies information about file formats produced by a mapo reduce
    instance.

    Attributes:
        supported_formats (list of string): Specifies the list of formats
            supported with integer enum mapping to file format.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "supported_formats":'supportedFormats'
    }

    def __init__(self,
                 supported_formats=None):
        """Constructor for the MapReduceFileFormats class"""

        # Initialize members of the class
        self.supported_formats = supported_formats


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
        supported_formats = dictionary.get('supportedFormats')

        # Return an object of this model
        return cls(supported_formats)


