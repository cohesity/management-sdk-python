# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class TagsOperationParameters(object):

    """Implementation of the 'TagsOperationParameters' model.

    TagsOperationParameters specifies tagging details.

    Attributes:
        cluster_id (int|long):  ClusterId is the Id of the cluster used for
            constructing JobUid.
        cluster_incarnation_id (int|long): ClusterIncarnationId is the
            incarnation Id of the cluster used for constructing JobUid.
        document_ids (list of string): DocumentIds are list of documents to be
            tagged.
        entity_id (int): EntityId is the Id of the entity where the file
            resides.
        job_id (int|long):  JobId is the Id of the job that took the snapshot.
        job_instance_ids (list of int|long): JobInstanceIds to tag
            corresponding snapshots.
        tag_ids (list of string): Tags are list of tags uuids that will be
            operated on to corresponding objects.
        tags (list of string): Tags are list of tags that will be operated on
            to corresponding objects.
            This is deprecated. Use tagIds instead.
            deprecated: true
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cluster_id": 'clusterId',
        "cluster_incarnation_id": 'clusterIncarnationId',
        "document_ids": 'documentIds',
        "entity_id": 'entityId',
        "job_id":'jobId',
        "job_instance_ids":'jobInstanceIds',
        "tag_ids":'tagIds',
        "tags":'tags'
    }

    def __init__(self,
                 cluster_id=None,
                 cluster_incarnation_id=None,
                 document_ids=None,
                 entity_id=None,
                 job_id=None,
                 job_instance_ids=None,
                 tag_ids=None,
                 tags=None):
        """Constructor for the TagsOperationParameters class"""

        # Initialize members of the class
        self.cluster_id = cluster_id
        self.cluster_incarnation_id = cluster_incarnation_id
        self.document_ids = document_ids
        self.entity_id = entity_id
        self.job_id = job_id
        self.job_instance_ids = job_instance_ids
        self.tag_ids = tag_ids
        self.tags = tags

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
        cluster_id = dictionary.get('clusterId')
        cluster_incarnation_id = dictionary.get('clusterIncarnationId')
        document_ids = dictionary.get('documentIds')
        entity_id = dictionary.get('entityId')
        job_id = dictionary.get('jobId')
        job_instance_ids = dictionary.get('jobInstanceIds')
        tag_ids = dictionary.get('tagIds')
        tags = dictionary.get('tags')

        # Return an object of this model
        return cls(cluster_id,
                   cluster_incarnation_id,
                   document_ids,
                   entity_id,
                   job_id,
                   job_instance_ids,
                   tag_ids,
                   tags)


