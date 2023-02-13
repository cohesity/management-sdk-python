# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class CloneDirectoryParams(object):

    """Implementation of the 'CloneDirectoryParams' model.

    Specifies the params that have to be provided to clone a directory.

    Attributes:
        destination_directory_name (string): Name of the new directory which
            will contain the clone contents.
        destination_parent_directory_path (string): Specifies the path of the
            destination parent directory. The source dir would be cloned as a
            child of destination parent dir.
        source_directory_path (string): Specifies the path of the source
            directory

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "destination_directory_name":'destinationDirectoryName',
        "destination_parent_directory_path":'destinationParentDirectoryPath',
        "source_directory_path":'sourceDirectoryPath'
    }

    def __init__(self,
                 destination_directory_name=None,
                 destination_parent_directory_path=None,
                 source_directory_path=None):
        """Constructor for the CloneDirectoryParams class"""

        # Initialize members of the class
        self.destination_directory_name = destination_directory_name
        self.destination_parent_directory_path = destination_parent_directory_path
        self.source_directory_path = source_directory_path


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
        destination_directory_name = dictionary.get('destinationDirectoryName')
        destination_parent_directory_path = dictionary.get('destinationParentDirectoryPath')
        source_directory_path = dictionary.get('sourceDirectoryPath')

        # Return an object of this model
        return cls(destination_directory_name,
                   destination_parent_directory_path,
                   source_directory_path)


