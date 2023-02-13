# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class CloseSmbFileOpenParameters(object):

    """Implementation of the 'CloseSmbFileOpenParameters' model.

    Specifies parameters required to force close an active SMB file open.

    Attributes:
        file_path (string): Specifies the filepath in the view relative to the
            root filesystem. If this field is specified, viewName field must
            also be specified.
        open_id (long|int): Specifies the id of the active open.
        view_name (string): Specifies the name of the View in which to search.
            If a view name is not specified, all the views in the Cluster is
            searched. This field is mandatory if filePath field is specified.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "file_path":'filePath',
        "open_id":'openId',
        "view_name":'viewName'
    }

    def __init__(self,
                 file_path=None,
                 open_id=None,
                 view_name=None):
        """Constructor for the CloseSmbFileOpenParameters class"""

        # Initialize members of the class
        self.file_path = file_path
        self.open_id = open_id
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
        file_path = dictionary.get('filePath')
        open_id = dictionary.get('openId')
        view_name = dictionary.get('viewName')

        # Return an object of this model
        return cls(file_path,
                   open_id,
                   view_name)


