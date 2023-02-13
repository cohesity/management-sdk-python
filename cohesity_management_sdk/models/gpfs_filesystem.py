# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class GpfsFilesystem(object):

    """Implementation of the 'GpfsFilesystem' model.

    Specifies information about filesystem in a GPFS Cluster.

    Attributes:
        id (string): Specifies the id of the file system.
        path (string): Specifies the path of the file system.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "path":'path'
    }

    def __init__(self,
                 id=None,
                 path=None):
        """Constructor for the GpfsFilesystem class"""

        # Initialize members of the class
        self.id = id
        self.path = path


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
        id = dictionary.get('id')
        path = dictionary.get('path')

        # Return an object of this model
        return cls(id,
                   path)


