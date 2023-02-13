# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.object_reference
import cohesity_management_sdk.models.pod_info_pod_spec_volume_info_csi_volume_attributes_entry

class PodInfo_PodSpec_VolumeInfo_CSI(object):

    """Implementation of the 'PodInfo_PodSpec_VolumeInfo_CSI' model.

    Specifies the parameters of updating view alias op.

    Attributes:
        controller_expand_secret_ref (ObjectReference): TODO: Type description
            here.
        controller_publish_secret_ref (ObjectReference): TODO: Type description
            here.
        driver (bool): TODO: Type description here.
        fs_type (bool): TODO: Type description here.
        node_publish_secret_ref (ObjectReference):  TODO: Type description here.
        node_stage_secret_ref (ObjectReference):  TODO: Type description here.
        read_only (bool): TODO: Type description here.
        volume_attributes (list of PodInfo_PodSpec_VolumeInfo_CSI_VolumeAttributesEntry):
            TODO: Type description here.
        volume_handle (string):  TODO: Type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "controller_expand_secret_ref":'controllerExpandSecretRef',
        "controller_publish_secret_ref":'controllerPublishSecretRef',
        "driver":'driver',
        "fs_type":'fsType',
        "node_publish_secret_ref":'nodePublishSecretRef',
        "node_stage_secret_ref":'nodeStageSecretRef',
        "volume_attributes":'volumeAttributes',
        "read_only":'readOnly',
        "volume_handle":'volumeHandle'
    }

    def __init__(self,
                 controller_expand_secret_ref=None,
                 controller_publish_secret_ref=None,
                 driver=None,
                 fs_type=None,
                 node_publish_secret_ref=None,
                 node_stage_secret_ref=None,
                 volume_attributes=None,
                 read_only=None,
                 volume_handle=None):
        """Constructor for the PodInfo_PodSpec_VolumeInfo_CSI class"""

        # Initialize members of the class
        self.controller_expand_secret_ref = controller_expand_secret_ref
        self.controller_publish_secret_ref = controller_publish_secret_ref
        self.driver = driver
        self.fs_type = fs_type
        self.node_publish_secret_ref = node_publish_secret_ref
        self.node_stage_secret_ref = node_stage_secret_ref
        self.volume_attributes = volume_attributes
        self.read_only = read_only
        self.volume_handle = volume_handle


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
        controller_expand_secret_ref = cohesity_management_sdk.models.object_reference.ObjectReference.from_dictionary(dictionary.get('controllerExpandSecretRef')) if dictionary.get('controllerExpandSecretRef') else None
        controller_publish_secret_ref = cohesity_management_sdk.models.object_reference.ObjectReference.from_dictionary(dictionary.get('controllerPublishSecretRef')) if dictionary.get('controllerPublishSecretRef') else None
        driver = dictionary.get('driver')
        fs_type = dictionary.get('fsType')
        node_publish_secret_ref = cohesity_management_sdk.models.object_reference.ObjectReference.from_dictionary(dictionary.get('nodePublishSecretRef')) if dictionary.get('nodePublishSecretRef') else None
        node_stage_secret_ref = cohesity_management_sdk.models.object_reference.ObjectReference.from_dictionary(dictionary.get('nodeStageSecretRef')) if dictionary.get('nodeStageSecretRef') else None
        volume_attributes = None
        if dictionary.get('volumeAttributes') != None:
            volume_attributes = list()
            for structure in dictionary.get('volumeAttributes'):
                volume_attributes.append(cohesity_management_sdk.models.pod_info_pod_spec_volume_info_csi_volume_attributes_entry.PodInfo_PodSpec_VolumeInfo_CSI_VolumeAttributesEntry.from_dictionary(structure))
        read_only = dictionary.get('readOnly')
        volume_handle = dictionary.get('volumeHandle')

        # Return an object of this model
        return cls(controller_expand_secret_ref,
                   controller_publish_secret_ref,
                   driver,
                   fs_type,
                   node_publish_secret_ref,
                   node_stage_secret_ref,
                   volume_attributes,
                   read_only,
                   volume_handle)