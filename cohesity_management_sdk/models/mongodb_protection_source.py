# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.mongo_db_cluster
import cohesity_management_sdk.models.mongo_db_collection
import cohesity_management_sdk.models.mongo_db_database

class MongoDBProtectionSource(object):

    """Implementation of the 'MongoDBProtectionSource' model.

    Specifies an Object representing MongoDB.

    Attributes:
        cluster_info (MongoDBCluster): Information of a mongodb cluster, only
            valid for an entity of type kCluster.
        collection_info (MongoDBCollection): Information about a mongodb
            collection, only valid for an entity of type kCollection.
        database_info (MongoDBDatabase): Information of a mongodb database,
            only valid for an entity of type kDatabase.
        name (string): Specifies the instance name of the MongoDB entity.
        mtype (TypeMongoDBProtectionSourceEnum): Specifies the type of the
            managed Object in MongoDB Protection Source.
            Specifies the type of an MongoDB source entity.
            'kCluster' indicates a mongodb cluster distributed over several
            physical nodes.
            'kDatabase' indicates a Database within the MongoDB environment.
            'kCollection' indicates a Collection in the MongoDB enironment.
        uuid (string):  Specifies the UUID for the MongoDB entity.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cluster_info":'clusterInfo',
        "collection_info":'collectionInfo',
        "database_info":'databaseInfo',
        "name":'name',
        "mtype":'type',
        "uuid":'uuid'
    }

    def __init__(self,
                 cluster_info=None,
                 collection_info=None,
                 database_info=None,
                 name=None,
                 mtype=None,
                 uuid=None):
        """Constructor for the MongoDBProtectionSource class"""

        # Initialize members of the class
        self.cluster_info = cluster_info
        self.collection_info = collection_info
        self.database_info = database_info
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
        cluster_info = cohesity_management_sdk.models.mongo_db_cluster.MongoDBCluster.from_dictionary(dictionary.get('clusterInfo')) if dictionary.get('clusterInfo') else None
        collection_info = cohesity_management_sdk.models.mongo_db_collection.MongoDBCollection.from_dictionary(dictionary.get('collectionInfo')) if dictionary.get('collectionInfo') else None
        database_info = cohesity_management_sdk.models.mongo_db_database.MongoDBDatabase.from_dictionary(dictionary.get('databaseInfo')) if dictionary.get('databaseInfo') else None
        name = dictionary.get('name')
        mtype = dictionary.get('type')
        uuid = dictionary.get('uuid')

        # Return an object of this model
        return cls(cluster_info,
                   collection_info,
                   database_info,
                   name,
                   mtype,
                   uuid)


