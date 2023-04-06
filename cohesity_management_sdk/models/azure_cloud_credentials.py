# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class AzureCloudCredentials(object):

    """Implementation of the 'AzureCloudCredentials' model.

    Specifies the cloud credentials to connect to a Microsoft Azure service
    account.


    Attributes:

        client_id (string): Specifies the client id of the managed identity
            assigned to the cluster. This is used only for clusters running as
            Azure VMs where authentication is done using AD.
        is_worm_enabled (bool): Specifies if write once read many (WORM)
            protection is enabled for the Azure container or not.
        storage_access_key (string): Specifies the access key to use when
            accessing a storage tier in a Azure cloud service.
        storage_account_name (string): Specifies the account name to use when
            accessing a storage tier in a Azure cloud service.
        tier_type (TierTypeAzureCloudCredentialsEnum): Specifies the storage
            class of Azure. AzureTierType specifies the storage class for
            Azure. 'kAzureTierHot' indicates a tier type of Azure properties
            that is accessed frequently. 'kAzureTierCool' indicates a tier type
            of Azure properties that is accessed less frequently, and stored
            for at least 30 days. 'kAzureTierArchive' indicates a tier type of
            Azure properties that is accessed rarely and stored for at least
            180 days.
        tiers (list of string): Specifies the list of all tiers for Amazon
            account.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "client_id":'clientId',
        "is_worm_enabled":'isWormEnabled',
        "storage_access_key":'storageAccessKey',
        "storage_account_name":'storageAccountName',
        "tier_type":'tierType',
        "tiers":'tiers',
    }
    def __init__(self,
                 client_id=None,
                 is_worm_enabled=None,
                 storage_access_key=None,
                 storage_account_name=None,
                 tier_type=None,
                 tiers=None,
            ):

        """Constructor for the AzureCloudCredentials class"""

        # Initialize members of the class
        self.client_id = client_id
        self.is_worm_enabled = is_worm_enabled
        self.storage_access_key = storage_access_key
        self.storage_account_name = storage_account_name
        self.tier_type = tier_type
        self.tiers = tiers

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
        client_id = dictionary.get('clientId')
        is_worm_enabled = dictionary.get('isWormEnabled')
        storage_access_key = dictionary.get('storageAccessKey')
        storage_account_name = dictionary.get('storageAccountName')
        tier_type = dictionary.get('tierType')
        tiers = dictionary.get("tiers")

        # Return an object of this model
        return cls(
            client_id,
            is_worm_enabled,
            storage_access_key,
            storage_account_name,
            tier_type,
            tiers
)