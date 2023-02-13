# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.latest_protection_run

class LatestProtectionJobRunInfo(object):

    """Implementation of the 'LatestProtectionJobRunInfo' model.

    Specifies the information about the Protection Runs per snapshot target.

    Attributes:
        latest_snapshot_info (LatestProtectionRun): Specifies the information
            about the latest Protection Run.
        location_name (string): Specifies the name of location that the object
            is backedup to.
        num_snapshots (long|int): Specifies of number of successful
            snapshots.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "latest_snapshot_info":'latestSnapshotInfo',
        "location_name":'locationName',
        "num_snapshots":'numSnapshots'
    }

    def __init__(self,
                 latest_snapshot_info=None,
                 location_name=None,
                 num_snapshots=None):
        """Constructor for the LatestProtectionJobRunInfo class"""

        # Initialize members of the class
        self.latest_snapshot_info = latest_snapshot_info
        self.location_name = location_name
        self.num_snapshots = num_snapshots


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
        latest_snapshot_info = cohesity_management_sdk.models.latest_protection_run.LatestProtectionRun.from_dictionary(dictionary.get('latestSnapshotInfo')) if dictionary.get('latestSnapshotInfo') else None
        location_name = dictionary.get('locationName')
        num_snapshots = dictionary.get('numSnapshots')

        # Return an object of this model
        return cls(latest_snapshot_info,
                   location_name,
                   num_snapshots)


