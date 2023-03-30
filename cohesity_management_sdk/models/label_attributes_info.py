# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class LabelAttributesInfo(object):

    """Implementation of the 'LabelAttributesInfo' model.

    TODO: type description here.


    Attributes:

        entity_id (long|int): Entity ID of the label entity in EH.
        name (string): Name of the label entity.
        uuid (string): UUID of the label entity.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "entity_id":'entityId',
        "name":'name',
        "uuid":'uuid',
    }
    def __init__(self,
                 entity_id=None,
                 name=None,
                 uuid=None,
            ):

        """Constructor for the LabelAttributesInfo class"""

        # Initialize members of the class
        self.entity_id = entity_id
        self.name = name
        self.uuid = uuid

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
        name = dictionary.get('name')
        uuid = dictionary.get('uuid')

        # Return an object of this model
        return cls(
            entity_id,
            name,
            uuid
)