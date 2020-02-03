# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.restore_oracle_app_object_params_alternate_location_params
import cohesity_management_sdk.models.clone_app_view_params
import cohesity_management_sdk.models.oracle_source_params

class RestoreOracleAppObjectParams(object):

    """Implementation of the 'RestoreOracleAppObjectParams' model.

    TODO: type model description here.

    Attributes:
        alternate_location_params
            (RestoreOracleAppObjectParamsAlternateLocationParams): For
            restoring to alternate location this message can not be empty and
            all the fields inside the message also can not be empty.
        no_open_mode (bool): If set to true, the recovered database will not
            be opened.
        oracle_clone_app_view_params_vec (list of CloneAppViewParams):
            Following field contains information related to view expose
            workflow. Ex mountpoint identifier specified by User from UI.
        oracle_target_params (OracleSourceParams): Message to capture
            additional backup/restore params for a Oracle source.
        parallel_op_enabled (bool): If set to true, parallel
            backups/restores/clones are enabled on same host.
        restore_time_secs (long|int): The time to which the Oracle database
            needs to be restored. This allows for granular recovery of Oracle
            databases. If this is not set, the Oracle database will be
            recovered to the full/incremental snapshot (specified in the
            owner's restore object in AppOwnerRestoreInfo). This is only
            applicable if restoring to the original Oracle instance.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "alternate_location_params":'alternateLocationParams',
        "no_open_mode":'noOpenMode',
        "oracle_clone_app_view_params_vec":'oracleCloneAppViewParamsVec',
        "oracle_target_params":'oracleTargetParams',
        "parallel_op_enabled":'parallelOpEnabled',
        "restore_time_secs":'restoreTimeSecs'
    }

    def __init__(self,
                 alternate_location_params=None,
                 no_open_mode=None,
                 oracle_clone_app_view_params_vec=None,
                 oracle_target_params=None,
                 parallel_op_enabled=None,
                 restore_time_secs=None):
        """Constructor for the RestoreOracleAppObjectParams class"""

        # Initialize members of the class
        self.alternate_location_params = alternate_location_params
        self.no_open_mode = no_open_mode
        self.oracle_clone_app_view_params_vec = oracle_clone_app_view_params_vec
        self.oracle_target_params = oracle_target_params
        self.parallel_op_enabled = parallel_op_enabled
        self.restore_time_secs = restore_time_secs


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
        no_open_mode = dictionary.get('noOpenMode')
        oracle_clone_app_view_params_vec = None
        if dictionary.get('oracleCloneAppViewParamsVec') != None:
            oracle_clone_app_view_params_vec = list()
            for structure in dictionary.get('oracleCloneAppViewParamsVec'):
                oracle_clone_app_view_params_vec.append(cohesity_management_sdk.models.clone_app_view_params.CloneAppViewParams.from_dictionary(structure))
        oracle_target_params = cohesity_management_sdk.models.oracle_source_params.OracleSourceParams.from_dictionary(dictionary.get('oracleTargetParams')) if dictionary.get('oracleTargetParams') else None
        parallel_op_enabled = dictionary.get('parallelOpEnabled')
        restore_time_secs = dictionary.get('restoreTimeSecs')

        # Return an object of this model
        return cls(alternate_location_params,
                   no_open_mode,
                   oracle_clone_app_view_params_vec,
                   oracle_target_params,
                   parallel_op_enabled,
                   restore_time_secs)


