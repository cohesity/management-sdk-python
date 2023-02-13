# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.pod_info_pod_spec_volume_info_downward_api_volume_file

class PodInfo_PodSpec_VolumeInfo_DownwardAPI(object):

    """Implementation of the 'PodInfo_PodSpec_VolumeInfo_DownwardAPI' model.

    DownwardAPIVolumeSource represents a volume containing downward API info.

    Attributes:
        default_mode (int): TODO: Type description here.
        items (list of PodInfo_PodSpec_VolumeInfo_DownwardAPIVolumeFile): TODO: Type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "default_mode": 'defaultMode',
        "items": 'items'
    }

    def __init__(self,
                 default_mode=None,
                 items=None):
        """Constructor for the PodInfo_PodSpec_VolumeInfo_DownwardAPI class"""

        # Initialize members of the class
        self.default_mode = default_mode
        self.items = items


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
        default_mode = dictionary.get('defaultMode', None)
        items = None
        if dictionary.get('items', None):
            items= list()
            for structure in dictionary.get('items'):
                items.append(cohesity_management_sdk.models.pod_info_pod_spec_volume_info_downward_api_volume_file.PodInfo_PodSpec_VolumeInfo_DownwardAPIVolumeFile.from_dictionary(structure))

        # Return an object of this model
        return cls(default_mode,
                   items)


