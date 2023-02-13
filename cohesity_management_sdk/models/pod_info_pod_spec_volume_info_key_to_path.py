# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class PodInfo_PodSpec_VolumeInfo_KeyToPath(object):

    """Implementation of the 'PodInfo_PodSpec_VolumeInfo_KeyToPath' model.

    Attributes:
        key (string):  TODO: Type description here.
        mode (int): TODO: Type description here.
        path (string): TODO: Type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "key":'key',
        "mode":'mode',
        "path":'path'
    }

    def __init__(self,
                 key=None,
                 mode=None,
                 path=None):
        """Constructor for the PodInfo_PodSpec_VolumeInfo_KeyToPath class"""

        # Initialize members of the class
        self.key = key
        self.mode = mode
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
        key = dictionary.get('key')
        mode = dictionary.get('mode')
        path = dictionary.get('path')

        # Return an object of this model
        return cls(key,
                   mode,
                   path)


