# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.pod_info_pod_spec_volume_info_projected_volume_projection

class PodInfo_PodSpec_VolumeInfo_Projected(object):

    """Implementation of the 'PodInfo_PodSpec_VolumeInfo_Projected' model.

    Attributes:
        default_mode (int): TODO: Type description here.
        sources (list of PodInfo_PodSpec_VolumeInfo_Projected_VolumeProjection):
            TODO: Type description here.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "default_mode": 'defaultMode',
        "sources": 'sources'
    }

    def __init__(self,
                 default_mode=None,
                 sources=None):
        """Constructor for the PodInfo_PodSpec_VolumeInfo_Projected class"""

        # Initialize members of the class
        self.default_mode = default_mode
        self.sources = sources


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
        sources = None
        if dictionary.get('sources', None):
            sources = list()
            for structure in dictionary.get('sources'):
                sources.append(cohesity_management_sdk.models.pod_info_pod_spec_volume_info_projected_volume_projection.PodInfo_PodSpec_VolumeInfo_Projected_VolumeProjection.from_dictionary(structure))

        # Return an object of this model
        return cls(default_mode,
                   sources)


