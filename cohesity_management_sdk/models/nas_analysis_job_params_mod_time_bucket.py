# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class NasAnalysisJobParams_ModTimeBucket(object):

    """Implementation of the 'NasAnalysisJobParams_ModTimeBucket' model.

    Modification time bucket.

    Attributes:
        mod_time_bucket_name (string): Tag representing the bucket for
            modified time of file.
            e.g. "1mo-3mo" represents 1 month to 3 month.
        mod_time_end_days (long|int): End time e.g. 1 year. Stored in
            days precision.
        mod_time_start_days (long|int): Start time e.g. 6 months. Stored in
            days precision.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mod_time_bucket_name":'modTimeBucketName',
        "mod_time_end_days":'modTimeEndDays',
        "mod_time_start_days":'modTimeStartDays'
    }

    def __init__(self,
                 mod_time_bucket_name=None,
                 mod_time_end_days=None,
                 mod_time_start_days=None):
        """Constructor for the NasAnalysisJobParams_ModTimeBucket class"""

        # Initialize members of the class
        self.mod_time_bucket_name = mod_time_bucket_name
        self.mod_time_end_days = mod_time_end_days
        self.mod_time_start_days = mod_time_start_days


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
        mod_time_bucket_name = dictionary.get('modTimeBucketName')
        mod_time_end_days = dictionary.get('modTimeEndDays')
        mod_time_start_days = dictionary.get('modTimeStartDays')

        # Return an object of this model
        return cls(mod_time_bucket_name,
                   mod_time_end_days,
                   mod_time_start_days)


