# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class Sample(object):

    """Implementation of the 'Sample' model.

    Specifies a sample of data collected at a timestamp.

    Attributes:
        float_value (float): Specifies the value of the data sample if the
            type is float64. This field is nil if the type of the data is not
            a float value.
        timestamp_msecs (long|int): Specifies the timestamp when the data
            sample occured.
        value (long|int): Specifies the value of the data sample if the type
            is int64. This field is nil if the type of the data is not an int
            value.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "float_value":'floatValue',
        "timestamp_msecs":'timestampMsecs',
        "value":'value'
    }

    def __init__(self,
                 float_value=None,
                 timestamp_msecs=None,
                 value=None):
        """Constructor for the Sample class"""

        # Initialize members of the class
        self.float_value = float_value
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
        float_value = dictionary.get('floatValue')
        timestamp_msecs = dictionary.get('timestampMsecs')
        value = dictionary.get('value')

        # Return an object of this model
        return cls(float_value,
                   timestamp_msecs,
                   value)


