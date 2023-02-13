# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ProtectionRunsStats(object):

    """Implementation of the 'ProtectionRunsStats' model.

    Specifies the Protection Runs statistics response.

    Attributes:
        num_archival_runs (long|int): Specifies the count of archival Runs.
        num_backup_runs (long|int): Specifies the count of backup Runs.
        num_replication_runs (long|int): Specifies the count of replication
            Runs.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "num_archival_runs":'numArchivalRuns',
        "num_backup_runs":'numBackupRuns',
        "num_replication_runs":'numReplicationRuns'
    }

    def __init__(self,
                 num_archival_runs=None,
                 num_backup_runs=None,
                 num_replication_runs=None):
        """Constructor for the ProtectionRunsStats class"""

        # Initialize members of the class
        self.num_archival_runs = num_archival_runs
        self.num_backup_runs = num_backup_runs
        self.num_replication_runs = num_replication_runs


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
        num_archival_runs = dictionary.get('numArchivalRuns')
        num_backup_runs = dictionary.get('numBackupRuns')
        num_replication_runs = dictionary.get('numReplicationRuns')

        # Return an object of this model
        return cls(num_archival_runs,
                   num_backup_runs,
                   num_replication_runs)


