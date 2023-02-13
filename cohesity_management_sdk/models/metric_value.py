# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.value

class MetricValue(object):

    """Implementation of the 'MetricValue' model.

    Specifies one data point of a metric.

    Attributes:
        metric_name (string): Specifies the metric name.
        timestamp_msecs (long|int): Specifies the creation time of a data
            point as a Unix epoch Timestamp (in milliseconds).
        value (Value): Specifies a data type and data field used to store
            data.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "metric_name":'metricName',
        "timestamp_msecs":'timestampMsecs',
        "value":'value'
    }

    def __init__(self,
                 metric_name=None,
                 timestamp_msecs=None,
                 value=None):
        """Constructor for the MetricValue class"""

        # Initialize members of the class
        self.metric_name = metric_name
        self.timestamp_msecs = timestamp_msecs
        self.value = value


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
        metric_name = dictionary.get('metricName')
        timestamp_msecs = dictionary.get('timestampMsecs')
        value = cohesity_management_sdk.models.value.Value.from_dictionary(dictionary.get('value')) if dictionary.get('value') else None

        # Return an object of this model
        return cls(metric_name,
                   timestamp_msecs,
                   value)


