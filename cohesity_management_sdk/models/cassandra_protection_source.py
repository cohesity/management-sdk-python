# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.cassandra_cluster
import cohesity_management_sdk.models.cassandra_keyspace

class CassandraProtectionSource(object):

    """Implementation of the 'CassandraProtectionSource' model.

    Specifies an Object representing Cassandra.

    Attributes:
        cluster_info (CassandraCluster): Information of a Cassandra cluster,
            only valid for an entity of type kCluster.
        keyspace_info (CassandraKeyspace): Information of a cassandra
            keyspapce, only valid for an entity of type kKeyspace.
        name (string): Specifies the instance name of the Cassandra entity.
        mtype (TypeCassandraProtectionSourceEnum): Specifies the type of the
            managed Object in Cassandra Protection Source.
            Replication strategy options for a keyspace.
            'kCluster' indicates a Cassandra cluster distributed over several
            physical nodes.
            'kKeyspace' indicates a Keyspace enclosing one or more tables.
            'kTable' indicates a Table in the Cassandra environment.
        uuid (string): Specifies the UUID for the Cassandra entity.
            Note : For each entity an ID unique within top level entity should
            be assigned by imanis backend. Example, UUID for a table can be
            the string <keyspace_name>.<table_name>

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cluster_info": 'clusterInfo',
        "keyspace_info": 'keyspaceInfo',
        "name": 'name',
        "mtype": 'type',
        "uuid":'uuid'
    }

    def __init__(self,
                 cluster_info=None,
                 keyspace_info=None,
                 name=None,
                 mtype=None,
                 uuid=None):
        """Constructor for the CassandraProtectionSource class"""

        # Initialize members of the class
        self.cluster_info = cluster_info
        self.keyspace_info = keyspace_info
        self.name = name
        self.mtype = mtype
        self.uuid = uuid

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
        cluster_info = cohesity_management_sdk.models.cassandra_cluster.CassandraCluster.from_dictionary(dictionary.get('clusterInfo')) if dictionary.get('clusterInfo') else None
        keyspace_info = cohesity_management_sdk.models.cassandra_keyspace.CassandraKeyspace.from_dictionary(dictionary.get('keyspaceInfo')) if dictionary.get('keyspaceInfo') else None
        name = dictionary.get('name')
        mtype = dictionary.get('type')
        uuid = dictionary.get('uuid')

        # Return an object of this model
        return cls(cluster_info,
                   keyspace_info,
                   name,
                   mtype,
                   uuid)


