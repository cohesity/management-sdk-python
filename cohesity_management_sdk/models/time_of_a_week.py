# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.time_of_day

class TimeOfAWeek(object):

    """Implementation of the 'TimeOfAWeek' model.

    Specifies a time period by specifying a single daily time period
    and one or more days of the week, for example 9 AM - 5 PM
    on Monday, Wednesday or Friday. If different time periods are required
    on different days, then multiple instances of this Weekly Time Period
    must be specified.

    Attributes:
        days (list of DayEnum): Array of Week Days.  Specifies a list of days
            of a week (such as 'kSunday') when the time period should be
            applied. If not set, the time range applies to all days of the
            week. Specifies a day in a week such as 'kSunday', 'kMonday',
            etc.
        end_time (TimeOfDay): Specifies the end time for the daily time
            period.
        is_all_day (bool): All Day.  Specifies that time range is applied for
            entire day.
        start_time (TimeOfDay): Specifies the start time for the daily time
            period.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "days":'days',
        "end_time":'endTime',
        "is_all_day":'isAllDay',
        "start_time":'startTime'
    }

    def __init__(self,
                 days=None,
                 end_time=None,
                 is_all_day=None,
                 start_time=None):
        """Constructor for the TimeOfAWeek class"""

        # Initialize members of the class
        self.days = days
        self.end_time = end_time
        self.is_all_day = is_all_day
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
        days = dictionary.get('days')
        end_time = cohesity_management_sdk.models.time_of_day.TimeOfDay.from_dictionary(dictionary.get('endTime')) if dictionary.get('endTime') else None
        is_all_day = dictionary.get('isAllDay')
        start_time = cohesity_management_sdk.models.time_of_day.TimeOfDay.from_dictionary(dictionary.get('startTime')) if dictionary.get('startTime') else None

        # Return an object of this model
        return cls(days,
                   end_time,
                   is_all_day,
                   start_time)


