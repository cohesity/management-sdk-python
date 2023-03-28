# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.day_time


class DayTimeWindow(object):

    """Implementation of the 'DayTimeWindow' model.

    TODO: type description here.


    Attributes:

        end_time (DayTime): EndTime of the throttling window.
        start_time (DayTime): StartTime of the throttling window.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "end_time":'endTime',
        "start_time":'startTime',
    }
    def __init__(self,
                 end_time=None,
                 start_time=None,
            ):

        """Constructor for the DayTimeWindow class"""

        # Initialize members of the class
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
        end_time = cohesity_management_sdk.models.day_time.DayTime.from_dictionary(dictionary.get('endTime')) if dictionary.get('endTime') else None
        start_time = cohesity_management_sdk.models.day_time.DayTime.from_dictionary(dictionary.get('startTime')) if dictionary.get('startTime') else None

        # Return an object of this model
        return cls(
            end_time,
            start_time
)