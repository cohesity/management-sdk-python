# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.universal_id

class ProtectedObject(object):

    """Implementation of the 'ProtectedObject' model.

    Provides details about a Protected Object.

    Attributes:
        job_id (UniversalId): Specifies an id for an object that is unique
            across Cohesity Clusters. The id is composite of all the ids
            listed below.
        protection_fauilure_reason (string): If protection fails then
            specifies why the protection failed on this object.
        protection_source_id (long|int): Specifies the id of the Protection
            Source.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "job_id":'jobId',
        "protection_fauilure_reason":'protectionFauilureReason',
        "protection_source_id":'protectionSourceId'
    }

    def __init__(self,
                 job_id=None,
                 protection_fauilure_reason=None,
                 protection_source_id=None):
        """Constructor for the ProtectedObject class"""

        # Initialize members of the class
        self.job_id = job_id
        self.protection_fauilure_reason = protection_fauilure_reason
        self.protection_source_id = protection_source_id


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
        job_id = cohesity_management_sdk.models.universal_id.UniversalId.from_dictionary(dictionary.get('jobId')) if dictionary.get('jobId') else None
        protection_fauilure_reason = dictionary.get('protectionFauilureReason')
        protection_source_id = dictionary.get('protectionSourceId')

        # Return an object of this model
        return cls(job_id,
                   protection_fauilure_reason,
                   protection_source_id)


