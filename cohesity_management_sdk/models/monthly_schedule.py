# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class MonthlySchedule(object):

    """Implementation of the 'MonthlySchedule' model.

    Specifies a monthly backup schedule by specifying a day in the week
    and a week in the month.
    For example, if day is set to 'kMonday' and dayCount is set
    to 'kThird', a Job Run is started on the third Monday of every month.

    Attributes:
        day (DayMonthlyScheduleEnum): Specifies the day of the week (such as
            'kMonday') to start the Job Run. Used with day count to define the
            day in the month to start the Job Run. Specifies a day in a week
            such as 'kSunday', 'kMonday', etc.
        day_count (DayCountEnum): Specifies the day count in the month (such
            as 'kThird') to start the Job Run. Used in combination with day to
            define the day in the month to start the Job Run. Specifies the
            day count in the month to start the backup. For example if day
            count is set to 'kThird' and day is set to 'kMonday', a backup is
            performed on the third Monday of every month. 'kFirst' indicates
            that the first week should be chosen for specified day of every
            month. 'kSecond' indicates that the second week should be chosen
            for specified day of every month. 'kThird' indicates that the
            third week should be chosen for specified day of every month.
            'kFourth' indicates that the fourth week should be chosen for
            specified day of every month. 'kLast' indicates that the last
            week should be chosen for specified day of every month.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "day":'day',
        "day_count":'dayCount'
    }

    def __init__(self,
                 day=None,
                 day_count=None):
        """Constructor for the MonthlySchedule class"""

        # Initialize members of the class
        self.day = day
        self.day_count = day_count


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
        day_count = dictionary.get('dayCount')

        # Return an object of this model
        return cls(day,
                   day_count)


