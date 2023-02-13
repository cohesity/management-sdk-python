# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ViewTimeSeriesStats(object):

    """Implementation of the 'ViewTimeSeriesStats' model.

    Specifies the View Time Series stats.

    Attributes:
        timestamp_msecs (long|int): Specifies the timestamp in milliseconds.
        value (long|int): Specifies the value of the specified metric at the
            timestamp.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "timestamp_msecs":'timestampMsecs',
        "value":'value'
    }

    def __init__(self,
                 timestamp_msecs=None,
                 value=None):
        """Constructor for the ViewTimeSeriesStats class"""

        # Initialize members of the class
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
        timestamp_msecs = dictionary.get('timestampMsecs')
        value = dictionary.get('value')

        # Return an object of this model
        return cls(timestamp_msecs,
                   value)


