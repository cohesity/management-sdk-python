# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.entity_proto


class RestoreExchangeParams_DatabaseOptions(object):

    """Implementation of the 'RestoreExchangeParams_DatabaseOptions' model.

    TODO: type description here.


    Attributes:

        dest_db_name (string): Destination Database Name
        dest_edb_filepath (string): Target EDB dir path. Example:
            e:\myexchange\hrdb\hr_db.edb.
        dest_log_dirpath (string): Target LOG dir path. Example:
            e:\myexchange\hrdb.
        entity_id (long|int): The windows machine to which the database will be
            restored. This field is deprecated.
        mount_db (bool): Mount the Database after successful recovery. For
            alternate location recovery this will result in Information Store
            Service restart on the target Exchange Node.
        progress_monitor_path (string): Progress monitor task path for this
            entity.
        restore_as_recovery_db (bool): Restore this DB as a Recovery Database
            on the target Exchange Node.
        target_host_entity (EntityProto): The entity proto for Exchange host to
            which the database will be restored.
        use_latest_logs (bool): When replaying the logs, use the latest logs on
            Exchange for this DB. Applicable for restoring to original location
            only.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "dest_db_name":'destDbName',
        "dest_edb_filepath":'destEdbFilepath',
        "dest_log_dirpath":'destLogDirpath',
        "entity_id":'entityId',
        "mount_db":'mountDb',
        "progress_monitor_path":'progressMonitorPath',
        "restore_as_recovery_db":'restoreAsRecoveryDb',
        "target_host_entity":'targetHostEntity',
        "use_latest_logs":'useLatestLogs',
    }
    def __init__(self,
                 dest_db_name=None,
                 dest_edb_filepath=None,
                 dest_log_dirpath=None,
                 entity_id=None,
                 mount_db=None,
                 progress_monitor_path=None,
                 restore_as_recovery_db=None,
                 target_host_entity=None,
                 use_latest_logs=None,
            ):

        """Constructor for the RestoreExchangeParams_DatabaseOptions class"""

        # Initialize members of the class
        self.dest_db_name = dest_db_name
        self.dest_edb_filepath = dest_edb_filepath
        self.dest_log_dirpath = dest_log_dirpath
        self.entity_id = entity_id
        self.mount_db = mount_db
        self.progress_monitor_path = progress_monitor_path
        self.restore_as_recovery_db = restore_as_recovery_db
        self.target_host_entity = target_host_entity
        self.use_latest_logs = use_latest_logs

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
        dest_db_name = dictionary.get('destDbName')
        dest_edb_filepath = dictionary.get('destEdbFilepath')
        dest_log_dirpath = dictionary.get('destLogDirpath')
        entity_id = dictionary.get('entityId')
        mount_db = dictionary.get('mountDb')
        progress_monitor_path = dictionary.get('progressMonitorPath')
        restore_as_recovery_db = dictionary.get('restoreAsRecoveryDb')
        target_host_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('targetHostEntity')) if dictionary.get('targetHostEntity') else None
        use_latest_logs = dictionary.get('useLatestLogs')

        # Return an object of this model
        return cls(
            dest_db_name,
            dest_edb_filepath,
            dest_log_dirpath,
            entity_id,
            mount_db,
            progress_monitor_path,
            restore_as_recovery_db,
            target_host_entity,
            use_latest_logs
)