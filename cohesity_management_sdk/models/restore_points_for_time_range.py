# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.full_snapshot_info
import cohesity_management_sdk.models.time_range_settings

class RestorePointsForTimeRange(object):

    """Implementation of the 'RestorePointsForTimeRange' model.

    Specifies the info returned by Magneto RestorePointsForTimeRange API.

    Attributes:
        full_snapshot_info (list of FullSnapshotInfo): Specifies the info
            related to the recovery object.
        time_ranges (list of TimeRangeSettings): Specifies the time ranges of
            the restore object between full snapshots.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "full_snapshot_info":'fullSnapshotInfo',
        "time_ranges":'timeRanges'
    }

    def __init__(self,
                 full_snapshot_info=None,
                 time_ranges=None):
        """Constructor for the RestorePointsForTimeRange class"""

        # Initialize members of the class
        self.full_snapshot_info = full_snapshot_info
        self.time_ranges = time_ranges


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
        full_snapshot_info = None
        if dictionary.get('fullSnapshotInfo') != None:
            full_snapshot_info = list()
            for structure in dictionary.get('fullSnapshotInfo'):
                full_snapshot_info.append(cohesity_management_sdk.models.full_snapshot_info.FullSnapshotInfo.from_dictionary(structure))
        time_ranges = None
        if dictionary.get('timeRanges') != None:
            time_ranges = list()
            for structure in dictionary.get('timeRanges'):
                time_ranges.append(cohesity_management_sdk.models.time_range_settings.TimeRangeSettings.from_dictionary(structure))

        # Return an object of this model
        return cls(full_snapshot_info,
                   time_ranges)


