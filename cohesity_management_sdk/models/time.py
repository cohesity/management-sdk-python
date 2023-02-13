# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class Time(object):

    """Implementation of the 'Time' model.

    A message to encapusulate time of a day. Users of this proto will have to
    store the timezone information separately. For example, when this proto
    is part of a backup job, timezone of the backup job is applied to get the
    absolute time.

    Attributes:
        hour (int): The hour when backup should be performed (0 - 23).
        minute (int): The minute when backup should be performed (0 - 59).

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "hour":'hour',
        "minute":'minute'
    }

    def __init__(self,
                 hour=None,
                 minute=None):
        """Constructor for the Time class"""

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


