# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.object_reference

class PodInfo_PodSpec_VolumeInfo_ScaleIO(object):

    """Implementation of the 'PodInfo_PodSpec_VolumeInfo_ScaleIO' model.

    Attributes:
        fs_type (string): TODO: Type description here.
        gateway (string): TODO: Type description here.
        protection_domain (string): TODO: Type description here.
        read_only (bool): TODO: Type description here.
        secret_ref (ObjectReference): TODO: Type description here.
        ssl_enabled (bool): TODO: Type description here.
        storage_mode (string): TODO: Type description here.
        storage_pool (string): TODO: Type description here.
        system (string): TODO: Type description here.
        volume_name (string): TODO: Type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "fs_type":'fsType',
        "gateway":'gateway',
        "protection_domain":'protectionDomain',
        "read_only":'readOnly',
        "secret_ref":'secretRef',
        "ssl_enabled":'sslEnabled',
        "storage_mode":'storageMode',
        "storage_pool":'storagePool',
        "system":'system',
        "volume_name":'volumeName'
    }

    def __init__(self,
                 fs_type=None,
                 gateway=None,
                 protection_domain=None,
                 read_only=None,
                 secret_ref=None,
                 ssl_enabled=None,
                 storage_mode=None,
                 storage_pool=None,
                 system=None,
                 volume_name=None):
        """Constructor for the PodInfo_PodSpec_VolumeInfo_ScaleIO class"""

        # Initialize members of the class
        self.fs_type = fs_type
        self.gateway = gateway
        self.protection_domain = protection_domain
        self.read_only = read_only
        self.secret_ref = secret_ref
        self.ssl_enabled = ssl_enabled
        self.storage_mode = storage_mode
        self.storage_pool = storage_pool
        self.system = system
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
        fs_type = dictionary.get('fsType')
        gateway = dictionary.get('gateway')
        protection_domain = dictionary.get('protectionDomain')
        read_only = dictionary.get('readOnly')
        secret_ref = cohesity_management_sdk.models.object_reference.ObjectReference.from_dictionary(dictionary.get('secretRef')) if dictionary.get('secretRef') else None
        ssl_enabled = dictionary.get('sslEnabled')
        storage_mode = dictionary.get('storageMode')
        storage_pool = dictionary.get('storagePool')
        system = dictionary.get('system')
        volume_name = dictionary.get('volumeName')

        # Return an object of this model
        return cls(fs_type,
                   gateway,
                   protection_domain,
                   read_only,
                   secret_ref,
                   ssl_enabled,
                   storage_mode,
                   storage_pool,
                   system,
                   volume_name)


