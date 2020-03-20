# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.


class AzureCloudCredentials(object):

    """Implementation of the 'AzureCloudCredentials' model.

    Specifies the cloud credentials to connect to a Microsoft
    Azure service account.

    Attributes:
        storage_access_key (string): Specifies the access key to use when
            accessing a storage tier in a Azure cloud service.
        storage_account_name (string): Specifies the account name to use when
            accessing a storage tier in a Azure cloud service.
        tier_type (TierTypeAzureCloudCredentialsEnum): Specifies the storage
            class of Azure. AzureTierType specifies the storage class for
            Azure. 'kAzureTierHot' indicates a tier type of Azure properties
            that is accessed frequently. 'kAzureTierCool' indicates a tier
            type of Azure properties that is accessed less frequently, and
            stored for at least 30 days. 'kAzureTierArchive' indicates a tier
            type of Azure properties that is accessed rarely and stored for at
            least 180 days.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "storage_access_key":'storageAccessKey',
        "storage_account_name":'storageAccountName',
        "tier_type":'tierType'
    }

    def __init__(self,
                 storage_access_key=None,
                 storage_account_name=None,
                 tier_type=None):
        """Constructor for the AzureCloudCredentials class"""

        # Initialize members of the class
        self.storage_access_key = storage_access_key
        self.storage_account_name = storage_account_name
        self.tier_type = tier_type


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
        storage_access_key = dictionary.get('storageAccessKey')
        storage_account_name = dictionary.get('storageAccountName')
        tier_type = dictionary.get('tierType')

        # Return an object of this model
        return cls(storage_access_key,
                   storage_account_name,
                   tier_type)


