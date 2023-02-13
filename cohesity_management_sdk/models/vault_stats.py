# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.vault_stats_info

class VaultStats(object):

    """Implementation of the 'VaultStats' model.

    Specifies the storage usage on vaults.

    Attributes:
        aws_usage_bytes (long|int): Specifies the usage on AWS vaults.
        azure_usage_bytes (long|int): Specifies the usage on Azure vaults.
        gcp_usage_bytes (long|int): Specifies the usage on GCP vaults.
        nas_usage_bytes (long|int): Specifies the usage on NAS vaults.
        oracle_usage_bytes (long|int): Specifies the usage on Oracle vaults.
        qstar_usage_bytes (long|int): Specifies the usage on QStar Tape
            vaults.
        s_3_c_usage_bytes (long|int): Specifies the usage on S3 Compatible
            vaults.
        vault_stats_list (list of VaultStatsInfo): Specifies the stats of all
            vaults on the cluster.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "aws_usage_bytes":'awsUsageBytes',
        "azure_usage_bytes":'azureUsageBytes',
        "gcp_usage_bytes":'gcpUsageBytes',
        "nas_usage_bytes":'nasUsageBytes',
        "oracle_usage_bytes":'oracleUsageBytes',
        "qstar_usage_bytes":'qstarUsageBytes',
        "s_3_c_usage_bytes":'s3cUsageBytes',
        "vault_stats_list":'vaultStatsList'
    }

    def __init__(self,
                 aws_usage_bytes=None,
                 azure_usage_bytes=None,
                 gcp_usage_bytes=None,
                 nas_usage_bytes=None,
                 oracle_usage_bytes=None,
                 qstar_usage_bytes=None,
                 s_3_c_usage_bytes=None,
                 vault_stats_list=None):
        """Constructor for the VaultStats class"""

        # Initialize members of the class
        self.aws_usage_bytes = aws_usage_bytes
        self.azure_usage_bytes = azure_usage_bytes
        self.gcp_usage_bytes = gcp_usage_bytes
        self.nas_usage_bytes = nas_usage_bytes
        self.oracle_usage_bytes = oracle_usage_bytes
        self.qstar_usage_bytes = qstar_usage_bytes
        self.s_3_c_usage_bytes = s_3_c_usage_bytes
        self.vault_stats_list = vault_stats_list


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
        aws_usage_bytes = dictionary.get('awsUsageBytes')
        azure_usage_bytes = dictionary.get('azureUsageBytes')
        gcp_usage_bytes = dictionary.get('gcpUsageBytes')
        nas_usage_bytes = dictionary.get('nasUsageBytes')
        oracle_usage_bytes = dictionary.get('oracleUsageBytes')
        qstar_usage_bytes = dictionary.get('qstarUsageBytes')
        s_3_c_usage_bytes = dictionary.get('s3cUsageBytes')
        vault_stats_list = None
        if dictionary.get('vaultStatsList') != None:
            vault_stats_list = list()
            for structure in dictionary.get('vaultStatsList'):
                vault_stats_list.append(cohesity_management_sdk.models.vault_stats_info.VaultStatsInfo.from_dictionary(structure))

        # Return an object of this model
        return cls(aws_usage_bytes,
                   azure_usage_bytes,
                   gcp_usage_bytes,
                   nas_usage_bytes,
                   oracle_usage_bytes,
                   qstar_usage_bytes,
                   s_3_c_usage_bytes,
                   vault_stats_list)


