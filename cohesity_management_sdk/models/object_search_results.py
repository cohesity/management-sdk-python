# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.object_snapshot_info

class ObjectSearchResults(object):

    """Implementation of the 'ObjectSearchResults' model.

    Specifies an array of backup objects and a count to indicate
    if additional requests must be made to get the full result.

    Attributes:
        object_snapshot_info (list of ObjectSnapshotInfo): Array of Snapshot
            Objects.  Specifies the list of backup objects returned by this
            request that match the specified search and filter criteria. The
            number of objects returned is limited by the pageCount field.
        total_count (long|int): Specifies the total number of backup objects
            that match the filter and search criteria. Use this value to
            determine how many additional requests are required to get the
            full result.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "object_snapshot_info":'objectSnapshotInfo',
        "total_count":'totalCount'
    }

    def __init__(self,
                 object_snapshot_info=None,
                 total_count=None):
        """Constructor for the ObjectSearchResults class"""

        # Initialize members of the class
        self.object_snapshot_info = object_snapshot_info
        self.total_count = total_count


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
        object_snapshot_info = None
        if dictionary.get('objectSnapshotInfo') != None:
            object_snapshot_info = list()
            for structure in dictionary.get('objectSnapshotInfo'):
                object_snapshot_info.append(cohesity_management_sdk.models.object_snapshot_info.ObjectSnapshotInfo.from_dictionary(structure))
        total_count = dictionary.get('totalCount')

        # Return an object of this model
        return cls(object_snapshot_info,
                   total_count)


