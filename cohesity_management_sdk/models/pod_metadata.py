# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.pod_metadata_volume_info


class PodMetadata(object):

    """Implementation of the 'PodMetadata' model.

    This message defines the pod metadata which will be stored in
    SnapshotInfoProto for Kubernetes backup and restore with Datamover.

    Attributes:
        name (string): Name of the pod.
        node_name (string): Name of the node where pod is running.
        uid (string): Uid of the pod.
        volume_vec (list of PodMetadata_VolumeInfo): Metadata of the volumes that are attached to this pod.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "node_name":'nodeName',
        "uid":'uid',
        "volume_vec":'volumeVec'
    }

    def __init__(self,
                 name=None,
                 node_name=None,
                 uid=None,
                 volume_vec=None):
        """Constructor for the PodMetadata class"""

        # Initialize members of the class
        self.name = name
        self.node_name = node_name
        self.uid = uid
        self.volume_vec = volume_vec


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
        name = dictionary.get('name')
        node_name = dictionary.get('nodeName')
        uid = dictionary.get('uid')
        volume_vec = None
        if dictionary.get('volumeVec'):
            volume_vec = list()
            for structure in dictionary.get('volumeVec'):
                volume_vec.append(cohesity_management_sdk.models.pod_metadata_volume_info.PodMetadata_VolumeInfo.from_dictionary(structure))


        # Return an object of this model
        return cls(name,
                   node_name,
                   uid,
                   volume_vec)


