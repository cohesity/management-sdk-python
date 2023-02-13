# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.entity_proto

class BackupJobProtoExcludeSource(object):

    """Implementation of the 'BackupJobProto_ExcludeSource' model.

    TODO: type model description here.

    Attributes:
        entities (list of EntityProto): An intersection of leaf-level entities
            will be obtained after expanding the following entities.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "entities":'entities'
    }

    def __init__(self,
                 entities=None):
        """Constructor for the BackupJobProtoExcludeSource class"""

        # Initialize members of the class
        self.entities = entities


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
        entities = None
        if dictionary.get('entities') != None:
            entities = list()
            for structure in dictionary.get('entities'):
                entities.append(cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(structure))

        # Return an object of this model
        return cls(entities)


