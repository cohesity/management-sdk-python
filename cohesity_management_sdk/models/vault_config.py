# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.amazon_cloud_credentials
import cohesity_management_sdk.models.azure_cloud_credentials
import cohesity_management_sdk.models.google_cloud_credentials
import cohesity_management_sdk.models.nas_credentials
import cohesity_management_sdk.models.oracle_cloud_credentials
import cohesity_management_sdk.models.q_star_server_credentials

class VaultConfig(object):

    """Implementation of the 'VaultConfig' model.

    Specifies the settings required to connect to a specific Vault type.
    For some Vaults, you must also specify a storage location (bucketName).

    Attributes:
        amazon (AmazonCloudCredentials): Specifies the cloud credentials to
            connect to a Amazon service account. Glacier, S3, and
            S3-compatible clouds all use these credentials.
        azure (AzureCloudCredentials): Specifies the cloud credentials to
            connect to a Microsoft Azure service account.
        bucket_name (string): Specifies the name of a storage location of the
            Vault, where objects are stored. For Google and AMS, this storage
            location is called a bucket. For Microsoft Azure, this storage
            location is called a container. For QStar and NAS, you do not
            specify a storage location.
        google (GoogleCloudCredentials): Specifies the cloud credentials to
            connect to a Google service account.
        nas (NasCredentials): Specifies the server credentials to connect to a
            NetApp server.
        oracle (OracleCloudCredentials): Specifies the Oracle Cloud
            Credentials to connect to an Oracle S3 Compatible vault account.
            Oracle Cloud Credentials Region, Access-Key-Id and
            Secret-Access-Key. Oracle Cloud properties Tenant and Tier Type.
        qstar (QStarServerCredentials): Specifies the server credentials to
            connect to a QStar service to manage the media Vault.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amazon":'amazon',
        "azure":'azure',
        "bucket_name":'bucketName',
        "google":'google',
        "nas":'nas',
        "oracle":'oracle',
        "qstar":'qstar'
    }

    def __init__(self,
                 amazon=None,
                 azure=None,
                 bucket_name=None,
                 google=None,
                 nas=None,
                 oracle=None,
                 qstar=None):
        """Constructor for the VaultConfig class"""

        # Initialize members of the class
        self.amazon = amazon
        self.azure = azure
        self.bucket_name = bucket_name
        self.google = google
        self.nas = nas
        self.oracle = oracle
        self.qstar = qstar


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
        amazon = cohesity_management_sdk.models.amazon_cloud_credentials.AmazonCloudCredentials.from_dictionary(dictionary.get('amazon')) if dictionary.get('amazon') else None
        azure = cohesity_management_sdk.models.azure_cloud_credentials.AzureCloudCredentials.from_dictionary(dictionary.get('azure')) if dictionary.get('azure') else None
        bucket_name = dictionary.get('bucketName')
        google = cohesity_management_sdk.models.google_cloud_credentials.GoogleCloudCredentials.from_dictionary(dictionary.get('google')) if dictionary.get('google') else None
        nas = cohesity_management_sdk.models.nas_credentials.NasCredentials.from_dictionary(dictionary.get('nas')) if dictionary.get('nas') else None
        oracle = cohesity_management_sdk.models.oracle_cloud_credentials.OracleCloudCredentials.from_dictionary(dictionary.get('oracle')) if dictionary.get('oracle') else None
        qstar = cohesity_management_sdk.models.q_star_server_credentials.QStarServerCredentials.from_dictionary(dictionary.get('qstar')) if dictionary.get('qstar') else None

        # Return an object of this model
        return cls(amazon,
                   azure,
                   bucket_name,
                   google,
                   nas,
                   oracle,
                   qstar)


