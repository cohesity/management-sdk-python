# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ObjectsByEnv(object):

    """Implementation of the 'ObjectsByEnv' model.

    Number of Objects by Type.

    Attributes:
        env_type (string): Environment Type.
        num_objects (int): Number of Objects.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "env_type":'envType',
        "num_objects":'numObjects'
    }

    def __init__(self,
                 env_type=None,
                 num_objects=None):
        """Constructor for the ObjectsByEnv class"""

        # Initialize members of the class
        self.env_type = env_type
        self.num_objects = num_objects


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
        env_type = dictionary.get('envType')
        num_objects = dictionary.get('numObjects')

        # Return an object of this model
        return cls(env_type,
                   num_objects)


