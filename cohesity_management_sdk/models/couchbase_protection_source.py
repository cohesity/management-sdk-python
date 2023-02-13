# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.couchbase_bucket
import cohesity_management_sdk.models.couchbase_cluster

class CouchbaseProtectionSource(object):

    """Implementation of the 'CouchbaseProtectionSource' model.

    Specifies an Object representing Couchbase.

    Attributes:
        bucket_info (CouchbaseBucket): Information of a Couchbase Bucket, only
            valid for an entity of type kBucket.
        cluster_info (CouchbaseCluster): Information of a couchbase cluster,
            only valid for an entity of type kCluster.
        name (string): Specifies the instance name of the Couchbase entity.
        mtype (TypeCouchbaseProtectionSourceEnum): Specifies the type of the
            managed Object in Couchbase Protection Source.
            Specifies the type of an Couchbase source entity.
            'kCluster' indicates a Couchbase cluster distributed over several
            physical nodes.
            'kBucket' indicates a bucket within the Couchbase environment.
        uuid (string): Specifies the UUID for the Couchbase entity.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bucket_info": 'bucketInfo',
        "cluster_info": 'clusterInfo',
        "name": 'name',
        "mtype": 'type',
        "uuid":'uuid'
    }

    def __init__(self,
                 bucket_info=None,
                 cluster_info=None,
                 name=None,
                 mtype=None,
                 uuid=None):
        """Constructor for the CouchbaseProtectionSource class"""

        # Initialize members of the class
        self.bucket_info = bucket_info
        self.cluster_info = cluster_info
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
        bucket_info = cohesity_management_sdk.models.couchbase_bucket.CouchbaseBucket.from_dictionary(dictionary.get('bucketInfo')) if dictionary.get('bucketInfo') else None
        cluster_info = cohesity_management_sdk.models.couchbase_cluster.CouchbaseCluster.from_dictionary(dictionary.get('clusterInfo')) if dictionary.get('clusterInfo') else None
        name = dictionary.get('name')
        mtype = dictionary.get('type')
        uuid = dictionary.get('uuid')

        # Return an object of this model
        return cls(bucket_info,
                   cluster_info,
                   name,
                   mtype,
                   uuid)


