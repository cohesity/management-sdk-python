# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.backup_policy_proto_exclusion_time_range

class BackupPolicyProtoContinuousSchedule(object):

    """Implementation of the 'BackupPolicyProto_ContinuousSchedule' model.

    TODO: type model description here.

    Attributes:
        backup_interval_mins (long|int): If this field is set, backups will be
            performed periodically every 'interval_mins' number of minutes.
            NOTE: This is the interval between the start time of two
            successive backups.
        exclusion_ranges (list of BackupPolicyProtoExclusionTimeRange): Do not
            start backups in these time-ranges. It's possible for a previously
            started backup to spill over into an exclusion range.  NOTE: This
            field has been deprecated. Use the exclusion_ranges field defined
            within BackupPolicyProto instead.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "backup_interval_mins":'backupIntervalMins',
        "exclusion_ranges":'exclusionRanges'
    }

    def __init__(self,
                 backup_interval_mins=None,
                 exclusion_ranges=None):
        """Constructor for the BackupPolicyProtoContinuousSchedule class"""

        # Initialize members of the class
        self.backup_interval_mins = backup_interval_mins
        self.exclusion_ranges = exclusion_ranges


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
        backup_interval_mins = dictionary.get('backupIntervalMins')
        exclusion_ranges = None
        if dictionary.get('exclusionRanges') != None:
            exclusion_ranges = list()
            for structure in dictionary.get('exclusionRanges'):
                exclusion_ranges.append(cohesity_management_sdk.models.backup_policy_proto_exclusion_time_range.BackupPolicyProtoExclusionTimeRange.from_dictionary(structure))

        # Return an object of this model
        return cls(backup_interval_mins,
                   exclusion_ranges)


