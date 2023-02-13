# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.cassandra_additional_params
import cohesity_management_sdk.models.cassandra_connect_params
import cohesity_management_sdk.models.couchbase_connect_params
import cohesity_management_sdk.models.hbase_connect_params
import cohesity_management_sdk.models.hdfs_connect_params
import cohesity_management_sdk.models.hive_connect_params
import cohesity_management_sdk.models.mongoDB_additional_params
import cohesity_management_sdk.models.mongo_db_connect_params

class NoSqlConnectParams(object):

    """Implementation of the 'NoSqlConnectParams' model.

    Attributes:
        cassandra_additional_params (CassandraAdditionalParams): Additional
            params required for cassandra backup.
        cassandra_connect_params (CassandraConnectParams): Connect params for
            connecting to cassandra cluster. Set only if env_type is
            kCassandra.
        couchbase_connect_params (CouchbaseConnectParams): Additional params
            for connecting to couchbase cluster. Set only if env_type is
            kCouchbase.
        hbase_connect_params (HBaseConnectParams): Additional params for
            connecting to hbase cluster. Set only if env_type is kHBase.
        hdfs_connect_params (HdfsConnectParams): Additional params for
            connecting to hdfs cluster. Set only if env_type is kHdfs.
        hive_connect_params (HiveConnectParams): Additional params for
            connecting to hive cluster. Set only if env_type is kHive.
        mongodb_additional_params (MongoDBAdditionalParams): Additional params
            required for mongodb backup.
        mongodb_connect_params (MongoDBConnectParams): Additional params for
            connecting to mongodb cluster. Set only if env_type is kMongoDB.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cassandra_additional_params":'cassandraAdditionalParams',
        "cassandra_connect_params":'cassandraConnectParams',
        "couchbase_connect_params":'couchbaseConnectParams',
        "hbase_connect_params":'hbaseConnectParams',
        "hdfs_connect_params":'hdfsConnectParams',
        "hive_connect_params":'hiveConnectParams',
        "mongodb_additional_params":'mongodbAdditionalParams',
        "mongodb_connect_params":'mongodbConnectParams'
    }

    def __init__(self,
                 cassandra_additional_params=None,
                 cassandra_connect_params=None,
                 couchbase_connect_params=None,
                 hbase_connect_params=None,
                 hdfs_connect_params=None,
                 hive_connect_params=None,
                 mongodb_additional_params=None,
                 mongodb_connect_params=None):
        """Constructor for the NoSqlConnectParams class"""

        # Initialize members of the class
        self.cassandra_additional_params = cassandra_additional_params
        self.cassandra_connect_params = cassandra_connect_params
        self.couchbase_connect_params = couchbase_connect_params
        self.hbase_connect_params = hbase_connect_params
        self.hdfs_connect_params = hdfs_connect_params
        self.hive_connect_params = hive_connect_params
        self.mongodb_additional_params = mongodb_additional_params
        self.mongodb_connect_params = mongodb_connect_params


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
        cassandra_additional_params = cohesity_management_sdk.models.cassandra_additional_params.CassandraAdditionalParams.from_dictionary(dictionary.get('cassandraAdditionalParams')) if dictionary.get('cassandraAdditionalParams') else None
        cassandra_connect_params = cohesity_management_sdk.models.cassandra_connect_params.CassandraConnectParams.from_dictionary(dictionary.get('cassandraConnectParams')) if dictionary.get('cassandraConnectParams') else None
        couchbase_connect_params = cohesity_management_sdk.models.couchbase_connect_params.CouchbaseConnectParams.from_dictionary(dictionary.get('couchbaseConnectParams')) if dictionary.get('couchbaseConnectParams') else None
        hbase_connect_params = cohesity_management_sdk.models.hbase_connect_params.HBaseConnectParams.from_dictionary(dictionary.get('hbaseConnectParams')) if dictionary.get('hbaseConnectParams') else None
        hdfs_connect_params = cohesity_management_sdk.models.hdfs_connect_params.HdfsConnectParams.from_dictionary(dictionary.get('hdfsConnectParams')) if dictionary.get('hdfsConnectParams') else None
        hive_connect_params = cohesity_management_sdk.models.hive_connect_params.HiveConnectParams.from_dictionary(dictionary.get('hiveConnectParams')) if dictionary.get('hiveConnectParams') else None
        mongodb_additional_params = cohesity_management_sdk.models.mongoDB_additional_params.MongoDBAdditionalParams.from_dictionary(dictionary.get('mongodbAdditionalParams')) if dictionary.get('mongodbAdditionalParams') else None
        mongodb_connect_params = cohesity_management_sdk.models.mongo_db_connect_params.MongoDBConnectParams.from_dictionary(dictionary.get('mongodbConnectParams')) if dictionary.get('mongodbConnectParams') else None

        # Return an object of this model
        return cls(cassandra_additional_params,
                   cassandra_connect_params,
                   couchbase_connect_params,
                   hbase_connect_params,
                   hdfs_connect_params,
                   hive_connect_params,
                   mongodb_additional_params,
                   mongodb_connect_params)


