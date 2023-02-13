# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class TrendingData(object):

    """Implementation of the 'TrendingData' model.

    Specifies protection runs information per object, aggregated over a
    period
    of time.

    Attributes:
        cancelled (long|int): Specifies number of cancelled runs.
        failed (long|int): Specifies number of failed runs.
        running (long|int): Specifies number of in-progress runs.
        successful (long|int): Specifies number of successful runs.
        total (long|int): Specifies total number of runs.
        trend_name (string): Specifies trend name. This is start of the
            day/week/month.
        trend_start_time_usecs (long|int): Specifies start of the
            day/week/month in micro seconds

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cancelled":'cancelled',
        "failed":'failed',
        "running":'running',
        "successful":'successful',
        "total":'total',
        "trend_name":'trendName',
        "trend_start_time_usecs":'trendStartTimeUsecs'
    }

    def __init__(self,
                 cancelled=None,
                 failed=None,
                 running=None,
                 successful=None,
                 total=None,
                 trend_name=None,
                 trend_start_time_usecs=None):
        """Constructor for the TrendingData class"""

        # Initialize members of the class
        self.cancelled = cancelled
        self.failed = failed
        self.running = running
        self.successful = successful
        self.total = total
        self.trend_name = trend_name
        self.trend_start_time_usecs = trend_start_time_usecs


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
        cancelled = dictionary.get('cancelled')
        failed = dictionary.get('failed')
        running = dictionary.get('running')
        successful = dictionary.get('successful')
        total = dictionary.get('total')
        trend_name = dictionary.get('trendName')
        trend_start_time_usecs = dictionary.get('trendStartTimeUsecs')

        # Return an object of this model
        return cls(cancelled,
                   failed,
                   running,
                   successful,
                   total,
                   trend_name,
                   trend_start_time_usecs)


