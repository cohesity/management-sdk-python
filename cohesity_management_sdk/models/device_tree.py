# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.device_tree_child_device


class DeviceTree(object):

    """Implementation of the 'DeviceTree' model.

    A logical volume is built on a tree where leaves are the slices of
    partitions (PartitionSlice) defined below and intermediate nodes are
    assembled by combining nodes in some mode (linear layout, striped,
    mirrored,
    RAID etc).
    A DeviceTree is a block device formed by combining one or more Devices
    using a combining strategy.

    Attributes:
        child_vec (list of DeviceTreeChildDevice): TODO: type description
            here.
        device_id (int): Internal device identifier of the device to be
            activated as a thin volume.
        device_length (long|int): The length of this device. This should match
            the length which is computable based on children and combining
            strategy.  e.g. if there is only one partition slice in an LVM
            volume, 'length' in the partition slice is equal to
            'device_length'.
        stripe_size (int): In case data is striped, this represents the length
            of the stripe. The number of stripes is defined by the size of
            child_vec above.
        thin_pool_chunk_size (int): Chunk size. Only populated if device type is
            thin pool.
        mtype (int): How to combine the children.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "child_vec":'childVec',
        "device_id":'deviceId',
        "device_length":'deviceLength',
        "stripe_size":'stripeSize',
        "thin_pool_chunk_size":'thinPoolChunkSize',
        "mtype":'type'
    }

    def __init__(self,
                 child_vec=None,
                 device_id=None,
                 device_length=None,
                 stripe_size=None,
                 thin_pool_chunk_size=None,
                 mtype=None):
        """Constructor for the DeviceTree class"""

        # Initialize members of the class
        self.child_vec = child_vec
        self.device_id = device_id
        self.device_length = device_length
        self.stripe_size = stripe_size
        self.thin_pool_chunk_size = thin_pool_chunk_size
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
        child_vec = None
        device_id = dictionary.get('deviceId', None)
        if dictionary.get('childVec') != None:
            child_vec = list()
            for structure in dictionary.get('childVec'):
                child_vec.append(cohesity_management_sdk.models.device_tree_child_device.DeviceTreeChildDevice.from_dictionary(structure))
        device_length = dictionary.get('deviceLength')
        stripe_size = dictionary.get('stripeSize')
        thin_pool_chunk_size = dictionary.get('thinPoolChunkSize', None)
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(child_vec,
                   device_id,
                   device_length,
                   stripe_size,
                   thin_pool_chunk_size,
                   mtype)
