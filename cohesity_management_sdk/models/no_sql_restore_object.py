# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.no_sql_restore_object_object_restore_properties_map_entry

class NoSqlRestoreObject(object):

    """Implementation of the 'NoSqlRestoreObject' model.

    TODO: Type model description here.

    Attributes:
        object_restore_properties_map (list of
            NoSqlRestoreObject_ObjectRestorePropertiesMapEntry): Key-Value
            pair for properties to apply on restore object.
        object_uuid (string): Uuid of the object to be restored.
        rename (string): The new name of the object after restore.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "object_restore_properties_map":'objectRestorePropertiesMap',
        "object_uuid":'objectUuid',
        "rename":'rename'
    }

    def __init__(self,
                 object_restore_properties_map=None,
                 object_uuid=None,
                 rename=None):
        """Constructor for the NoSqlRestoreObject class"""

        # Initialize members of the class
        self.object_restore_properties_map = object_restore_properties_map
        self.object_uuid = object_uuid
        self.rename = rename


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
        object_restore_properties_map = None
        if dictionary.get('objectRestorePropertiesMap') != None:
            object_restore_properties_map = list()
            for structure in dictionary.get('objectRestorePropertiesMap'):
                object_restore_properties_map.append(cohesity_management_sdk.models.no_sql_restore_object_object_restore_properties_map_entry.NoSqlRestoreObject_ObjectRestorePropertiesMapEntry.from_dictionary(structure))
        object_uuid = dictionary.get('objectUuid')
        rename = dictionary.get('rename')

        # Return an object of this model
        return cls(object_restore_properties_map,
                   object_uuid,
                   rename)


