# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.time


class DateTime(object):

    """Implementation of the 'DateTime' model.

    TODO: type description here.


    Attributes:

        day_of_the_month (int): Indicates day of the month.
        month (int): Indicates month for specific date.
        time (Time): Indicates the time in 24 hrs format.
        year (int): Indicates year for specific date.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "day_of_the_month":'dayOfTheMonth',
        "month":'month',
        "time":'time',
        "year":'year',
    }
    def __init__(self,
                 day_of_the_month=None,
                 month=None,
                 time=None,
                 year=None,
            ):

        """Constructor for the DateTime class"""

        # Initialize members of the class
        self.day_of_the_month = day_of_the_month
        self.month = month
        self.time = time
        self.year = year

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
        day_of_the_month = dictionary.get('dayOfTheMonth')
        month = dictionary.get('month')
        time = cohesity_management_sdk.models.time.Time.from_dictionary(dictionary.get('time')) if dictionary.get('time') else None
        year = dictionary.get('year')

        # Return an object of this model
        return cls(
            day_of_the_month,
            month,
            time,
            year
)