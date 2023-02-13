# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.backup_run
import cohesity_management_sdk.models.copy_run
import cohesity_management_sdk.models.universal_id
import cohesity_management_sdk.models.protection_source
import cohesity_management_sdk.models.source_special_parameter

class ProtectedSourceSummary(object):

    """Implementation of the 'ProtectedSourceSummary' model.

    ProtectedSourceSummary is the summary of all the Protection Runs for the
    Protection Jobs using the Specified Protection Policy. This is only
    populated for a policy of type kRPO.

    Attributes:
        backup_run (BackupRun): Specifies details about the Backup task for a
            Job Run. A Backup task captures the original backup snapshots for
            each Protection Source in the Job.
        copy_runs (list of CopyRun): Specifies details about the Copy tasks of
            the Job Run. A Copy task copies the captured snapshots to an
            external target or a Remote Cohesity Cluster.
        is_paused (bool): Specifies the status of the backup job.
        next_protection_run_time_usecs (long|int): Specifies the time at which
            the next Protection Run is scheduled for the given Protection
            Source in Unix epoch Time (microseconds).
        protected_source_uid (UniversalId): Specifies an id for an object that
            is unique across Cohesity Clusters. The id is composite of all the
            ids listed below.
        protection_source (ProtectionSource): Specifies a generic structure
            that represents a node in the Protection Source tree. Node details
            will depend on the environment of the Protection Source.
        source_parameters (list of SourceSpecialParameter): Specifies
            additional special settings for a single Protected Source.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "backup_run":'backupRun',
        "copy_runs":'copyRuns',
        "is_paused":'isPaused',
        "next_protection_run_time_usecs":'nextProtectionRunTimeUsecs',
        "protected_source_uid":'protectedSourceUid',
        "protection_source":'protectionSource',
        "source_parameters":'sourceParameters'
    }

    def __init__(self,
                 backup_run=None,
                 copy_runs=None,
                 is_paused=None,
                 next_protection_run_time_usecs=None,
                 protected_source_uid=None,
                 protection_source=None,
                 source_parameters=None):
        """Constructor for the ProtectedSourceSummary class"""

        # Initialize members of the class
        self.backup_run = backup_run
        self.copy_runs = copy_runs
        self.is_paused = is_paused
        self.next_protection_run_time_usecs = next_protection_run_time_usecs
        self.protected_source_uid = protected_source_uid
        self.protection_source = protection_source
        self.source_parameters = source_parameters


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
        is_paused = dictionary.get('isPaused')
        next_protection_run_time_usecs = dictionary.get('nextProtectionRunTimeUsecs')
        protected_source_uid = cohesity_management_sdk.models.universal_id.UniversalId.from_dictionary(dictionary.get('protectedSourceUid')) if dictionary.get('protectedSourceUid') else None
        protection_source = cohesity_management_sdk.models.protection_source.ProtectionSource.from_dictionary(dictionary.get('protectionSource')) if dictionary.get('protectionSource') else None
        source_parameters = None
        if dictionary.get('sourceParameters') != None:
            source_parameters = list()
            for structure in dictionary.get('sourceParameters'):
                source_parameters.append(cohesity_management_sdk.models.source_special_parameter.SourceSpecialParameter.from_dictionary(structure))

        # Return an object of this model
        return cls(backup_run,
                   copy_runs,
                   is_paused,
                   next_protection_run_time_usecs,
                   protected_source_uid,
                   protection_source,
                   source_parameters)


