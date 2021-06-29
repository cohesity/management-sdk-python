# -*- coding: utf-8 -*-
# Copyright 2021 Cohesity Inc.

import cohesity_management_sdk.models.vlan_params

class OracleBackupJobParams(object):

    """Implementation of the 'OracleBackupJobParams' model.

    Message to capture any additional backup params specific to Oracle.

    Attributes:
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
        "persist_mountpoints": 'persistMountpoints',
        "vlan_params": "vlanParams"
    }

    def __init__(self,
                 persist_mountpoints=None,
                 vlan_params=None):
        """Constructor for the OracleBackupJobParams class"""

        # Initialize members of the class
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
        persist_mountpoints = dictionary.get('persistMountpoints')
        vlan_params = cohesity_management_sdk.models.vlan_params.VlanParams.from_dictionary(dictionary.get('vlanParams')) if dictionary.get('vlanParams') else None

        # Return an object of this model
        return cls(persist_mountpoints,
                   vlan_params)


