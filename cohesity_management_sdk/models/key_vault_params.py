# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.azure_kms_credentials


class KeyVaultParams(object):

    """Implementation of the 'KeyVaultParams' model.

    TODO: type description here.


    Attributes:

        azure_credentials (AzureKmsCredentials): Specifies the Azure
            credentials.
        customer_secret_name (string): Specifies the name of client secret
            stored in cohesity keyvault. This is used only for customer managed
            keys.
        key_name (string): Specifies the Key name used to encrypt and decrypt
            DEK.
        keyvault_url (string): Specifies the URL of the Azure key vault.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "azure_credentials":'azureCredentials',
        "customer_secret_name":'customerSecretName',
        "key_name":'keyName',
        "keyvault_url":'keyvaultUrl',
    }
    def __init__(self,
                 azure_credentials=None,
                 customer_secret_name=None,
                 key_name=None,
                 keyvault_url=None,
            ):

        """Constructor for the KeyVaultParams class"""

        # Initialize members of the class
        self.azure_credentials = azure_credentials
        self.customer_secret_name = customer_secret_name
        self.key_name = key_name
        self.keyvault_url = keyvault_url

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
        azure_credentials = cohesity_management_sdk.models.azure_kms_credentials.AzureKmsCredentials.from_dictionary(dictionary.get('azureCredentials')) if dictionary.get('azureCredentials') else None
        customer_secret_name = dictionary.get('customerSecretName')
        key_name = dictionary.get('keyName')
        keyvault_url = dictionary.get('keyvaultUrl')

        # Return an object of this model
        return cls(
            azure_credentials,
            customer_secret_name,
            key_name,
            keyvault_url
)