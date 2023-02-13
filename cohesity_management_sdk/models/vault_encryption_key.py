# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.universal_id

class VaultEncryptionKey(object):

    """Implementation of the 'VaultEncryptionKey' model.

    Specifies the encrytion information needed to restore data.

    Attributes:
        cluster_name (string): Specifies the name of the source Cohesity
            Cluster that archived the data on the Vault.
        encryption_key_data (string): Specifies the encryption key data
            corresponding to the specified keyUid. It contains a Key
            Encryption Key (KEK) or a Encrypted Data Encryption Key (eDEK).
        key_uid (UniversalId): Specifies the universal id of the Data
            Encryption Key.
        vault_id (long|int): Specifies the id of the Vault whose data is
            encrypted by this key.
        vault_name (string): Specifies the name of the Vault whose data is
            encrypted by this key.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cluster_name":'clusterName',
        "encryption_key_data":'encryptionKeyData',
        "key_uid":'keyUid',
        "vault_id":'vaultId',
        "vault_name":'vaultName'
    }

    def __init__(self,
                 cluster_name=None,
                 encryption_key_data=None,
                 key_uid=None,
                 vault_id=None,
                 vault_name=None):
        """Constructor for the VaultEncryptionKey class"""

        # Initialize members of the class
        self.cluster_name = cluster_name
        self.encryption_key_data = encryption_key_data
        self.key_uid = key_uid
        self.vault_id = vault_id
        self.vault_name = vault_name


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
        cluster_name = dictionary.get('clusterName')
        encryption_key_data = dictionary.get('encryptionKeyData')
        key_uid = cohesity_management_sdk.models.universal_id.UniversalId.from_dictionary(dictionary.get('keyUid')) if dictionary.get('keyUid') else None
        vault_id = dictionary.get('vaultId')
        vault_name = dictionary.get('vaultName')

        # Return an object of this model
        return cls(cluster_name,
                   encryption_key_data,
                   key_uid,
                   vault_id,
                   vault_name)


