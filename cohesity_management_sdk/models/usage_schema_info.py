# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.schema_info

class UsageSchemaInfo(object):

    """Implementation of the 'UsageSchemaInfo' model.

    UsageSchemaInfo describes the schema info of the usage.

    Attributes:
        schema_info_list (list of SchemaInfo): Specifies the list of the
            schema info for an entity.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "schema_info_list":'schemaInfoList'
    }

    def __init__(self,
                 schema_info_list=None):
        """Constructor for the UsageSchemaInfo class"""

        # Initialize members of the class
        self.schema_info_list = schema_info_list


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
        schema_info_list = None
        if dictionary.get('schemaInfoList') != None:
            schema_info_list = list()
            for structure in dictionary.get('schemaInfoList'):
                schema_info_list.append(cohesity_management_sdk.models.schema_info.SchemaInfo.from_dictionary(structure))

        # Return an object of this model
        return cls(schema_info_list)


