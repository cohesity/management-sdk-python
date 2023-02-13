# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.value

class EntityIdentifier(object):

    """Implementation of the 'EntityIdentifier' model.

    Specifies a unique identifier for the entity.

    Attributes:
        entity_id (Value): Specifies a data type and data field used to store
            data.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "entity_id":'entityId'
    }

    def __init__(self,
                 entity_id=None):
        """Constructor for the EntityIdentifier class"""

        # Initialize members of the class
        self.entity_id = entity_id


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
        entity_id = cohesity_management_sdk.models.value.Value.from_dictionary(dictionary.get('entityId')) if dictionary.get('entityId') else None

        # Return an object of this model
        return cls(entity_id)


