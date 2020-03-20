# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.time_of_day

class BlackoutPeriod(object):

    """Implementation of the 'BlackoutPeriod' model.

    Specifies a time range in a single day when new Job Runs of
    Protection Jobs cannot be started. For example, a Protection Job
    with a daily schedule could define a blackout period for Sunday.

    Attributes:
        day (DayBlackoutPeriodEnum): Blackout Day.  Specifies a day in the
            week when no new Job Runs should be started such as 'kSunday'. If
            not set, the time range applies to all days. Specifies a day in a
            week such as 'kSunday', 'kMonday', etc.
        end_time (TimeOfDay): Specifies the end time of the blackout time
            range.
        start_time (TimeOfDay): Specifies the start time of the blackout time
            range.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "day":'day',
        "end_time":'endTime',
        "start_time":'startTime'
    }

    def __init__(self,
                 day=None,
                 end_time=None,
                 start_time=None):
        """Constructor for the BlackoutPeriod class"""

        # Initialize members of the class
        self.day = day
        self.end_time = end_time
        self.start_time = start_time


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
        day = dictionary.get('day')
        end_time = cohesity_management_sdk.models.time_of_day.TimeOfDay.from_dictionary(dictionary.get('endTime')) if dictionary.get('endTime') else None
        start_time = cohesity_management_sdk.models.time_of_day.TimeOfDay.from_dictionary(dictionary.get('startTime')) if dictionary.get('startTime') else None

        # Return an object of this model
        return cls(day,
                   end_time,
                   start_time)


