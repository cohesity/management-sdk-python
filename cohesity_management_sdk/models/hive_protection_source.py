# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.hive_table

class HiveProtectionSource(object):

    """Implementation of the 'HiveProtectionSource' model.

    Specifies an Object representing Hive.

    Attributes:
        name (string): Specifies the instance name of the Hive entity.
        table_info (HiveTable): Information of a Hive Table, only valid for an
            entity of type kTable.
        mtype (TypeHiveProtectionSourceEnum): Specifies the type of the
            managed Object in Hive Protection Source.
            Specifies the type of an Hive source entity.
            'kCluster' indicates a Hive cluster distributed over several
            physical nodes.
            'kDatabase' indicates a Database in the Hive environment.
            'kTable' indicates a Table in the Hive environment.
        uuid (string):  Specifies the UUID for the Hive entity.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "table_info":'tableInfo',
        "mtype":'type',
        "uuid":'uuid'
    }

    def __init__(self,
                 name=None,
                 table_info=None,
                 mtype=None,
                 uuid=None):
        """Constructor for the HiveProtectionSource class"""

        # Initialize members of the class
        self.name = name
        self.table_info = table_info
        self.mtype = mtype
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
        name = dictionary.get('name')
        table_info = cohesity_management_sdk.models.hive_table.HiveTable.from_dictionary(dictionary.get('tableInfo')) if dictionary.get('tableInfo') else None
        mtype = dictionary.get('type')
        uuid = dictionary.get('uuid')

        # Return an object of this model
        return cls(name,
                   table_info,
                   mtype,
                   uuid)


