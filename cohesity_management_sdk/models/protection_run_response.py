# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.latest_protection_job_run_info

class ProtectionRunResponse(object):

    """Implementation of the 'ProtectionRunResponse' model.

    Specifies the information about the Protection Runs across all snapshot
    target locations.

    Attributes:
        archival_runs (list of LatestProtectionJobRunInfo): Specifies the list
            of archival job information.
        backup_runs (list of LatestProtectionJobRunInfo): Specifies the list
            of local backup job information.
        replication_runs (list of LatestProtectionJobRunInfo): Specifies the
            list of replication job information.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "archival_runs":'archivalRuns',
        "backup_runs":'backupRuns',
        "replication_runs":'replicationRuns'
    }

    def __init__(self,
                 archival_runs=None,
                 backup_runs=None,
                 replication_runs=None):
        """Constructor for the ProtectionRunResponse class"""

        # Initialize members of the class
        self.archival_runs = archival_runs
        self.backup_runs = backup_runs
        self.replication_runs = replication_runs


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
        archival_runs = None
        if dictionary.get('archivalRuns') != None:
            archival_runs = list()
            for structure in dictionary.get('archivalRuns'):
                archival_runs.append(cohesity_management_sdk.models.latest_protection_job_run_info.LatestProtectionJobRunInfo.from_dictionary(structure))
        backup_runs = None
        if dictionary.get('backupRuns') != None:
            backup_runs = list()
            for structure in dictionary.get('backupRuns'):
                backup_runs.append(cohesity_management_sdk.models.latest_protection_job_run_info.LatestProtectionJobRunInfo.from_dictionary(structure))
        replication_runs = None
        if dictionary.get('replicationRuns') != None:
            replication_runs = list()
            for structure in dictionary.get('replicationRuns'):
                replication_runs.append(cohesity_management_sdk.models.latest_protection_job_run_info.LatestProtectionJobRunInfo.from_dictionary(structure))

        # Return an object of this model
        return cls(archival_runs,
                   backup_runs,
                   replication_runs)


