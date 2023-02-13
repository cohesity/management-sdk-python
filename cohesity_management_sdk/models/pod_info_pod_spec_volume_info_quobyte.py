# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class PodInfo_PodSpec_VolumeInfo_Quobyte(object):

    """Implementation of the 'PodInfo_PodSpec_VolumeInfo_Quobyte' model.

    Represents a Quobyte mount that lasts the lifetime of a pod.

    Attributes:
        group (string): TODO: Type description here.
        read_only (bool): TODO: Type description here.
        registry (string): TODO: Type description here.
        tenant (string): TODO: Type description here.
        user (string): TODO: Type description here.
        volume (string): TODO: Type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "group": 'group',
        "read_only": 'readOnly',
        "registry":'registry',
        "tenant":'tenant',
        "user":'user',
        "volume":'volume'
    }

    def __init__(self,
                 group=None,
                 read_only=None,
                 registry=None,
                 tenant=None,
                 user=None,
                 volume=None
                 ):
        """Constructor for the PodInfo_PodSpec_VolumeInfo_Quobyte class"""

        # Initialize members of the class
        self.group = group
        self.read_only = read_only
        self.registry = registry
        self.tenant = tenant
        self.user = user
        self.volume = volume

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
        group = dictionary.get('group')
        read_only = dictionary.get('readOnly')
        registry = dictionary.get('registry')
        tenant = dictionary.get('tenant')
        user = dictionary.get('user')
        volume = dictionary.get('volume')

        # Return an object of this model
        return cls(group,
                   read_only,
                   registry,
                   tenant,
                   user,
                   volume)


