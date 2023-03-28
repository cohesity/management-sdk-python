# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.dse_solr_info
import cohesity_management_sdk.models.node_to_tiered_storage_directories_map


class CassandraAdditionalParams(object):

    """Implementation of the 'CassandraAdditionalParams' model.

    Contains additional parameters required by the agents to backup data from
    Cassandra.


    Attributes:

        cassandra_classpath_suffix (string): Cassandra classpath suffix.
        cassandra_partitioner (string): Required in compaction.
        cassandra_version (string): Cassandra and DSE Versions. Discovery code
            will attempt to discover the versions.
        commit_log_backup_location (string): Commit Log Backup location used
            for PITR feature
        data_center_vec (list of string): Data center information is required
            for backup and recovery.
        dse_solr_info (DSESolrInfo): In case this Cassandra has a Solr node.
        dse_version (string): TODO: Type description here.
        tiered_storage_dirs_map (list of NodeToTieredStorageDirectoriesMap):
            Map of nodes to tiered storage directories
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "cassandra_classpath_suffix":'cassandraClasspathSuffix',
        "cassandra_partitioner":'cassandraPartitioner',
        "cassandra_version":'cassandraVersion',
        "commit_log_backup_location":'commitLogBackupLocation',
        "data_center_vec":'dataCenterVec',
        "dse_solr_info":'dseSolrInfo',
        "dse_version":'dseVersion',
        "tiered_storage_dirs_map":'tieredStorageDirsMap',
    }
    def __init__(self,
                 cassandra_classpath_suffix=None,
                 cassandra_partitioner=None,
                 cassandra_version=None,
                 commit_log_backup_location=None,
                 data_center_vec=None,
                 dse_solr_info=None,
                 dse_version=None,
                 tiered_storage_dirs_map=None,
            ):

        """Constructor for the CassandraAdditionalParams class"""

        # Initialize members of the class
        self.cassandra_classpath_suffix = cassandra_classpath_suffix
        self.cassandra_partitioner = cassandra_partitioner
        self.cassandra_version = cassandra_version
        self.commit_log_backup_location = commit_log_backup_location
        self.data_center_vec = data_center_vec
        self.dse_solr_info = dse_solr_info
        self.dse_version = dse_version
        self.tiered_storage_dirs_map = tiered_storage_dirs_map

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
        cassandra_classpath_suffix = dictionary.get('cassandraClasspathSuffix')
        cassandra_partitioner = dictionary.get('cassandraPartitioner')
        cassandra_version = dictionary.get('cassandraVersion')
        commit_log_backup_location = dictionary.get('commitLogBackupLocation')
        data_center_vec = dictionary.get("dataCenterVec")
        dse_solr_info = cohesity_management_sdk.models.dse_solr_info.DSESolrInfo.from_dictionary(dictionary.get('dseSolrInfo')) if dictionary.get('dseSolrInfo') else None
        dse_version = dictionary.get('dseVersion')
        tiered_storage_dirs_map = None
        if dictionary.get('tieredStorageDirsMap') != None:
            tiered_storage_dirs_map = list()
            for structure in dictionary.get('tieredStorageDirsMap'):
                tiered_storage_dirs_map.append(cohesity_management_sdk.models.node_to_tiered_storage_directories_map.NodeToTieredStorageDirectoriesMap.from_dictionary(structure))

        # Return an object of this model
        return cls(
            cassandra_classpath_suffix,
            cassandra_partitioner,
            cassandra_version,
            commit_log_backup_location,
            data_center_vec,
            dse_solr_info,
            dse_version,
            tiered_storage_dirs_map
)