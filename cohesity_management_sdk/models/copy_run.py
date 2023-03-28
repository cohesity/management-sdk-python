# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.copy_run_stats
import cohesity_management_sdk.models.copy_snapshot_task_status
import cohesity_management_sdk.models.data_lock_constraints
import cohesity_management_sdk.models.legal_holdings
import cohesity_management_sdk.models.snapshot_target_settings
import cohesity_management_sdk.models.universal_id


class CopyRun(object):

    """Implementation of the 'CopyRun' model.

    Specifies details about the Copy Run for a backup run of a Job Run. A Copy
    task copies snapshots resulted from a backup run to a snapshot target which
    could be 'kLocal', 'kArchival', or 'kRemote'.


    Attributes:

        copy_snapshot_tasks (list of CopySnapshotTaskStatus): Specifies the
            status information of each task that copies the snapshot taken for
            a Protection Source.
        data_lock_constraints (DataLockConstraints): Specifies the datalock
            constraints for a copy run task.
        error (string): Specifies if an error occurred (if any) while running
            this task. This field is populated when the status is equal to
            'kFailure'.
        expiry_time_usecs (long|int): Specifies expiry time of the copies of
            the snapshots in this Protection Run.
        hold_for_legal_purpose (bool): Specifies whether legal hold is enabled
            on this run. It is true if the run is put on legal hold.
            Independent of this flag, some of the entities may be on legal
            hold.
        legal_holdings (list of LegalHoldings): Specifies the list of
            Protection Source Ids and the legal hold status.
        run_start_time_usecs (long|int): Specifies start time of the copy run.
        stats (CopyRunStats): Specifies the aggregated information of all the
            copy tasks.
        status (StatusCopyRunEnum): Specifies the aggregated status of copy
            tasks such as 'kRunning', 'kSuccess', 'kFailure' etc. 'kAccepted'
            indicates the task is queued to run but not yet running. 'kRunning'
            indicates the task is running. 'kCanceling' indicates a request to
            cancel the task has occurred but the task is not yet canceled.
            'kCanceled' indicates the task has been canceled. 'kSuccess'
            indicates the task was successful. 'kFailure' indicates the task
            failed. 'kWarning' indicates the task has finished with warning.
            'kOnHold' indicates the task is kept onHold. 'kMissed' indicates
            the task is missed. 'Finalizing' indicates the task is finalizing.
        target (SnapshotTargetSettings): Specifies the target of the copy task
            such as an external target or a Remote Cohesity Cluster.
        task_uid (UniversalId): Specifies a globally unique id of the copy
            task.
        user_action_message (string): Specifies a message to the user if any
            manual intervention is needed to make forward progress for the
            archival task. This message is mainly relevant for tape based
            archival tasks where a backup admin might be asked to load a new
            media when the tape library does not have any more media to use.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "copy_snapshot_tasks":'copySnapshotTasks',
        "data_lock_constraints":'dataLockConstraints',
        "error":'error',
        "expiry_time_usecs":'expiryTimeUsecs',
        "hold_for_legal_purpose":'holdForLegalPurpose',
        "legal_holdings":'legalHoldings',
        "run_start_time_usecs":'runStartTimeUsecs',
        "stats":'stats',
        "status":'status',
        "target":'target',
        "task_uid":'taskUid',
        "user_action_message":'userActionMessage',
    }
    def __init__(self,
                 copy_snapshot_tasks=None,
                 data_lock_constraints=None,
                 error=None,
                 expiry_time_usecs=None,
                 hold_for_legal_purpose=None,
                 legal_holdings=None,
                 run_start_time_usecs=None,
                 stats=None,
                 status=None,
                 target=None,
                 task_uid=None,
                 user_action_message=None,
            ):

        """Constructor for the CopyRun class"""

        # Initialize members of the class
        self.copy_snapshot_tasks = copy_snapshot_tasks
        self.data_lock_constraints = data_lock_constraints
        self.error = error
        self.expiry_time_usecs = expiry_time_usecs
        self.hold_for_legal_purpose = hold_for_legal_purpose
        self.legal_holdings = legal_holdings
        self.run_start_time_usecs = run_start_time_usecs
        self.stats = stats
        self.status = status
        self.target = target
        self.task_uid = task_uid
        self.user_action_message = user_action_message

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
        copy_snapshot_tasks = None
        if dictionary.get('copySnapshotTasks') != None:
            copy_snapshot_tasks = list()
            for structure in dictionary.get('copySnapshotTasks'):
                copy_snapshot_tasks.append(cohesity_management_sdk.models.copy_snapshot_task_status.CopySnapshotTaskStatus.from_dictionary(structure))
        data_lock_constraints = cohesity_management_sdk.models.data_lock_constraints.DataLockConstraints.from_dictionary(dictionary.get('dataLockConstraints')) if dictionary.get('dataLockConstraints') else None
        error = dictionary.get('error')
        expiry_time_usecs = dictionary.get('expiryTimeUsecs')
        hold_for_legal_purpose = dictionary.get('holdForLegalPurpose')
        legal_holdings = None
        if dictionary.get('legalHoldings') != None:
            legal_holdings = list()
            for structure in dictionary.get('legalHoldings'):
                legal_holdings.append(cohesity_management_sdk.models.legal_holdings.LegalHoldings.from_dictionary(structure))
        run_start_time_usecs = dictionary.get('runStartTimeUsecs')
        stats = cohesity_management_sdk.models.copy_run_stats.CopyRunStats.from_dictionary(dictionary.get('stats')) if dictionary.get('stats') else None
        status = dictionary.get('status')
        target = cohesity_management_sdk.models.snapshot_target_settings.SnapshotTargetSettings.from_dictionary(dictionary.get('target')) if dictionary.get('target') else None
        task_uid = cohesity_management_sdk.models.universal_id.UniversalId.from_dictionary(dictionary.get('taskUid')) if dictionary.get('taskUid') else None
        user_action_message = dictionary.get('userActionMessage')

        # Return an object of this model
        return cls(
            copy_snapshot_tasks,
            data_lock_constraints,
            error,
            expiry_time_usecs,
            hold_for_legal_purpose,
            legal_holdings,
            run_start_time_usecs,
            stats,
            status,
            target,
            task_uid,
            user_action_message
)