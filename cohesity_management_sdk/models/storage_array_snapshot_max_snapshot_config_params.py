# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class StorageArraySnapshotMaxSnapshotConfigParams(object):

    """Implementation of the 'StorageArraySnapshotMaxSnapshotConfigParams' model.

    TODO: type description here.


    Attributes:

        max_snapshots (int): Max number of storage snapshots allowed per
            volume/lun.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "max_snapshots":'maxSnapshots',
    }
    def __init__(self,
                 max_snapshots=None,
            ):

        """Constructor for the StorageArraySnapshotMaxSnapshotConfigParams class"""

        # Initialize members of the class
        self.max_snapshots = max_snapshots

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
        max_snapshots = dictionary.get('maxSnapshots')

        # Return an object of this model
        return cls(
            max_snapshots
)