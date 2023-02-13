# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class OracleCloudCredentials(object):

    """Implementation of the 'OracleCloudCredentials' model.

    Specifies the Oracle Cloud Credentials to connect to an Oracle S3
    Compatible
    vault account.
    Oracle Cloud Credentials Region, Access-Key-Id and Secret-Access-Key.
    Oracle Cloud properties Tenant and Tier Type.

    Attributes:
        access_key_id (string): Specifies access key to connect to Oracle S3
            Compatible vault account.
        region (string): Specifies the region for Oracle S3 Compatible vault
            account.
        secret_access_key (string): Specifies the secret access key for Oracle
            S3 Compatible vault account.
        tenant (string): Specifies the tenant which is part of the REST
            endpoints for Oracle S3 compatible vaults.
        tier_type (TierTypeOracleCloudCredentialsEnum): Specifies the storage
            class of Oracle vault. OracleTierType specifies the storage class
            for Oracle. 'kOracleTierStandard' indicates a tier type of Oracle
            properties that requires fast, immediate and frequent access.
            'kOracleTierArchive' indicates a tier type of Oracle properties
            that is rarely accesed and preserved for long times.
        tiers (list of string): Specifies the list of all tiers for Amazon
            account.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "access_key_id":'accessKeyId',
        "region":'region',
        "secret_access_key":'secretAccessKey',
        "tenant":'tenant',
        "tier_type":'tierType',
        "tiers":'tiers'
    }

    def __init__(self,
                 access_key_id=None,
                 region=None,
                 secret_access_key=None,
                 tenant=None,
                 tier_type=None,
                 tiers=None):
        """Constructor for the OracleCloudCredentials class"""

        # Initialize members of the class
        self.access_key_id = access_key_id
        self.region = region
        self.secret_access_key = secret_access_key
        self.tenant = tenant
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
        access_key_id = dictionary.get('accessKeyId')
        region = dictionary.get('region')
        secret_access_key = dictionary.get('secretAccessKey')
        tenant = dictionary.get('tenant')
        tier_type = dictionary.get('tierType')
        tiers = dictionary.get('tiers')

        # Return an object of this model
        return cls(access_key_id,
                   region,
                   secret_access_key,
                   tenant,
                   tier_type,
                   tiers)


