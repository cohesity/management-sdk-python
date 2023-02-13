# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class ClearNlmLocksParameters(object):

    """Implementation of the 'ClearNlmLocksParameters' model.

    Specifies parameters required to force clear NLM Locks.

    Attributes:
        client_id (string): Specifies the id of the client, related NLM locks
            needs to be clear.
        file_path (string): Specifies the filepath in the view relative to the
            root filesystem. If this field is specified, viewName field must
            also be specified.
        view_name (string): Specifies the name of the View in which to search.
            If a view name is not specified, all the views in the Cluster is
            searched. This field is mandatory if filePath field is specified.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "client_id":'clientId',
        "file_path":'filePath',
        "view_name":'viewName'
    }

    def __init__(self,
                 client_id=None,
                 file_path=None,
                 view_name=None):
        """Constructor for the ClearNlmLocksParameters class"""

        # Initialize members of the class
        self.client_id = client_id
        self.file_path = file_path
        self.view_name = view_name


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
        client_id = dictionary.get('clientId')
        file_path = dictionary.get('filePath')
        view_name = dictionary.get('viewName')

        # Return an object of this model
        return cls(client_id,
                   file_path,
                   view_name)


