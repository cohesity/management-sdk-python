# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.run_job_snapshot_target
import cohesity_management_sdk.models.universal_id

class UpdateProtectionJobRun(object):

    """Implementation of the 'UpdateProtectionJobRun' model.

    Specifies a Job Run and the expiration time to update. The expiration
    time defines the retention period for the Job Run and its snapshots.

    Attributes:
        copy_run_targets (list of RunJobSnapshotTarget): Specifies the
            retention for archival, replication or extended local retention.
        job_uid (UniversalId): Specifies a unique universal id for the Job.
        run_start_time_usecs (long|int): Specifies the start time of the Job
            Run to update. The start time is specified as a Unix epoch
            Timestamp (in microseconds). This uniquely identifies a snapshot.
            This parameter is required.
        source_ids (list of long|int): Ids of the Protection Sources. If this
            is specified, retention time will only be updated for the sources
            specified.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "copy_run_targets":'copyRunTargets',
        "job_uid":'jobUid',
        "run_start_time_usecs":'runStartTimeUsecs',
        "source_ids":'sourceIds'
    }

    def __init__(self,
                 copy_run_targets=None,
                 job_uid=None,
                 run_start_time_usecs=None,
                 source_ids=None):
        """Constructor for the UpdateProtectionJobRun class"""

        # Initialize members of the class
        self.copy_run_targets = copy_run_targets
        self.job_uid = job_uid
        self.run_start_time_usecs = run_start_time_usecs
        self.source_ids = source_ids


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
        copy_run_targets = None
        if dictionary.get('copyRunTargets') != None:
            copy_run_targets = list()
            for structure in dictionary.get('copyRunTargets'):
                copy_run_targets.append(cohesity_management_sdk.models.run_job_snapshot_target.RunJobSnapshotTarget.from_dictionary(structure))
        job_uid = cohesity_management_sdk.models.universal_id.UniversalId.from_dictionary(dictionary.get('jobUid')) if dictionary.get('jobUid') else None
        run_start_time_usecs = dictionary.get('runStartTimeUsecs')
        source_ids = dictionary.get('sourceIds')

        # Return an object of this model
        return cls(copy_run_targets,
                   job_uid,
                   run_start_time_usecs,
                   source_ids)


