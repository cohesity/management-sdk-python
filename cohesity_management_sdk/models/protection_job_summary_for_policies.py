# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.backup_run
import cohesity_management_sdk.models.copy_run
import cohesity_management_sdk.models.protection_job

class ProtectionJobSummaryForPolicies(object):

    """Implementation of the 'ProtectionJobSummaryForPolicies' model.

    ProtectionJobSummaryForPolicies is the summary of a Protection
    Jobs associated with the Specified Protection Policy. This is only
    populated for a policy of type kRegular.

    Attributes:
        backup_run (BackupRun): Specifies details about the Backup task for a
            Job Run. A Backup task captures the original backup snapshots for
            each Protection Source in the Job.
        copy_runs (list of CopyRun): Specifies details about the Copy tasks of
            the Job Run. A Copy task copies the captured snapshots to an
            external target or a Remote Cohesity Cluster.
        protection_job (ProtectionJob): Specifies the Protection job
            information.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "backup_run":'backupRun',
        "copy_runs":'copyRuns',
        "protection_job":'protectionJob'
    }

    def __init__(self,
                 backup_run=None,
                 copy_runs=None,
                 protection_job=None):
        """Constructor for the ProtectionJobSummaryForPolicies class"""

        # Initialize members of the class
        self.backup_run = backup_run
        self.copy_runs = copy_runs
        self.protection_job = protection_job


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
        backup_run = cohesity_management_sdk.models.backup_run.BackupRun.from_dictionary(dictionary.get('backupRun')) if dictionary.get('backupRun') else None
        copy_runs = None
        if dictionary.get('copyRuns') != None:
            copy_runs = list()
            for structure in dictionary.get('copyRuns'):
                copy_runs.append(cohesity_management_sdk.models.copy_run.CopyRun.from_dictionary(structure))
        protection_job = cohesity_management_sdk.models.protection_job.ProtectionJob.from_dictionary(dictionary.get('protectionJob')) if dictionary.get('protectionJob') else None

        # Return an object of this model
        return cls(backup_run,
                   copy_runs,
                   protection_job)


