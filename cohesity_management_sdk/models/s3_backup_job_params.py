# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

class S3BackupJobParams(object):

    """Implementation of the 'S3BackupJobParams' model.

    TODO: type description here.


    Attributes:

        skip_files_on_error (bool): If true then backup job will skip the S3
            objects whose backup get failed. Basically, won't fail the backup
            job if some of the objects gets failed.
        storage_classes (list of int): Objects whose storage class is not in
            the selected storage classes will be skipped.
    """


    # Create a mapping from Model property names to API property names
    _names = {
        "skip_files_on_error":'skipFilesOnError',
        "storage_classes":'storageClasses',
    }
    def __init__(self,
                 skip_files_on_error=None,
                 storage_classes=None,
            ):

        """Constructor for the S3BackupJobParams class"""

        # Initialize members of the class
        self.skip_files_on_error = skip_files_on_error
        self.storage_classes = storage_classes

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
        skip_files_on_error = dictionary.get('skipFilesOnError')
        storage_classes = dictionary.get("storageClasses")

        # Return an object of this model
        return cls(
            skip_files_on_error,
            storage_classes
)