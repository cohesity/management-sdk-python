# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class NasAnalysisJobParams_FileSizeBucket(object):

    """Implementation of the 'NasAnalysisJobParams_FileSizeBucket' model.

    File size bucket.

    Attributes:
        file_size_bucket_name (string):  Tag representing the bucket for size
            of file.
            e.g. "1M-10M" represents 1 MB to 10 MB.
        file_size_end_bytes (long|int): End size for the bucket e.g. 500MB.
        file_size_start_bytes (long|int): Start size for the bucket e.g. 50MB.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "file_size_bucket_name":'fileSizeBucketName',
        "file_size_end_bytes":'fileSizeEndBytes',
        "file_size_start_bytes":'fileSizeStartBytes'
    }

    def __init__(self,
                 file_size_bucket_name=None,
                 file_size_end_bytes=None,
                 file_size_start_bytes=None):
        """Constructor for the NasAnalysisJobParams_FileSizeBucket class"""

        # Initialize members of the class
        self.file_size_bucket_name = file_size_bucket_name
        self.file_size_end_bytes = file_size_end_bytes
        self.file_size_start_bytes = file_size_start_bytes


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
        file_size_bucket_name = dictionary.get('fileSizeBucketName')
        file_size_end_bytes = dictionary.get('fileSizeEndBytes')
        file_size_start_bytes = dictionary.get('fileSizeStartBytes')

        # Return an object of this model
        return cls(file_size_bucket_name,
                   file_size_end_bytes,
                   file_size_start_bytes)


