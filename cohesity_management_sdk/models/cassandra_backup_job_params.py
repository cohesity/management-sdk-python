# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.cassandra_additional_params


class CassandraBackupJobParams(object):

    """Implementation of the 'CassandraBackupJobParams' model.

    Contains any additional cassandra environment specific backup params at the
    job level.


    Attributes:

        cassandra_additional_info (CassandraAdditionalParams): Additional
            parameters required for Cassandra backup.
        graph_handling_enabled (bool): whether special graph handling is
            enabled
        is_only_log_backup_job (bool): If this backup job is only responsible
            for the log backups. Presently this is used for cassandra log
            backups.
        retention_period_in_secs (long|int): Retention period in seconds. This
            is read from the policy currently attached to the protection job.
            This field is used only in case of log backups and ignored for
            other backups.
        selected_data_center_vec (list of string): The data centers selected
            for backup.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "cassandra_additional_info":'cassandraAdditionalInfo',
        "graph_handling_enabled":'graphHandlingEnabled',
        "is_only_log_backup_job":'isOnlyLogBackupJob',
        "retention_period_in_secs":'retentionPeriodInSecs',
        "selected_data_center_vec":'selectedDataCenterVec',
    }
    def __init__(self,
                 cassandra_additional_info=None,
                 graph_handling_enabled=None,
                 is_only_log_backup_job=None,
                 retention_period_in_secs=None,
                 selected_data_center_vec=None,
            ):

        """Constructor for the CassandraBackupJobParams class"""

        # Initialize members of the class
        self.cassandra_additional_info = cassandra_additional_info
        self.graph_handling_enabled = graph_handling_enabled
        self.is_only_log_backup_job = is_only_log_backup_job
        self.retention_period_in_secs = retention_period_in_secs
        self.selected_data_center_vec = selected_data_center_vec

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
        cassandra_additional_info = cohesity_management_sdk.models.cassandra_additional_params.CassandraAdditionalParams.from_dictionary(dictionary.get('cassandraAdditionalInfo')) if dictionary.get('cassandraAdditionalInfo') else None
        graph_handling_enabled = dictionary.get('graphHandlingEnabled')
        is_only_log_backup_job = dictionary.get('isOnlyLogBackupJob')
        retention_period_in_secs = dictionary.get('retentionPeriodInSecs')
        selected_data_center_vec = dictionary.get("selectedDataCenterVec")

        # Return an object of this model
        return cls(
            cassandra_additional_info,
            graph_handling_enabled,
            is_only_log_backup_job,
            retention_period_in_secs,
            selected_data_center_vec
)