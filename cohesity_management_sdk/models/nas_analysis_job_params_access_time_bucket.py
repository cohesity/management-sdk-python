# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class NasAnalysisJobParams_AccessTimeBucket(object):

    """Implementation of the 'NasAnalysisJobParams_AccessTimeBucket' model.

    Access time bucket.

    Attributes:
        access_time_bucket_name (string): Tag representing the bucket for
            access time of file.
            e.g. "1mo-3mo" represents 1 month to 3 month.
        access_time_end_days (long|int): End time e.g. 1 year. Stored in
            days precision.
        access_time_start_days (long|int): Start time e.g. 6 months. Stored in
            days precision.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "access_time_bucket_name":'accessTimeBucketName',
        "access_time_end_days":'accessTimeEndDays',
        "access_time_start_days":'accessTimeStartDays'
    }

    def __init__(self,
                 access_time_bucket_name=None,
                 access_time_end_days=None,
                 access_time_start_days=None):
        """Constructor for the NasAnalysisJobParams_AccessTimeBucket class"""

        # Initialize members of the class
        self.access_time_bucket_name = access_time_bucket_name
        self.access_time_end_days = access_time_end_days
        self.access_time_start_days = access_time_start_days


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
        access_time_bucket_name = dictionary.get('accessTimeBucketName')
        access_time_end_days = dictionary.get('accessTimeEndDays')
        access_time_start_days = dictionary.get('accessTimeStartDays')

        # Return an object of this model
        return cls(access_time_bucket_name,
                   access_time_end_days,
                   access_time_start_days)


