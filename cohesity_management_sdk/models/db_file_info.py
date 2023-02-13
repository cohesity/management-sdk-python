# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class DbFileInfo(object):

    """Implementation of the 'DbFileInfo' model.

    Specifies information about a database file.

    Attributes:
        file_type (FileTypeEnum): Specifies the format type of the file that
            SQL database stores the data. Specifies the format type of the
            file that SQL database stores the data. 'kRows' refers to a data
            file 'kLog' refers to a log file 'kFileStream' refers to a
            directory containing FILESTREAM data 'kNotSupportedType' is for
            information purposes only. Not supported. 'kFullText' refers to a
            full-text catalog.
        full_path (string): Specifies the full path of the database file on
            the SQL host machine.
        size_bytes (long|int): Specifies the last known size of the database
            file.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "file_type":'fileType',
        "full_path":'fullPath',
        "size_bytes":'sizeBytes'
    }

    def __init__(self,
                 file_type=None,
                 full_path=None,
                 size_bytes=None):
        """Constructor for the DbFileInfo class"""

        # Initialize members of the class
        self.file_type = file_type
        self.full_path = full_path
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
        file_type = dictionary.get('fileType')
        full_path = dictionary.get('fullPath')
        size_bytes = dictionary.get('sizeBytes')

        # Return an object of this model
        return cls(file_type,
                   full_path,
                   size_bytes)


