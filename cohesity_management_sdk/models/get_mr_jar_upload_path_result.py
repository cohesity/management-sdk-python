# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.error_proto

class GetMRJarUploadPathResult(object):

    """Implementation of the 'GetMRJarUploadPathResult' model.

    User can upload jar files containing mappers and reducers. Iris will
    upload these jar files in Yoda's internal view. Yoda will mount its
    internal view and send Iris the mount point.

    Attributes:
        error (ErrorProto): Status code for this http rpc.
        jar_upload_path (string): Path where Jars can be uploaded by Iris.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "error": 'error',
        "jar_upload_path": 'jarUploadPath'
    }

    def __init__(self,
                 error=None,
                 jar_upload_path=None):
        """Constructor for the GetMRJarUploadPathResult class"""

        # Initialize members of the class
        self.error = error
        self.jar_upload_path = jar_upload_path


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
        error = cohesity_management_sdk.models.error_proto.ErrorProto.from_dictionary(dictionary.get('error')) if dictionary.get('error') else None
        jar_upload_path = dictionary.get('jarUploadPath', None)

        # Return an object of this model
        return cls(error,
                   jar_upload_path)


