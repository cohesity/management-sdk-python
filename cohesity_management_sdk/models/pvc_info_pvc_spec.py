# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.label_selector
import cohesity_management_sdk.models.object_reference
import cohesity_management_sdk.models.pvc_info_pvc_spec_resources


class PVCInfo_PVCSpec(object):

    """Implementation of the 'PVCInfo_PVCSpec' model.

    TODO: type description here.


    Attributes:

        access_modes (list of string): AccessModes contains the desired access
            modes the volume should have.
        data_source (ObjectReference): This field can be used to specify
            either: An existing VolumeSnapshot object An existing PVC
            (PersistentVolumeClaim) An existing custom resource/object that
            implements data population.
        resources (PVCInfo_PVCSpec_Resources): Resources represents the minimum
            resources the volume should have.
        selector (LabelSelector): A label query over volumes to consider for
            binding.
        storage_class_name (string): Name of the StorageClass required by the
            claim.
        volume_mode (string): volumeMode defines what type of volume is
            required by the claim. Value of Filesystem is implied when not
            included in claim spec.
        volume_name (string): Name of the volume that is using this PVC.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "access_modes":'accessModes',
        "data_source":'dataSource',
        "resources":'resources',
        "selector":'selector',
        "storage_class_name":'storageClassName',
        "volume_mode":'volumeMode',
        "volume_name":'volumeName',
    }
    def __init__(self,
                 access_modes=None,
                 data_source=None,
                 resources=None,
                 selector=None,
                 storage_class_name=None,
                 volume_mode=None,
                 volume_name=None,
            ):

        """Constructor for the PVCInfo_PVCSpec class"""

        # Initialize members of the class
        self.access_modes = access_modes
        self.data_source = data_source
        self.resources = resources
        self.selector = selector
        self.storage_class_name = storage_class_name
        self.volume_mode = volume_mode
        self.volume_name = volume_name

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
        access_modes = dictionary.get("accessModes")
        data_source = cohesity_management_sdk.models.object_reference.ObjectReference.from_dictionary(dictionary.get('dataSource')) if dictionary.get('dataSource') else None
        resources = cohesity_management_sdk.models.pvc_info_pvc_spec_resources.PVCInfo_PVCSpec_Resources.from_dictionary(dictionary.get('resources')) if dictionary.get('resources') else None
        selector = cohesity_management_sdk.models.label_selector.LabelSelector.from_dictionary(dictionary.get('selector')) if dictionary.get('selector') else None
        storage_class_name = dictionary.get('storageClassName')
        volume_mode = dictionary.get('volumeMode')
        volume_name = dictionary.get('volumeName')

        # Return an object of this model
        return cls(
            access_modes,
            data_source,
            resources,
            selector,
            storage_class_name,
            volume_mode,
            volume_name
)