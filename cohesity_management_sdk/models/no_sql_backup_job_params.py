# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

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
        compaction_job_interval_secs (long|int): Frequency at which compaction
            jobs should run in seconds. Will be only applicable for Cassandra,
            Mongo and Couchbase environment.
        concurrency (int): Max number of mappers.
        couchbase_backup_job_params (CouchbaseBackupJobParams): Contains any
            additional couchbase environment specific backup params at the job
            level.
        gc_job_interval_secs (long|int): Frequency at which garbage collection
            jobs should run in seconds.
        gc_retention_period_days (int): Retention period for logs of this job
            in days.
        hbase_backup_job_params (HBaseBackupJobParams): Contains any additional
            couchbase environment specific backup params at the job level.
        hdfs_backup_job_params (HdfsBackupJobParams): Contains any additional hdfs
            environment specific backup params at the job level.
        hive_backup_job_params(HiveBackupJobParams): Contains any additional hive
            environment specific backup params at the job level.
        last_compaction_run_time_usecs (long|int): The last time (in usecs)
            when the compaction ran for this jobs.
        last_gc_run_time_usecs (long|int): The last time (in usecs) when the
            gc ran for this jobs.
        mongodb_backup_job_params (mongodbBackupJobParams): Contains any additional
            mongodb environment specific backup params at the job level.
        previous_protected_entity_ids_vec (list of str): List of Magneto entity
            Ids for the entities that were protected in the previous run.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bandwidth_bytes_per_second":'bandwidthBytesPerSecond',
        "cassandra_backup_job_params":'cassandraBackupJobParams',
        "compaction_job_interval_secs":'compactionJobIntervalSecs',
        "concurrency":'concurrency',
        "couchbase_backup_job_params":'couchbaseBackupJobParams',
        "gc_job_interval_secs":'gcJobIntervalSecs',
        "gc_retention_period_days":'gcRetentionPeriodDays',
        "hbase_backup_job_params":'hbaseBackupJobParams',
        "hdfs_backup_job_params":'hdfsBackupJobParams',
        "hive_backup_job_params":'hiveBackupJobParams',
        "last_compaction_run_time_usecs":'lastCompactionRunTimeUsecs',
        "last_gc_run_time_usecs":'lastGcRunTimeUsecs',
        "mongodb_backup_job_params":'mongodbBackupJobParams',
        "previous_protected_entity_ids_vec":'previousProtectedEntityIdsVec'
        }

    def __init__(self,
                 bandwidth_bytes_per_second=None,
                 cassandra_backup_job_params=None,
                 compaction_job_interval_secs=None,
                 concurrency=None,
                 couchbase_backup_job_params=None,
                 gc_job_interval_secs=None,
                 gc_retention_period_days=None,
                 hbase_backup_job_params=None,
                 hdfs_backup_job_params=None,
                 hive_backup_job_params=None,
                 last_compaction_run_time_usecs=None,
                 last_gc_run_time_usecs=None,
                 mongodb_backup_job_params=None,
                 previous_protected_entity_ids_vec=None):
        """Constructor for the NoSqlBackupJobParams class"""

        # Initialize members of the class
        self.bandwidth_bytes_per_second = bandwidth_bytes_per_second
        self.cassandra_backup_job_params = cassandra_backup_job_params
        self.compaction_job_interval_secs = compaction_job_interval_secs
        self.concurrency = concurrency
        self.couchbase_backup_job_params = couchbase_backup_job_params
        self.gc_job_interval_secs = gc_job_interval_secs
        self.gc_retention_period_days = gc_retention_period_days
        self.hbase_backup_job_params = hbase_backup_job_params
        self.hdfs_backup_job_params = hdfs_backup_job_params
        self.hive_backup_job_params = hive_backup_job_params
        self.last_compaction_run_time_usecs = last_compaction_run_time_usecs
        self.last_gc_run_time_usecs = last_gc_run_time_usecs
        self.mongodb_backup_job_params = mongodb_backup_job_params
        self.previous_protected_entity_ids_vec = previous_protected_entity_ids_vec


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
        compaction_job_interval_secs = dictionary.get('compactionJobIntervalSecs')
        concurrency = dictionary.get('concurrency', None)
        couchbase_backup_job_params = cohesity_management_sdk.models.couchbase_backup_job_params.CouchbaseBackupJobParams.from_dictionary(dictionary.get('couchbaseBackupJobParams')) if dictionary.get('couchbaseBackupJobParams') else None
        gc_job_interval_secs = dictionary.get('gcJobIntervalSecs')
        gc_retention_period_days = dictionary.get('gcRetentionPeriodDays')
        hbase_backup_job_params = cohesity_management_sdk.models.h_base_backup_job_params.HBaseBackupJobParams.from_dictionary(dictionary.get('hbaseBackupJobParams')) if dictionary.get('hbaseBackupJobParams') else None
        hdfs_backup_job_params = cohesity_management_sdk.models.hdfs_backup_job_params.HdfsBackupJobParams.from_dictionary(dictionary.get('hdfsBackupJobParams')) if dictionary.get('hdfsBackupJobParams') else None
        hive_backup_job_params = cohesity_management_sdk.models.hive_backup_job_params.HiveBackupJobParams.from_dictionary(dictionary.get('hiveBackupJobParams', None)) if dictionary.get('hiveBackupJobParams', None) else None
        last_compaction_run_time_usecs = dictionary.get('lastCompactionRunTimeUsecs')
        last_gc_run_time_usecs = dictionary.get('lastGcRunTimeUsecs')
        mongodb_backup_job_params = cohesity_management_sdk.models.mongoDB_backup_job_params.MongoDBBackupJobParams.from_dictionary(dictionary.get('mongodbBackupJobParams', None)) if dictionary.get('mongodbBackupJobParams', None) else None
        previous_protected_entity_ids_vec = dictionary.get('previousProtectedEntityIdsVec')

        # Return an object of this model
        return cls(bandwidth_bytes_per_second,
                   cassandra_backup_job_params,
                   compaction_job_interval_secs,
                   concurrency,
                   couchbase_backup_job_params,
                   gc_job_interval_secs,
                   gc_retention_period_days,
                   hbase_backup_job_params,
                   hdfs_backup_job_params,
                   hive_backup_job_params,
                   last_compaction_run_time_usecs,
                   last_gc_run_time_usecs,
                   mongodb_backup_job_params,
                   previous_protected_entity_ids_vec)


