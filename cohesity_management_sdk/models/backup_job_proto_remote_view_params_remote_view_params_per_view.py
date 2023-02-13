# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.


class BackupJobProto_RemoteViewParams_RemoteViewParamsPerView(object):

    """Implementation of the 'BackupJobProto_RemoteViewParams_RemoteViewParamsPerView' model.

    IP Range for range of vip address addition.

    Attributes:
        remote_view_name (string): If 'use_same_name_as_source_view' is false,
            below name should be populated.
        use_same_name_as_source_view (bool): Whether remote view name will be
            same as the source view name.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "remote_view_name": 'remoteViewName',
        "use_same_name_as_source_view": 'useSameNameAsSourceView'
    }

    def __init__(self,
                 remote_view_name=None,
                 use_same_name_as_source_view=None):
        """Constructor for the BackupJobProto_RemoteViewParams_RemoteViewParamsPerView class"""

        # Initialize members of the class
        self.remote_view_name = remote_view_name
        self.use_same_name_as_source_view = use_same_name_as_source_view


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
        remote_view_name = dictionary.get('remoteViewName', None)
        use_same_name_as_source_view = dictionary.get('useSameNameAsSourceView', None)

        # Return an object of this model
        return cls(remote_view_name,
                   use_same_name_as_source_view)


