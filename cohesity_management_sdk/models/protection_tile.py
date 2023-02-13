# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.protection_stats

class ProtectionTile(object):

    """Implementation of the 'ProtectionTile' model.

    Protection information and statistics.

    Attributes:
        last_day_archival (ProtectionStats): Protection Statistics.
        last_day_backup (ProtectionStats): Protection Statistics.
        last_day_replication_in (ProtectionStats): Protection Statistics.
        last_day_replication_out (ProtectionStats): Protection Statistics.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "last_day_archival":'lastDayArchival',
        "last_day_backup":'lastDayBackup',
        "last_day_replication_in":'lastDayReplicationIn',
        "last_day_replication_out":'lastDayReplicationOut'
    }

    def __init__(self,
                 last_day_archival=None,
                 last_day_backup=None,
                 last_day_replication_in=None,
                 last_day_replication_out=None):
        """Constructor for the ProtectionTile class"""

        # Initialize members of the class
        self.last_day_archival = last_day_archival
        self.last_day_backup = last_day_backup
        self.last_day_replication_in = last_day_replication_in
        self.last_day_replication_out = last_day_replication_out


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
        last_day_archival = cohesity_management_sdk.models.protection_stats.ProtectionStats.from_dictionary(dictionary.get('lastDayArchival')) if dictionary.get('lastDayArchival') else None
        last_day_backup = cohesity_management_sdk.models.protection_stats.ProtectionStats.from_dictionary(dictionary.get('lastDayBackup')) if dictionary.get('lastDayBackup') else None
        last_day_replication_in = cohesity_management_sdk.models.protection_stats.ProtectionStats.from_dictionary(dictionary.get('lastDayReplicationIn')) if dictionary.get('lastDayReplicationIn') else None
        last_day_replication_out = cohesity_management_sdk.models.protection_stats.ProtectionStats.from_dictionary(dictionary.get('lastDayReplicationOut')) if dictionary.get('lastDayReplicationOut') else None

        # Return an object of this model
        return cls(last_day_archival,
                   last_day_backup,
                   last_day_replication_in,
                   last_day_replication_out)


