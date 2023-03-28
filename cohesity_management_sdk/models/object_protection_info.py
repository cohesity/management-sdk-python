# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class ObjectProtectionInfo(object):

    """Implementation of the 'ObjectProtectionInfo' model.

    TODO: type description here.


    Attributes:

        auto_protect_parent_id (long|int): Specifies the auto protect parent id
            if this entity is protected based on auto protection. This is only
            specified for leaf entities.
        entity_id (long|int): Specifies the entity id.
        has_active_object_protection_spec (bool): Specifies if the entity is
            under object protection
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "auto_protect_parent_id":'autoProtectParentId',
        "entity_id":'entityId',
        "has_active_object_protection_spec":'hasActiveObjectProtectionSpec',
    }
    def __init__(self,
                 auto_protect_parent_id=None,
                 entity_id=None,
                 has_active_object_protection_spec=None,
            ):

        """Constructor for the ObjectProtectionInfo class"""

        # Initialize members of the class
        self.auto_protect_parent_id = auto_protect_parent_id
        self.entity_id = entity_id
        self.has_active_object_protection_spec = has_active_object_protection_spec

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
        auto_protect_parent_id = dictionary.get('autoProtectParentId')
        entity_id = dictionary.get('entityId')
        has_active_object_protection_spec = dictionary.get('hasActiveObjectProtectionSpec')

        # Return an object of this model
        return cls(
            auto_protect_parent_id,
            entity_id,
            has_active_object_protection_spec
)