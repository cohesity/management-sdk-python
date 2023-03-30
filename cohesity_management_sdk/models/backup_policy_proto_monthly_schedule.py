# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.time


class BackupPolicyProto_MonthlySchedule(object):

    """Implementation of the 'BackupPolicyProto_MonthlySchedule' model.

    TODO: type description here.


    Attributes:

        count (int): Count of the day on which to perform the backup (look
            above for a more detailed description).
        day (int): The day of the month the backup is to be performed.
        time (Time): Time when the monthly backup should be performed.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "count":'count',
        "day":'day',
        "time":'time',
    }
    def __init__(self,
                 count=None,
                 day=None,
                 time=None,
            ):

        """Constructor for the BackupPolicyProto_MonthlySchedule class"""

        # Initialize members of the class
        self.count = count
        self.day = day
        self.time = time

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
        count = dictionary.get('count')
        day = dictionary.get('day')
        time = cohesity_management_sdk.models.time.Time.from_dictionary(dictionary.get('time')) if dictionary.get('time') else None

        # Return an object of this model
        return cls(
            count,
            day,
            time
)