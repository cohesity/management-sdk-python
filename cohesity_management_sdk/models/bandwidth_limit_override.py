# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.time_of_a_week

class BandwidthLimitOverride(object):

    """Implementation of the 'BandwidthLimitOverride' model.

    Specifies bandwidth limit override value to be enforced during
    the specified daily time period for the specified days of the week.

    Attributes:
        bytes_per_second (long|int): Specifies the value to override the
            regular maximum bandwidth rate (rateLimitBytesPerSec) for the
            specified time period. The value is specified in bytes per
            second.
        io_rate (int): Specifies the value to override the default IO rate for
            the specified time period.
        time_periods (TimeOfAWeek): Specifies a time period by specifying a
            single daily time period and one or more days of the week, for
            example 9 AM - 5 PM on Monday, Wednesday or Friday. If different
            time periods are required on different days, then multiple
            instances of this Weekly Time Period must be specified.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bytes_per_second":'bytesPerSecond',
        "io_rate":'ioRate',
        "time_periods":'timePeriods'
    }

    def __init__(self,
                 bytes_per_second=None,
                 io_rate=None,
                 time_periods=None):
        """Constructor for the BandwidthLimitOverride class"""

        # Initialize members of the class
        self.bytes_per_second = bytes_per_second
        self.io_rate = io_rate
        self.time_periods = time_periods


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
        bytes_per_second = dictionary.get('bytesPerSecond')
        io_rate = dictionary.get('ioRate')
        time_periods = cohesity_management_sdk.models.time_of_a_week.TimeOfAWeek.from_dictionary(dictionary.get('timePeriods')) if dictionary.get('timePeriods') else None

        # Return an object of this model
        return cls(bytes_per_second,
                   io_rate,
                   time_periods)


