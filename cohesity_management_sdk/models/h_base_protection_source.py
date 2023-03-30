# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.hbase_table

class HBaseProtectionSource(object):

    """Implementation of the 'HBaseProtectionSource' model.

    Specifies an Object representing HBase.

    Attributes:
        name (string): Specifies the instance name of the HBase entity.
        table_info (HBaseTable): Information of a HBase Table, only valid for
            an entity of type kTable.
        mtype (TypeHBaseProtectionSourceEnum): Specifies the type of the
            managed Object in HBase Protection Source.
            Specifies the type of an HBase source entity.
            'kCluster' indicates a HBase cluster distributed over several
            physical nodes.
            'kNamespace' indicates a Namespace in the HBase environment.
            'kTable' indicates a Table in the HBase environment.
        uuid (string): Specifies the UUID for the HBase entity.

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
        """Constructor for the HBaseProtectionSource class"""

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
        table_info = cohesity_management_sdk.models.hbase_table.HBaseTable.from_dictionary(dictionary.get('tableInfo')) if dictionary.get('tableInfo') else None
        mtype = dictionary.get('type')
        uuid = dictionary.get('uuid')

        # Return an object of this model
        return cls(name,
                   table_info,
                   mtype,
                   uuid)


