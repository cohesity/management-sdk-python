# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class CloudArchivalInfo(object):

    """Implementation of the 'CloudArchivalInfo' model.

    Specifies the cloud archival for active and finished tasks.

    Attributes:
        is_active_task (bool): Specifies if the task if active or finished.
        public_status (PublicStatusCloudArchivalInfoEnum): Specifies the
            public status type.
        status (StatusCloudArchivalInfoEnum): Specifies the status type.
        vault_id (long|int): Specifies the id of Archival Vault assigned by
            the Cohesity Cluster.
        vault_name (string): Name of the Archival Vault.
        vault_type (VaultTypeEnum): Specifies the type of the Archival
            External Target such as 'kCloud', 'kTape' or 'kNas'.
            'kCloud' indicates the archival location as Cloud.
            'kTape' indicates the archival location as Tape.
            'kNas' indicates the archival location as Network Attached Storage
            (Nas).

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "is_active_task": 'isActiveTask',
        "public_status": 'publicStatus',
        "status": 'status',
        "vault_id":'vaultId',
        "vault_name":'vaultName',
        "vault_type":'vaultType'
    }

    def __init__(self,
                 is_active_task=None,
                 public_status=None,
                 status=None,
                 vault_id=None,
                 vault_name=None,
                 vault_type=None):
        """Constructor for the CloudArchivalInfo class"""

        # Initialize members of the class
        self.is_active_task = is_active_task
        self.public_status = public_status
        self.status = status
        self.vault_id = vault_id
        self.vault_name = vault_name
        self.vault_type = vault_type

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
        is_active_task = dictionary.get('isActiveTask')
        public_status = dictionary.get('publicStatus')
        status = dictionary.get('status')
        vault_id = dictionary.get('vaultId')
        vault_name = dictionary.get('vaultName')
        vault_type = dictionary.get('vaultType')

        # Return an object of this model
        return cls(is_active_task,
                   public_status,
                   status,
                   vault_id,
                   vault_name,
                   vault_type)


