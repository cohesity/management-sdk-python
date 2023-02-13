# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class SchedulingPolicyProtoDailySchedule(object):

    """Implementation of the 'SchedulingPolicyProto_DailySchedule' model.

    Sample protos:
    Every n days (n >= 1)
    Ex: For every 2 days, { frequency : 2 }
    Weekly schedule (Few selected weekdays)
    Ex: For every Monday, Tuesday { days : {kMonday, kTuesday} }
    NOTE: Only one of the 'days' and 'frequency' should be populated.

    Attributes:
        days (list of int): The list of weekdays for scheduling a backup. This
            is populated only for selected weekday schedules.
        frequency (long|int): This is set only for every-n-day schedules.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "days":'days',
        "frequency":'frequency'
    }

    def __init__(self,
                 days=None,
                 frequency=None):
        """Constructor for the SchedulingPolicyProtoDailySchedule class"""

        # Initialize members of the class
        self.days = days
        self.frequency = frequency


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
        frequency = dictionary.get('frequency')

        # Return an object of this model
        return cls(days,
                   frequency)


