# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class FileDistributionMetrics(object):

    """Implementation of the 'FileDistributionMetrics' model.

    Specifies the File distribution metrics.

    Attributes:
        metric_name (string): Specifies the name of the metric.
        value (long|int): Specifies the value of specified metric name.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "metric_name":'metricName',
        "value":'value'
    }

    def __init__(self,
                 metric_name=None,
                 value=None):
        """Constructor for the FileDistributionMetrics class"""

        # Initialize members of the class
        self.metric_name = metric_name
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
        value = dictionary.get('value')

        # Return an object of this model
        return cls(metric_name,
                   value)


