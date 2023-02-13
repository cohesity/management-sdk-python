# -*- coding: utf-8 -*-
# Copyright 2023 Cohesity Inc.

import cohesity_management_sdk.models.smb_active_session

class SmbActiveFilePath(object):

    """Implementation of the 'SmbActiveFilePath' model.

    Specifies a file path in an SMB view that has active sessions and opens.

    Attributes:
        active_sessions (list of SmbActiveSession): Specifies the sessions
            where the file is open.
        file_path (string): Specifies the filepath in the view.
        view_id (long|int): Specifies the id of the View assigned by the
            Cohesity Cluster. Either viewName or viewId must be specified.
        view_name (string): Specifies the name of the View.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "active_sessions":'activeSessions',
        "file_path":'filePath',
        "view_id":'viewId',
        "view_name":'viewName'
    }

    def __init__(self,
                 active_sessions=None,
                 file_path=None,
                 view_id=None,
                 view_name=None):
        """Constructor for the SmbActiveFilePath class"""

        # Initialize members of the class
        self.active_sessions = active_sessions
        self.file_path = file_path
        self.view_id = view_id
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
        active_sessions = None
        if dictionary.get('activeSessions') != None:
            active_sessions = list()
            for structure in dictionary.get('activeSessions'):
                active_sessions.append(cohesity_management_sdk.models.smb_active_session.SmbActiveSession.from_dictionary(structure))
        file_path = dictionary.get('filePath')
        view_id = dictionary.get('viewId')
        view_name = dictionary.get('viewName')

        # Return an object of this model
        return cls(active_sessions,
                   file_path,
                   view_id,
                   view_name)


