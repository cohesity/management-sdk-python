# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class SchemaInfo(object):

    """Implementation of the 'SchemaInfo' model.

    Specifies the metric data point where public data metric name as key and
    the
    schema defined metric name as a value.

    Attributes:
        entity_id (string): Specifies the id of the entity represented as a
            string.
        key (string): Specifies the key which is public facing name for metric
            name.
        metric_name (string): Specifies the Apollo schema metric name.
        schema_name (string): Specifies the name of entity schema such as
            'ApolloViewBoxStats'.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "entity_id":'entityId',
        "key":'key',
        "metric_name":'metricName',
        "schema_name":'schemaName'
    }

    def __init__(self,
                 entity_id=None,
                 key=None,
                 metric_name=None,
                 schema_name=None):
        """Constructor for the SchemaInfo class"""

        # Initialize members of the class
        self.entity_id = entity_id
        self.key = key
        self.metric_name = metric_name
        self.schema_name = schema_name


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
        entity_id = dictionary.get('entityId')
        key = dictionary.get('key')
        metric_name = dictionary.get('metricName')
        schema_name = dictionary.get('schemaName')

        # Return an object of this model
        return cls(entity_id,
                   key,
                   metric_name,
                   schema_name)


