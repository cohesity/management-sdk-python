# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.cassandra_recover_job_params
import cohesity_management_sdk.models.couchbase_recover_job_params
import cohesity_management_sdk.models.h_base_recover_job_params
import cohesity_management_sdk.models.hdfs_recover_job_params
import cohesity_management_sdk.models.hive_recover_job_params
import cohesity_management_sdk.models.mongodb_recover_job_params

class NoSqlRecoverJobParams(object):

    """Implementation of the 'NoSqlRecoverJobParams' model.

    TODO: Type model description here.

    Attributes:
        bandwidth_bytes_per_second (long|int): Net bandwidth bytes per second.
        cassandra_recover_job_params (CassandraRecoverJobParams): Params
            specific to cassandra backup job.
        concurrency (int): Max number of mappers.
        couchbase_recover_job_params (CouchbaseRecoverJobParams): Params
            specific to couchbase recover job.
        hbase_recover_job_params (HbaseRecoverJobParams): Params specific to
            hbase recover job.
        hdfs_recover_job_params (HdfsRecoverJobParams):  Params specific to
            hdfs recover job.
        hive_recover_job_params (HiveRecoverJobParams): Params specific to
            hive recover job.
        mongodb_recover_job_params (MongoDBRecoverJobParams): Params specific
            to mongodb recover job.
        overwrite (bool): Whether to overwrite or keep the object if the
            object being recovered already exists in the destination.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bandwidth_bytes_per_second":'bandwidthBytesPerSecond',
        "cassandra_recover_job_params":'cassandraRecoverJobParams',
        "concurrency":'concurrency',
        "couchbase_recover_job_params":'couchbaseRecoverJobParams',
        "hbase_recover_job_params":'hbaseRecoverJobParams',
        "hdfs_recover_job_params":'hdfsRecoverJobParams',
        "hive_recover_job_params":'hiveRecoverJobParams',
        "mongodb_recover_job_params":'mongodbRecoverJobParams',
        "overwrite":'overwrite'
        }

    def __init__(self,
                 bandwidth_bytes_per_second=None,
                 cassandra_recover_job_params=None,
                 concurrency=None,
                 couchbase_recover_job_params=None,
                 hbase_recover_job_params=None,
                 hdfs_recover_job_params=None,
                 hive_recover_job_params=None,
                 mongodb_recover_job_params=None,
                 overwrite=None):

        """Constructor for the NoSqlRecoverJobParams class"""
        # Initialize members of the class
        self.bandwidth_bytes_per_second = bandwidth_bytes_per_second
        self.cassandra_recover_job_params = cassandra_recover_job_params
        self.concurrency = concurrency
        self.couchbase_recover_job_params = couchbase_recover_job_params
        self.hbase_recover_job_params = hbase_recover_job_params
        self.hdfs_recover_job_params = hdfs_recover_job_params
        self.hive_recover_job_params = hive_recover_job_params
        self.mongodb_recover_job_params = mongodb_recover_job_params
        self.overwrite = overwrite


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
        cassandra_recover_job_params = cohesity_management_sdk.models.cassandra_recover_job_params.CassandraRecoverJobParams.from_dictionary(dictionary.get('cassandraRecoverJobParams')) if dictionary.get('cassandraRecoverJobParams') else None
        concurrency = dictionary.get('concurrency', None)
        couchbase_recover_job_params = cohesity_management_sdk.models.couchbase_recover_job_params.CouchbaseRecoverJobParams.from_dictionary(dictionary.get('couchbaseRecoverJobParams')) if dictionary.get('couchbaseRecoverJobParams') else None
        hbase_recover_job_params = cohesity_management_sdk.models.h_base_recover_job_params.HBaseRecoverJobParams.from_dictionary(dictionary.get('hbaseRecoverJobParams')) if dictionary.get('hbaseRecoverJobParams') else None
        hdfs_recover_job_params = cohesity_management_sdk.models.hdfs_recover_job_params.HdfsRecoverJobParams.from_dictionary(dictionary.get('hdfsRecoverJobParams')) if dictionary.get('hdfsRecoverJobParams') else None
        hive_recover_job_params = cohesity_management_sdk.models.hive_recover_job_params.HiveRecoverJobParams.from_dictionary(dictionary.get('hiveRecoverJobParams', None)) if dictionary.get('hiveRecoverJobParams', None) else None
        mongodb_recover_job_params = cohesity_management_sdk.models.mongodb_recover_job_params.MongoDBRecoverJobParams.from_dictionary(dictionary.get('mongodbRecoverJobParams', None)) if dictionary.get('mongodbRecoverJobParams', None) else None
        overwrite = dictionary.get('overwrite')

        # Return an object of this model
        return cls(bandwidth_bytes_per_second,
                   cassandra_recover_job_params,
                   concurrency,
                   couchbase_recover_job_params,
                   hbase_recover_job_params,
                   hdfs_recover_job_params,
                   hive_recover_job_params,
                   mongodb_recover_job_params,
                   overwrite)

