# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.connector_params
import cohesity_management_sdk.models.entity_proto

class StorageSnapshotProviderParams(object):

    """Implementation of the 'StorageSnapshotProviderParams' model.

    TODO: type model description here.

    Attributes:
        connector_params (ConnectorParams): Message that encapsulates the
            various params required to establish a connection with a
            particular environment.
        entity (EntityProto): Specifies the attributes and the latest
            statistics about an entity.
        root_entity (EntityProto): The root entity that the entity was
            running under.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "connector_params":'connectorParams',
        "entity":'entity',
        "root_entity":'rootEntity'
    }

    def __init__(self,
                 connector_params=None,
                 entity=None,
                 root_entity=None):
        """Constructor for the StorageSnapshotProviderParams class"""

        # Initialize members of the class
        self.connector_params = connector_params
        self.entity = entity
        self.root_entity = root_entity


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
        connector_params = cohesity_management_sdk.models.connector_params.ConnectorParams.from_dictionary(dictionary.get('connectorParams')) if dictionary.get('connectorParams') else None
        entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('entity')) if dictionary.get('entity') else None
        root_entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('rootEntity')) if dictionary.get('rootEntity') else None

        # Return an object of this model
        return cls(connector_params,
                   entity,
                   root_entity)


