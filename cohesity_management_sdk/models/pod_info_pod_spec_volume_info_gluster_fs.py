# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class PodInfo_PodSpec_VolumeInfo_GlusterFs(object):

    """Implementation of the 'PodInfo_PodSpec_VolumeInfo_GlusterFs' model.

    Attributes:
        endpoints (string): TODO: Type description here.
        path (string): TODO: Type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "endpoints": 'endpoints',
        "path": 'path'
    }

    def __init__(self,
                 endpoints=None,
                 path=None):
        """Constructor for the PodInfo_PodSpec_VolumeInfo_GlusterFs class"""

        # Initialize members of the class
        self.endpoints = endpoints
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
        endpoints = dictionary.get('endpoints', None)
        path = dictionary.get('path', None)

        # Return an object of this model
        return cls(endpoints,
                   path)


