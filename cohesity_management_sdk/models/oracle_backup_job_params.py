# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.vlan_params

class OracleBackupJobParams(object):

    """Implementation of the 'OracleBackupJobParams' model.

    Message to capture any additional backup params specific to Oracle.

    Attributes:
    full_auto_kill_timeout_secs (long|int): Time in seconds after which the
        full backup of the database in given backup job should be auto-killed.
        If set to -1, then the backup will run until completion.
    incr_auto_kill_timeout_secs (long|int): Time in seconds after which the
        incremental backup of the database in given backup job should be
        auto-killed.
        If set to -1, then the backup will run until completion.
    log_auto_kill_timeout_secs (long|int): Time in seconds after which the
        log backup of the database in given backup job should be auto-killed.
        If set to -1, then the backup will run until completion.
    persist_mountpoints (bool): Indicates whether the mountpoints created
        while backing up Oracle DBs should be persisted. If this is set to
        'false' all Oracle views mounted to the hosts will be unmounted at the
        end.
        Note: This parameter is for the entire Job. For overriding persistence of
        mountpoints for a subset of Oracle hosts within the job,
        refer OracleSourceParams.
    vlan_params (VlanParams): Contains vlan params associated with the
        backup/restore operation.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "full_auto_kill_timeout_secs":'fullAutoKillTimeoutSecs',
        "incr_auto_kill_timeout_secs":'incrAutoKillTimeoutSecs',
        "log_auto_kill_timeout_secs":'logAutoKillTimeoutSecs',
        "persist_mountpoints": 'persistMountpoints',
        "vlan_params": "vlanParams"
    }

    def __init__(self,
                 full_auto_kill_timeout_secs=None,
                 incr_auto_kill_timeout_secs=None,
                 log_auto_kill_timeout_secs=None,
                 persist_mountpoints=None,
                 vlan_params=None):
        """Constructor for the OracleBackupJobParams class"""

        # Initialize members of the class
        self.full_auto_kill_timeout_secs = full_auto_kill_timeout_secs
        self.incr_auto_kill_timeout_secs   = incr_auto_kill_timeout_secs
        self.log_auto_kill_timeout_secs = log_auto_kill_timeout_secs
        self.persist_mountpoints = persist_mountpoints
        self.vlan_params = vlan_params


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
        full_auto_kill_timeout_secs = dictionary.get('fullAutoKillTimeoutSecs')
        incr_auto_kill_timeout_secs = dictionary.get('incrAutoKillTimeoutSecs')
        log_auto_kill_timeout_secs = dictionary.get('logAutoKillTimeoutSecs')
        persist_mountpoints = dictionary.get('persistMountpoints')
        vlan_params = cohesity_management_sdk.models.vlan_params.VlanParams.from_dictionary(dictionary.get('vlanParams')) if dictionary.get('vlanParams') else None

        # Return an object of this model
        return cls(full_auto_kill_timeout_secs,
                   incr_auto_kill_timeout_secs,
                   log_auto_kill_timeout_secs,
                   persist_mountpoints,
                   vlan_params)


