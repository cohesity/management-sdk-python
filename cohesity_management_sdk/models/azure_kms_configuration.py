# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.key_vault_params


class AzureKmsConfiguration(object):

    """Implementation of the 'AzureKmsConfiguration' model.

    TODO: type description here.


    Attributes:

        cohesity_key_vault (KeyVaultParams): Specifies the cohesity managed key
            vault details.
        customer_key_vault (KeyVaultParams): Specifies the customer managed key
            vault details.
        vault_owner (VaultOwnerEnum): Specifies if its a cohesity managed or
            customer managed key vault. 'kCohesityManaged' indicates an
            internal KMS object. 'kCustomerManaged' indicates an Aws KMS
            object.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "cohesity_key_vault":'cohesityKeyVault',
        "customer_key_vault":'customerKeyVault',
        "vault_owner":'vaultOwner',
    }
    def __init__(self,
                 cohesity_key_vault=None,
                 customer_key_vault=None,
                 vault_owner=None,
            ):

        """Constructor for the AzureKmsConfiguration class"""

        # Initialize members of the class
        self.cohesity_key_vault = cohesity_key_vault
        self.customer_key_vault = customer_key_vault
        self.vault_owner = vault_owner

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
        cohesity_key_vault = cohesity_management_sdk.models.key_vault_params.KeyVaultParams.from_dictionary(dictionary.get('cohesityKeyVault')) if dictionary.get('cohesityKeyVault') else None
        customer_key_vault = cohesity_management_sdk.models.key_vault_params.KeyVaultParams.from_dictionary(dictionary.get('customerKeyVault')) if dictionary.get('customerKeyVault') else None
        vault_owner = dictionary.get('vaultOwner')

        # Return an object of this model
        return cls(
            cohesity_key_vault,
            customer_key_vault,
            vault_owner
)