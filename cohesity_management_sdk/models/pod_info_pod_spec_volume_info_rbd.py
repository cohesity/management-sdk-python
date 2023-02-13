# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.object_reference

class PodInfo_PodSpec_VolumeInfo_RBD(object):

    """Implementation of the 'PodInfo_PodSpec_VolumeInfo_RBD' model.

    Represents a Rados Block Device mount that lasts the lifetime of a pod.

    Attributes:
        fs_type (string): TODO: Type description here.
        image (string): TODO: Type description here.
        keyring (bool): TODO: Type description here.
        monitors (list of string): TODO: Type description here.
        pool (bool): TODO: Type description here.
        read_only (string): TODO: Type description here.
        secret_ref (ObjectReference): TODO: Type description here.
        user (string): TODO: Type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "fs_type":'fsType',
        "image":'image',
        "keyring":'keyring',
        "monitors":'monitors',
        "pool":'pool',
        "read_only":'readOnly',
        "secret_ref":'secretRef',
        "user":'user'
    }

    def __init__(self,
                 fs_type=None,
                 image=None,
                 keyring=None,
                 monitors=None,
                 pool=None,
                 read_only=None,
                 secret_ref=None,
                 user=None):
        """Constructor for the PodInfo_PodSpec_VolumeInfo_RBD class"""

        # Initialize members of the class
        self.fs_type = fs_type
        self.image = image
        self.keyring = keyring
        self.monitors = monitors
        self.pool = pool
        self.read_only = read_only
        self.secret_ref = secret_ref
        self.user = user


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
        image = dictionary.get('image')
        keyring = dictionary.get('keyring')
        monitors = dictionary.get('monitors')
        pool = dictionary.get('pool')
        read_only = dictionary.get('readOnly')
        secret_ref = cohesity_management_sdk.models.object_reference.ObjectReference.from_dictionary(dictionary.get('secretRef')) if dictionary.get('secretRef') else None
        user = dictionary.get('user')

        # Return an object of this model
        return cls(fs_type,
                   image,
                   keyring,
                   monitors,
                   pool,
                   read_only,
                   secret_ref,
                   user)


