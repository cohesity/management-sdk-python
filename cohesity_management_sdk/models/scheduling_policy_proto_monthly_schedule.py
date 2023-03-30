# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class SchedulingPolicyProto_MonthlySchedule(object):

    """Implementation of the 'SchedulingPolicyProto_MonthlySchedule' model.

    TODO: type description here.


    Attributes:

        count (int): Count of the day on which to perform the backup (look
            above for a more detailed description).
        day (int): The day of the month the backup is to be performed.
        day_of_month (int): Specific date of the month on which to perform the
            backup.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "count":'count',
        "day":'day',
        "day_of_month":'dayOfMonth',
    }
    def __init__(self,
                 count=None,
                 day=None,
                 day_of_month=None,
            ):

        """Constructor for the SchedulingPolicyProto_MonthlySchedule class"""

        # Initialize members of the class
        self.count = count
        self.day = day
        self.day_of_month = day_of_month

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
        day_of_month = dictionary.get('dayOfMonth')

        # Return an object of this model
        return cls(
            count,
            day,
            day_of_month
)