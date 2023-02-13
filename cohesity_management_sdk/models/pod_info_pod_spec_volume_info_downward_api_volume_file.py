# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.pod_info_pod_spec_volume_info_downward_api_volume_file_object_field_selector
import cohesity_management_sdk.models.pod_info_pod_spec_volume_info_downward_api_volume_file_resource_field_selector

class PodInfo_PodSpec_VolumeInfo_DownwardAPIVolumeFile(object):

    """Implementation of the 'PodInfo_PodSpec_VolumeInfo_DownwardAPIVolumeFile' model.

    DownwardAPIVolumeFile represents information to create the file containing
    the pod field.

    Attributes:
        field_ref (PodInfo_PodSpec_VolumeInfo_DownwardAPIVolumeFile_ObjectFieldSelector):
            TODO: Type description here.
        mode (int): TODO: Type description here.
        path (string): TODO: Type description here.
        resource_field_ref (PodInfo_PodSpec_VolumeInfo_DownwardAPIVolumeFile_ResourceFieldSelector): TODO: Type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "field_ref":'fieldRef',
        "mode":'mode',
        "path":'path',
        "resource_field_ref":'resourceFieldRef'
    }

    def __init__(self,
                 field_ref=None,
                 mode=None,
                 path=None,
                 resource_field_ref=None):
        """Constructor for the PodInfo_PodSpec_VolumeInfo_DownwardAPIVolumeFile class"""

        # Initialize members of the class
        self.field_ref = field_ref
        self.mode = mode
        self.path = path
        self.resource_field_ref = resource_field_ref


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
        field_ref = cohesity_management_sdk.models.pod_info_pod_spec_volume_info_downward_api_volume_file_object_field_selector.PodInfo_PodSpec_VolumeInfo_DownwardAPIVolumeFile_ObjectFieldSelector.from_dictionary(dictionary.get('fieldRef')) if dictionary.get('fieldRef') else None
        mode = dictionary.get('mode')
        path = dictionary.get('path')
        resource_field_ref = cohesity_management_sdk.models.pod_info_pod_spec_volume_info_downward_api_volume_file_resource_field_selector.PodInfo_PodSpec_VolumeInfo_DownwardAPIVolumeFile_ResourceFieldSelector.from_dictionary(dictionary.get('resourceFieldRef')) if dictionary.get('resourceFieldRef') else None

        # Return an object of this model
        return cls(field_ref,
                   mode,
                   path,
                   resource_field_ref)


