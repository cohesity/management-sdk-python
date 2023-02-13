# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class PodInfo_PodSpec_VolumeInfo_EmptyDir(object):

    """Implementation of the 'PodInfo_PodSpec_VolumeInfo_EmptyDir' model.

    Attributes:
    """

    # Create a mapping from Model property names to API property names
    _names = {
    }

    def __init__(self):
        """Constructor for the PodInfo_PodSpec_VolumeInfo_EmptyDir class"""

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


