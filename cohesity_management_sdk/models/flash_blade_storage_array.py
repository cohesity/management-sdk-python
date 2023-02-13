# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.flash_blade_network_interface

class FlashBladeStorageArray(object):

    """Implementation of the 'FlashBladeStorageArray' model.

    Specifies information about a Pure Storage FlashBlade Array.

    Attributes:
        capacity_bytes (long|int): Specifies the total capacity in bytes of
            the Pure Storage FlashBlade Array.
        id (string): Specifies a unique id of a Pure Storage FlashBlade Array.
            The id is unique across Cohesity Clusters.
        networks (list of FlashBladeNetworkInterface): Specifies the network
            interfaces of the Pure Storage FlashBlade Array.
        physical_used_bytes (long|int): Specifies the space used for physical
            data in bytes.
        revision (string): Specifies the revision of the Pure Storage
            FlashBlade software.
        version (string): Specifies the software version running on the Pure
            Storage FlashBlade Array.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "capacity_bytes":'capacityBytes',
        "id":'id',
        "networks":'networks',
        "physical_used_bytes":'physicalUsedBytes',
        "revision":'revision',
        "version":'version'
    }

    def __init__(self,
                 capacity_bytes=None,
                 id=None,
                 networks=None,
                 physical_used_bytes=None,
                 revision=None,
                 version=None):
        """Constructor for the FlashBladeStorageArray class"""

        # Initialize members of the class
        self.capacity_bytes = capacity_bytes
        self.id = id
        self.networks = networks
        self.physical_used_bytes = physical_used_bytes
        self.revision = revision
        self.version = version


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
        capacity_bytes = dictionary.get('capacityBytes')
        id = dictionary.get('id')
        networks = None
        if dictionary.get('networks') != None:
            networks = list()
            for structure in dictionary.get('networks'):
                networks.append(cohesity_management_sdk.models.flash_blade_network_interface.FlashBladeNetworkInterface.from_dictionary(structure))
        physical_used_bytes = dictionary.get('physicalUsedBytes')
        revision = dictionary.get('revision')
        version = dictionary.get('version')

        # Return an object of this model
        return cls(capacity_bytes,
                   id,
                   networks,
                   physical_used_bytes,
                   revision,
                   version)


