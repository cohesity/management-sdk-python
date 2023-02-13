# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class PodInfo_PodSpec_VolumeInfo_DownwardAPIVolumeFile_ResourceFieldSelector(object):

    """Implementation of the 'PodInfo_PodSpec_VolumeInfo_DownwardAPIVolumeFile_ResourceFieldSelector' model.

    Attributes:
        container_name (string): TODO: Type description here.
        divisor (string): TODO: Type description here.
        resource (string): TODO: Type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "container_name":'containerName',
        "divisor":'divisor',
        "resource":'resource'
    }

    def __init__(self,
                 container_name=None,
                 divisor=None,
                 resource=None):
        """Constructor for the PodInfo_PodSpec_VolumeInfo_DownwardAPIVolumeFile_ResourceFieldSelector class"""

        # Initialize members of the class
        self.container_name = container_name
        self.divisor = divisor
        self.resource = resource


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
        container_name = dictionary.get('containerName')
        divisor = dictionary.get('divisor')
        resource = dictionary.get('resource')

        # Return an object of this model
        return cls(container_name,
                   divisor,
                   resource)


