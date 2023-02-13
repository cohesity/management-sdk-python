# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class PodInfo_PodSpec_VolumeInfo_Cephfs(object):

    """Implementation of the 'PodInfo_PodSpec_VolumeInfo_Cephfs' model.

    Attributes:
        monitors (list of string): TODO: Type description here.
        read_only (string): TODO: Type description here.
        secret_file (string): TODO: Type description here.
        user (string): TODO: Type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "monitors":'monitors',
        "read_only":'readOnly',
        "secret_file":'secretFile',
        "user":'user'
    }

    def __init__(self,
                 monitors=None,
                 read_only=None,
                 secret_file=None,
                 user=None):
        """Constructor for the PodInfo_PodSpec_VolumeInfo_Cephfs class"""

        # Initialize members of the class
        self.monitors = monitors
        self.read_only = read_only
        self.secret_file = secret_file
        self.user = user


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
        monitors = dictionary.get('monitors')
        read_only = dictionary.get('readOnly')
        secret_file = dictionary.get('secretFile')
        user = dictionary.get('user')

        # Return an object of this model
        return cls(monitors,
                   read_only,
                   secret_file,
                   user)


