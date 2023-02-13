# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.restore_oracle_app_object_params_alternate_location_params
import cohesity_management_sdk.models.clone_app_view_params
import cohesity_management_sdk.models.granular_restore_info
import cohesity_management_sdk.models.oracle_source_params
import cohesity_management_sdk.models.oracle_update_restore_task_options
import cohesity_management_sdk.models.restore_oracle_app_object_params_key_value_pair

class RestoreOracleAppObjectParams(object):

    """Implementation of the 'RestoreOracleAppObjectParams' model.

    TODO: type model description here.

    Attributes:
        alternate_location_params
            (RestoreOracleAppObjectParamsAlternateLocationParams): For
            restoring to alternate location this message can not be empty and
            all the fields inside the message also can not be empty.
        granular_restore_info (GranularRestoreInfo): Contains information
            about list of objects (PDB/Table/DataFile) to restore.
        is_multi_stage_restore (bool): Will be set to true if this is a
            multistage restore.
        no_open_mode (bool): If set to true, the recovered database will not
            be opened.
        oracle_clone_app_view_params_vec (list of CloneAppViewParams):
            Following field contains information related to view expose
            workflow. Ex mountpoint identifier specified by User from UI.
        oracle_target_params (OracleSourceParams): Message to capture
            additional backup/restore params for a Oracle source.
        oracle_update_restore_options (OracleUpdateRestoreTaskOptions): Contains
            parameter information about any update task which needed to be
            performed on a sucessful restore/clone task. Ex Instant restore of
            Clone.

        parallel_op_enabled (bool): If set to true, parallel
            backups/restores/clones are enabled on same host.
        restore_time_secs (long|int): The time to which the Oracle database
            needs to be restored. This allows for granular recovery of Oracle
            databases. If this is not set, the Oracle database will be
            recovered to the full/incremental snapshot (specified in the
            owner's restore object in AppOwnerRestoreInfo). This is only
            applicable if restoring to the original Oracle instance.
        shell_environment_vec (list of
            RestoreOracleAppObjectParams_KeyValuePair): TODO: Type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "alternate_location_params":'alternateLocationParams',
        "granular_restore_info":'granularRestoreInfo',
        "is_multi_stage_restore":'isMultiStageRestore',
        "no_open_mode":'noOpenMode',
        "oracle_clone_app_view_params_vec":'oracleCloneAppViewParamsVec',
        "oracle_target_params":'oracleTargetParams',
        "oracle_update_restore_options":'oracleUpdateRestoreOptions',
        "parallel_op_enabled":'parallelOpEnabled',
        "restore_time_secs":'restoreTimeSecs',
        "shell_environment_vec":'shellEnvironmentVec'
    }

    def __init__(self,
                 alternate_location_params=None,
                 granular_restore_info=None,
                 is_multi_stage_restore=None,
                 no_open_mode=None,
                 oracle_clone_app_view_params_vec=None,
                 oracle_target_params=None,
                 oracle_update_restore_options=None,
                 parallel_op_enabled=None,
                 restore_time_secs=None,
                 shell_environment_vec=None):
        """Constructor for the RestoreOracleAppObjectParams class"""

        # Initialize members of the class
        self.alternate_location_params = alternate_location_params
        self.granular_restore_info = granular_restore_info
        self.is_multi_stage_restore = is_multi_stage_restore
        self.no_open_mode = no_open_mode
        self.oracle_clone_app_view_params_vec = oracle_clone_app_view_params_vec
        self.oracle_target_params = oracle_target_params
        self.oracle_update_restore_options = oracle_update_restore_options
        self.parallel_op_enabled = parallel_op_enabled
        self.restore_time_secs = restore_time_secs
        self.shell_environment_vec = shell_environment_vec


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
        alternate_location_params = cohesity_management_sdk.models.restore_oracle_app_object_params_alternate_location_params.RestoreOracleAppObjectParamsAlternateLocationParams.from_dictionary(dictionary.get('alternateLocationParams')) if dictionary.get('alternateLocationParams') else None
        granular_restore_info = cohesity_management_sdk.models.granular_restore_info.GranularRestoreInfo.from_dictionary(dictionary.get('granularRestoreInfo')) if dictionary.get('granularRestoreInfo') else None
        is_multi_stage_restore = dictionary.get('isMultiStageRestore')
        no_open_mode = dictionary.get('noOpenMode')
        oracle_clone_app_view_params_vec = None
        if dictionary.get('oracleCloneAppViewParamsVec') != None:
            oracle_clone_app_view_params_vec = list()
            for structure in dictionary.get('oracleCloneAppViewParamsVec'):
                oracle_clone_app_view_params_vec.append(cohesity_management_sdk.models.clone_app_view_params.CloneAppViewParams.from_dictionary(structure))
        oracle_target_params = cohesity_management_sdk.models.oracle_source_params.OracleSourceParams.from_dictionary(dictionary.get('oracleTargetParams')) if dictionary.get('oracleTargetParams') else None
        oracle_update_restore_options = cohesity_management_sdk.models.oracle_update_restore_task_options.OracleUpdateRestoreTaskOptions.from_dictionary(dictionary.get('oracleUpdateRestoreOptions')) if dictionary.get('oracleUpdateRestoreOptions') else None
        parallel_op_enabled = dictionary.get('parallelOpEnabled')
        restore_time_secs = dictionary.get('restoreTimeSecs')
        shell_environment_vec = None
        if dictionary.get('shellEnvironmentVec') != None:
            shell_environment_vec = list()
            for structure in dictionary.get('shellEnvironmentVec'):
                shell_environment_vec.append(cohesity_management_sdk.models.restore_oracle_app_object_params_key_value_pair.RestoreOracleAppObjectParams_KeyValuePair.from_dictionary(structure))

        # Return an object of this model
        return cls(alternate_location_params,
                   granular_restore_info,
                   is_multi_stage_restore,
                   no_open_mode,
                   oracle_clone_app_view_params_vec,
                   oracle_target_params,
                   oracle_update_restore_options,
                   parallel_op_enabled,
                   restore_time_secs,
                   shell_environment_vec)


