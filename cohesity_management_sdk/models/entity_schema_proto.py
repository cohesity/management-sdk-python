# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.entity_schema_proto_attributes_descriptor
import cohesity_management_sdk.models.entity_schema_proto_time_series_descriptor

class EntitySchemaProto(object):

    """Implementation of the 'EntitySchemaProto' model.

    Specifies the meta-data associated with entity such as the list of
    attributes and time series data.

    Attributes:
        attributes_descriptor (EntitySchemaProtoAttributesDescriptor):
            Specifies a list of attributes about an entity.
        is_internal_schema (bool): Specifies if this schema should be
            displayed in Advanced Diagnostics of the Cohesity Dashboard. If
            false, the schema is displayed.
        name (string): Specifies a name that uniquely identifies an entity
            schema such as 'kBridgeClusterStats'.
        schema_descriptive_name (string): Specifies the name of the Schema as
            displayed in Advanced Diagnostics of the Cohesity Dashboard. For
            example for the 'kBridgeClusterStats' Schema, the descriptive name
            is 'Cluster Physical Stats'.
        schema_help_text (string): Specifies an optional informational
            description about the schema.
        time_series_descriptor_vec (list of
            EntitySchemaProtoTimeSeriesDescriptor): Array of Time Series.
            List of time series of data (set of data points) for metrics.
        version (long|int): Specifies the version of the entity schema.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "attributes_descriptor":'attributesDescriptor',
        "is_internal_schema":'isInternalSchema',
        "name":'name',
        "schema_descriptive_name":'schemaDescriptiveName',
        "schema_help_text":'schemaHelpText',
        "time_series_descriptor_vec":'timeSeriesDescriptorVec',
        "version":'version'
    }

    def __init__(self,
                 attributes_descriptor=None,
                 is_internal_schema=None,
                 name=None,
                 schema_descriptive_name=None,
                 schema_help_text=None,
                 time_series_descriptor_vec=None,
                 version=None):
        """Constructor for the EntitySchemaProto class"""

        # Initialize members of the class
        self.attributes_descriptor = attributes_descriptor
        self.is_internal_schema = is_internal_schema
        self.name = name
        self.schema_descriptive_name = schema_descriptive_name
        self.schema_help_text = schema_help_text
        self.time_series_descriptor_vec = time_series_descriptor_vec
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
        is_internal_schema = dictionary.get('isInternalSchema')
        name = dictionary.get('name')
        schema_descriptive_name = dictionary.get('schemaDescriptiveName')
        schema_help_text = dictionary.get('schemaHelpText')
        time_series_descriptor_vec = None
        if dictionary.get('timeSeriesDescriptorVec') != None:
            time_series_descriptor_vec = list()
            for structure in dictionary.get('timeSeriesDescriptorVec'):
                time_series_descriptor_vec.append(cohesity_management_sdk.models.entity_schema_proto_time_series_descriptor.EntitySchemaProtoTimeSeriesDescriptor.from_dictionary(structure))
        version = dictionary.get('version')

        # Return an object of this model
        return cls(attributes_descriptor,
                   is_internal_schema,
                   name,
                   schema_descriptive_name,
                   schema_help_text,
                   time_series_descriptor_vec,
                   version)


