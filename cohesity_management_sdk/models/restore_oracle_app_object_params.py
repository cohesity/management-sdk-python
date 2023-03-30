# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.clone_app_view_params
import cohesity_management_sdk.models.granular_restore_info
import cohesity_management_sdk.models.oracle_archive_log_info
import cohesity_management_sdk.models.oracle_recovery_validation_info
import cohesity_management_sdk.models.oracle_source_params
import cohesity_management_sdk.models.oracle_update_restore_task_options
import cohesity_management_sdk.models.restore_oracle_app_object_params_alternate_location_params
import cohesity_management_sdk.models.restore_oracle_app_object_params_key_value_pair
import cohesity_management_sdk.models.restore_spfile_or_pfile_info


class RestoreOracleAppObjectParams(object):

    """Implementation of the 'RestoreOracleAppObjectParams' model.

    TODO: type description here.


    Attributes:

        alternate_location_params
            (RestoreOracleAppObjectParams_AlternateLocationParams): TODO: Type
            description here.
        attempt_complete_recovery (bool): Whether or not this is a complete
            recovery attempt.
        granular_restore_info (GranularRestoreInfo): Contains information about
            list of objects (PDB/Table/DataFile) to restore.
        is_multi_stage_restore (bool): Will be set to true if this is a
            multistage restore.
        no_open_mode (bool): If set to true, the recovered database will not be
            opened.
        oracle_archive_log_restore_info (OracleArchiveLogInfo): Contains
            information related to archive log restore.
        oracle_clone_app_view_params_vec (list of CloneAppViewParams):
            Following field contains information related to view expose
            workflow. Ex mountpoint identifier specified by User from UI.
        oracle_recovery_validation_info (OracleRecoveryValidationInfo):
            Contains information related to recovery validations.
        oracle_target_params (OracleSourceParams): Contains information
            regarding oracle sources, channel information and host nomination
            details.
        oracle_update_restore_options (OracleUpdateRestoreTaskOptions):
            Contains parameter information about any update task which needed
            to be performed on a sucessful restore/clone task. Ex Instant
            restore of Clone.
        parallel_op_enabled (bool): If set to true, parallel
            backups/restores/clones are enabled on same host.
        restore_spfile_or_pfile_info (RestoreSpfileOrPfileInfo): Contains
            information related spfile/pfile restore.
        restore_time_secs (long|int): The time to which the Oracle database
            needs to be restored. This allows for granular recovery of Oracle
            databases. If this is not set, the Oracle database will be
            recovered to the full/incremental snapshot (specified in the
            owner's restore object in AppOwnerRestoreInfo). This is only
            applicable if restoring to the original Oracle instance.
        roll_forward_log_path_vec (list of string): List of archive logs to
            apply on Database after overwrite restore.
        roll_forward_time_msecs (long|int): Time till which we have to
            roll-forward the database. This overrides user mentioned point in
            time(if any).
        shell_environment_vec (list of
            RestoreOracleAppObjectParams_KeyValuePair): TODO: Type description
            here.
        skip_clone_nid (bool): Whether or not to skip the nid step in Oracle
            Clone workflow. Applicable to both smart and old clone workflow.
        use_scn_for_restore (bool): Whether database recovery should be
            performed using the SCN value or time value. Currently this is
            applicable only during overwrite restore and clone workflow. In
            case of alternate restore we cannot use it since we cannot set
            until scn clause if we don't catalog the backup view.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "alternate_location_params":'alternateLocationParams',
        "attempt_complete_recovery":'attemptCompleteRecovery',
        "granular_restore_info":'granularRestoreInfo',
        "is_multi_stage_restore":'isMultiStageRestore',
        "no_open_mode":'noOpenMode',
        "oracle_archive_log_restore_info":'oracleArchiveLogRestoreInfo',
        "oracle_clone_app_view_params_vec":'oracleCloneAppViewParamsVec',
        "oracle_recovery_validation_info":'oracleRecoveryValidationInfo',
        "oracle_target_params":'oracleTargetParams',
        "oracle_update_restore_options":'oracleUpdateRestoreOptions',
        "parallel_op_enabled":'parallelOpEnabled',
        "restore_spfile_or_pfile_info":'restoreSpfileOrPfileInfo',
        "restore_time_secs":'restoreTimeSecs',
        "roll_forward_log_path_vec":'rollForwardLogPathVec',
        "roll_forward_time_msecs":'rollForwardTimeMsecs',
        "shell_environment_vec":'shellEnvironmentVec',
        "skip_clone_nid":'skipCloneNid',
        "use_scn_for_restore":'useScnForRestore',
    }
    def __init__(self,
                 alternate_location_params=None,
                 attempt_complete_recovery=None,
                 granular_restore_info=None,
                 is_multi_stage_restore=None,
                 no_open_mode=None,
                 oracle_archive_log_restore_info=None,
                 oracle_clone_app_view_params_vec=None,
                 oracle_recovery_validation_info=None,
                 oracle_target_params=None,
                 oracle_update_restore_options=None,
                 parallel_op_enabled=None,
                 restore_spfile_or_pfile_info=None,
                 restore_time_secs=None,
                 roll_forward_log_path_vec=None,
                 roll_forward_time_msecs=None,
                 shell_environment_vec=None,
                 skip_clone_nid=None,
                 use_scn_for_restore=None,
            ):

        """Constructor for the RestoreOracleAppObjectParams class"""

        # Initialize members of the class
        self.alternate_location_params = alternate_location_params
        self.attempt_complete_recovery = attempt_complete_recovery
        self.granular_restore_info = granular_restore_info
        self.is_multi_stage_restore = is_multi_stage_restore
        self.no_open_mode = no_open_mode
        self.oracle_archive_log_restore_info = oracle_archive_log_restore_info
        self.oracle_clone_app_view_params_vec = oracle_clone_app_view_params_vec
        self.oracle_recovery_validation_info = oracle_recovery_validation_info
        self.oracle_target_params = oracle_target_params
        self.oracle_update_restore_options = oracle_update_restore_options
        self.parallel_op_enabled = parallel_op_enabled
        self.restore_spfile_or_pfile_info = restore_spfile_or_pfile_info
        self.restore_time_secs = restore_time_secs
        self.roll_forward_log_path_vec = roll_forward_log_path_vec
        self.roll_forward_time_msecs = roll_forward_time_msecs
        self.shell_environment_vec = shell_environment_vec
        self.skip_clone_nid = skip_clone_nid
        self.use_scn_for_restore = use_scn_for_restore

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
        alternate_location_params = cohesity_management_sdk.models.restore_oracle_app_object_params_alternate_location_params.RestoreOracleAppObjectParams_AlternateLocationParams.from_dictionary(dictionary.get('alternateLocationParams')) if dictionary.get('alternateLocationParams') else None
        attempt_complete_recovery = dictionary.get('attemptCompleteRecovery')
        granular_restore_info = cohesity_management_sdk.models.granular_restore_info.GranularRestoreInfo.from_dictionary(dictionary.get('granularRestoreInfo')) if dictionary.get('granularRestoreInfo') else None
        is_multi_stage_restore = dictionary.get('isMultiStageRestore')
        no_open_mode = dictionary.get('noOpenMode')
        oracle_archive_log_restore_info = cohesity_management_sdk.models.oracle_archive_log_info.OracleArchiveLogInfo.from_dictionary(dictionary.get('oracleArchiveLogRestoreInfo')) if dictionary.get('oracleArchiveLogRestoreInfo') else None
        oracle_clone_app_view_params_vec = None
        if dictionary.get('oracleCloneAppViewParamsVec') != None:
            oracle_clone_app_view_params_vec = list()
            for structure in dictionary.get('oracleCloneAppViewParamsVec'):
                oracle_clone_app_view_params_vec.append(cohesity_management_sdk.models.clone_app_view_params.CloneAppViewParams.from_dictionary(structure))
        oracle_recovery_validation_info = cohesity_management_sdk.models.oracle_recovery_validation_info.OracleRecoveryValidationInfo.from_dictionary(dictionary.get('oracleRecoveryValidationInfo')) if dictionary.get('oracleRecoveryValidationInfo') else None
        oracle_target_params = cohesity_management_sdk.models.oracle_source_params.OracleSourceParams.from_dictionary(dictionary.get('oracleTargetParams')) if dictionary.get('oracleTargetParams') else None
        oracle_update_restore_options = cohesity_management_sdk.models.oracle_update_restore_task_options.OracleUpdateRestoreTaskOptions.from_dictionary(dictionary.get('oracleUpdateRestoreOptions')) if dictionary.get('oracleUpdateRestoreOptions') else None
        parallel_op_enabled = dictionary.get('parallelOpEnabled')
        restore_spfile_or_pfile_info = cohesity_management_sdk.models.restore_spfile_or_pfile_info.RestoreSpfileOrPfileInfo.from_dictionary(dictionary.get('restoreSpfileOrPfileInfo')) if dictionary.get('restoreSpfileOrPfileInfo') else None
        restore_time_secs = dictionary.get('restoreTimeSecs')
        roll_forward_log_path_vec = dictionary.get("rollForwardLogPathVec")
        roll_forward_time_msecs = dictionary.get('rollForwardTimeMsecs')
        shell_environment_vec = None
        if dictionary.get('shellEnvironmentVec') != None:
            shell_environment_vec = list()
            for structure in dictionary.get('shellEnvironmentVec'):
                shell_environment_vec.append(cohesity_management_sdk.models.restore_oracle_app_object_params_key_value_pair.RestoreOracleAppObjectParams_KeyValuePair.from_dictionary(structure))
        skip_clone_nid = dictionary.get('skipCloneNid')
        use_scn_for_restore = dictionary.get('useScnForRestore')

        # Return an object of this model
        return cls(
            alternate_location_params,
            attempt_complete_recovery,
            granular_restore_info,
            is_multi_stage_restore,
            no_open_mode,
            oracle_archive_log_restore_info,
            oracle_clone_app_view_params_vec,
            oracle_recovery_validation_info,
            oracle_target_params,
            oracle_update_restore_options,
            parallel_op_enabled,
            restore_spfile_or_pfile_info,
            restore_time_secs,
            roll_forward_log_path_vec,
            roll_forward_time_msecs,
            shell_environment_vec,
            skip_clone_nid,
            use_scn_for_restore
)