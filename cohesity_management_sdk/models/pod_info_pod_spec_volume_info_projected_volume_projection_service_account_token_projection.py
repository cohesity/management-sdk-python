# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class PodInfo_PodSpec_VolumeInfo_Projected_VolumeProjection_ServiceAccountTokenProjection(object):

    """Implementation of the 'PodInfo_PodSpec_VolumeInfo_Projected_VolumeProjection_ServiceAccountTokenProjection' model.

    Attributes:
        audience (string): TODO: Type description here.
        expiration_seconds (int): TODO: Type description here.
        path (string): TODO: Type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "audience":'audience',
        "expiration_seconds":'expirationSeconds',
        "path":'path'
    }

    def __init__(self,
                 audience=None,
                 expiration_seconds=None,
                 path=None):
        """Constructor for the PodInfo_PodSpec_VolumeInfo_Projected_VolumeProjection_ServiceAccountTokenProjection class"""

        # Initialize members of the class
        self.audience = audience
        self.expiration_seconds = expiration_seconds
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
        audience = dictionary.get('audience')
        expiration_seconds = dictionary.get('expirationSeconds')
        path = dictionary.get('path')

        # Return an object of this model
        return cls(audience,
                   expiration_seconds,
                   path)


