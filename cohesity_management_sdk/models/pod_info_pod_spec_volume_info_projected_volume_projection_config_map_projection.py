# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.pod_info_pod_spec_volume_info_key_to_path

class PodInfo_PodSpec_VolumeInfo_Projected_VolumeProjection_ConfigMapProjection(object):

    """Implementation of the 'PodInfo_PodSpec_VolumeInfo_Projected_VolumeProjection_ConfigMapProjection' model.

    Attributes:
        items (list of PodInfo_PodSpec_VolumeInfo_KeyToPath): 
            TODO: Type description here.
        name (string): TODO: Type description here.
        optional (bool): TODO: Type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "items":'items',
        "name":'name',
        "optional":'optional'
    }

    def __init__(self,
                 items=None,
                 name=None,
                 optional=None):
        """Constructor for the PodInfo_PodSpec_VolumeInfo_Projected_VolumeProjection_ConfigMapProjection class"""

        # Initialize members of the class
        self.items = items
        self.name = name
        self.optional = optional


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
        items = None
        if dictionary.get('items'):
            items = list()
            for structure in dictionary.get('items'):
                items.append(cohesity_management_sdk.models.pod_info_pod_spec_volume_info_key_to_path.PodInfo_PodSpec_VolumeInfo_KeyToPath.from_dictionary(structure))
        name = dictionary.get('name')
        optional = dictionary.get('optional')

        # Return an object of this model
        return cls(items,
                   name,
                   optional)


