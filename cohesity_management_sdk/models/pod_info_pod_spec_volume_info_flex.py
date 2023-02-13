# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.object_reference
import cohesity_management_sdk.models.pod_info_pod_spec_volume_info_flex_options_entry

class PodInfo_PodSpec_VolumeInfo_Flex(object):

    """Implementation of the 'PodInfo_PodSpec_VolumeInfo_Flex' model.

    Specifies an Object representing Universal Data Adapter.

    Attributes:
        driver (string): TODO: Type description here.
        fs_type (string): TODO: Type description here.
        options (list of PodInfo_PodSpec_VolumeInfo_Flex_OptionsEntry): TODO: Type description here.
        read_only (bool): TODO: Type description here.
        secretRef (ObjectReference): TODO: Type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "driver":'driver',
        "fs_type":'fsType',
        "options":'options',
        "read_only":'readOnly',
        "secretRef":'secretRef'
    }

    def __init__(self,
                 driver=None,
                 fs_type=None,
                 options=None,
                 read_only=None,
                 secretRef=None):
        """Constructor for the PodInfo_PodSpec_VolumeInfo_Flex class"""

        # Initialize members of the class
        self.driver = driver
        self.fs_type = fs_type
        self.options = options
        self.read_only = read_only
        self.secretRef = secretRef


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
        driver = cohesity_management_sdk.models.uda_cluster.UdaCluster.from_dictionary(dictionary.get('driver')) if dictionary.get('driver') else None
        fs_type = dictionary.get('fsType')
        options = None
        if dictionary.get('options'):
            options = list()
            for structure in dictionary.get('options'):
                options.append(cohesity_management_sdk.models.pod_info_pod_spec_volume_info_flex_options_entry.PodInfo_PodSpec_VolumeInfo_Flex_OptionsEntry.from_dictionary(structure))
        read_only = dictionary.get('readOnly')
        secretRef = cohesity_management_sdk.models.object_reference.ObjectReference.from_dictionary(dictionary.get('secretRef')) if dictionary.get('secretRef') else None

        # Return an object of this model
        return cls(driver,
                   fs_type,
                   options,
                   read_only,
                   secretRef)


