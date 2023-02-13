# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class PodInfo_PodSpec_VolumeInfo_DownwardAPIVolumeFile_ObjectFieldSelector(object):

    """Implementation of the 'PodInfo_PodSpec_VolumeInfo_DownwardAPIVolumeFile_ObjectFieldSelector' model.

    IP Range for range of vip address addition.

    Attributes:
        api_version (string): TODO: Type description here.
        field_path (string): TODO: Type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "api_version": 'apiVersion',
        "field_path": 'fieldPath'
    }

    def __init__(self,
                 api_version=None,
                 field_path=None):
        """Constructor for the PodInfo_PodSpec_VolumeInfo_DownwardAPIVolumeFile_ObjectFieldSelector class"""

        # Initialize members of the class
        self.api_version = api_version
        self.field_path = field_path


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
        api_version = dictionary.get('apiVersion', None)
        field_path = dictionary.get('fieldPath', None)

        # Return an object of this model
        return cls(api_version,
                   field_path)


