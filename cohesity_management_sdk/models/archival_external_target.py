# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ArchivalExternalTarget(object):

    """Implementation of the 'ArchivalExternalTarget' model.

    Specifies settings about the Archival External Target (such as Tape or
    AWS).

    Attributes:
        vault_id (long|int): Specifies the id of Archival Vault assigned by
            the Cohesity Cluster.
        vault_name (string): Name of the Archival Vault.
        vault_type (VaultTypeEnum): Specifies the type of the Archival
            External Target such as 'kCloud', 'kTape' or 'kNas'. 'kCloud'
            indicates the archival location as Cloud. 'kTape' indicates the
            archival location as Tape. 'kNas' indicates the archival location
            as Network Attached Storage (Nas).

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "vault_id":'vaultId',
        "vault_name":'vaultName',
        "vault_type":'vaultType'
    }

    def __init__(self,
                 vault_id=None,
                 vault_name=None,
                 vault_type=None):
        """Constructor for the ArchivalExternalTarget class"""

        # Initialize members of the class
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
        vault_id = dictionary.get('vaultId')
        vault_name = dictionary.get('vaultName')
        vault_type = dictionary.get('vaultType')

        # Return an object of this model
        return cls(vault_id,
                   vault_name,
                   vault_type)


