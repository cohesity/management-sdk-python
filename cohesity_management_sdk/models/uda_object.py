
# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class UdaObject(object):

    """Implementation of the 'UdaObject' model.

    Specifies an Object containing information about a Universal Data Adapter
    object.

    Attributes:
        :TODO Add description here.
    """

    # Create a mapping from Model property names to API property names
    _names = {
    }

    def __init__(self):
        """Constructor for the UdaObject class"""

        # Initialize members of the class
        pass


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

        # Return an object of this model
        return cls()

