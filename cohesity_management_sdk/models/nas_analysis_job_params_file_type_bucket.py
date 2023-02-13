# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class NasAnalysisJobParams_FileTypeBucket(object):

    """Implementation of the 'NasAnalysisJobParams_FileTypeBucket' model.

    File type bucket.

    Attributes:
        file_type_bucket_extensions (list of string): File extensions
            e.g. <vmdk, ova>.
        file_type_bucket_name (string): File type bucket name,
            e.g. VMs.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "file_type_bucket_extensions": 'fileTypeBucketExtensions',
        "file_type_bucket_name": 'fileTypeBucketName'
    }

    def __init__(self,
                 file_type_bucket_extensions=None,
                 file_type_bucket_name=None):
        """Constructor for the NasAnalysisJobParams_FileTypeBucket class"""

        # Initialize members of the class
        self.file_type_bucket_extensions = file_type_bucket_extensions
        self.file_type_bucket_name = file_type_bucket_name


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
        file_type_bucket_extensions = dictionary.get('fileTypeBucketExtensions', None)
        file_type_bucket_name = dictionary.get('fileTypeBucketName', None)

        # Return an object of this model
        return cls(file_type_bucket_extensions,
                   file_type_bucket_name)


