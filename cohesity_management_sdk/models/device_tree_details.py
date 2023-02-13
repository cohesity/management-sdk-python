# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.device_node

class DeviceTreeDetails(object):

    """Implementation of the 'DeviceTreeDetails' model.

    Specifies a logical volume stored as a tree where the leaves are
    the blocks of partitions and intermediate nodes are assembled by
    combining
    nodes using one of the following modes: linear layout, striped,
    mirrored, RAID etc.
    A deviceTree is a block device formed by combining one or more Devices
    using a combining strategy.

    Attributes:
        combine_method (CombineMethodEnum): Specifies how to combine the
            children of this node. The combining strategy for child devices.
            Some of these strategies imply constraint on the number of child
            devices. e.g. RAID5 will have 5 children. 'LINEAR' indicates
            children are juxtaposed to form this device. 'STRIPE' indicates
            children are striped. 'MIRROR' indicates children are mirrored.
            'RAID5' 'RAID6' 'ZERO' 'THIN' 'THINPOOL' 'SNAPSHOT' 'CACHE'
            'CACHEPOOL'
        device_length (long|int): Specifies the length of this device. This
            number should match the length that is calculated from the
            children and combining method.
        device_nodes (list of DeviceNode): Specifies the children of this node
            in the device tree.
        stripe_size (int): Specifies the size of the striped data if the data
            is striped.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "combine_method":'combineMethod',
        "device_length":'deviceLength',
        "device_nodes":'deviceNodes',
        "stripe_size":'stripeSize'
    }

    def __init__(self,
                 combine_method=None,
                 device_length=None,
                 device_nodes=None,
                 stripe_size=None):
        """Constructor for the DeviceTreeDetails class"""

        # Initialize members of the class
        self.combine_method = combine_method
        self.device_length = device_length
        self.device_nodes = device_nodes
        self.stripe_size = stripe_size


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
        combine_method = dictionary.get('combineMethod')
        device_length = dictionary.get('deviceLength')
        device_nodes = None
        if dictionary.get('deviceNodes') != None:
            device_nodes = list()
            for structure in dictionary.get('deviceNodes'):
                device_nodes.append(cohesity_management_sdk.models.device_node.DeviceNode.from_dictionary(structure))
        stripe_size = dictionary.get('stripeSize')

        # Return an object of this model
        return cls(combine_method,
                   device_length,
                   device_nodes,
                   stripe_size)


