# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class HiveTable(object):

    """Implementation of the 'HiveTable' model.

    Specifies an Object containing information about a Hive table.

    Attributes:
        approx_size_bytes (int): Specifies the approx size of the table in
            bytes.
        created_on (int): Specifies the created on, epoch millis.
        is_transactional_table (bool): Specifies if this is a transactional table.
        owner (string): Specifies the owner of the table.
        table_type (TypeHiveTableEnum): Specifies the type of table ex.
            MANAGED,VIRTUAL etc.
            Specifies the type of an Hive table.
            'kManaged' indicates a MANAGED Hive table.
            'kExternal' indicates a EXTERNAL Hive table.
            'kVirtual' indicates a VIRTUAL Hive tablet.
            'kIndex' indicates a INDEX Hive table.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "approx_size_bytes":'approxSizeBytes',
        "created_on":'createdOn',
        "is_transactional_table":'isTransactionalTable',
        "owner":'owner',
        "table_type":'tableType'
    }

    def __init__(self,
                 approx_size_bytes=None,
                 created_on=None,
                 is_transactional_table=None,
                 owner=None,
                 table_type=None):
        """Constructor for the HiveTable class"""

        # Initialize members of the class
        self.approx_size_bytes = approx_size_bytes
        self.created_on = created_on
        self.is_transactional_table = is_transactional_table
        self.owner = owner
        self.table_type = table_type


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
        approx_size_bytes = dictionary.get('approxSizeBytes')
        created_on = dictionary.get('createdOn')
        is_transactional_table = dictionary.get('isTransactionalTable')
        table_type = dictionary.get('tableType')
        owner = dictionary.get('owner')

        # Return an object of this model
        return cls(approx_size_bytes,
                   created_on,
                   is_transactional_table,
                   owner,
                   table_type)


