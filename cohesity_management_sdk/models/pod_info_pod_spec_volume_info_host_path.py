# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class PodInfo_PodSpec_VolumeInfo_HostPath(object):

    """Implementation of the 'PodInfo_PodSpec_VolumeInfo_HostPath' model.

    Attributes:
        path (string): TODO: Type description here.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "path":'path'
    }

    def __init__(self,
                 path=None):
        """Constructor for the PodInfo_PodSpec_VolumeInfo_HostPath class"""

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


