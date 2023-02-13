# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.entity_proto

class DestroyClonedEntityInfoProtoClonedEntity(object):

    """Implementation of the 'DestroyClonedEntityInfoProto_ClonedEntity' model.

    TODO: type model description here.

    Attributes:
        entity (EntityProto): Specifies the attributes and the latest
            statistics about an entity.
        relative_restore_path_vec (list of string): Path of all files created
            by the clone operation. Each path is relative to the clone view.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "entity":'entity',
        "relative_restore_path_vec":'relativeRestorePathVec'
    }

    def __init__(self,
                 entity=None,
                 relative_restore_path_vec=None):
        """Constructor for the DestroyClonedEntityInfoProtoClonedEntity class"""

        # Initialize members of the class
        self.entity = entity
        self.relative_restore_path_vec = relative_restore_path_vec


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
        entity = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('entity')) if dictionary.get('entity') else None
        relative_restore_path_vec = dictionary.get('relativeRestorePathVec')

        # Return an object of this model
        return cls(entity,
                   relative_restore_path_vec)


