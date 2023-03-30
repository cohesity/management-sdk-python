# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.time


class DayTime(object):

    """Implementation of the 'DayTime' model.

    TODO: type description here.


    Attributes:

        day (DayEnum): Specifies the day of the week (such as 'kMonday') for
            scheduling throttling. Specifies a day in a week such as 'kSunday',
            'kMonday', etc.
        time (Time): Specifies the information regarding the scheduled time.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "day":'day',
        "time":'time',
    }
    def __init__(self,
                 day=None,
                 time=None,
            ):

        """Constructor for the DayTime class"""

        # Initialize members of the class
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
        day = dictionary.get('day')
        time = cohesity_management_sdk.models.time.Time.from_dictionary(dictionary.get('time')) if dictionary.get('time') else None

        # Return an object of this model
        return cls(
            day,
            time
)