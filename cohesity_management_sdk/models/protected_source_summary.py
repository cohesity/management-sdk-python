# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.backup_run_task
import cohesity_management_sdk.models.copy_run_task
import cohesity_management_sdk.models.unique_global_id
import cohesity_management_sdk.models.protection_source

class ProtectedSourceSummary(object):

    """Implementation of the 'ProtectedSourceSummary' model.

    ProtectedSourceSummary is the summary of all the Protection Runs for the
    Protection Jobs using the Specified Protection Policy. This is only
    populated for a policy of type kRPO.

    Attributes:
        backup_run (BackupRunTask): Specifies details about the Backup task
            for a Job Run. A Backup task captures the original backup
            snapshots for each Protection Source in the Job.
        copy_runs (list of CopyRunTask): Specifies details about the Copy
            tasks of the Job Run. A Copy task copies the captured snapshots to
            an external target or a Remote Cohesity Cluster.
        job_uid (UniqueGlobalId): Specifies an id for an object that is unique
            across Cohesity Clusters. The id is composite of all the ids
            listed below.
        next_protection_run_time_usecs (long|int): Specifies the time at which
            the next Protection Run is scheduled for the given Protection
            Source in Unix epoch Time (microseconds).
        protection_source (ProtectionSource): Specifies a generic structure
            that represents a node in the Protection Source tree. Node details
            will depend on the environment of the Protection Source.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "backup_run":'backupRun',
        "copy_runs":'copyRuns',
        "job_uid":'jobUid',
        "next_protection_run_time_usecs":'nextProtectionRunTimeUsecs',
        "protection_source":'protectionSource'
    }

    def __init__(self,
                 backup_run=None,
                 copy_runs=None,
                 job_uid=None,
                 next_protection_run_time_usecs=None,
                 protection_source=None):
        """Constructor for the ProtectedSourceSummary class"""

        # Initialize members of the class
        self.backup_run = backup_run
        self.copy_runs = copy_runs
        self.job_uid = job_uid
        self.next_protection_run_time_usecs = next_protection_run_time_usecs
        self.protection_source = protection_source


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
        backup_run = cohesity_management_sdk.models.backup_run_task.BackupRunTask.from_dictionary(dictionary.get('backupRun')) if dictionary.get('backupRun') else None
        copy_runs = None
        if dictionary.get('copyRuns') != None:
            copy_runs = list()
            for structure in dictionary.get('copyRuns'):
                copy_runs.append(cohesity_management_sdk.models.copy_run_task.CopyRunTask.from_dictionary(structure))
        job_uid = cohesity_management_sdk.models.unique_global_id.UniqueGlobalId.from_dictionary(dictionary.get('jobUid')) if dictionary.get('jobUid') else None
        next_protection_run_time_usecs = dictionary.get('nextProtectionRunTimeUsecs')
        protection_source = cohesity_management_sdk.models.protection_source.ProtectionSource.from_dictionary(dictionary.get('protectionSource')) if dictionary.get('protectionSource') else None

        # Return an object of this model
        return cls(backup_run,
                   copy_runs,
                   job_uid,
                   next_protection_run_time_usecs,
                   protection_source)


