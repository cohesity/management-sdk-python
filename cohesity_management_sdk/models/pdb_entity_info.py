# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class PDBEntityInfo(object):

    """Implementation of the 'PDBEntityInfo' model.

    Proto to capture the Pluggable database information.

    Attributes:
        db_id (string): Pluggable database identifier.
        name (string): Name of the DB.
        open_mode (int): PDB open mode.
        size_bytes (long|int): Size in bytes.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "db_id":'dbId',
        "name":'name',
        "open_mode":'openMode',
        "size_bytes":'sizeBytes'
    }

    def __init__(self,
                 db_id=None,
                 name=None,
                 open_mode=None,
                 size_bytes=None):
        """Constructor for the PDBEntityInfo class"""

        # Initialize members of the class
        self.db_id = db_id
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
        db_id = dictionary.get('dbId')
        name = dictionary.get('name')
        open_mode = dictionary.get('openMode')
        size_bytes = dictionary.get('sizeBytes')

        # Return an object of this model
        return cls(db_id,
                   name,
                   open_mode,
                   size_bytes)


