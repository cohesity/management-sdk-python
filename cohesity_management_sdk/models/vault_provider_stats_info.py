# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.vault_provider_stats_by_env

class VaultProviderStatsInfo(object):

    """Implementation of the 'VaultProviderStatsInfo' model.

    Specifies the stats for each vault.

    Attributes:
        change_rate (long|int): Specifies the relative change of size of
            entities on the vault.
        cluster_id (long|int): Specifies the cluster id.
        cluster_incarnation_id (long|int): Specifies the cluster incarnation
            id.
        cluster_name (string): Specifies the cluster name.
        read_bandwidth (long|int): Specifies the average read bandwidth over
            the last 24 hours.
        stats_by_env (list of VaultProviderStatsByEnv): Specifies the stats by
            environments.
        vault_group (VaultGroupEnum): Specifies the cloud vendor type.
        vault_id (long|int): Specifies the Vault id.
        vault_type (VaultTypeVaultProviderStatsInfoEnum): Specifies the
            External Target type.
        vaultname (string): Specifies the Vault name.
        write_bandwidth (long|int): Specifies the average write bandwidth over
            the last 24 hours.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "change_rate":'changeRate',
        "cluster_id":'clusterId',
        "cluster_incarnation_id":'clusterIncarnationId',
        "cluster_name":'clusterName',
        "read_bandwidth":'readBandwidth',
        "stats_by_env":'statsByEnv',
        "vault_group":'vaultGroup',
        "vault_id":'vaultId',
        "vault_type":'vaultType',
        "vaultname":'vaultname',
        "write_bandwidth":'writeBandwidth'
    }

    def __init__(self,
                 change_rate=None,
                 cluster_id=None,
                 cluster_incarnation_id=None,
                 cluster_name=None,
                 read_bandwidth=None,
                 stats_by_env=None,
                 vault_group=None,
                 vault_id=None,
                 vault_type=None,
                 vaultname=None,
                 write_bandwidth=None):
        """Constructor for the VaultProviderStatsInfo class"""

        # Initialize members of the class
        self.change_rate = change_rate
        self.cluster_id = cluster_id
        self.cluster_incarnation_id = cluster_incarnation_id
        self.cluster_name = cluster_name
        self.read_bandwidth = read_bandwidth
        self.stats_by_env = stats_by_env
        self.vault_group = vault_group
        self.vault_id = vault_id
        self.vault_type = vault_type
        self.vaultname = vaultname
        self.write_bandwidth = write_bandwidth


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
        change_rate = dictionary.get('changeRate')
        cluster_id = dictionary.get('clusterId')
        cluster_incarnation_id = dictionary.get('clusterIncarnationId')
        cluster_name = dictionary.get('clusterName')
        read_bandwidth = dictionary.get('readBandwidth')
        stats_by_env = None
        if dictionary.get('statsByEnv') != None:
            stats_by_env = list()
            for structure in dictionary.get('statsByEnv'):
                stats_by_env.append(cohesity_management_sdk.models.vault_provider_stats_by_env.VaultProviderStatsByEnv.from_dictionary(structure))
        vault_group = dictionary.get('vaultGroup')
        vault_id = dictionary.get('vaultId')
        vault_type = dictionary.get('vaultType')
        vaultname = dictionary.get('vaultname')
        write_bandwidth = dictionary.get('writeBandwidth')

        # Return an object of this model
        return cls(change_rate,
                   cluster_id,
                   cluster_incarnation_id,
                   cluster_name,
                   read_bandwidth,
                   stats_by_env,
                   vault_group,
                   vault_id,
                   vault_type,
                   vaultname,
                   write_bandwidth)


