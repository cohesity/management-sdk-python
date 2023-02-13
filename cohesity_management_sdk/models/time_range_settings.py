# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.universal_id

class TimeRangeSettings(object):

    """Implementation of the 'TimeRangeSettings' model.

    Specifies the time range struct.

    Attributes:
        end_time_usecs (long|int): Specifies the end time specified as a Unix
            epoch Timestamp (in microseconds).
        job_uid (UniversalId): Specifies an id for an object that is unique
            across Cohesity Clusters. The id is composite of all the ids
            listed below.
        start_time_usecs (long|int): Specifies the start time specified as a
            Unix epoch Timestamp (in microseconds).

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "end_time_usecs":'endTimeUsecs',
        "job_uid":'jobUid',
        "start_time_usecs":'startTimeUsecs'
    }

    def __init__(self,
                 end_time_usecs=None,
                 job_uid=None,
                 start_time_usecs=None):
        """Constructor for the TimeRangeSettings class"""

        # Initialize members of the class
        self.end_time_usecs = end_time_usecs
        self.job_uid = job_uid
        self.start_time_usecs = start_time_usecs


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
        end_time_usecs = dictionary.get('endTimeUsecs')
        job_uid = cohesity_management_sdk.models.universal_id.UniversalId.from_dictionary(dictionary.get('jobUid')) if dictionary.get('jobUid') else None
        start_time_usecs = dictionary.get('startTimeUsecs')

        # Return an object of this model
        return cls(end_time_usecs,
                   job_uid,
                   start_time_usecs)


