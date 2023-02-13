# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.entity_schema_proto_attributes_descriptor
import cohesity_management_sdk.models.entity_schema_proto_granularity
import cohesity_management_sdk.models.entity_schema_proto_time_series_descriptor

class EntitySchemaProto(object):

    """Implementation of the 'EntitySchemaProto' model.

    Specifies the meta-data associated with entity such as the list of
    attributes and time series data.

    Attributes:
        attributes_descriptor (EntitySchemaProtoAttributesDescriptor):
            Specifies a list of attributes about an entity.
        enable_rollup (bool): Timeseries for an entity schema is rolled up
            based on this setting.
            Rollup is disabled by default.
            Rollups cannot be done for metrics with value_type other than
            kInt64 or kDouble.
        flush_interval_secs (int): Defines the interval used to flush in
            memory stats to scribe table. During this time if the stats server
            is down before flushing, it could loose some of the stats. Modules
            can flush any critical stats via AddEntitiesStats API. But this
            should be used very judiciously as it causes lot of overhead for
            stats.
        is_internal_schema (bool): Specifies if this schema should be
            displayed in Advanced Diagnostics of the Cohesity Dashboard. If
            false, the schema is displayed.
        largest_flush_interval_secs (int): Use can change the flush interval
            secs via gflag and this store the largest interval seconds set.
            This is used to round up the timestamp to this flush interval secs
            during range scan.
        name (string): Specifies a name that uniquely identifies an entity
            schema such as 'kBridgeClusterStats'. Name cannot have ':' as
            character.
        rollup_granularity_vec (list of EntitySchemaProto_Granularity): TODO:
            type description here.
        schema_descriptive_name (string): Specifies the name of the Schema as
            displayed in Advanced Diagnostics of the Cohesity Dashboard. For
            example for the 'kBridgeClusterStats' Schema, the descriptive name
            is 'Cluster Physical Stats'.
        schema_help_text (string): Specifies an optional informational
            description about the schema.
        time_series_descriptor_vec (list of
            EntitySchemaProtoTimeSeriesDescriptor): Array of Time Series.
            List of time series of data (set of data points) for metrics.
        time_to_live_secs (int): Specifies how long the timeseries data of
            this. After expiry the entire data point(all metrics) is garbage
            collected.
        version (long|int): Specifies the version of the entity schema.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "attributes_descriptor":'attributesDescriptor',
        "enable_rollup":'enableRollup',
        "flush_interval_secs":'flushIntervalSecs',
        "is_internal_schema":'isInternalSchema',
        "largest_flush_interval_secs":'largestFlushIntervalSecs',
        "name":'name',
        "rollup_granularity_vec": 'rollupGranularityVec',
        "schema_descriptive_name":'schemaDescriptiveName',
        "schema_help_text":'schemaHelpText',
        "time_series_descriptor_vec":'timeSeriesDescriptorVec',
        "time_to_live_secs": 'timeToLiveSecs',
        "version":'version'
    }

    def __init__(self,
                 attributes_descriptor=None,
                 enable_rollup=None,
                 flush_interval_secs=None,
                 is_internal_schema=None,
                 largest_flush_interval_secs=None,
                 name=None,
                 rollup_granularity_vec=None,
                 schema_descriptive_name=None,
                 schema_help_text=None,
                 time_series_descriptor_vec=None,
                 time_to_live_secs=None,
                 version=None):
        """Constructor for the EntitySchemaProto class"""

        # Initialize members of the class
        self.attributes_descriptor = attributes_descriptor
        self.enable_rollup = enable_rollup
        self.flush_interval_secs = flush_interval_secs
        self.is_internal_schema = is_internal_schema
        self.largest_flush_interval_secs = largest_flush_interval_secs
        self.name = name
        self.rollup_granularity_vec = rollup_granularity_vec
        self.schema_descriptive_name = schema_descriptive_name
        self.schema_help_text = schema_help_text
        self.time_series_descriptor_vec = time_series_descriptor_vec
        self.time_to_live_secs = time_to_live_secs
        self.version = version


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
        attributes_descriptor = cohesity_management_sdk.models.entity_schema_proto_attributes_descriptor.EntitySchemaProtoAttributesDescriptor.from_dictionary(dictionary.get('attributesDescriptor')) if dictionary.get('attributesDescriptor') else None
        enable_rollup = dictionary.get('enableRollup', None)
        flush_interval_secs = dictionary.get('flushIntervalSecs')
        is_internal_schema = dictionary.get('isInternalSchema')
        largest_flush_interval_secs = dictionary.get('largestFlushIntervalSecs')
        name = dictionary.get('name')
        rollup_granularity_vec = None
        if dictionary.get('rollupGranularityVec') != None:
            rollup_granularity_vec = list()
            for structure in dictionary.get('rollupGranularityVec'):
                rollup_granularity_vec.append(cohesity_management_sdk.models.entity_schema_proto_granularity.EntitySchemaProto_Granularity.from_dictionary(structure))
        schema_descriptive_name = dictionary.get('schemaDescriptiveName')
        schema_help_text = dictionary.get('schemaHelpText')
        time_series_descriptor_vec = None
        if dictionary.get('timeSeriesDescriptorVec') != None:
            time_series_descriptor_vec = list()
            for structure in dictionary.get('timeSeriesDescriptorVec'):
                time_series_descriptor_vec.append(cohesity_management_sdk.models.entity_schema_proto_time_series_descriptor.EntitySchemaProtoTimeSeriesDescriptor.from_dictionary(structure))
        time_to_live_secs = dictionary.get('timeToLiveSecs', None)
        version = dictionary.get('version')

        # Return an object of this model
        return cls(attributes_descriptor,
                   enable_rollup,
                   flush_interval_secs,
                   is_internal_schema,
                   largest_flush_interval_secs,
                   name,
                   rollup_granularity_vec,
                   schema_descriptive_name,
                   schema_help_text,
                   time_series_descriptor_vec,
                   time_to_live_secs,
                   version)


