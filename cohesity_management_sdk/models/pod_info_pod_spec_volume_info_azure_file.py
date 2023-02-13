# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class PodInfo_PodSpec_VolumeInfo_AzureFile(object):

    """Implementation of the 'PodInfo_PodSpec_VolumeInfo_AzureFile' model.

    Attributes:
        read_only (string): TODO: Type description here.
        secret_name (string): TODO: Type description here.
        share_name (string): TODO: Type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "read_only":'readOnly',
        "secret_name":'secretName',
        "share_name":'shareName'
    }

    def __init__(self,
                 read_only=None,
                 secret_name=None,
                 share_name=None):
        """Constructor for the PodInfo_PodSpec_VolumeInfo_AzureFile class"""

        # Initialize members of the class
        self.read_only = read_only
        self.secret_name = secret_name
        self.share_name = share_name


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
        read_only = dictionary.get('readOnly')
        secret_name = dictionary.get('secretName')
        share_name = dictionary.get('shareName')

        # Return an object of this model
        return cls(read_only,
                   secret_name,
                   share_name)


