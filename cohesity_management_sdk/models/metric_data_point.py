# -*- coding: utf-8 -*-
# Copyright 2020 Cohesity Inc.

import cohesity_management_sdk.models.value_data

class MetricDataPoint(object):

    """Implementation of the 'MetricDataPoint' model.

    Specifies information about a single data point in a time series.

    Attributes:
        data (ValueData): Specifies the fields to store data of a given type.
            Specify data in the appropriate field for the current data type.
        timestamp_msecs (long|int): Specifies a timestamp when the metric data
            point was captured.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "data":'data',
        "timestamp_msecs":'timestampMsecs'
    }

    def __init__(self,
                 data=None,
                 timestamp_msecs=None):
        """Constructor for the MetricDataPoint class"""

        # Initialize members of the class
        self.data = data
        self.timestamp_msecs = timestamp_msecs


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
        data = cohesity_management_sdk.models.value_data.ValueData.from_dictionary(dictionary.get('data')) if dictionary.get('data') else None
        timestamp_msecs = dictionary.get('timestampMsecs')

        # Return an object of this model
        return cls(data,
                   timestamp_msecs)


