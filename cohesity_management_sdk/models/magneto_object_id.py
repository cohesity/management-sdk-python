# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.entity_proto
import cohesity_management_sdk.models.universal_id_proto


class MagnetoObjectId(object):

    """Implementation of the 'MagnetoObjectId' model.

    TODO: type description here.


    Attributes:

        entity (EntityProto): Entity proto that represents the object being
            snapshotted.
        job_id (long|int): The id of the local job that the object belongs to,
            which may or may not match the object_id field in job_uid below
            depending on whether the object originally belonged to this local
            job or to a different remote job.
        job_uid (UniversalIdProto): The globally unique id of the job that the
            object originally belonged to. If this object originally belonged
            to a job from a remote cluster, this field will contain the uid of
            the remote job, else it will contain the uid of the local job.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "entity":'entity',
        "job_id":'jobId',
        "job_uid":'jobUid',
    }
    def __init__(self,
                 entity=None,
                 job_id=None,
                 job_uid=None,
            ):

        """Constructor for the MagnetoObjectId class"""

        # Initialize members of the class
        self.entity = entity
        self.job_id = job_id
        self.job_uid = job_uid

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
        entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('entity')) if dictionary.get('entity') else None
        job_id = dictionary.get('jobId')
        job_uid = cohesity_management_sdk.models.universal_id_proto.UniversalIdProto.from_dictionary(dictionary.get('jobUid')) if dictionary.get('jobUid') else None

        # Return an object of this model
        return cls(
            entity,
            job_id,
            job_uid
)