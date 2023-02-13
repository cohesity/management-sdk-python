# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.key_value_pair
import cohesity_management_sdk.models.entity_identifier
import cohesity_management_sdk.models.metric_value

class EntityProto(object):

    """Implementation of the 'EntityProto' model.

    Specifies the attributes and the latest statistics about an entity.

    Attributes:
        attribute_vec (list of KeyValuePair): Array of Attributes.  List of
            attributes of an entity.
        entity_id (EntityIdentifier): Specifies a unique identifier for the
            entity.
        latest_metric_vec (list of MetricValue): Array of Metric Statistics.
            List of the latest statistics for all metrics defined in the
            schema that this entity belongs to. If statistics for a metric is
            not available, then that data point is not returned.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "attribute_vec":'attributeVec',
        "entity_id":'entityId',
        "latest_metric_vec":'latestMetricVec'
    }

    def __init__(self,
                 attribute_vec=None,
                 entity_id=None,
                 latest_metric_vec=None):
        """Constructor for the EntityProto class"""

        # Initialize members of the class
        self.attribute_vec = attribute_vec
        self.entity_id = entity_id
        self.latest_metric_vec = latest_metric_vec


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
        attribute_vec = None
        if dictionary.get('attributeVec') != None:
            attribute_vec = list()
            for structure in dictionary.get('attributeVec'):
                attribute_vec.append(cohesity_management_sdk.models.key_value_pair.KeyValuePair.from_dictionary(structure))
        entity_id = cohesity_management_sdk.models.entity_identifier.EntityIdentifier.from_dictionary(dictionary.get('entityId')) if dictionary.get('entityId') else None
        latest_metric_vec = None
        if dictionary.get('latestMetricVec') != None:
            latest_metric_vec = list()
            for structure in dictionary.get('latestMetricVec'):
                latest_metric_vec.append(cohesity_management_sdk.models.metric_value.MetricValue.from_dictionary(structure))

        # Return an object of this model
        return cls(attribute_vec,
                   entity_id,
                   latest_metric_vec)


