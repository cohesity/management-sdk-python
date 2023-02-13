# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.metric_data_point

class MetricDataBlock(object):

    """Implementation of the 'MetricDataBlock' model.

    Specifies a series of metric data points for a time series.

    Attributes:
        data_point_vec (list of MetricDataPoint): Array of Data Points.
            Specifies a list of metric data points for a time series.
        metric_name (string): Specifies the name of a metric such as
            'kDiskAwaitTimeMsecs'.
        mtype (int): Specifies the data type of the data points. 0 specifies a
            data point of type Int64. 1 specifies a data point of type Double.
            2 specifies a data point of type String. 3 specifies a data point
            of type Bytes.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "data_point_vec":'dataPointVec',
        "metric_name":'metricName',
        "mtype":'type'
    }

    def __init__(self,
                 data_point_vec=None,
                 metric_name=None,
                 mtype=None):
        """Constructor for the MetricDataBlock class"""

        # Initialize members of the class
        self.data_point_vec = data_point_vec
        self.metric_name = metric_name
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
        data_point_vec = None
        if dictionary.get('dataPointVec') != None:
            data_point_vec = list()
            for structure in dictionary.get('dataPointVec'):
                data_point_vec.append(cohesity_management_sdk.models.metric_data_point.MetricDataPoint.from_dictionary(structure))
        metric_name = dictionary.get('metricName')
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(data_point_vec,
                   metric_name,
                   mtype)


