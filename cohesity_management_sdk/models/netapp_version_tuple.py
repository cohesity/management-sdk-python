# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class NetappVersionTuple(object):

    """Implementation of the 'NetappVersionTuple' model.

    TODO: type description here.


    Attributes:

        generation (int): Netapp generation.
        major_version (int): Major version number.
        minor_version (int): Minor version number.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "generation":'generation',
        "major_version":'majorVersion',
        "minor_version":'minorVersion',
    }
    def __init__(self,
                 generation=None,
                 major_version=None,
                 minor_version=None,
            ):

        """Constructor for the NetappVersionTuple class"""

        # Initialize members of the class
        self.generation = generation
        self.major_version = major_version
        self.minor_version = minor_version

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
        generation = dictionary.get('generation')
        major_version = dictionary.get('majorVersion')
        minor_version = dictionary.get('minorVersion')

        # Return an object of this model
        return cls(
            generation,
            major_version,
            minor_version
)