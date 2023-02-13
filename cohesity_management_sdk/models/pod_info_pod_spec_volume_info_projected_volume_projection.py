# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc

import cohesity_management_sdk.models.pod_info_pod_spec_volume_info_projected_volume_projection_config_map_projection
import cohesity_management_sdk.models.pod_info_pod_spec_volume_info_projected_volume_projection_downward_api_projection
import cohesity_management_sdk.models.pod_info_pod_spec_volume_info_projected_volume_projection_service_account_token_projection

class PodInfo_PodSpec_VolumeInfo_Projected_VolumeProjection(object):

    """Implementation of the 'PodInfo_PodSpec_VolumeInfo_Projected_VolumeProjection' model.

    Specifies the parameters for configuration of IPMI. This is only needed
    for physical clusters.

    Attributes:
        config_map (PodInfo_PodSpec_VolumeInfo_Projected_VolumeProjection_ConfigMapProjection):
            TODO: Type description here
        downward_api (PodInfo_PodSpec_VolumeInfo_Projected_VolumeProjection_DownwardAPIProjection): TODO: Type description here
        secret (PodInfo_PodSpec_VolumeInfo_Projected_VolumeProjection_ConfigMapProjection): TODO: Type description here
        service_account_token (PodInfo_PodSpec_VolumeInfo_Projected_VolumeProjection_ServiceAccountTokenProjection): TODO: Type description here

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "config_map":'configMap',
        "downward_api":'downwardApi',
        "secret":'secret',
        "service_account_token":'serviceAccountToken'
    }

    def __init__(self,
                 config_map=None,
                 downward_api=None,
                 secret=None,
                 service_account_token=None):
        """Constructor for the PodInfo_PodSpec_VolumeInfo_Projected_VolumeProjection class"""

        # Initialize members of the class
        self.config_map = config_map
        self.downward_api = downward_api
        self.secret = secret
        self.service_account_token = service_account_token


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
        config_map = cohesity_management_sdk.models.pod_info_pod_spec_volume_info_projected_volume_projection_config_map_projection.PodInfo_PodSpec_VolumeInfo_Projected_VolumeProjection_ConfigMapProjection.from_dictionary(dictionary.get('configMap')) if dictionary.get('configMap') else None
        downward_api = cohesity_management_sdk.models.pod_info_pod_spec_volume_info_projected_volume_projection_downward_api_projection.PodInfo_PodSpec_VolumeInfo_Projected_VolumeProjection_DownwardAPIProjection.from_dictionary(dictionary.get('downwardApi')) if dictionary.get('downwardApi') else None
        secret = cohesity_management_sdk.models.pod_info_pod_spec_volume_info_projected_volume_projection_config_map_projection.PodInfo_PodSpec_VolumeInfo_Projected_VolumeProjection_ConfigMapProjection.from_dictionary(dictionary.get('secret')) if dictionary.get('secret') else None
        service_account_token = cohesity_management_sdk.models.pod_info_pod_spec_volume_info_projected_volume_projection_service_account_token_projection.PodInfo_PodSpec_VolumeInfo_Projected_VolumeProjection_ServiceAccountTokenProjection.from_dictionary(dictionary.get('serviceAccountToken')) if dictionary.get('serviceAccountToken') else None

        # Return an object of this model
        return cls(config_map,
                   downward_api,
                   secret,
                   service_account_token)


