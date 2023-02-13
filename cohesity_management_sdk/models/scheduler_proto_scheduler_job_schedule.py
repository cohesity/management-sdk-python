# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class SchedulerProtoSchedulerJobSchedule(object):

    """Implementation of the 'SchedulerProto_SchedulerJob_Schedule' model.

    A message which specifies the schedule of execution of the job.

    Attributes:
        day (int): The day of the week when schedule should be executed
            (0-6).
        hour (int): The hour of the day when schedule should be executed
            (0-23).
        timezone (string): The timezone for the execution of the schedule.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "day":'day',
        "hour":'hour',
        "timezone":'timezone'
    }

    def __init__(self,
                 day=None,
                 hour=None,
                 timezone=None):
        """Constructor for the SchedulerProtoSchedulerJobSchedule class"""

        # Initialize members of the class
        self.day = day
        self.hour = hour
        self.timezone = timezone


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
        hour = dictionary.get('hour')
        timezone = dictionary.get('timezone')

        # Return an object of this model
        return cls(day,
                   hour,
                   timezone)


