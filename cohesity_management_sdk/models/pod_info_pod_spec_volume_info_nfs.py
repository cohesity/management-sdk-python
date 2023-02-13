# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class PodInfo_PodSpec_VolumeInfo_NFS(object):

    """Implementation of the 'PodInfo_PodSpec_VolumeInfo_NFS' model.

    Attributes:
        path (string):  TODO: Type description here.
        read_only (bool): TODO: Type description here.
        server (string): TODO: Type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "path":'path',
        "read_only":'readOnly',
        "server":'server'
    }

    def __init__(self,
                 path=None,
                 read_only=None,
                 server=None):
        """Constructor for the PodInfo_PodSpec_VolumeInfo_NFS class"""

        # Initialize members of the class
        self.path = path
        self.read_only = read_only
        self.server = server


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
        read_only = dictionary.get('readOnly')
        server = dictionary.get('server')

        # Return an object of this model
        return cls(path,
                   read_only,
                   server)


