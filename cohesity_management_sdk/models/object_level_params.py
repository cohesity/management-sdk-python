# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class ObjectLevelParams(object):

    """Implementation of the 'ObjectLevelParams' model.

    TODO: type description here.


    Attributes:

        entity_id (long|int): Entity id of the object.
        excluded_fields_vec (list of string): List of the field names that the
            user excluded in this object.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "entity_id":'entityId',
        "excluded_fields_vec":'excludedFieldsVec',
    }
    def __init__(self,
                 entity_id=None,
                 excluded_fields_vec=None,
            ):

        """Constructor for the ObjectLevelParams class"""

        # Initialize members of the class
        self.entity_id = entity_id
        self.excluded_fields_vec = excluded_fields_vec

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
        excluded_fields_vec = dictionary.get("excludedFieldsVec")

        # Return an object of this model
        return cls(
            entity_id,
            excluded_fields_vec
)