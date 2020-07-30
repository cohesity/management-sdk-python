# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.cassandra_ports_info

class CassandraConnectParams(object):

    """Implementation of the 'CassandraConnectParams' model.

    Specifies an Object containing information about a registered cassandra
    source.

    Attributes:
        cassandra_ports_info (CassandraPortsInfo): Specifies the ports related
            info.
        config_directory (string): Specifies the Directory path containing
            Config YAML for discovery.
        data_centers (list of string): Specifies the List of all physical data
            center or virtual data center. In most cases, the data centers
            will be listed after discovery operation however, if they are not
            listed, you must manually type the data center names. Leaving the
            field blank will disallow data center-specific backup or restore.
            Entering a subset of all data centers may cause problems in data
            movement.
        dse_config_directory (string): Specifies the Directory from where DSE
            specific configuration can be read.
        is_dse_authenticator (bool): Specifies whether this cluster has DSE
            Authenticator.
        is_dse_tiered_storage (bool): Specifies whether this cluster has DSE
            tiered storage.
        jaas_config_path (string): Specifies the Path to the JAAS Config file
            on the Imanis node.
        primary_host (string): Specifies the Primary Host for the Cassandra
            cluster.
        seeds (list of string): Specifies the Seed nodes of this Cassandra
            cluster.
        solr_nodes (list of string): Specifies the Solr node IP Addresses
        solr_port (int): Specifies the Solr node Port.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cassandra_ports_info":'cassandraPortsInfo',
        "config_directory":'configDirectory',
        "data_centers":'dataCenters',
        "dse_config_directory":'dseConfigDirectory',
        "is_dse_authenticator":'isDseAuthenticator',
        "is_dse_tiered_storage":'isDseTieredStorage',
        "jaas_config_path":'jaasConfigPath',
        "primary_host":'primaryHost',
        "seeds":'seeds',
        "solr_nodes":'solrNodes',
        "solr_port":'solrPort',
    }

    def __init__(self,
                 cassandra_ports_info=None,
                 config_directory=None,
                 data_centers=None,
                 dse_config_directory=None,
                 is_dse_authenticator=None,
                 is_dse_tiered_storage=None,
                 jaas_config_path=None,
                 primary_host=None,
                 seeds=None,
                 solr_nodes=None,
                 solr_port=None):
        """Constructor for the CassandraConnectParams class"""

        # Initialize members of the class
        self.cassandra_ports_info = cassandra_ports_info
        self.config_directory = config_directory
        self.data_centers = data_centers
        self.dse_config_directory = dse_config_directory
        self.is_dse_authenticator = is_dse_authenticator
        self.is_dse_tiered_storage = is_dse_tiered_storage
        self.jaas_config_path = jaas_config_path
        self.primary_host = primary_host
        self.seeds = seeds
        self.solr_nodes = solr_nodes
        self.solr_port = solr_port


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
        cassandra_ports_info = cohesity_management_sdk.models.cassandra_ports_info.CassandraPortsInfo.from_dictionary(dictionary.get('cassandraPortsInfo')) if dictionary.get('cassandraPortsInfo') else None
        config_directory = dictionary.get('configDirectory')
        data_centers = dictionary.get('dataCenters')
        dse_config_directory = dictionary.get('dseConfigDirectory')
        is_dse_authenticator = dictionary.get('isDseAuthenticator')
        is_dse_tiered_storage = dictionary.get('isDseTieredStorage')
        jaas_config_path = dictionary.get('jaasConfigPath')
        primary_host = dictionary.get('primaryHost')
        seeds = dictionary.get('seeds', None)
        solr_nodes = dictionary.get('solrNodes')
        solr_port = dictionary.get('solrPort')

        # Return an object of this model
        return cls(cassandra_ports_info,
                   config_directory,
                   data_centers,
                   dse_config_directory,
                   is_dse_authenticator,
                   is_dse_tiered_storage,
                   jaas_config_path,
                   primary_host,
                   seeds,
                   solr_nodes,
                   solr_port)


