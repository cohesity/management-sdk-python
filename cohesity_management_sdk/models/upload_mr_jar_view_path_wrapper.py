# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class UploadMRJarViewPathWrapper(object):

    """Implementation of the 'UploadMRJarViewPathWrapper' model.

    UploadMRJarViewPathWrapper contains jar name and local mount path where
    the Jars will be uploaded.

    Attributes:
        jar_name (string): JarName is the name of the uploaded jar.
        jar_path (string): JarPath is the path for the directory where
            uploaded jar is stored.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "jar_name": 'jarName',
        "jar_path": 'JarPath'
    }

    def __init__(self,
                 jar_name=None,
                 jar_path=None):
        """Constructor for the UploadMRJarViewPathWrapper class"""

        # Initialize members of the class
        self.jar_name = jar_name
        self.jar_path = jar_path


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
        jar_name = dictionary.get('jarName', None)
        jar_path = dictionary.get('JarPath', None)

        # Return an object of this model
        return cls(jar_name,
                   jar_path)


