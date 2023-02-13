# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class DownloadCftResponse(object):

    """Implementation of the 'DownloadCftResponse' model.

    TODO: Type model description here.

    Attributes:
        content (list of int|long): Specifies the content of the file.
        file_name (string): Specifies the content of the CFT.
            in: body
            Specifies the file name of the cloud formation template.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "content": 'content',
        "file_name": 'fileName'
    }

    def __init__(self,
                 content=None,
                 file_name=None):
        """Constructor for the DownloadCftResponse class"""

        # Initialize members of the class
        self.content = content
        self.file_name = file_name


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
        content = dictionary.get('content', None)
        file_name = dictionary.get('fileName', None)

        # Return an object of this model
        return cls(content,
                   file_name)


