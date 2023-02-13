# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.object_reference

class PodInfo_PodSpec_VolumeInfo_StorageOS(object):

    """Implementation of the 'PodInfo_PodSpec_VolumeInfo_StorageOS' model.

    Specifies an Object representing Universal Data Adapter.

    Attributes:
        fs_type (string): TODO: Type description here.
        read_only (bool): TODO: Type description here.
        secret_ref (ObjectReference): TODO: Type description here.
        volume_name (string): TODO: Type description here.
        volume_namespace (TypePodInfo_PodSpec_VolumeInfo_StorageOSEnum):TODO: Type description here.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "fs_type":'fsType',
        "read_only":'readOnly',
        "secret_ref":'secretRef',
        "volume_name":'volumeName',
        "volume_namespace":'volumeNamespace'
    }

    def __init__(self,
                 fs_type=None,
                 read_only=None,
                 secret_ref=None,
                 volume_name=None,
                 volume_namespace=None):
        """Constructor for the PodInfo_PodSpec_VolumeInfo_StorageOS class"""

        # Initialize members of the class
        self.fs_type = fs_type
        self.read_only = read_only
        self.secret_ref = secret_ref
        self.volume_name = volume_name
        self.volume_namespace = volume_namespace


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
        fs_type =  dictionary.get('fsType')
        read_only = dictionary.get('readOnly')
        secret_ref = cohesity_management_sdk.models.object_reference.ObjectReference.from_dictionary(dictionary.get('secretRef')) if dictionary.get('secretRef') else None
        volume_namespace = dictionary.get('volumeNamespace')
        volume_name = dictionary.get('volumeName')

        # Return an object of this model
        return cls(fs_type,
                   read_only,
                   secret_ref,
                   volume_name,
                   volume_namespace)


