# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.sql_update_restore_task_options
import cohesity_management_sdk.models.files_to_directory_mapping

class RestoreSqlAppObjectParams(object):

    """Implementation of the 'RestoreSqlAppObjectParams' model.

    TODO: type model description here.

    Attributes:
        capture_tail_logs (bool): Set to true if tail logs are to be captured
            before the restore operation. This is only applicable if we are
            restoring the SQL database to its original source, and the
            database is not being renamed.
        data_file_destination (string): Which directory to put the database
            data files. Missing directory will be automatically created.
            Cannot be empty if not restoring to the original SQL instance.
        db_restore_overwrite_policy (int): Policy to overwrite an existing DB
            during a restore operation.
        instance_name (string): The name of the SQL instance that we restore
            database to. If target_host is not empty, this also cannot be
            empty.
        is_multi_stage_restore (bool): The following field is set if we are
            creating a multi-stage SQL restore task needed for features such
            as Hot-Standby.
        log_file_destination (string): Which directory to put the database log
            files. Missing directory will be automatically created. Cannot be
            empty if not restoring to the original SQL instance.
        multi_stage_restore_options (SqlUpdateRestoreTaskOptions): TODO: type
            description here.
        new_database_name (string): The new name of the database, if it is
            going to be renamed. app_entity in RestoreAppObject has to be
            non-empty for the renaming, otherwise it does not make sense to
            rename all databases in the owner.
        restore_time_secs (long|int): The time to which the SQL database needs
            to be restored. This allows for granular recovery of SQL
            databases. If this is not set, the SQL database will be recovered
            to the full/incremental snapshot (specified in the owner's restore
            object in AppOwnerRestoreInfo). This is only applicable if
            restoring to the original SQL instance.
        secondary_data_file_destination (string): Which directory to put the
            secondary data files of the database. Secondary data files are
            optional and are user defined. The recommended file name extension
            for these is ".ndf".  If this option is specified, the directory
            will be automatically created if its missing.
        secondary_data_file_destination_vec (list of FilesToDirectoryMapping):
            Specify the secondary data files and corresponding direcories of
            the DB. Secondary data files are optional and are user defined.
            The recommended file extension for secondary files is ".ndf".  If
            this option is specified and the destination folders do not exist
            they will be automatically created.
        with_no_recovery (bool): Set to true if we want to recover the
            database in "NO_RECOVERY" mode which does not bring it online
            after restore.  Note: This is only applicable if we are restoring
            the database back to its original location.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "capture_tail_logs":'captureTailLogs',
        "data_file_destination":'dataFileDestination',
        "db_restore_overwrite_policy":'dbRestoreOverwritePolicy',
        "instance_name":'instanceName',
        "is_multi_stage_restore":'isMultiStageRestore',
        "log_file_destination":'logFileDestination',
        "multi_stage_restore_options":'multiStageRestoreOptions',
        "new_database_name":'newDatabaseName',
        "restore_time_secs":'restoreTimeSecs',
        "secondary_data_file_destination":'secondaryDataFileDestination',
        "secondary_data_file_destination_vec":'secondaryDataFileDestinationVec',
        "with_no_recovery":'withNoRecovery'
    }

    def __init__(self,
                 capture_tail_logs=None,
                 data_file_destination=None,
                 db_restore_overwrite_policy=None,
                 instance_name=None,
                 is_multi_stage_restore=None,
                 log_file_destination=None,
                 multi_stage_restore_options=None,
                 new_database_name=None,
                 restore_time_secs=None,
                 secondary_data_file_destination=None,
                 secondary_data_file_destination_vec=None,
                 with_no_recovery=None):
        """Constructor for the RestoreSqlAppObjectParams class"""

        # Initialize members of the class
        self.capture_tail_logs = capture_tail_logs
        self.data_file_destination = data_file_destination
        self.db_restore_overwrite_policy = db_restore_overwrite_policy
        self.instance_name = instance_name
        self.is_multi_stage_restore = is_multi_stage_restore
        self.log_file_destination = log_file_destination
        self.multi_stage_restore_options = multi_stage_restore_options
        self.new_database_name = new_database_name
        self.restore_time_secs = restore_time_secs
        self.secondary_data_file_destination = secondary_data_file_destination
        self.secondary_data_file_destination_vec = secondary_data_file_destination_vec
        self.with_no_recovery = with_no_recovery


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
        capture_tail_logs = dictionary.get('captureTailLogs')
        data_file_destination = dictionary.get('dataFileDestination')
        db_restore_overwrite_policy = dictionary.get('dbRestoreOverwritePolicy')
        instance_name = dictionary.get('instanceName')
        is_multi_stage_restore = dictionary.get('isMultiStageRestore')
        log_file_destination = dictionary.get('logFileDestination')
        multi_stage_restore_options = cohesity_management_sdk.models.sql_update_restore_task_options.SqlUpdateRestoreTaskOptions.from_dictionary(dictionary.get('multiStageRestoreOptions')) if dictionary.get('multiStageRestoreOptions') else None
        new_database_name = dictionary.get('newDatabaseName')
        restore_time_secs = dictionary.get('restoreTimeSecs')
        secondary_data_file_destination = dictionary.get('secondaryDataFileDestination')
        secondary_data_file_destination_vec = None
        if dictionary.get('secondaryDataFileDestinationVec') != None:
            secondary_data_file_destination_vec = list()
            for structure in dictionary.get('secondaryDataFileDestinationVec'):
                secondary_data_file_destination_vec.append(cohesity_management_sdk.models.files_to_directory_mapping.FilesToDirectoryMapping.from_dictionary(structure))
        with_no_recovery = dictionary.get('withNoRecovery')

        # Return an object of this model
        return cls(capture_tail_logs,
                   data_file_destination,
                   db_restore_overwrite_policy,
                   instance_name,
                   is_multi_stage_restore,
                   log_file_destination,
                   multi_stage_restore_options,
                   new_database_name,
                   restore_time_secs,
                   secondary_data_file_destination,
                   secondary_data_file_destination_vec,
                   with_no_recovery)


