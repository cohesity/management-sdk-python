# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class OraclePluggableDatabaseInfo(object):

    """Implementation of the 'OraclePluggableDatabaseInfo' model.

    Specifies the informatiomn about the pluggable database. A Pluggabele
    Database(PDB) is a portable collection of schemas, schema objects, and
    nonschema objects that appears to an Oracle Net client as a non-CDB.

    Attributes:
    database_id (string): Specifies the ID of the Pluggable Database.
    name (string): Speicifes the name of the Pluggable Database.
    open_mode (OpenModeEnum): Specifies the OPEN_MODE information.
        Specifies the OPEN_MODE type for the Oracle database.
        'kMounted' indicates that the database is open in Mounted mode.
        'kReadWrite' indicates that the database is open in R/W mode.
        'kReadOnly' indicates that the database is open in ReadOnly mode.
        'kMigrate' indicates that the database is open in Migrate mode.
    size_bytes (int): Specifies the Size in Bytes of the Pluggable Database.
    """

    # Create a mapping from Model property names to API property names
    _names = {
        "database_id":'databaseId',
        "name":'name',
        "open_mode":'openMode',
        "size_bytes":'sizeBytes'
    }

    def __init__(self,
                 database_id=None,
                 name=None,
                 open_mode=None,
                 size_bytes=None):
        """Constructor for the OraclePluggableDatabaseInfo class"""

        # Initialize members of the class
        self.database_id = database_id
        self.name = name
        self.open_mode = open_mode
        self.size_bytes = size_bytes


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
        database_id = dictionary.get('databaseId')
        name = dictionary.get('name')
        open_mode = dictionary.get('openMode')
        size_bytes = dictionary.get('sizeBytes')
        

        # Return an object of this model
        return cls(database_id,
                   name,
                   open_mode,
                   size_bytes)


