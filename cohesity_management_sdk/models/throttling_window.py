# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.day_time_window


class ThrottlingWindow(object):

    """Implementation of the 'ThrottlingWindow' model.

    TODO: type description here.


    Attributes:

        day_time_window (DayTimeWindow): Day time window. This captures day and
            time window on that day.
        threshold (long|int): Throttling threshold applicable in the window.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "day_time_window":'dayTimeWindow',
        "threshold":'threshold',
    }
    def __init__(self,
                 day_time_window=None,
                 threshold=None,
            ):

        """Constructor for the ThrottlingWindow class"""

        # Initialize members of the class
        self.day_time_window = day_time_window
        self.threshold = threshold

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
        day_time_window = cohesity_management_sdk.models.day_time_window.DayTimeWindow.from_dictionary(dictionary.get('dayTimeWindow')) if dictionary.get('dayTimeWindow') else None
        threshold = dictionary.get('threshold')

        # Return an object of this model
        return cls(
            day_time_window,
            threshold
)