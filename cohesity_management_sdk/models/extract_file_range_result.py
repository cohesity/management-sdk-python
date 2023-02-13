# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.error_proto

class ExtractFileRangeResult(object):

    """Implementation of the 'ExtractFileRangeResult' model.

    This will capture output of ExtractFileRange and ExtractNFSFileRange.

    Attributes:
        data (list of int|long): The actual data bytes.
        eof (bool): Will be true if start_offset > file length or EOF is
            reached. This is an alternative to using file_length to determine
            when entire file is read. Used when fetching from a view.
        error (ErrorProto): Success/error status of the operation.
        file_length (int|long): The total length of the file. This field would
            be set provided no error had occurred (indicated by error field
            above).
        start_offset (int|long): The offset from which data was read.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "data": 'data',
        "eof": 'eof',
        "error": 'error',
        "file_length": 'fileLength',
        "start_offset":'startOffset'
    }

    def __init__(self,
                 data=None,
                 eof=None,
                 error=None,
                 file_length=None,
                 start_offset=None):
        """Constructor for the ExtractFileRangeResult class"""

        # Initialize members of the class
        self.data = data
        self.eof = eof
        self.error = error
        self.file_length = file_length
        self.start_offset = start_offset

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
        data = dictionary.get('data')
        eof = dictionary.get('eof')
        error = cohesity_management_sdk.models.error_proto.ErrorProto.from_dictionary(dictionary.get('error')) if dictionary.get('error') else None
        file_length = dictionary.get('fileLength')
        start_offset = dictionary.get('startOffset')

        # Return an object of this model
        return cls(data,
                   eof,
                   error,
                   file_length,
                   start_offset)


