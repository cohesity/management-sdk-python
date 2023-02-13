# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.entity_schema_proto_time_series_descriptor_metric_unit

class EntitySchemaProtoTimeSeriesDescriptor(object):

    """Implementation of the 'EntitySchemaProto_TimeSeriesDescriptor' model.

    Specifies the meta-data required to define a time series of data
    (set of data points) for a metric.

    Attributes:
        metric_descriptive_name (string): Specifies a descriptive name for the
            metric that is displayed in the Advanced Diagnostics of the
            Cohesity Dashboard. For example for the 'kUnmorphedUsageBytes'
            metric, the descriptive name is "Total Logical Space Used".
        metric_name (string): Specifies the name of the metric such as
            'kUnmorphedUsageBytes'. It should be unique in an entity schema.
        metric_unit (EntitySchemaProtoTimeSeriesDescriptorMetricUnit):
            Specifies the unit of measure for the metric. O specifies a unit
            of space used such as free disk space. 1 specifies a Unix epoch
            Timestamp (in microseconds). 2 specifies a Unix epoch Timestamp
            (in milliseconds). 3 specifies a Unix epoch Timestamp (in
            seconds). 4 specifies a Unix epoch Timestamp (in minutes). 5
            specifies a counter such as the read IO metric. 6 specifies the
            temperature in Centigrade. 7 specifies the temperature in
            Fahrenheit. 8 specifies revolutions per minute such as a CPU fan
            speed. 9 specifies a percentage such as CPU or memory usage.
        raw_metric_publish_interval_hint_secs (int): Specifies a suggestion
            for the interval to collect raw data points.
        time_to_live_secs (long|int): Specifies how long the data point will be
            stored. Note: In statsv2, as timeseries data of an entity is stored
            per scribe row with metrics as columns, it is good to have
            time_to_live_secs per schema(defined below)
            For existing schemas, we will consider highest time_to_live_secs
            of all metrics as expiration time for all metrics defined in schema.
        value_type (int): Specifies the value type for this metric. A metric
            of type 'string" is not supported, instead use 'bytes'. Note that
            an aggregate metric of type 'bytes' is not supported. 0 specifies
            a value type of Int64. 1 specifies a value type of Double. 2
            specifies a value type of String. 3 specifies a value type of
            Bytes.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "metric_descriptive_name":'metricDescriptiveName',
        "metric_name":'metricName',
        "metric_unit":'metricUnit',
        "raw_metric_publish_interval_hint_secs":'rawMetricPublishIntervalHintSecs',
        "time_to_live_secs":'timeToLiveSecs',
        "value_type":'valueType'
    }

    def __init__(self,
                 metric_descriptive_name=None,
                 metric_name=None,
                 metric_unit=None,
                 raw_metric_publish_interval_hint_secs=None,
                 time_to_live_secs=None,
                 value_type=None):
        """Constructor for the EntitySchemaProtoTimeSeriesDescriptor class"""

        # Initialize members of the class
        self.metric_descriptive_name = metric_descriptive_name
        self.metric_name = metric_name
        self.metric_unit = metric_unit
        self.raw_metric_publish_interval_hint_secs = raw_metric_publish_interval_hint_secs
        self.time_to_live_secs = time_to_live_secs
        self.value_type = value_type


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
        metric_descriptive_name = dictionary.get('metricDescriptiveName')
        metric_name = dictionary.get('metricName')
        metric_unit = cohesity_management_sdk.models.entity_schema_proto_time_series_descriptor_metric_unit.EntitySchemaProtoTimeSeriesDescriptorMetricUnit.from_dictionary(dictionary.get('metricUnit')) if dictionary.get('metricUnit') else None
        raw_metric_publish_interval_hint_secs = dictionary.get('rawMetricPublishIntervalHintSecs')
        time_to_live_secs = dictionary.get('timeToLiveSecs')
        value_type = dictionary.get('valueType')

        # Return an object of this model
        return cls(metric_descriptive_name,
                   metric_name,
                   metric_unit,
                   raw_metric_publish_interval_hint_secs,
                   time_to_live_secs,
                   value_type)


