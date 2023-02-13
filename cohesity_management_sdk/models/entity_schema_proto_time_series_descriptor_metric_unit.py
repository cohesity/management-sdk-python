# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class EntitySchemaProtoTimeSeriesDescriptorMetricUnit(object):

    """Implementation of the 'EntitySchemaProto_TimeSeriesDescriptor_MetricUnit' model.

    Specifies the unit of measure for the metric.
    O specifies a unit of space used such as free disk space.
    1 specifies a Unix epoch Timestamp (in microseconds).
    2 specifies a Unix epoch Timestamp (in milliseconds).
    3 specifies a Unix epoch Timestamp (in seconds).
    4 specifies a Unix epoch Timestamp (in minutes).
    5 specifies a counter such as the read IO metric.
    6 specifies the temperature in Centigrade.
    7 specifies the temperature in Fahrenheit.
    8 specifies revolutions per minute such as a CPU fan speed.
    9 specifies a percentage such as CPU or memory usage.

    Attributes:
        mtype (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtype":'type'
    }

    def __init__(self,
                 mtype=None):
        """Constructor for the EntitySchemaProtoTimeSeriesDescriptorMetricUnit class"""

        # Initialize members of the class
        self.mtype = mtype


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
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(mtype)


