# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.uda_cluster
import cohesity_management_sdk.models.uda_object

class UdaProtectionSource(object):

    """Implementation of the 'UdaProtectionSource' model.

    Specifies an Object representing Universal Data Adapter.

    Attributes:
        cluster_info (UdaCluster): Information of a Universal Data
            Adapter cluster, only valid for an entity of mtype kCluster.
        name (string): Specifies the instance name of the Universal Data
            Adapter entity.
        object_info (UdaObject): Information of a Universal Data Adapter
            object, only valid for an entity of
        uuid (string): Specifies the UUID for the Universal Data Adapter entity.
        mtype (TypeUdaProtectionSourceEnum): Specifies the mtype of the managed
            Object in Universal Data Adapter Protection Source.
            Specifies the mtype of an Universal Data Adapter source entity.
            'kCluster' indicates a Universal Data Adapter source, possibly
            distributed over several physical nodes.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cluster_info":'clusterInfo',
        "name":'name',
        "object_info":'objectInfo',
        "uuid":'uuid',
        "mtype":'type'
    }

    def __init__(self,
                 cluster_info=None,
                 name=None,
                 object_info=None,
                 uuid=None,
                 mtype=None):
        """Constructor for the UdaProtectionSource class"""

        # Initialize members of the class
        self.cluster_info = cluster_info
        self.name = name
        self.object_info = object_info
        self.uuid = uuid
        self.mtype = mtype


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
        cluster_info = cohesity_management_sdk.models.uda_cluster.UdaCluster.from_dictionary(dictionary.get('clusterInfo')) if dictionary.get('clusterInfo') else None
        name = dictionary.get('name')
        object_info = cohesity_management_sdk.models.uda_object.UdaObject.from_dictionary(dictionary.get('objectInfo')) if dictionary.get('objectInfo') else None
        mtype = dictionary.get('type')
        uuid = dictionary.get('uuid')

        # Return an object of this model
        return cls(cluster_info,
                   name,
                   object_info,
                   uuid,
                   mtype)


