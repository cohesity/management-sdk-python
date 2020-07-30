# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.cassandra_backup_job_params
import cohesity_management_sdk.models.couchbase_backup_job_params
import cohesity_management_sdk.models.h_base_backup_job_params
import cohesity_management_sdk.models.hdfs_backup_job_params
import cohesity_management_sdk.models.hive_backup_job_params
import cohesity_management_sdk.models.mongoDB_backup_job_params

class NoSqlBackupJobParams(object):

    """Implementation of the 'NoSqlBackupJobParams' model.

    Contains backup params at the job level applicable for nosql environment.

    Attributes:
        bandwidth_bytes_per_second (int): Net bandwidth bytes per second.
        cassandra_backup_job_params (CassandraBackupJobParams): Params
            specific to cassandra backup job.
        concurrency (int): Max number of mappers
        couchbase_backup_job_params (CouchbaseBackupJobParams): Contains any
            additional couchbase environment specific backup params at the job
            level.
        hbase_backup_job_params (HBaseBackupJobParams): Contains any additional
            couchbase environment specific backup params at the job level.
        hdfs_backup_job_params (HdfsBackupJobParams): Contains any additional hdfs
            environment specific backup params at the job level.
        hive_backup_job_params(HiveBackupJobParams): Contains any additional hive
            environment specific backup params at the job level.
        mongodb_backup_job_params (mongodbBackupJobParams): Contains any additional
            mongodb environment specific backup params at the job level.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bandwidth_bytes_per_second":'bandwidthBytesPerSecond',
        "cassandra_backup_job_params":'cassandraBackupJobParams',
        "concurrency":'concurrency',
        "couchbase_backup_job_params":'couchbaseBackupJobParams',
        "hbase_backup_job_params":'hbaseBackupJobParams',
        "hdfs_backup_job_params":'hdfsBackupJobParams',
        "hive_backup_job_params":'hiveBackupJobParams',
        "mongodb_backup_job_params":'mongodbBackupJobParams'
        }

    def __init__(self,
                 bandwidth_bytes_per_second=None,
                 cassandra_backup_job_params=None,
                 concurrency=None,
                 couchbase_backup_job_params=None,
                 hbase_backup_job_params=None,
                 hdfs_backup_job_params=None,
                 hive_backup_job_params=None,
                 mongodb_backup_job_params=None):
        """Constructor for the NoSqlBackupJobParams class"""

        # Initialize members of the class
        self.bandwidth_bytes_per_second = bandwidth_bytes_per_second
        self.cassandra_backup_job_params = cassandra_backup_job_params
        self.concurrency = concurrency
        self.couchbase_backup_job_params = couchbase_backup_job_params
        self.hbase_backup_job_params = hbase_backup_job_params
        self.hdfs_backup_job_params = hdfs_backup_job_params
        self.hive_backup_job_params = hive_backup_job_params
        self.mongodb_backup_job_params = mongodb_backup_job_params


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
        bandwidth_bytes_per_second = dictionary.get('bandwidthBytesPerSecond', None)
        cassandra_backup_job_params = cohesity_management_sdk.models.cassandra_backup_job_params.CassandraBackupJobParams.from_dictionary(dictionary.get('cassandraBackupJobParams')) if dictionary.get('cassandraBackupJobParams') else None
        concurrency = dictionary.get('concurrency', None)
        couchbase_backup_job_params = cohesity_management_sdk.models.couchbase_backup_job_params.CouchbaseBackupJobParams.from_dictionary(dictionary.get('couchbaseBackupJobParams')) if dictionary.get('couchbaseBackupJobParams') else None
        hbase_backup_job_params = cohesity_management_sdk.models.h_base_backup_job_params.HBaseBackupJobParams.from_dictionary(dictionary.get('hbaseBackupJobParams')) if dictionary.get('hbaseBackupJobParams') else None
        hdfs_backup_job_params = cohesity_management_sdk.models.hdfs_backup_job_params.HdfsBackupJobParams.from_dictionary(dictionary.get('hdfsBackupJobParams')) if dictionary.get('hdfsBackupJobParams') else None
        hive_backup_job_params = cohesity_management_sdk.models.hive_backup_job_params.HiveBackupJobParams.from_dictionary(dictionary.get('hiveBackupJobParams', None)) if dictionary.get('hiveBackupJobParams', None) else None
        mongodb_backup_job_params = cohesity_management_sdk.models.mongoDB_backup_job_params.MongoDBBackupJobParams.from_dictionary(dictionary.get('mongodbBackupJobParams', None)) if dictionary.get('mongodbBackupJobParams', None) else None

        # Return an object of this model
        return cls(bandwidth_bytes_per_second,
                   cassandra_backup_job_params,
                   concurrency,
                   couchbase_backup_job_params,
                   hbase_backup_job_params,
                   hdfs_backup_job_params,
                   hive_backup_job_params,
                   mongodb_backup_job_params)


