# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class HypervDatastore(object):

    """Implementation of the 'HypervDatastore' model.

    Specifies information about a Datastore Object in HyperV environment.

    Attributes:
        capacity (int): Specifies the capacity of the datastore in bytes.
        free_space (int): Specifies the available space on the datastore in
            bytes.
        mount_points (list of string): Specifies the available mount points on
            the datastore.
        mtype (TypeHypervDatastoreEnum): Specifies the type of the datastore
            object like kFileShare or kVolume. overrideDescription: true
            Specifies the type of a HyperV datastore object. 'kFileShare'
            indicates SMB file share datastore. 'kVolume' indicates a volume
            which can a LUN.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "capacity":'capacity',
        "free_space":'freeSpace',
        "mount_points":'mountPoints',
        "mtype":'type'
    }

    def __init__(self,
                 capacity=None,
                 free_space=None,
                 mount_points=None,
                 mtype=None):
        """Constructor for the HypervDatastore class"""

        # Initialize members of the class
        self.capacity = capacity
        self.free_space = free_space
        self.mount_points = mount_points
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
        capacity = dictionary.get('capacity')
        free_space = dictionary.get('freeSpace')
        mount_points = dictionary.get('mountPoints')
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(capacity,
                   free_space,
                   mount_points,
                   mtype)


