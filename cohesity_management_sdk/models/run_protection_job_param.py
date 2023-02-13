# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.run_job_snapshot_target
import cohesity_management_sdk.models.run_now_parameters

class RunProtectionJobParam(object):

    """Implementation of the 'RunProtectionJobParam' model.

    Specify the parameters to run a protection job.

    Attributes:
        copy_run_targets (list of RunJobSnapshotTarget): Optional parameter to
            be set if you want specific replication or archival associated
            with the policy to run.
        run_now_parameters (list of RunNowParameters): Optional parameters of
            a Run Now operation.
        run_type (RunTypeRunProtectionJobParamEnum): Specifies the type of
            backup. If not specified, 'kRegular' is assumed. 'kRegular'
            indicates a incremental (CBT) backup. Incremental backups
            utilizing CBT (if supported) are captured of the target protection
            objects. The first run of a kRegular schedule captures all the
            blocks. 'kFull' indicates a full (no CBT) backup. A complete
            backup (all blocks) of the target protection objects are always
            captured and Change Block Tracking (CBT) is not utilized. 'kLog'
            indicates a Database Log backup. Capture the database transaction
            logs to allow rolling back to a specific point in time. 'kSystem'
            indicates a system backup. System backups are used to do bare
            metal recovery of the system to a specific point in time.
        source_ids (list of long|int): Optional parameter if you want to back
            up only a subset of sources that are protected by the job in this
            run. If a Run Now operation is to be performed then the source ids
            should only be provided in the runNowParameters along with the
            database Ids.
        use_policy_defaults (bool): Specifies if default policy settings should
            be used interanally to copy snapshots to external targets already
            configured in policy. This field will only apply if "CopyRunTargets"
            is empty.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "copy_run_targets":'copyRunTargets',
        "run_now_parameters":'runNowParameters',
        "run_type":'runType',
        "source_ids":'sourceIds',
        "use_policy_defaults":'usePolicyDefaults'
    }

    def __init__(self,
                 copy_run_targets=None,
                 run_now_parameters=None,
                 run_type=None,
                 source_ids=None,
                 use_policy_defaults=None):
        """Constructor for the RunProtectionJobParam class"""

        # Initialize members of the class
        self.copy_run_targets = copy_run_targets
        self.run_now_parameters = run_now_parameters
        self.run_type = run_type
        self.source_ids = source_ids
        self.use_policy_defaults = use_policy_defaults


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
        run_now_parameters = None
        if dictionary.get('runNowParameters') != None:
            run_now_parameters = list()
            for structure in dictionary.get('runNowParameters'):
                run_now_parameters.append(cohesity_management_sdk.models.run_now_parameters.RunNowParameters.from_dictionary(structure))
        run_type = dictionary.get('runType')
        source_ids = dictionary.get('sourceIds')
        use_policy_defaults = dictionary.get('usePolicyDefaults')

        # Return an object of this model
        return cls(copy_run_targets,
                   run_now_parameters,
                   run_type,
                   source_ids,
                   use_policy_defaults)


