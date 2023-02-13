# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class TimeOfDay(object):

    """Implementation of the 'TimeOfDay' model.

    Specifies a time in day with hours and minutes.

    Attributes:
        hour (int): Specifies an (0-23) hour in a day.
        minute (int): Specifies a (0-59) minute in an hour.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "hour":'hour',
        "minute":'minute'
    }

    def __init__(self,
                 hour=None,
                 minute=None):
        """Constructor for the TimeOfDay class"""

        # Initialize members of the class
        self.hour = hour
        self.minute = minute


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
        hour = dictionary.get('hour')
        minute = dictionary.get('minute')

        # Return an object of this model
        return cls(hour,
                   minute)


